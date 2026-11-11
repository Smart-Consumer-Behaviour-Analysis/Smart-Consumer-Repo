# Smart Consumer Behaviour Analysis

A Data Analysis and Visualization project focused on understanding consumer behaviour through data collection, cleaning, exploratory analysis, visualization, and an interactive dashboard.

> **Project status:** Repository structure and documentation scaffold. Add the approved dataset, analysis notebooks, source code, and verified findings as the team completes each stage.

## Project workflow

1. **Project overview** – define the problem, objectives, scope, and expected outcomes.
2. **Data collection** – identify reliable data sources and document the dataset.
3. **Data preprocessing** – inspect, clean, transform, and validate the data.
4. **Data analysis** – perform exploratory analysis and answer the project questions.
5. **Data visualization** – create charts that communicate the findings.
6. **Dashboard** – bring the important metrics and visualizations together in one interface.

## Repository structure

```text
Smart-Consumer-Repo/
├── 01_Project_Overview/
├── 02_Data_Collection/
├── 03_Data_Preprocessing/
├── 04_Data_Analysis/
├── 05_Data_Visualization/
├── 06_Dashboard/
├── data/
│   ├── raw/
│   └── processed/
├── docs/
├── notebooks/
├── src/
├── visualizations/
├── data_dictionary.md
├── data_sources.md
├── requirements.txt
├── .gitignore
└── README.md
```

## Dataset

Place original, unchanged datasets in `data/raw/` and cleaned datasets in `data/processed/`. Do not commit private, personal, or confidential consumer information. Record each dataset's origin, collection date, license/permission, and limitations in [data_sources.md](data_sources.md).

The [data dictionary](data_dictionary.md) should describe every field, its data type, meaning, units, and any transformations. No dataset or analysis results are included in this scaffold yet.

## Getting started

1. Clone this repository.
2. Create and activate a Python virtual environment.
3. Install the packages listed in `requirements.txt`.
4. Add the project dataset and document its source.
5. Complete the workflow folders in order.

```bash
git clone https://github.com/Smart-Consumer-Behaviour-Analysis/Smart-Consumer-Repo.git
cd Smart-Consumer-Repo
python -m venv .venv
```

Activate the environment:

- Windows PowerShell: `.venv\\Scripts\\Activate.ps1`
- macOS/Linux: `source .venv/bin/activate`

Install dependencies:

```bash
pip install -r requirements.txt
```

## Team contribution

- Use GitHub Issues for individual tasks and bug reports.
- Create a separate branch for each feature or task.
- Submit changes through pull requests.
- Keep documentation updated when datasets, methods, or outputs change.

## Reproducibility and responsible data use

- Keep raw data unchanged; write cleaned outputs to `data/processed/`.
- Never commit passwords, API keys, access tokens, or local environment files.
- Avoid exposing personal or sensitive consumer information.
- Explain assumptions, missing values, limitations, and transformations.
- Do not report conclusions until they have been supported by the actual analysis.

## Project documentation

See the numbered workflow folders for stage-specific guidance, and the `docs/` folder for consolidated project documentation.
