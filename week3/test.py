from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql://postgres:admin123@localhost:5432/label_db"

try:
    engine = create_engine(DATABASE_URL)

    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("Database connection successful!")
        print("Test query result:", result.fetchone())

except Exception as e:
    print("Database connection failed!")
    print("Error:", e)   