import sqlite3
import sys

db_path = "empire_vault.db"

def add_entry(text):
    conn = sqlite3.connect(db_path)
    curr = conn.cursor()
    curr.execute("INSERT INTO ledger (entry) VALUES (?)", (text,))
    conn.commit()
    conn.close()
    print(f"[LOG] Data Archived: {text}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        add_entry(" ".join(sys.argv[1:]))
    else:
        print("Usage: python archive_tool.py 'Your message here'")
