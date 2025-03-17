# Mock Sociodemographic Data & SQLite Integration

This project generates mock sociodemographic data, calculates the Charlson score and saves the data to a CSV file. It is designed for testing data analysis pipelines with realistic yet randomly generated data.

## Project Structure

```
Project Root
├── generate_mock_clinical_data.py   # Generates fake data and saves it to CSV
├── mock_clinical_data.csv  # Generated mock data file
└── README.md                     # Project documentation
```

## How It Works

### 1. Requirements
Before running the scripts, install the required dependencies :

**run** `pip install pandas faker`

if using Pip, or, if using Anaconda : 

**run** `conda install pandas faker`

### 2. Generate Mock Data
Generates a CSV file of 20 random mock patient records including name, date, address, RAMQ health insurance number, reason for visit and other attributes :

**run** `python generate_mock_clinical_data.py`