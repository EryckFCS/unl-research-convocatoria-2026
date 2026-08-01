# unl-research-convocatoria-2026

Nodo federado destinado a formular, procesar y redactar la propuesta para la **Convocatoria de Proyectos de Investigación con Fondos Institucionales 2026 de la Universidad Nacional de Loja (UNL)**.

## Estructura del Nodo (Blueprint v8.1.5)

- `.agents/`: Reglas de gobernanza e instrucciones específicas de ecosistema.
- `bibliography/`: Literatura científica y referencias en BibTeX organizadas para el RAG.
- `config/`: Configuración y enlaces simbólicos al Data Lake centralizado.
- `data/`: Microdatos no estructurados y de control.
- `docs/vaults/`: Unidades de evidencia de diseño del proyecto.
- `docs/readings/`: Lecturas y marco conceptual de soporte.
- `docs/syllabus/`: Bases institucionales y lineamientos de la convocatoria.
- `docs/writing/`: Narrativa y propuesta final redactada en Quarto.
- `src/`: Lógica econométrica y análisis de datos.
- `tests/`: Batería de validación y gatekeepers del nodo.

## Uso del Entorno

Instalación de dependencias:
```bash
uv sync
```

Ejecución de validación de cumplimiento estructural:
```bash
uv run pytest tests/system/test_architecture.py
```
