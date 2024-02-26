import sqlite3
import os

from regex import D

DATABASE_path = os.path.join('Final','database', 'raw_database.db')
# print(os.listdir())
# print(os.listdir('Final/database'))
conn = sqlite3.connect(DATABASE_path)
cursor = conn.cursor()


cursor.execute("""
               CREATE TABLE applicants (
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL, 
                   contact_no TEXT NOT NULL,
                   email TEXT NOT NULL,
                   projectLinks TEXT,
                   job_role TEXT NOT NULL, 
                   resume_file TEXT,
                   skills TEXT NOT NULL, 
                   isEligible INTEGER NOT NULL 
               )
               """)

conn.commit()
conn.close()