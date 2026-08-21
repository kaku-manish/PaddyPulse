# PaddyPulse

PaddyPulse is an AI-powered platform for monitoring and managing rice (paddy) cultivation. It combines a React frontend, a Python FastAPI backend, and YOLO-based machine learning models to detect diseases from images, integrate IoT sensor data, and provide actionable recommendations.

**Quick summary:**
- **Frontend:** React (Vite) + Tailwind, bilingual UI (English / Telugu)
- **Backend:** Python (FastAPI), REST endpoints, ML integration
- **ML:** YOLOv8 models and training scripts for paddy disease classification

**This README** gives a concise overview, local setup instructions, where to find important files, and next steps.

**Project structure (high level)**

- `Frontend/` — React app and client (Vite). See `Frontend/README.md` for more details.
- `backend/` — Python backend, API routes, database helpers, ML inference wrappers.
- `paddy_disease_model/` & `runs/` — training artifacts and model weights (YOLO).

**Prerequisites**

- Git
- Python 3.10+ (for backend and ML)
- Node.js / npm (for frontend client)

**Quickstart - Backend**

1. Open a terminal and create a virtual environment:

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

2. Run the backend (example):

```powershell
python main.py
# or use start_backend.bat from the repo root on Windows
```

Files to check in `backend/`:

- `main.py` — backend entrypoint
- `routes/` — API endpoints (auth, prediction, reports, etc.)
- `ml_engine/` & `ml_engine/predict_yolo.py` — ML inference and helpers

**Quickstart - Frontend (development)**

```bash
cd Frontend/client
npm install
npm run dev
```

The frontend README contains additional info: see `Frontend/README.md`.

**Machine learning / models**

- Trained weights are present under `yolov8n-cls.pt` (root) and `paddy_disease_model/runs/.../weights/`.
- Training and inference helpers are in `backend/ml_engine/` and `ml_engine/` subfolders. Use the `train_yolo.py` scripts in `ml_engine/` to retrain.

**Tests & utilities**

- Several test scripts exist under `backend/` such as `test_pipeline.py`, `test_report_image.py`, and `test_all_farms.py`.
- Database helpers and migration scripts are in `backend/database_migrations.py`, `setup_db.py` and `migrate_data.py`.

**Notes about nested Git metadata**

During repository preparation nested `.git` folders were detected in `Frontend/` and `backend/`. Those nested `.git` folders have been backed up to a folder placed outside the repository at:

```
C:\Users\kakum\Desktop\nested_git_backups_paddypulse
```

If you prefer to preserve sub-repo history as submodules, I can restore those backups and configure proper `git submodule` entries.

**Contributing**

- Create issues and pull requests on the repository.
- Follow existing code styles in frontend and backend folders. Run linters (`eslint`) before submitting frontend PRs.

**License & contact**

Add your license file (e.g., `LICENSE`) and a maintainer contact email if you want public contributions.

---

If you want, I can:

- Expand any section with exact run commands and environment variables (DB URL, Supabase settings).
- Convert the nested backups into submodules preserving history.
- Add CI (GitHub Actions) to run tests and linting on push.

Tell me which of the above you'd like next.