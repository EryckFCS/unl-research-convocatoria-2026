# AGENTS.md - Nodo Federado: Convocatoria de Investigación UNL 2026

> Este repositorio es un Nodo Puro de la Arquitectura Federada v8.1.5.
> Opera bajo la Constitución centralizada en `capital-workstation-libs`.

## 1. Identidad del Nodo y Gobernanza

| Campo | Valor |
| --- | --- |
| **Nodo** | Convocatoria Investigación UNL 2026 |
| **Estado** | Activo - Master Blueprint v8.1.5 |
| **Librería Central** | `ecs_quantitative` (capital-workstation-libs) |
| **Nivel de Inteligencia** | 5 - Intelligent Ecosystem with Controlled Autonomy |
| **Gatekeeper** | `tests/system/test_architecture.py` |

## 2. Capacidades de Inteligencia (v3.0)

Este nodo está diseñado para formular, modelar y redactar la propuesta de investigación para la convocatoria de la UNL 2026.

1. **Autonomous Vaults**: Cada unidad de evidencia en `docs/vaults/` contiene sus propios scripts, logs y assets para reproducibilidad.
2. **Standardized RAG Pipeline**: Procesa literatura y bases de la convocatoria en un flujo PDF -> Markdown -> Sanitized para RAG de exocórtex.
3. **Data Lake Integration**: Los conjuntos de datos pesados (ENEMDU, series del BCE) se referencian mediante enlaces simbólicos gestionados por `config/resources.json`.

## 3. Protocolos Operativos

### 3.1. Architecture Governance Protocol (AGP)
- **Invariante**: Cualquier cambio estructural debe satisfacer el test de arquitectura.
- **Acción**: Ejecutar `uv run pytest tests/system/test_architecture.py` antes de realizar commits.

### 3.2. Research Protocol
- **Ubicación**: Las evidencias del análisis viven en `docs/vaults/`; las lecturas y bases en `docs/readings/` y `docs/syllabus/`; los entregables finales Quarto en `docs/writing/`.

## 4. Arquitectura de Bóvedas (v8.1.5)

```text
.
├── bibliography/            # raw/, processed/, sanitized/
├── config/                  # resources.json, settings.toml
├── data/                    # Datos no bibliográficos
├── docs/
│   ├── vaults/              # Bóvedas de evidencia atómica por fase
│   ├── management/          # Planificación y gestión de riesgos
│   ├── readings/            # Literatura científica de soporte
│   └── syllabus/            # Bases de la convocatoria de la UNL
├── src/                     # Lógica econométrica y de procesamiento
└── tests/                   # Tests de arquitectura y regresión
```

## 5. Mantenimiento y Resiliencia

```bash
uv sync
# Verificar cumplimiento de arquitectura
uv run pytest tests/system/test_architecture.py
```
