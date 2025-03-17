import sqlite3
import pandas as pd

# Load CSV file
df = pd.read_csv("mock_sociodemo_ramq_data.csv")

# Connect to the SQLite database
conn = sqlite3.connect('SQL_test_table')
cursor = conn.cursor()

# Insert data into test_table with error handling
for _, row in df.iterrows():
    try:
        cursor.execute('''
            INSERT INTO test_table (
                RECORD_ID, NO_DOSSIER, NO_RAMQ, PRENOM, NOM, DDN, ADDRESS, DATE_SORTIE, DESCRIPTION_DX, RAISON_VISITE
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            int(row['RecordID']),
            int(row['No_dossier']),
            row['RAMQ'],
            row['First_Name'],
            row['Last_Name'],
            row['DDN'],
            row['Adresse'],
            row['Date_Heure_sortie'],
            "Tumeur à son petit cerveau",
            "Hospitalization"
        ))
    except sqlite3.IntegrityError:
        print(f"Duplicate RecordID {row['RecordID']} skipped.")

# Commit and close connection
conn.commit()
conn.close()

print("Data successfully inserted into SQLite database.")