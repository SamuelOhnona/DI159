import requests
import random
import psycopg2

# --- Connect to your PostgreSQL database ---
conn = psycopg2.connect(
    dbname="your_db_name",
    user="your_db_user",
    password="your_db_password",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# --- Create the table if it doesn't exist ---
cur.execute("""
    CREATE TABLE IF NOT EXISTS countries (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        capital VARCHAR(100),
        flag TEXT,
        subregion VARCHAR(100),
        population BIGINT
    );
""")

# --- Get random countries from the API ---
response = requests.get("https://restcountries.com/v3.1/all")
countries = random.sample(response.json(), 10)

# --- Insert each country into the table ---
for country in countries:
    name = country.get("name", {}).get("common", "N/A")
    capital = country.get("capital", ["N/A"])[0] if country.get("capital") else "N/A"
    flag = country.get("flags", {}).get("png", "")
    subregion = country.get("subregion", "N/A")
    population = country.get("population", 0)

    cur.execute("""
        INSERT INTO countries (name, capital, flag, subregion, population)
        VALUES (%s, %s, %s, %s, %s)
    """, (name, capital, flag, subregion, population))

conn.commit()
cur.close()
conn.close()

print("✅ 10 random countries inserted.")