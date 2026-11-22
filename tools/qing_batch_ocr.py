#!/usr/bin/env python3
"""Prepare batch review images for scanned vertical-Chinese source pages.

PyMuPDF renders the requested PDF range; each spread is split into left/right
page images. Optional Tesseract OCR is only a draft, never verified text.
Requires: pymupdf, pillow. Optional OCR: tesseract + HanT_vert language data.
"""
from __future__ import annotations
import argparse
import json
import shutil
from pathlib import Path
import fitz
from PIL import Image, ImageEnhance


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--start", type=int, required=True)
    parser.add_argument("--end", type=int, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--dpi", type=int, default=300)
    parser.add_argument("--ocr", action="store_true", help="run slow experimental Tesseract OCR")
    parser.add_argument("--lang", default="HanT_vert")
    parser.add_argument("--psm", type=int, default=5)
    args = parser.parse_args()
    if args.start < 1 or args.end < args.start:
        raise SystemExit("invalid page range")
    if args.ocr and not shutil.which("tesseract"):
        raise SystemExit("missing executable: tesseract")
    args.out.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(args.pdf)
    if args.end > doc.page_count:
        raise SystemExit(f"end page exceeds PDF page count ({doc.page_count})")
    scale = args.dpi / 72
    rows = []
    for page_no in range(args.start, args.end + 1):
        page = doc.load_page(page_no - 1)
        pix = page.get_pixmap(matrix=fitz.Matrix(scale, scale), alpha=False)
        full_image = args.out / f"render-{page_no:04d}.png"
        pix.save(full_image)
        image = Image.open(full_image).convert("L")
        width, height = image.size
        overlap = max(12, round(width * 0.006))
        for side, bounds in (
            ("left", (0, 0, width // 2 + overlap, height)),
            ("right", (width // 2 - overlap, 0, width, height)),
        ):
            image_path = args.out / f"pdf-{page_no:04d}-{side}.png"
            base = args.out / f"pdf-{page_no:04d}-{side}"
            ImageEnhance.Contrast(image.crop(bounds)).enhance(1.35).save(image_path)
            item = {"pdf_page": page_no, "side": side, "image": image_path.name,
                    "status": "high_resolution_image_ready_for_visual_transcription"}
            if args.ocr:
                import subprocess
                subprocess.run(["tesseract", str(image_path), str(base), "-l", args.lang,
                                "--psm", str(args.psm), "txt", "tsv"], check=True,
                               stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
                tsv = base.with_suffix(".tsv")
                confidences = []
                for line in tsv.read_text(encoding="utf-8", errors="replace").splitlines()[1:]:
                    fields = line.split("\t")
                    if len(fields) > 10 and fields[10] not in ("", "-1"):
                        try:
                            confidences.append(float(fields[10]))
                        except ValueError:
                            pass
                item.update({
                    "ocr_text": base.with_suffix(".txt").name,
                    "ocr_tsv": tsv.name,
                    "mean_token_confidence": round(sum(confidences) / len(confidences), 1) if confidences else None,
                    "token_count": len(confidences),
                    "status": "machine_draft_requires_full_visual_verification",
                })
            rows.append(item)
        full_image.unlink(missing_ok=True)
    index = {
        "source_pdf": str(args.pdf), "pdf_pages": [args.start, args.end],
        "dpi": args.dpi, "ocr_enabled": args.ocr,
        "warning": "Images are review assets. Optional OCR is a draft only and never verified text.",
        "items": rows,
    }
    (args.out / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"pages": args.end - args.start + 1,
                      "page_sides": len(rows), "output": str(args.out)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
