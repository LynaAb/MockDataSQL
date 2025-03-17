# Mock Sociodemographic Data & SQLite Integration

This project generates mock sociodemographic data, saves it to a CSV file, and loads it into an SQLite database. It is designed for testing data processing pipelines with realistic yet randomly generated data.

## Project Structure

```
Project Root
├── mock_sociodemo_ramq_data.py   # Generates fake data and saves it to CSV
├── SQL_table_creation.py         # Creates an SQLite database and table
├── load_data_to_sqlite.py        # Loads CSV data into SQLite
├── mock_sociodemo_ramq_data.csv  # Generated mock data file
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

**run** `python mock_sociodemo_ramq_data.py`

### 3. Create the SQLite Database
Creates the SQLite database named SQL_test_table and table called test_table :

**run** `python SQL_table_creation.py`

### 4. Load Data into SQLite
Loads generated CSV mock data file into the SQL database:

**run** `python load_data_to_sqlite.py`
