import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import sqlite3

nyu = pd.read_csv('https://raw.githubusercontent.com/daniloui001/sqlite_database_operations/main/NYU_Langone_Hospital_Aetna.csv')
northshore = pd.read_csv('https://raw.githubusercontent.com/daniloui001/sqlite_database_operations/main/North_Shore_Hospital_Aetna.csv')

print(nyu.columns)
print(northshore.columns)

print(nyu.isnull().sum())
print(northshore.isnull().sum())

print(nyu['NYU Langone Long Island Gross Charges'].describe())
print(nyu['NYU Langone Long Island Discounted Cash Price'].describe())
print(nyu['AETNA HMO'].describe())

print(northshore['Gross Charges'].describe())
print(northshore['Discounted Cash Price'].describe())
print(northshore['Aetna Better Health Medicaid HMO'].describe())

### insights - there's a lot of missing data in the northshore dataset while there's no missing data in the nyu dataset.

conn = sqlite3.connect('exampledatabase.db')
c = conn.cursor()

c.execute('''CREATE TABLE nyuhealth
                (
                    [hospital_name] text, 
                    [Identifier Code] integer, 
                    [Billing code] integer, 
                    [Identifier Description] text, 
                    [Aetna HMO] integer, 
                    [cost_maximum] real
                )''')

conn.commit()

c.execute('''
          SELECT *
          FROM sqlite_master 
          WHERE type='integer';
          ''')


sql_query = """

INSERT INTO nyuhealth (
    'hospital_name', 
    'Identifier Code', 
    'Billing code',
    'Identifier Description',
    'Aetna HMO',
    'cost_maximum'
    ) 
    values (
        'NYU Langone Hospital',
        1,
        99214,
        'office visit',
        100.00,
        1000.00
    );
"""