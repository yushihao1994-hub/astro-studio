#!/usr/bin/env python3
"""Create OCR drafts and review assets for scanned vertical-Chinese source pages.

OCR output is a draft only. Every page must be checked against its retained
image before any text is marked as a verified transcription.
"""
from __future__ import annotations
import argparse
import json
import shutil
import subprocess
from pathlib import Path
from PIL import Image, ImageEnhance


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--start", type=int, required=True)
    parser.add_argument("--end", type=int, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--dpi", type=int, default=350)
    parser.add_argument("--lang", default="HanT_vert")
    parser.add_argument("--psm", type=int, default=5)
    args = parser.parse_args()
    if args.start < 1 or args.end < args.start:
        raise SystemExit("invalid page range")
    for executable in ("pdftoppm", "tesseract"):
        if not shutil.which(executable):
            raise SystemExit(f"missing executable: {executable}")
    args.out.mkdir(parents=True, exist_ok=True)
    rows = []
    for page in range(args.start, args.end + 1):
        stem = args.out / f"pdf-{page:04d}"
        raw = stem.with_suffix(".png")
        run(["pdftoppm", "-f", str(page), "-l", str(page), "-png",
             "-r", str(args.dpi), "-singlefile", str(args.pdf), str(stem)])
        image = Image.open(raw).convert("L")
        width, height = image.size
        overlap = max(12, round(width * 0.006))
        halves = [
            ("left", (0, 0, width // 2 + overlap, height)),
            ("right", (width // 2 - overlap, 0, width, height)),
        ]
        for side, bounds in halves:
            image_path = args.out / f"pdf-{page:04d}-{side}.png"
            output_base = args.out / f"pdf-{page:04d}-{side}"
            crop = ImageEnhance.Contrast(image.crop(bounds)).enhance(1.35)
            crop.save(image_path)
            run(["tesseract", str(image_path), str(output_base), "-l", args.lang,
                 "--psm", str(args.psm), "txt", "tsv"])
            text_path = output_base.with_suffix(".txt")
            tsv_path = output_base.with_suffix(".tsv")
            confidences = []
            for line in tsv_path.read_text(encoding="utf-8", errors="replace").splitlines()[1:]:
                fields = line.split("\t")
                if len(fields) > 10 and fields[10].strip() and fields[10] != "-1":
                    try:
                        confidences.append(float(fields[10]))
                    except ValueError:
                        pass
            rows.append({
                "pdf_page": page, "side": side, "image": image_path.name,
                "ocr_text": text_path.name, "ocr_tsv": tsv_path.name,
                "mean_token_confidence": round(sum(confidences) / len(confidences), 1) if confidences else None,
                "token_count": len(confidences),
                "status": "machine_draft_requires_full_visual_verification",
            })
        raw.unlink(missing_ok=True)
    index = {
        "source_pdf": str(args.pdf), "pdf_pages": [args.start, args.end],
        "dpi": args.dpi, "language_model": args.lang, "psm": args.psm,
        "warning": "OCR is a draft only; never treat as verified source text.",
        "items": rows,
    }
    index_path = args.out / "index.json"
    index_path.write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"pages": args.end - args.start + 1,
                      "page_sides": len(rows), "output": str(args.out),
                      "index": str(index_path)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
