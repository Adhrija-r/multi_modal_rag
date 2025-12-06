# minimal PDF parser skeleton using pdfplumber
import pdfplumber
from pathlib import Path
import json

def parse_pdf(path, out_dir="data/parsed"):
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    pages = []
    with pdfplumber.open(path) as pdf:
        for i, page in enumerate(pdf.pages, start=1):
            text = page.extract_text() or ""
            img_path = f"{out_dir}/page_{i}.png"
            # save page image for debugging (pdfplumber page.to_image requires pillow)
            try:
                page.to_image(resolution=150).save(img_path)
            except Exception:
                img_path = None
            pages.append({"page": i, "text": text, "img": img_path})
    # save summary json
    with open(f"{out_dir}/{Path(path).stem}_pages.json", "w", encoding="utf-8") as f:
        json.dump(pages, f, indent=2, ensure_ascii=False)
    return pages

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python pdf_parser.py <pdf_path>")
    else:
        parse_pdf(sys.argv[1])
