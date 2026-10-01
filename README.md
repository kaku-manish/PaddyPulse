# 🌾 PaddyPulse
### AI-Powered Paddy Disease Detection & Smart Farm Monitoring Platform

[![FastAPI](https://img.shields.io/badge/Backend-FastAPI%200.111-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/Frontend-React%2019%20%7C%20Vite-61DAFB?style=for-the-badge&logo=react&logoColor=black)](https://react.dev/)
[![YOLOv8](https://img.shields.io/badge/ML%20Vision-Ultralytics%20YOLOv8-00FFFF?style=for-the-badge&logo=yolo&logoColor=black)](https://github.com/ultralytics/ultralytics)
[![Python](https://img.shields.io/badge/Language-Python%203.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![PostgreSQL](https://img.shields.io/badge/Cloud%20DB-Supabase%20PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)](https://supabase.com)
[![SQLite](https://img.shields.io/badge/Local%20DB-SQLite3-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://sqlite.org)
[![Tailwind CSS](https://img.shields.io/badge/Styling-Tailwind%20CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com)

> **PaddyPulse** is an end-to-end precision agriculture platform combining **YOLOv8 computer vision**, **IoT environmental telemetry**, **agronomic risk modeling**, **automated multilingual PDF/WhatsApp reporting**, and an **interactive bilingual dashboard (English & Telugu)** to detect paddy crop diseases early, forecast outbreak trajectories, and provide actionable treatment guidance for rice farmers.

---

## 📖 Table of Contents
1. [Project Overview](#-project-overview)
2. [Problem Statement](#-problem-statement)
3. [Key Features](#-key-features)
4. [Supported Paddy Diseases](#-supported-paddy-diseases)
5. [Technology Stack](#-technology-stack)
6. [System Architecture](#-system-architecture)
7. [How PaddyPulse Works (Step-by-Step Workflow)](#-how-paddypulse-works)
8. [Machine Learning Pipeline](#-machine-learning-pipeline)
9. [IoT & Environmental Telemetry Integration](#-iot--environmental-telemetry-integration)
10. [Drone Technology & Aerial Survey Integration](#-drone-technology--aerial-survey-integration)
11. [Backend Architecture](#-backend-architecture)
12. [API Endpoints Reference](#-api-endpoints-reference)
13. [Frontend Architecture](#-frontend-architecture)
14. [Database Design & Schema](#-database-design--schema)
15. [Project Structure](#-project-structure)
16. [Installation & Setup](#-installation--setup)
17. [Environment Configuration](#-environment-configuration)
18. [Running the Application](#-running-the-application)
19. [Example Prediction Lifecycle](#-example-prediction-lifecycle)
20. [Application Screenshots](#-application-screenshots)
21. [Testing Suite](#-testing-suite)
22. [Engineering Decisions & Technical Challenges](#-engineering-decisions--technical-challenges)
23. [Future Enhancements](#-future-enhancements)
24. [Real-World Use Case](#-real-world-use-case)
25. [Project Highlights](#-project-highlights)
26. [Author & Contact](#-author--contact)

---

## 🌟 Project Overview

Rice (*Oryza sativa*) is the primary dietary staple for more than 3.5 billion people worldwide. However, paddy yields are vulnerable to severe bacterial and fungal pathogen infections, resulting in an estimated **20% to 40% annual yield loss** if left unmanaged.

**PaddyPulse** was built to bridge the gap between advanced artificial intelligence and practical grassroots agriculture. Rather than treating disease diagnosis as an isolated image classification task, PaddyPulse treats crop health as a multi-dimensional ecosystem problem by synthesizing:
- **Computer Vision:** Fine-tuned YOLOv8 deep learning models for multi-disease leaf classification and visual defect annotation.
- **Computer Vision Preprocessing:** Color-space heuristics (HSV greenness ratio analysis) to filter invalid, non-plant imagery before model inference.
- **Environmental Context (IoT):** Soil moisture, ambient temperature, relative humidity, and water level monitoring to gauge pathogen reproduction viability.
- **Agronomic Risk Decision Engine:** Mathematical synthesis of Disease Severity (DSS), Weather Risk Index (WRI), Soil Stress Index (SSI), and Historical Trends (HTF).
- **Economic Treatment Planning:** Accurate per-acre chemical dosage calculations, equipment costs, labor expense estimates, and comparison against secondary/generic chemical alternatives.
- **Farmer-Centric Accessibility:** Instant A4 PDF reports (ReportLab), shareable WhatsApp infographic cards (Pillow), and a bilingual interface in **English** and **Telugu**.

---

## 🚨 Problem Statement

Traditional paddy cultivation faces persistent operational hurdles:

1. **Delayed Disease Identification:** Farmers typically recognize symptoms only after discoloration or necrosis has spread across large field patches, drastically lowering treatment efficacy.
2. **Visual Misdiagnosis:** Several paddy diseases (such as *Bacterial Leaf Blight* vs. *Brown Spot* or early-stage *Blast*) share similar visual symptoms, leading to incorrect chemical usage.
3. **Blanket Chemical Application:** Farmers often over-spray expensive, broad-spectrum fungicides without knowing the precise severity or optimal weather window, leading to chemical run-off, soil toxicity, and unnecessary financial debt.
4. **Lack of Environmental Correlation:** Pathogen spore germination depends heavily on microclimates (e.g., temperatures between 24°C–30°C coupled with humidity above 85%). Traditional diagnosis ignores current and forecast field conditions.
5. **Language & Usability Barriers:** Most digital agriculture apps are strictly in English and provide complex charts that fail to reach regional farmers who require clear, localized advice via familiar channels like WhatsApp.

**PaddyPulse addresses these challenges** by delivering sub-second AI diagnoses from field photographs or drone surveys, pairing the diagnosis with ambient environmental telemetry, calculating tailored treatment budgets, and publishing actionable prescriptions in the farmer's native language.

---

## ✨ Key Features

| Category | Feature | Description |
| :--- | :--- | :--- |
| **AI Vision** | **YOLOv8 Disease Classification** | Fine-tuned `yolov8n-cls` model identifying 10 paddy health classes with top-1 and top-3 multi-disease detection. |
| **AI Vision** | **OpenCV Crop Validation** | HSV color mask filters non-crop uploads (requires $\ge 10\%$ green vegetation) to avoid false inferences. |
| **AI Vision** | **Visual Anomaly Annotation** | Automatic generation of analyzed image overlays highlighting affected leaf regions using OpenCV and Ultralytics plotting. |
| **IoT & Sensors** | **Field Telemetry Monitoring** | Real-time and historical logging of soil moisture, ambient temperature, humidity, and water levels. |
| **Decision Engine** | **Agronomic Risk Scoring** | Multi-factor risk calculation combining Disease Severity (DSS), Weather Risk (WRI), Soil Stress (SSI), and Trend Multipliers. |
| **Outbreak Prediction** | **7-Day & 14-Day Forecasting** | Predictive outbreak modeling forecasting risk escalation probabilities based on weather trends and crop growth stages. |
| **Geospatial** | **Field Heatmap Tessellation** | Leaflet-powered GIS heatmap dividing fields into 10-meter grid tiles with Point-in-Polygon spatial infection clustering. |
| **Economics** | **Cost & Dosage Estimator** | Calculates chemical quantity required per acre, equipment hire, and labor costs with alternative chemical cost comparisons. |
| **E-Commerce** | **Medicine Marketplace** | In-app order placement pipeline for recommended agrochemicals with complete order tracking and history. |
| **Reporting** | **Automated PDF Health Reports** | Server-side generated multi-page A4 PDF diagnostic reports rendered in English or Telugu via ReportLab. |
| **Reporting** | **WhatsApp Diagnostic Cards** | Generation of lightweight, shareable PNG infographic cards tailored for instant WhatsApp distribution. |
| **Automation** | **APScheduler Cron Service** | Background jobs running automated daily health scans (6:00 PM) and weekly agricultural summaries (Sunday 8:00 AM). |
| **Management** | **Farm & Zone Administration** | Multi-farm profile management, field boundary polygon mapping, and crop phenological stage tracking. |
| **Drone Operations**| **Operator Booking & Payouts** | Commercial drone pilot booking system with KYC verification, per-acre quotes, scheduling, and operator payout tracking. |
| **Localization** | **Bilingual Interface** | English and Telugu translation toggling across the entire dashboard powered by `i18next`. |
| **Security** | **JWT Authentication** | Role-based authorization (`farmer`, `admin`) secured with bcrypt password hashing. |

---

## 🦠 Supported Paddy Diseases

PaddyPulse is trained on the benchmark **Paddy Doctor Dataset** covering **10 distinct classes** (9 pathological conditions and 1 healthy control class):

| Disease Class | Biological Agent / Type | Visual Symptoms | Model Output Label | First-Line Chemical Treatment |
| :--- | :--- | :--- | :--- | :--- |
| **Bacterial Leaf Blight** | *Xanthomonas oryzae pv. oryzae* | Water-soaked lesions turning yellow/gray with wavy margins along leaf tips | `bacterial_leaf_blight` | Copper Hydroxide 50% WP / Streptomycin Sulfate |
| **Bacterial Leaf Streak** | *Xanthomonas oryzae pv. oryzicola* | Narrow, brownish translucent interveinal streaks with tiny amber bacterial beads | `bacterial_leaf_streak` | Copper Oxychloride / Agrimycin |
| **Bacterial Panicle Blight** | *Burkholderia glumae* | Discoloration of florets, aborted panicles remaining erect at maturity | `bacterial_panicle_blight` | Oxolinic Acid / Kasugamycin |
| **Blast** | *Magnaporthe oryzae* (Fungal) | Diamond-shaped / spindle lesions with gray/whitish centers and dark borders | `blast` | Tricyclazole 75% WP / Isoprothiolane 40% EC |
| **Brown Spot** | *Bipolaris oryzae* (Fungal) | Oval, dark brown lesions with yellow halo across leaf blades and glumes | `brown_spot` | Mancozeb 75% WP / Propiconazole 25% EC |
| **Dead Heart** | *Scirpophaga incertulas* (Stem Borer) | Larval boring causing central tiller shoots to dry, turn yellow, and detach | `dead_heart` | Cartap Hydrochloride 4% GR / Chlorantraniliprole |
| **Downy Mildew** | *Sclerophthora macrospora* | Chlorotic yellow stripes, leaf curling, stunted growth, twisted panicles | `downy_mildew` | Metalaxyl + Mancozeb / Azoxystrobin |
| **Hispa** | *Dicladispa armigera* (Insect pest) | White parallel streaks scraped on upper leaf epidermis; leaves wither into blistered parchment | `hispa` | Chlorpyrifos 20% EC / Quinalphos 25% EC |
| **Normal (Healthy)** | N/A (Control) | Clean green leaves, uniform tillering, absence of chlorosis or fungal spots | `normal` | Routine monitoring & balanced N-P-K fertilization |
| **Tungro** | Rice Tungro Bacilliform/Spherical Virus (GLH vector) | Yellow-orange leaf discoloration, delayed flowering, stunted tiller height | `tungro` | Imidacloprid 17.8% SL (Leafhopper vector control) |

---

## 💻 Technology Stack

| Layer | Technology | Version / Specification | Role in Project |
| :--- | :--- | :--- | :--- |
| **Frontend Framework** | **React.js** | `^19.2.0` | Reactive component hierarchy and user interface |
| **Build Tool** | **Vite** | `^5.x` / ES Modules | Development server, hot-module replacement, and production bundling |
| **Styling** | **Tailwind CSS** | `^3.4` | Responsive layout, modern dark/light styling, and UI components |
| **Animations** | **GSAP & Framer Motion** | GSAP `^3.14`, Framer Motion `^12.30` | Header typography reveals (`SplitText`) and smooth state transitions |
| **Mapping & GIS** | **Leaflet & React-Leaflet** | Leaflet `^1.9.4`, React-Leaflet `^5.0.0` | Interactive field zone maps and infection heatmaps |
| **Data Visualization** | **Recharts** | `^3.7.0` | Severity trend forecasts, outbreak curves, and telemetry telemetry charts |
| **Internationalization**| **i18next** | `^25.7.3` & `react-i18next` | Runtime switching between English (`en`) and Telugu (`te`) |
| **Iconography** | **Lucide React** | `^0.563.0` | Agricultural and dashboard vector iconography |
| **Backend Framework** | **FastAPI** | `0.111.0` | Asynchronous REST API layer, request validation, and OpenAPI documentation |
| **ASGI Web Server** | **Uvicorn** | `0.30.1` | High-performance asynchronous Python web server |
| **Machine Learning** | **Ultralytics YOLOv8** | Fine-tuned `yolov8n-cls` | In-process paddy disease classification and visual annotation |
| **Computer Vision** | **OpenCV (Headless)** | `opencv-python-headless` | Image matrix manipulation, HSV greenness segmentation, and file export |
| **Data Science** | **NumPy, Pandas, Scikit-learn** | Latest stable | Metric evaluation, array mathematics, and statistical trend modeling |
| **Primary Database (Cloud)**| **Supabase PostgreSQL** | `psycopg` v3 (`>=3.2.0`) | Production cloud storage for users, farms, scans, and telemetry |
| **Fallback Database (Local)**| **SQLite3 / aiosqlite** | `aiosqlite 0.20.0` | Zero-configuration local database (`agriculture.db`) for offline development |
| **Task Scheduling** | **APScheduler** | `3.11.2` (`AsyncIOScheduler`) | Automated cron background jobs for daily and weekly report batches |
| **Document Generation**| **ReportLab & Pillow** | ReportLab + PIL | Dynamic generation of A4 PDF reports and PNG WhatsApp visual cards |
| **Security & Auth** | **PyJWT & Passlib** | `pyjwt 2.8.0`, `passlib[bcrypt] 1.7.4` | JWT bearer token creation, validation, and bcrypt salt hashing |

---

## 🏛️ System Architecture

PaddyPulse follows a decoupled, service-oriented architecture designed to handle concurrent inference and real-time telemetry updates.

```mermaid
flowchart TB
    subgraph Client_Layer ["Client Layer (Bilingual UI)"]
        A[Farmer / Drone Pilot / Admin]
        B[React 19 + Vite Dashboard]
        A -->|Browser / Mobile| B
        B -->|Toggle Locale| B1[i18next Engine: English / Telugu]
        B -->|Interactive Maps| B2[Leaflet GIS & Recharts Visualizations]
    end

    subgraph API_Gateway ["Backend Gateway (FastAPI on Port 3000)"]
        C[FastAPI Core Server & CORS Middleware]
        B -->|REST API Requests & Multipart Form Data| C
        C --> D1[Auth Router]
        C --> D2[Drone & Image Router]
        C --> D3[Farm & Zone Router]
        C --> D4[Precision & Heatmap Router]
        C --> D5[Prediction & Forecast Router]
        C --> D6[Cost & Orders Router]
        C --> D7[Reports Router]
        C --> D8[IoT Ingestion Router]
    end

    subgraph Compute_Engines ["Domain Analytics & AI Processing"]
        E1[OpenCV HSV Pre-validator]
        E2[YOLOv8 In-Process Inference Engine]
        E3[Precision Agronomy Engine: DSS + WRI + SSI]
        E4[Predictive Outbreak & Trend Engine]
        E5[ReportLab & Pillow Document Engine]
        E6[APScheduler Background Cron]
        
        D2 --> E1 --> E2
        D4 --> E3
        D5 --> E4
        D7 --> E5
        E6 -->|Daily & Weekly Triggers| E5
    end

    subgraph Storage_Layer ["Data Persistence & Storage"]
        F1[(Cloud: Supabase PostgreSQL via psycopg3)]
        F2[(Local: SQLite3 agriculture.db via aiosqlite)]
        F3[Static File Store /uploads]
        
        C -->|DATABASE_URL present| F1
        C -->|Default Fallback| F2
        E2 -->|Annotated JPG| F3
        E5 -->|Generated PDF & PNG Cards| F3
    end

    D7 -->|Download URLs / Stream| B
```

---

## 🔄 How PaddyPulse Works

```mermaid
sequenceDiagram
    autonumber
    actor Farmer as Farmer / Operator
    participant UI as React Client (Dashboard)
    participant API as FastAPI Backend (/drone/analysis)
    participant CV as OpenCV Image Validator
    participant YOLO as YOLOv8 ML Engine (best.pt)
    participant Engine as Precision & Cost Engine
    participant DB as Database (SQLite / Postgres)
    participant Doc as Report Engine (PDF / Card)

    Farmer->>UI: Selects farm & uploads crop photograph
    UI->>API: POST /drone/analysis (Multipart Form: image, farm_id)
    API->>CV: validate_image(image_path)
    alt Green Pixel Ratio < 10%
        CV-->>API: Rejected ("Not enough greenery")
        API-->>UI: 400 Bad Request (Invalid Crop Image)
    else Green Pixel Ratio >= 10%
        CV-->>API: Image Approved
        API->>YOLO: run_prediction(image_path)
        YOLO-->>API: primary_disease, confidence, all_detected, annotated_image
        API->>DB: INSERT into disease_analyses (disease_name, confidence, severity)
        API->>Engine: estimate_cost(farm_id) & generate_recommendation()
        Engine-->>API: Dosage, Chemical cost, Labor cost, Spray timing
        API-->>UI: 200 OK (JSON with classification, advice & annotated image)
        UI-->>Farmer: Displays disease details, confidence & visual overlay
        
        opt Download Full Report
            Farmer->>UI: Clicks "Generate PDF Report"
            UI->>API: POST /reports/generate (farm_id, language='te')
            API->>Doc: generate_pdf() & generate_whatsapp_cards()
            Doc-->>API: PDF & PNG Card Filepaths
            API->>DB: INSERT into reports
            API-->>UI: PDF download URL & Card image URL
            UI-->>Farmer: Downloads Telugu Health Report & WhatsApp Card
        end
    end
```

### Execution Steps
1. **User Authentication & Farm Selection:** The farmer logs in via JWT authentication and selects their registered farm profile.
2. **Image Ingestion:** The farmer captures or uploads an infected leaf photo (or submits a drone survey batch).
3. **OpenCV Heuristic Validation:** The backend inspects the image in the HSV color space. If green pixels account for less than 10% of the image surface, the upload is rejected immediately to prevent erroneous non-plant predictions.
4. **YOLOv8 In-Process Inference:** The image is passed to the pre-loaded YOLOv8 model in RAM. The model calculates class probabilities across all 10 trained categories.
5. **Multi-Disease Thresholding:** If secondary classifications exceed a 15% confidence threshold, they are logged alongside the primary disease to account for complex co-infections.
6. **Visual Defect Overlay:** Ultralytics plotting and OpenCV write an annotated copy (`_analyzed.jpg`) showcasing detected patterns.
7. **Agronomic Risk Synthesis:** The backend correlates visual results with current field IoT sensor logs (temperature, humidity, soil moisture) to compute environmental risk multipliers.
8. **Cost & Dosage Calculation:** Farm acreage is multiplied against dosage tables from the agricultural knowledge base to calculate chemical quantity, medicine costs, and labor estimates.
9. **Localized Reporting:** If requested, the report engine synthesizes the diagnosis, field maps, and dosage guidance into a localized A4 PDF and a compact WhatsApp graphic card in English or Telugu.

---

## 🧠 Machine Learning Pipeline

### 1. Model Architecture
- **Base Architecture:** YOLOv8 Nano Classifier (`yolov8n-cls`) from Ultralytics.
- **Task:** Multi-Class Image Classification (with multi-label thresholding during post-processing).
- **Input Resolution:** $224 \times 224 \times 3$ RGB.
- **Model Size:** 5.56 MB (`best.pt`).

### 2. Dataset & Training Configuration
- **Dataset:** Paddy Doctor Disease Classification benchmark dataset.
- **Training Script:** `backend/ml_engine/train_yolo.py`
- **Output Weights:** `backend/runs/classify/ml_engine/runs/paddy_cls2/weights/best.pt`
- **Hardware Profile:** Trained with single-worker CPU/GPU compatible configuration (`batch=8`, `workers=1`, `epochs=30`, `imgsz=224`).

### 3. Quantitative Training Metrics
Metrics logged during the training run (`backend/runs/classify/ml_engine/runs/paddy_cls2/results.csv`):

| Epoch | Top-1 Accuracy | Top-5 Accuracy | Training Loss | Validation Loss | Learning Rate |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | 66.00% | 96.55% | 1.7822 | 0.9936 | 0.000237 |
| 2 | 79.03% | 98.51% | 1.1973 | 0.6050 | 0.000460 |
| 3 | 85.46% | 99.10% | 0.9585 | 0.4424 | 0.000666 |
| 4 | 89.72% | 99.60% | 0.8253 | 0.3218 | 0.000643 |
| 5 | 91.58% | 99.73% | 0.7112 | 0.2775 | 0.000619 |
| **6 (Best)**| **94.68%** | **99.74%** | **0.6372** | **0.1925** | **0.000596** |

> *Note:* Training achieved **94.68% Top-1 accuracy** and **99.74% Top-5 accuracy** with validation loss decreasing steadily to **0.1925**.

### 4. Inference & Post-Processing Architecture
- **In-Process Singleton:** Instead of invoking slow OS subprocesses on every upload, `backend/routes/drone.py` initializes the model once at server startup (`get_model()`), ensuring **sub-second inference response times (< 250ms on standard CPUs)**.
- **Multi-Label Detection Logic:**
  ```python
  primary_disease = result.names[top5_indices[0]]
  primary_conf = top5_confs[0]
  detected_diseases = [primary_disease]
  for i in range(1, min(3, len(top5_indices))):
      if top5_confs[i] >= 0.15:  # Secondary disease threshold
          detected_diseases.append(result.names[top5_indices[i]])
  ```

---

## 📡 IoT & Environmental Telemetry Integration

PaddyPulse pairs visual disease classification with microclimate telemetry to predict disease risk before visible symptoms become irreversible.

### 1. Ingested Telemetry Parameters
- **Soil Moisture (%):** Monitored to detect water stress or root hypoxia.
- **Water Level (cm):** Evaluates whether paddies are properly submerged or draining excessively.
- **Ambient Temperature (°C):** Tracks thermal conditions conducive to fungal blast ($22^\circ\text{C} - 30^\circ\text{C}$) or brown spot ($25^\circ\text{C} - 35^\circ\text{C}$).
- **Relative Humidity (%):** High humidity ($> 85\%$) exponentially accelerates spore germination.
- **NPK & Soil pH:** Used for soil nutrient balancing and crop stage recommendations.

### 2. Agronomic Decision Formula
In `backend/engine/precision_engine.py`, the risk engine calculates an **Overall Risk Score ($0 - 100$)**:

$$\text{Risk Score} = \Big( (\text{DSS} \times 0.50) + (\text{WRI} \times 0.25) + (\text{SSI} \times 0.15) + (\text{HTF} \times 0.10) \Big) \times M_{\text{stage}}$$

- **DSS (Disease Severity Score):** Derived from bounding area coverage and model prediction confidence.
- **WRI (Weather Risk Index):** Evaluated from relative humidity, temperature, and rain probability.
- **SSI (Soil Stress Index):** Evaluated from soil moisture deficits and standing water variance.
- **HTF (Historical Trend Factor):** Computed from week-over-week rate of change in infection severity.
- **$M_{\text{stage}}$ (Crop Stage Multiplier):** Phenological weighting ($1.2\times$ for Seedling, $1.0\times$ for Tillering, $1.5\times$ for Panicle emergence, $1.8\times$ for Flowering, $0.8\times$ for Maturity).

### 3. Spray Window Weather Constraints
Recommendations enforce specific weather windows (`backend/config/disease_rules.py`) to prevent chemical wash-off and spray drift:
- Maximum Wind Speed: $\le 15 \text{ km/h}$
- Rain-Free Forecast: $\ge 6 \text{ hours}$
- Temperature Range: $10^\circ\text{C} \le T \le 32^\circ\text{C}$
- Minimum Relative Humidity: $\ge 40\%$

---

## 🚁 Drone Technology & Aerial Survey Integration

PaddyPulse incorporates a dedicated aerial survey and drone fleet infrastructure designed for field-scale crop scouting, automated aerial disease screening, and commercial drone operator dispatch.

```mermaid
flowchart LR
    A[Drone Survey Flight] -->|Overhead Canopy Capture| B(High-Res Aerial Orthophoto)
    B -->|POST /drone/analysis| C{OpenCV Green Mask}
    C -- Failed (<10% Green) --> D[Reject: Camera Angle Off-Target]
    C -- Passed (>=10% Green) --> E[In-Process YOLOv8 Inference]
    E --> F[Generate Annotated Visual Map]
    E --> G[(Save DB: source='drone')]
    G --> H[Admin Drone Control Center]
    G --> I[Branded Drone PDF Report: 'Analyzed Drone View']
```

### 1. Aerial Survey & Ingestion Pipeline
While single-leaf smartphone uploads assist localized spot-checks, managing large-scale rice paddies requires aerial monitoring:
- **Overhead Aerial Ingestion (`POST /drone/analysis`):** Ingests aerial flight imagery along with farm identification (`farm_id`), predicted disease classes, and field severity indicators.
- **Canopy Verification Pre-Filter:** Utilizes OpenCV HSV color masking to verify that aerial camera angles capture viable crop canopy rather than irrigation canals, field bunds, or bare soil.
- **Sub-Second Aerial Classification:** Evaluates images using the in-process YOLOv8 model, generating an annotated orthophoto crop (`_analyzed.jpg`) and logging the entry to the `disease_analyses` table with `source='drone'`.
- **Historical Survey Auditing (`GET /drone/history/{farmId}`):** Maintains an immutable audit trail of past aerial surveys, enabling longitudinal comparison of disease progression across flight dates.

### 2. Commercial Drone Operator Marketplace (`/ops`)
PaddyPulse features a dedicated module connecting farmers with certified commercial drone pilots:
- **Pilot KYC & Verification:** Validates pilot licensing, experience flight counts, and verification status (`kyc_status: 'verified' | 'pending'`).
- **Dynamic Per-Acre Pricing:** Calculates automated survey quotations based on farm acreage and operator base rates (`base_rate_per_acre`, default ₹150/acre).
- **Booking & Flight Dispatch (`POST /ops/book`):** Enables farmers to schedule aerial surveys with exact GPS field coordinates (`lat`, `lng`) and desired survey dates.
- **Automated Payout Engine (`operator_payouts`):** Computes operator compensation upon completed scan delivery, including performance bonuses and delay penalties.

### 3. Drone-Specific Branded Health Reports
Reports generated from aerial survey data automatically receive custom drone branding via `backend/routes/reports.py` and `report_engine.py`:
- **Visual Badge:** Generates the `"AI Vision: Analyzed Drone View"` (or `"AI దృష్టి: Drone View"` in Telugu) banner directly on generated A4 PDF reports.
- **Spatial Alignment:** Embeds annotated aerial defect maps into the medical-style bulletin alongside chemical prescriptions, dosage requirements, and weather-safe flight/spray windows.

### 4. Administrative Drone Control Center
The platform provides administrative oversight via `AdminDroneAnalysis.jsx` and `AdminDroneReportControl.jsx`:
- **Flight & Batch Telemetry:** Real-time visibility into survey upload streams, multi-class confidence ratings, and operator schedules.
- **Simulated Survey Controls:** Allows administrators and researchers to initiate automated survey workflows and batch-process multi-zone field scans.

---

## 🛠️ Backend Architecture

The backend is built with **FastAPI** following clean modular separation between routing, business logic engines, database adapters, and machine learning components:

```text
backend/
├── main.py                     # Application entrypoint, CORS, static mounts, router setup
├── database.py                 # Dual database manager (Supabase Postgres & local SQLite)
├── setup_db.py                 # Database initialization script (29 relational tables)
├── seed_paddy_diseases.py      # Seeds 10 disease profiles and 18 medicine market prices
├── requirements.txt            # Python production dependencies
├── start_backend.bat           # Windows 1-click startup batch script
│
├── routes/                     # Modular API router controllers
│   ├── auth.py                 # Authentication, registration, JWT tokens, profile updates
│   ├── drone.py                # Image upload, OpenCV validation, YOLO inference, scan history
│   ├── farm.py                 # Farm status, user farm linkage, recommendation query
│   ├── precision.py            # Field scan batch ingestion, multi-factor risk assessment
│   ├── heatmap.py              # Spatial tessellation and GeoJSON grid generation
│   ├── prediction.py           # 7-day and 14-day outbreak forecasts, early alerts
│   ├── cost.py                 # Dosage calculation, price lookup, treatment estimation
│   ├── reports.py              # Report generation, PDF & WhatsApp card downloads
│   ├── iot.py                  # IoT telemetry ingestion (soil moisture, temperature, humidity)
│   ├── orders.py               # Agrochemical marketplace checkout and order tracking
│   ├── operators.py            # Commercial drone operator profiles, bookings, and payouts
│   ├── business.py             # SaaS subscription plans, scans, organizations, invoices
│   ├── geospatial.py           # GeoJSON boundaries, farm polygon coordinates
│   └── admin.py                # Platform administration, user overview, system stats
│
├── engine/                     # Core computational & agronomic engines
│   ├── recommender.py          # Blends IoT, drone, and crop knowledge into unified advice
│   ├── precision_engine.py     # Multi-variable decision engine (DSS, WRI, SSI, HTF)
│   ├── heatmap_engine.py       # Ray-casting point-in-polygon & spatial tile clustering
│   ├── forecast_engine.py      # Statistical trend forecasting for 7-day severity trajectories
│   ├── prediction_engine.py    # Outbreak probability modeling with weather factor rules
│   ├── report_engine.py        # ReportLab PDF synthesis & Pillow WhatsApp card generation
│   └── summary_engine.py       # Natural language multilingual advisory text generator
│
├── ml_engine/                  # Machine learning models & training artifacts
│   ├── train_yolo.py           # YOLOv8 classification training pipeline
│   ├── predict_yolo.py         # Subprocess inference fallback script
│   ├── validate_image.py       # HSV vegetation check script
│   └── runs/paddy_cls2/        # Best trained weights (best.pt) and metrics
│
├── services/
│   └── cron_service.py         # APScheduler background tasks (daily & weekly batch runs)
├── middleware/
│   └── auth.py                 # Bearer token JWT verification middleware
├── config/
│   └── disease_rules.py        # Agronomic rules, chemical dosages, and stage multipliers
└── uploads/                    # Physical storage for uploads, annotated photos, and PDFs
```

---

## 🌐 API Endpoints Reference

All endpoints are hosted by default on `http://localhost:3000`. Full interactive documentation is available at `/docs` (Swagger UI) and `/redoc` (ReDoc).

### Authentication & Profiles (`/auth`)
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/auth/register` | Registers a new farmer/user and creates a default farm entity |
| `POST` | `/auth/login` | Authenticates username/password and issues a JWT token |
| `PUT` | `/auth/profile` | Updates farmer name, phone number, location, and field size |

### Disease Detection & Drone Surveys (`/drone`)
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/drone/analysis` | Uploads crop photograph, validates vegetation, and executes YOLO prediction |
| `GET` | `/drone/history/{farmId}` | Fetches chronological scan history with original and annotated image links |

### Farm Management & Advisory (`/farm`)
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/farm/{farm_id}/status` | Aggregates farm profile, latest IoT reading, latest scan, and recommendations |
| `GET` | `/farm/user/{user_id}/status` | Retrieves farm status by associated user ID |

### Diagnostics & Automated Reports (`/reports`)
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/reports/generate` | Generates localized A4 PDF report and WhatsApp card (`en` or `te`) |
| `GET` | `/reports/{farm_id}` | Retrieves all generated reports for a specific farm |
| `GET` | `/reports/download/{filename}` | Streams generated PDF file to client |
| `GET` | `/reports/cards/{filename}` | Streams generated WhatsApp infographic card (PNG) to client |
| `GET` | `/reports/field/{farm_id}/message-summary`| Returns formatted natural language summary for SMS/WhatsApp |

### Outbreak Prediction & Forecasting (`/predict`)
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/predict/zone/{zone_id}/severity-forecast` | Calculates 7-day severity trend using historical risk data |
| `POST` | `/predict/sync/{zone_id}` | Triggers outbreak probability recalculation (7-day and 14-day) |
| `GET` | `/predict/field/{farm_id}/alerts` | Fetches active outbreak alert notifications |
| `GET` | `/predict/zone/{zone_id}/predictions` | Returns latest disease outbreak predictions and explanation reasons |

### Precision Agriculture & Heatmaps (`/precision` & `/heatmap`)
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/precision/scan-results` | Ingests drone batch detections and calculates zone risk breakdown |
| `GET` | `/heatmap/field/{field_id}` | Generates 10-meter GeoJSON spatial tile grid with infection density scores |

### Financial Cost Estimation (`/cost`)
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/cost/estimate/{farm_id}` | Calculates chemical quantities, brand prices, equipment, and labor costs |
| `POST` | `/cost/medicines` | Adds or updates medicines and brand unit prices |

### IoT Telemetry Ingestion (`/iot`)
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/iot/reading` | Ingests soil moisture, temperature, humidity, and water level readings |

### Agrochemical Marketplace (`/orders`)
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/orders` | Places an agrochemical order with delivery address and payment method |
| `GET` | `/orders/user/{user_id}` | Retrieves order history for a specific farmer |
| `GET` | `/orders` | Lists all marketplace orders (Admin view) |

### Commercial Drone Operators (`/ops`)
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/ops/operators` | Lists registered drone operators, ratings, and base rates per acre |
| `POST` | `/ops/book` | Books a drone flight survey for a given farm acreage |
| `GET` | `/ops/bookings/{org_id}` | Lists drone booking requests and execution statuses |

---

## 🎨 Frontend Architecture

The frontend is an interactive single-page application built on **React 19** and **Vite**, featuring an agricultural design system styled with **Tailwind CSS**, **Framer Motion**, and **GSAP**:

```text
Frontend/client/
├── src/
│   ├── main.jsx                    # React root mounting and i18n initialization
│   ├── App.jsx                     # Route definitions and ProtectedRoute role gates
│   ├── i18n.js                     # Localization setup with English and Telugu dictionaries
│   ├── api/
│   │   └── config.js               # API base URL configuration (http://localhost:3000)
│   ├── pages/
│   │   ├── Login.jsx               # Farmer / Admin authentication screen
│   │   └── Signup.jsx              # User registration and organization onboarding
│   └── components/
│       ├── Dashboard.jsx           # Main unified command center with tab navigation
│       ├── ImageUpload.jsx         # Drag-and-drop crop photo uploader with preview & diagnosis
│       ├── IoTSensors.jsx          # Real-time telemetry cards (Soil moisture, humidity, temp)
│       ├── ActionPlan.jsx          # Recommended chemical & organic treatment protocols
│       ├── CostEstimation.jsx      # Financial budgeting, brand comparisons, and cost breakdowns
│       ├── Reports.jsx             # PDF report generator and WhatsApp card preview modal
│       ├── DiseaseHeatmap.jsx      # Leaflet interactive field map with GeoJSON infection tiles
│       ├── SeverityForecast.jsx    # Recharts 7-day severity trajectory visualization
│       ├── PredictiveAlerts.jsx    # Early warning outbreak probability banners
│       ├── DiseaseHistory.jsx      # Historical log of previous scans and annotated images
│       ├── MedicineMarketplace.jsx # E-commerce checkout for prescribed treatments
│       ├── LanguageSelector.jsx    # English / Telugu toggle switch
│       ├── AgriChatbot.jsx         # AI agricultural query assistant
│       └── AdminDashboard.jsx      # Administrative drone oversight, user list, and orders
```

---

## 🗄️ Database Design & Schema

PaddyPulse employs an enterprise-grade relational schema comprising **29 tables** (created via `setup_db.py`). The application supports both **Cloud PostgreSQL (Supabase)** and **Local SQLite (`agriculture.db`)**:

```mermaid
erDiagram
    USERS ||--o{ FARMS : owns
    FARMS ||--o{ FIELD_ZONES : contains
    FARMS ||--o{ DISEASE_ANALYSES : logs
    FARMS ||--o{ SENSOR_READINGS : records
    FARMS ||--o{ REPORTS : generates
    FARMS ||--o{ ORDERS : places
    FIELD_ZONES ||--o{ SCAN_BATCHES : groups
    SCAN_BATCHES ||--o{ SCAN_DETECTIONS : contains
    FIELD_ZONES ||--o{ DISEASE_RISK_ASSESSMENTS : receives
    FIELD_ZONES ||--o{ DISEASE_PREDICTIONS : forecasts
    KB_DISEASES ||--o{ MEDICINE_PRICES : catalogs
    USERS ||--o{ DRONE_OPERATORS : registers
    DRONE_OPERATORS ||--o{ OPERATOR_BOOKINGS : accepts

    USERS {
        int id PK
        string username
        string password_hash
        string role
        string full_name
        string phone
    }

    FARMS {
        int id PK
        int user_id FK
        string farmer_name
        string location
        string soil_type
        float field_size
        string current_crop
    }

    DISEASE_ANALYSES {
        int id PK
        int farm_id FK
        string disease_name
        string severity
        float confidence
        string image_path
        string annotated_path
        string source
        datetime created_at
    }

    SENSOR_READINGS {
        int id PK
        int farm_id FK
        float temperature
        float humidity
        float soil_moisture
        datetime recorded_at
    }

    KB_DISEASES {
        int id PK
        string disease_name
        string medicine
        string medicine_secondary
        string dosage
        string timeline
        string preventive_measures
    }

    MEDICINE_PRICES {
        int id PK
        string medicine_name
        string brand_name
        float unit_price
        string unit
        string disease_name
    }

    REPORTS {
        int id PK
        int farm_id FK
        string title
        string file_path
        string card_path
        string status
        datetime created_at
    }
```

---

## 📁 Project Structure

```text
PaddyPulse/
├── README.md                       # Comprehensive Project Documentation
│
├── backend/                        # Python FastAPI Backend & ML Service
│   ├── main.py                     # Server entrypoint and router configuration
│   ├── database.py                 # Unified PostgreSQL / SQLite database driver
│   ├── setup_db.py                 # Database initialization and table creator
│   ├── seed_paddy_diseases.py      # Disease knowledge base and pricing seeds
│   ├── requirements.txt            # Python dependencies
│   ├── start_backend.bat           # 1-click Windows startup script
│   ├── routes/                     # 14 REST API routers
│   ├── engine/                     # 8 computational and agronomic engines
│   ├── ml_engine/                  # YOLOv8 training and inference scripts
│   ├── services/                   # APScheduler background tasks
│   ├── config/                     # Agronomic threshold and constraint rules
│   ├── tests/                      # Validation and pipeline test scripts
│   └── uploads/                    # Processed and annotated media artifacts
│
└── Frontend/
    └── client/                     # React 19 + Vite Frontend Application
        ├── package.json            # Node.js dependencies and scripts
        ├── vite.config.js          # Vite build and path alias configuration
        ├── tailwind.config.js      # Tailwind CSS design tokens
        ├── index.html              # HTML entry template
        └── src/
            ├── App.jsx             # React Router routing configuration
            ├── main.jsx            # Application root mounting
            ├── i18n.js             # English and Telugu localization
            ├── api/                # API client configuration
            ├── components/         # 27 modular React components
            └── pages/              # Login and Registration views
```

---

## ⚡ Installation & Setup

### Prerequisites
- **Git:** Version 2.30+
- **Python:** Version 3.10 to 3.12 installed ([python.org](https://www.python.org))
- **Node.js:** Version 18.0+ & npm 9.0+ ([nodejs.org](https://nodejs.org))

---

### Step 1: Clone the Repository
```bash
git clone https://github.com/kaku-manish/PaddyPulse.git
cd PaddyPulse
```

---

### Step 2: Backend Setup (Python & FastAPI)

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create and activate a Python virtual environment:
   - **Windows (PowerShell):**
     ```powershell
     python -m venv venv
     .\venv\Scripts\activate
     ```
   - **Linux / macOS:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. Install required Python packages:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. Initialize and seed the local database:
   ```bash
   python setup_db.py
   python seed_paddy_diseases.py
   ```
   *(Creates all 29 relational tables in `agriculture.db` and populates disease guidelines and medicine prices).*

---

### Step 3: Frontend Setup (React & Vite)

1. Open a new terminal and navigate to the frontend client directory:
   ```bash
   cd Frontend/client
   ```

2. Install Node dependencies:
   ```bash
   npm install
   ```

---

## ⚙️ Environment Configuration

### Backend Environment Variables
Create a `.env` file inside `backend/.env` (optional — defaults to local SQLite if omitted):

```env
# Server Port (Default: 3000)
PORT=3000

# JWT Authentication Secret Key
JWT_SECRET=your_super_secret_paddypulse_jwt_key

# Database Connection URL (Optional)
# If left commented or unset, the system automatically uses local SQLite (agriculture.db)
# DATABASE_URL=postgresql://postgres:password@db.supabase.co:5432/postgres
```

---

## 🚀 Running the Application

### Option A: Using the Windows Batch Script
You can double-click or run the provided script from the `backend/` folder:
```powershell
.\backend\start_backend.bat
```

### Option B: Manual Command-Line Startup

#### Terminal 1: Backend Server
```powershell
cd backend
.\venv\Scripts\activate
python -m uvicorn main:app --host 0.0.0.0 --port 3000 --reload
```
*Backend runs on:* `http://localhost:3000`  
*Interactive Swagger Documentation:* `http://localhost:3000/docs`

#### Terminal 2: Frontend Client
```powershell
cd Frontend/client
npm run dev
```
*Frontend runs on:* `http://localhost:5173`

---

### Default Credentials
| Role | Username | Password | Access Level |
| :--- | :--- | :--- | :--- |
| **System Administrator** | `admin` | `admin123` | Full access to Admin Console, drone oversight, and orders |
| **New Farmer** | *(Register via UI)* | *(User defined)* | Full access to Farm Dashboard, diagnosis, and reports |

---

## 🔬 Example Prediction Lifecycle

```text
[Farmer UI]
    │ 1. Uploads leaf photograph of infected crop (e.g., blast_sample.jpg)
    ▼
[FastAPI /drone/analysis]
    │ 2. OpenCV reads image and verifies HSV greenness ratio >= 0.10
    ▼
[YOLOv8 ML Engine (best.pt)]
    │ 3. Classifies image:
    │    - Dominant Class: Blast (Confidence: 94.6%)
    │    - Secondary Class: Brown Spot (Confidence: 16.2% -> Flagged as co-infection)
    │ 4. Generates visual overlay: uploads/blast_sample_analyzed.jpg
    ▼
[Precision Agronomy Engine]
    │ 5. Reads field IoT telemetry: Humidity = 88%, Temp = 27°C (High fungal risk)
    │ 6. Computes Overall Risk Score: 78 / 100 (CRITICAL)
    │ 7. Determines Optimal Spray Window: 06:00 AM - 09:00 AM (Wind < 15 km/h)
    ▼
[Financial Cost Engine]
    │ 8. Pulls dosage for 2-acre farm:
    │    - Primary Chemical: Tricyclazole 75% WP (240g total) -> ₹144
    │    - Equipment Cost: ₹300 | Application Labor: ₹300
    │    - Total Estimated Treatment Cost: ₹744
    ▼
[Report Generation Engine]
    │ 9. Synthesizes Telugu A4 PDF and WhatsApp PNG Card
    ▼
[Farmer Dashboard]
    │ 10. Displays diagnosis, treatment steps, and one-click WhatsApp share
```

---

## 📸 Application Screenshots

*(Placeholders for system interface screenshots)*

### 1. Farmer Command Dashboard & Environmental Telemetry
![Farmer Dashboard Preview](https://raw.githubusercontent.com/kaku-manish/PaddyPulse/main/docs/screenshots/dashboard.png)
*Displays real-time ambient temperature, humidity, soil moisture readings, crop stage, and quick diagnostic actions.*

### 2. AI Crop Leaf Disease Analysis & Visual Anomaly Map
![AI Disease Analysis Preview](https://raw.githubusercontent.com/kaku-manish/PaddyPulse/main/docs/screenshots/disease_analysis.png)
*Interactive upload interface showing OpenCV validation, predicted disease name, confidence score, and annotated overlay.*

### 3. Spatial Field Heatmap & Infection Clustering
![Field Heatmap Preview](https://raw.githubusercontent.com/kaku-manish/PaddyPulse/main/docs/screenshots/heatmap.png)
*Leaflet.js GIS map displaying 10-meter grid tiles with color-coded infection severity across field zones.*

### 4. Bilingual PDF Health Report & WhatsApp Infographic Card
![Report Generation Preview](https://raw.githubusercontent.com/kaku-manish/PaddyPulse/main/docs/screenshots/report.png)
*Downloadable A4 medical-style crop health report and shareable WhatsApp graphic rendered in Telugu.*

---

## 🧪 Testing Suite

The repository contains automated test scripts located in `backend/` to validate model execution, document rendering, and database queries:

| Test Script | Target Component | Description | Execution Command |
| :--- | :--- | :--- | :--- |
| `test_pipeline.py` | OpenCV & YOLO Pipeline | Generates a synthetic crop image, tests HSV validation, and runs YOLO inference | `python test_pipeline.py` |
| `test_report_image.py` | ReportLab & Pillow Engine | Tests end-to-end PDF canvas generation and WhatsApp square card creation | `python test_report_image.py` |
| `test_all_farms.py` | Database Join Logic | Tests SQL query consistency across all registered farms and disease analyses | `python test_all_farms.py` |
| `test_report_query.py` | Report Data Fetching | Verifies relational joins between risk assessments and drone analysis records | `python test_report_query.py` |

---

## 💡 Engineering Decisions & Technical Challenges

1. **In-Process Inference vs. External Subprocesses:**
   - *Problem:* Early versions executed inference via Python CLI subprocesses, incurring noticeable process startup overhead and memory spikes.
   - *Solution:* Refactored the architecture in `backend/routes/drone.py` to load the YOLOv8 model as an in-process singleton at server startup, decreasing inference response times to **under 250ms**.
2. **False-Positive Filtering via Color Space Heuristics:**
   - *Problem:* Users occasionally upload arbitrary non-crop images (documents, human faces, machinery), confusing deep learning classifiers.
   - *Solution:* Implemented an OpenCV HSV vegetation mask (`validate_image()`) checking for a minimum 10% green pixel ratio before routing images to the neural network.
3. **Dual Database Architecture (Cloud + Local Fallback):**
   - *Problem:* Requiring a live cloud database hampers local development and offline field demonstrations.
   - *Solution:* Designed a dynamic database layer in `database.py` that connects to cloud PostgreSQL (Supabase) if `DATABASE_URL` is configured, while automatically defaulting to a local SQLite database (`agriculture.db`) with SQL dialect translation (`?` to `$n`).
4. **Offline-First Regional Reporting:**
   - *Problem:* Rural farmers frequently have unstable internet connectivity and struggle to navigate multi-tab web applications.
   - *Solution:* Added server-side generation of lightweight, compressed WhatsApp infographic cards (Pillow) and localized A4 PDFs (ReportLab) in Telugu, allowing farmers to share and store advice offline.

---

## 🔮 Future Enhancements

- [ ] **Live Drone WebRTC / RTSP Video Stream Inference:** Real-time aerial video frame processing for continuous field flight surveys.
- [ ] **Edge Deployment on NVIDIA Jetson / Raspberry Pi:** Packaging the YOLOv8 inference engine for autonomous, offline edge operation mounted directly on agricultural spray drones.
- [ ] **Satellite Multispectral Indexing:** Integrating Sentinel-2 / Landsat satellite imagery for automated NDVI (Normalized Difference Vegetation Index) calculation across large agricultural cooperatives.
- [ ] **Automated WhatsApp Business Bot:** Directly receiving farmer leaf photos and dispatching diagnostic cards via the official WhatsApp Cloud API.
- [ ] **Hardware LoRaWAN Sensor Gateways:** Long-range wireless integration with field-installed soil NPK probes and solar-powered weather stations.

---

## 🌾 Real-World Use Case

1. **Morning Inspection:** A smallholder rice farmer in Andhra Pradesh notices yellowing lesions with dark borders on crop leaves.
2. **Photograph Capture:** The farmer opens PaddyPulse on a mobile browser and uploads a photo of the affected plant.
3. **Automated Verification:** The system verifies the image contains paddy vegetation and triggers the YOLOv8 classifier.
4. **Immediate Diagnosis:** PaddyPulse identifies **Rice Blast** with 94.6% confidence and flags a secondary risk of **Brown Spot**.
5. **Contextual Risk Assessment:** Correlating the diagnosis with the farm's telemetry (88% relative humidity and 27°C ambient temperature), the engine marks the outbreak risk as **CRITICAL**.
6. **Actionable Prescription:** The platform recommends spraying *Tricyclazole 75% WP* at 120g per acre, prescribes an optimal spray window of *06:00 AM – 09:00 AM* to prevent chemical drift, and calculates a total chemical expense of ₹744.
7. **WhatsApp Sharing:** The farmer downloads the Telugu summary card and forwards it to the local agricultural officer and input retailer via WhatsApp.

---

## 🏆 Project Highlights

- **Production-Grade Computer Vision:** Fine-tuned YOLOv8 classification achieving **94.68% Top-1 Accuracy** across 10 benchmark paddy health classes.
- **Multimodal Agronomic Intelligence:** Synthesizes image classification with real-time IoT microclimate telemetry to generate contextual risk scores.
- **Micro-Budgeting & Economic Guidance:** Translates complex diagnoses into realistic chemical dosages and financial estimates per acre.
- **Inclusive Multilingual Engineering:** Native support for English and Telugu, complete with automated A4 PDF and WhatsApp infographic card generation.
- **Enterprise-Ready Full-Stack Architecture:** Asynchronous FastAPI backend, dual PostgreSQL/SQLite database support, and modern React 19 frontend.

---

## 👨‍💻 Author & Contact

**Kaku Manish Kumar**  
*Department of Artificial Intelligence & Data Science*  
*Specialization in Cloud Computing*  
- **GitHub:** [@kaku-manish](https://github.com/kaku-manish)  
- **Repository:** [https://github.com/kaku-manish/PaddyPulse](https://github.com/kaku-manish/PaddyPulse)

---
*Built with ❤️ for Indian and global paddy farmers.*