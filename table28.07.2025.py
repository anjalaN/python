import psycopg2
import glob
import os
import csv
import uuid
from datetime import datetime

from dotenv import load_dotenv

load_dotenv(dotenv_path="../ex00/.env")  # path to ex00 .env

conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME").strip(),
    user=os.getenv("DB_USER").strip(),
    password=os.getenv("DB_PASSWORD").strip(),
    host=os.getenv("DB_HOST").strip(),
    port=os.getenv("DB_PORT").strip()
)
#  print("connection ok")
csv_files = glob.glob("../subject/customer/*.csv")
#  print(csv_files)

for file in csv_files:
    #  table_name = os.path.splitext(os.path.basename(file))[0]
    table_name = os.path.splitext(os.path.basename(file))[0].replace("-", "_").lower()


    try:
        with conn.cursor() as cur:
            cur.execute(f'DROP TABLE IF EXISTS "{table_name}";')
            cur.execute(f'''
                CREATE TABLE "{table_name}" (
                    event_time TIMESTAMP NOT NULL,
                    event_type TEXT,
                    product_id VARCHAR(50),
                    price NUMERIC(10,2),
                    user_id BIGINT,
                    user_session UUID
                );
            ''')
    

            # with open(file, newline='', encoding='utf-8') as csvfile:
            with open(file, 'r', encoding='utf-8') as f:
                # cur.copy_expert(f'''COPY "{table_name}" FROM STDIN WITH CSV HEADER''', f)

                reader = csv.DictReader(f)
                for row in reader:
                    try:
                        user_session = str(uuid.UUID(row['user_session']))  # ← CORRECT: Parse existing UUID
                    except (ValueError, AttributeError):
                        user_session = str(uuid.uuid4())  # ← CORRECT: Generate new UUID if malformed

                    print(f"Processing row in {file}: {row}")

                    cur.execute(
                        f'''INSERT INTO "{table_name}" (event_time, event_type, product_id, price, user_id, user_session)
                            VALUES (%s, %s, %s, %s, %s, %s)
                        ''',
                        (
                            row['event_time'],
                            row['event_type'],
                            # row.get('is_promo', 'false').lower() == 'true',
                            row['product_id'],
                            float(row['price']),
                            int(row['user_id']),
                            #str(uuid.UUID(row['user_session']))
                            user_session

                        )
                    )

        conn.commit()
        print(f"data insert into table '{table_name}'")
    except Exception as e:
        print(f"Erroe processing {file}: {e}")

    conn.commit()

conn.close()



