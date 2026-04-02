import csv
from connect import connect

def create_table():
    conn = connect()                                     # Establish connection to PostgreSQL
    if conn:
        cur = conn.cursor()                              # Create a cursor to execute SQL commands
        cur.execute("""
            CREATE TABLE IF NOT EXISTS contacts (        -- SQL to create the table structure
                id SERIAL PRIMARY KEY,                   -- Auto-incrementing unique identifier
                name VARCHAR(100) UNIQUE,                -- Name must be unique (prevents duplicates)
                phone VARCHAR(20)                        -- Phone number field
            );
        """)
        conn.commit()                                    # Permanently save changes to the database
        cur.close()                                      # Close the cursor
        conn.close()                                     # Close the connection

def show_all():
    """Выводит все контакты в виде таблицы"""
    conn = connect()
    if conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM get_all_contacts()")  # Call a stored SQL Function to get data
        rows = cur.fetchall()                            # Fetch all results into a Python list
        print(f"\n{'ID':<5} | {'Имя':<20} | {'Телефон':<15}")
        print("-" * 45)
        for r in rows:
            print(f"{r[0]:<5} | {r[1]:<20} | {r[2]:<15}") # Format output for a clean table view
        cur.close()
        conn.close()

def search():
    pattern = input("Введите текст для поиска: ")
    conn = connect()
    if conn:
        cur = conn.cursor()
        # Use %s placeholder to prevent SQL Injection (security best practice)
        cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))
        for r in cur.fetchall():
            print(f"ID: {r[0]} | Имя: {r[1]} | Тел: {r[2]}")
        cur.close()
        conn.close()

def add_or_update():
    name = input("Имя: ")
    phone = input("Телефон: ")
    conn = connect()
    if conn:
        cur = conn.cursor()
        # CALL is used for Procedures. This one handles both INSERT and UPDATE (Upsert)
        cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
        conn.commit()                                    # Commit is required for Data Manipulation (DML)
        cur.close()
        conn.close()
        print("Контакт сохранен.")

def import_csv():
    filename = input("Имя CSV файла: ")
    names, phones = [], []                               # Initialize lists for batch processing
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)                   # Read CSV using headers as keys
            for row in reader:
                names.append(row['name'])
                phones.append(row['phone'])
        conn = connect()
        if conn:
            cur = conn.cursor()
            # Send arrays to the database for high-performance bulk insertion
            cur.execute("CALL insert_many_contacts(%s, %s)", (names, phones))
            conn.commit()
            for notice in conn.notices: print(notice.strip()) # Show database feedback/logs
            cur.close()
            conn.close()
            print("Импорт завершен.")
    except Exception as e:
        print(f"Ошибка чтения файла: {e}")

def show_paginated():
    limit = int(input("Кол-во записей: "))               # Number of rows to show per page
    offset = int(input("Смещение: "))                    # Number of rows to skip
    conn = connect()
    if conn:
        cur = conn.cursor()
        # Pagination prevents system overload by loading data in small chunks
        cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))
        for r in cur.fetchall(): print(r)
        cur.close()
        conn.close()

def delete():
    val = input("Введите имя или телефон для удаления: ")
    conn = connect()
    if conn:
        cur = conn.cursor()
        # Explicitly cast %s to varchar for strict PostgreSQL type checking
        cur.execute("CALL delete_contact_adv(%s::varchar)", (val,))
        conn.commit()
        cur.close()
        conn.close()
        print(f"Запрос на удаление '{val}' выполнен.")

def menu():
    while True:                                          # Infinite loop for the User Interface
        print("\n--- PhoneBook Меню ---")
        print("1. Поиск")
        print("2. Добавить/Обновить")
        print("3. Массовый импорт (CSV)")
        print("4. Пагинация")
        print("5. Удалить")
        print("6. Показать ВСЕ")
        print("7. Выход")
        
        choice = input("Выберите действие: ")            # Capture user selection
        if choice == '1': search()
        elif choice == '2': add_or_update()
        elif choice == '3': import_csv()
        elif choice == '4': show_paginated()
        elif choice == '5': delete()
        elif choice == '6': show_all()
        elif choice == '7': break                        # Exit the loop and terminate the app

if __name__ == "__main__":
    create_table()                                       # Ensure DB is ready on startup
    menu()                                               # Launch the interactive menu