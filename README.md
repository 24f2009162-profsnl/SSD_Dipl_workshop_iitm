# SSD_Dipl_workshop_iitm
# 🎀 Custom Skin-Match Makeup Store
*A Spec-Driven Development (SDD) vs. Vibe Coding Experiment*

## 📖 Overview
This repository serves as a comparative study between unstructured AI-assisted coding ("Vibe Coding") and structured, architecture-first implementation ("Spec-Driven Development"). The core application is a lightweight Python CLI that recommends tailored makeup products based on a user's skin profile.

## 🌿 Branch Architecture
To demonstrate the workshop's core concepts, this repository is split into distinct workflows:

* **`vibe_coded_submission` Branch:** Features `makeup_store.py`, developed using raw, unstructured LLM prompting. It relies on heavy, nested `if/else` conditional logic.
* **`sdd_submission` Branch:** Features `makeup.py` and `project.md`, developed using strict Spec-Driven Development principles. The architecture was planned in Markdown first, resulting in a clean, scalable dictionary-mapping algorithm that completely avoids nested conditionals.

# Reports API

A small FastAPI service that exposes a paginated `/reports` endpoint backed by a deterministic in-memory dataset.

## Layout

```
app/
├── __init__.py
├── data.py        # Seed dataset (120 rows, deterministic)
├── models.py      # Pydantic models — internal vs public
├── reports.py     # Filter / sort / pagination query layer
└── main.py        # FastAPI HTTP layer
```

## Requirements

- Python 3.10+
- pip

## Setup

```bash
git clone https://github.com/IITMBSMLOps/SpecDrivenDevelopmentBase.git
cd SpecDrivenDevelopmentBase

python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

pip install -e .
```

## Run the API

```bash
uvicorn app.main:app --reload --port 8000
```

Then hit it from another terminal:

```bash
curl "http://localhost:8000/health"
curl "http://localhost:8000/reports?limit=3" | python -m json.tool
```

## Endpoints

| Method | Path       | Description                                            |
| ------ | ---------- | ------------------------------------------------------ |
| GET    | `/health`  | Liveness probe — returns `{"status": "ok"}`.           |
| GET    | `/reports` | Paginated list of reports with filtering and sorting.  |

### `GET /reports` query parameters

| Param        | Type            | Default      | Notes                                            |
| ------------ | --------------- | ------------ | ------------------------------------------------ |
| `status`     | enum            | —            | One of `pending`, `approved`, `rejected`, `archived`. |
| `date_from`  | datetime (ISO)  | —            | Lower bound on `created_at` (inclusive).         |
| `date_to`    | datetime (ISO)  | —            | Upper bound on `created_at` (inclusive).         |
| `sort`       | string          | `created_at` | One of `id`, `title`, `status`, `owner`, `amount`, `created_at`. |
| `descending` | bool            | `true`       | Sort direction.                                  |
| `offset`     | int (>=0)       | `0`          | Pagination offset.                               |
| `limit`      | int (1..200)    | `20`         | Page size.                                       |

## ⚙️ How to Run
```bash
# Run the SDD version
python makeup.py

# Run the Vibe Coded version
python makeup_store.py

Acknowledgments
A sincere thank you to the professors and instructors of the Future of Software Development with LLM: Spec Driven Development workshop at IIT Madras. The insights provided regarding state management, AI agent workflows, and the transition from chaotic prompt engineering to structured SDD architecture have been incredibly valuable to my engineering toolkit.
