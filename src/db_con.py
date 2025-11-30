from sqlalchemy import create_engine, text

server   = "SHUBHAMS\\MSSQLSERVER01"
database = "SalaryAnalysis_Db"

engine = create_engine(
    f"mssql+pyodbc://@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
)

with engine.connect() as conn:

    # 1️⃣ CREATE TABLE IF NOT EXISTS (FIXED)
    conn.execute(text("""
        IF NOT EXISTS (
            SELECT * FROM INFORMATION_SCHEMA.TABLES 
            WHERE TABLE_NAME = 'TestTable'
        )
        BEGIN
            CREATE TABLE TestTable (
                id INT IDENTITY(1,1) PRIMARY KEY,
                name VARCHAR(100),
                salary INT
            );
        END
    """))
    conn.commit()
    print("🛠️ TestTable ensured (created if missing).")

    # 2️⃣ INSERT SAMPLE DATA
    conn.execute(
        text("INSERT INTO TestTable (name, salary) VALUES (:name, :salary)"),
        {"name": "Shubham_Test", "salary": 50000}
    )
    conn.commit()
    print("✨ Test data inserted successfully.")

    # 3️⃣ FETCH AND DISPLAY
    result = conn.execute(text("SELECT * FROM TestTable"))
    print("\n📦 Data inside TestTable:")
    for row in result:
        print(row)
