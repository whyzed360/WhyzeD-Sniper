import sqlite3
import os

db_path = "empire_vault.db"

def initialize():
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    # Create a table for Imperial Assets (Digital Property)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS assets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            type TEXT NOT NULL,
            value_zed REAL DEFAULT 0,
            status TEXT DEFAULT 'SECURED'
        )
    ''')
    
    # Create a table for the Imperial Ledger (Journal/History)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ledger (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            entry TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    connection.commit()
    connection.close()
    print(f"[LOG] Imperial Archive Initialized at {db_path}")

if __name__ == "__main__":
    initialize()
