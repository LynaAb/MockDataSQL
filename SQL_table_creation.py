import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('SQL_test_table')
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS test_table (
        RECORD_ID INTEGER PRIMARY KEY,
        NO_DOSSIER INTEGER UNIQUE,
        NO_RAMQ TEXT NOT NULL,
        PRENOM TEXT NOT NULL,
        NOM TEXT NOT NULL,
        DDN TEXT NOT NULL,
        ADDRESS TEXT,
        DATE_DEBUT DATETIME DEFAULT CURRENT_TIMESTAMP,
        DATE_SORTIE DATETIME DEFAULT CURRENT_TIMESTAMP,
        DUREE_OCCUPATION_CIVIERE INTEGER DEFAULT 0,
        PRIORITE_TRIAGE INTEGER DEFAULT 3,
        CMD_CODE INTEGER,
        DESCRIPTION_DX TEXT,
        PROVENANCE TEXT DEFAULT "Unknown",
        MODE_ARRIVEE TEXT DEFAULT "Walk-in",
        PT_COUCHE_CIVIERE BOOLEAN DEFAULT 0,
        RAISON_VISITE TEXT,
        TEMPS_CIVIERE REAL DEFAULT 0.0,
        MORT BOOLEAN DEFAULT 0,
        DATE_MORT DATETIME,
        MD_FAMILLE BOOLEAN DEFAULT 0
    )
''')

# Confirm table creation
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='test_table'")
if cursor.fetchone():
    print("Table 'test_table' successfully created or already exists.")
else:
    print("Table 'test_table' was NOT created.")

# Commit and close connection
conn.commit()
conn.close()