import sys
from pathlib import Path
from ecs_quantitative.ingestion.parser import UniversalParser
from ecs_quantitative.nlp.rag.markdown_sanitizer import MarkdownSanitizer

def main():
    root_dir = Path(__file__).resolve().parents[1]
    raw_dir = root_dir / "bibliography" / "raw"
    processed_dir = root_dir / "bibliography" / "processed"
    sanitized_dir = root_dir / "bibliography" / "sanitized"

    processed_dir.mkdir(parents=True, exist_ok=True)
    sanitized_dir.mkdir(parents=True, exist_ok=True)

    parser = UniversalParser()
    sanitizer = MarkdownSanitizer()

    pdf_files = list(raw_dir.glob("*.pdf"))
    if not pdf_files:
        print("No se encontraron archivos PDF en bibliography/raw/")
        return

    print(f"Se encontraron {len(pdf_files)} archivos PDF para procesar.")

    for i, pdf_path in enumerate(pdf_files, 1):
        print(f"[{i}/{len(pdf_files)}] Procesando: {pdf_path.name}")
        try:
            # 1. Parsear PDF a Markdown/Texto crudo
            raw_data = parser.parse_pdf(pdf_path)
            text = raw_data.get("text", "")
            
            # Guardar en processed
            processed_file = processed_dir / f"{pdf_path.stem}.md"
            with open(processed_file, "w", encoding="utf-8") as f:
                f.write(text)
            
            # 2. Sanitizar
            sanitized_text = sanitizer.sanitize(text)
            
            # Guardar en sanitized
            sanitized_file = sanitized_dir / f"{pdf_path.stem}.md"
            with open(sanitized_file, "w", encoding="utf-8") as f:
                f.write(sanitized_text)
                
            print(f"    -> Completado: {pdf_path.stem}.md")
        except Exception as e:
            print(f"    -> ERROR al procesar {pdf_path.name}: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
