# Data Observability Platform

An open-source data observability platform focused on metadata discovery, schema monitoring, and schema drift detection for PostgreSQL-based data systems.

## Overview

This project is being developed to help data engineers automatically discover database metadata, monitor schema changes, and improve reliability in data pipelines and warehouse systems.

The platform currently supports:

* PostgreSQL connectivity
* Dynamic metadata discovery
* Table and column inspection
* Schema snapshotting
* Schema drift detection
* CLI-based interaction

The long-term goal is to evolve this into a modular, extensible, metadata-driven observability platform supporting multiple databases and monitoring capabilities.

---

# Features

## Current Features

* PostgreSQL connector using SQLAlchemy
* Metadata discovery using `information_schema`
* Dynamic table discovery
* Dynamic column discovery
* Structured metadata extraction
* JSON-based schema snapshotting
* Basic schema drift detection
* Command Line Interface (CLI)

---

# Project Structure

```text
app/
├── connectors/
│   └── postgres_connector.py
│
├── metadata/
│   ├── discovery.py
│   ├── snapshot.py
│   └── drift_detector.py
│
main.py
requirements.txt
.env.example
README.md
```

---

# Tech Stack

* Python
* PostgreSQL
* SQLAlchemy
* psycopg2
* argparse
* python-dotenv

---

# Installation

## Clone Repository

```bash
git clone <your_repo_url>
cd data-observability-platform
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the project root.

Example:

```env
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=observability_demo
```

---

# Usage

## List Tables

```bash
python main.py tables
```

---

## Get Columns From Table

```bash
python main.py columns orders
```

---

## Discover Entire Database Metadata

```bash
python main.py database
```

---

## Save Schema Snapshot

```bash
python main.py snapshot
```

---

## Detect Schema Drift

```bash
python main.py detect_drift
```

---

# Example Output

```json
{
    "orders": [
        {
            "column_name": "order_id",
            "data_type": "integer"
        },
        {
            "column_name": "amount",
            "data_type": "numeric"
        }
    ]
}
```

---

# Roadmap

## Planned Features

* Advanced schema drift comparison
* Detailed drift reporting
* Multiple database connectors
* Data quality checks
* Logging and monitoring
* FastAPI integration
* Docker support
* CI/CD pipelines
* Plugin architecture
* Dashboard/UI
* Alerting system

---

# Contributing

Contributions, suggestions, and discussions are welcome.

Future contributors will be able to:

* add database connectors
* improve drift detection
* implement observability checks
* extend monitoring features

---

# License

This project is currently under active development.
License will be added in a future release.
