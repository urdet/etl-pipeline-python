# ETL Pipeline with Python, Pandas & SQLAlchemy

## Overview

This project implements a simple and production-oriented **ETL (Extract, Transform, Load) pipeline** using **Python**, **Pandas**, and **SQLAlchemy**.  
The pipeline extracts data from a **MySQL database**, applies transformations, and loads clean data while supporting **incremental loading** using checkpoints.

This project is suitable for:
- Data Engineering practice
- Academic projects
- GitHub portfolio demonstration

---

## Project Structure

## Project Structure

```text
etl-pipeline-python/
│
├── main.py              # ETL orchestration
├── extract.py           # Data extraction logic
├── transform.py         # Data cleaning and transformation
├── load.py              # Load transformed data
├── checkpoint.py        # Incremental load management
├── checkpoints/         # Stores last execution metadata
├── requirements.txt     # Python dependencies
├── .gitignore           # Ignored files and secrets
└── README.md
``` 

---

## ETL Workflow

1. **Extract**
   - Connects to MySQL using SQLAlchemy
   - Reads data into a Pandas DataFrame
   - Supports incremental extraction using `updated_at`

2. **Transform**
   - Removes duplicate rows
   - Handles missing values
   - Applies basic data validation

3. **Load**
   - Loads cleaned data into the target table
   - Ensures idempotent execution

4. **Checkpoint**
   - Saves the last successful run timestamp
   - Enables incremental data loading

---

## Technologies Used

- Python 3.11+
- Pandas
- SQLAlchemy 2.x
- PyMySQL
- MySQL
- Git & GitHub

---
## Setup Instructions

### Clone the repository

```bash
git clone https://github.com/urdet/etl-pipeline-python.git
cd etl-pipeline-python
```

### Create a virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```
---

## Configuration

Create a local config.py file (ignored by Git):

``MYSQL_URI = "mysql+pymysql://user:password@localhost:3306/database"``

---

## Run the ETL Pipeline

```bash
python main.py
```
First run loads all data
Next runs load only new or updated records

---

## Sample Source Table

```code
CREATE TABLE orders (
    order_id INT,
    customer_id INT,
    quantity INT,
    unit_price DECIMAL(10,2),
    status VARCHAR(50),
    updated_at DATETIME
);
```

---

## Future Improvements

- Add logging
- Add unit tests
- Dockerize the pipeline
- Integrate with Airflow
- Add data quality checks
- Support cloud databases

---

## Author

Rida Elantari
Data Engineering & AI Student – EST Béni Mellal

GitHub: https://github.com/urdet
