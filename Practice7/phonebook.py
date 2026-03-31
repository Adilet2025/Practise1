# phonebook.py
import csv
from connect import connect

def create_table():
    conn = connect()
    if conn:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS contacts (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                phone VARCHAR(20)
            );
        """)
        conn.commit()
        cur.close()
        conn.close()

def insert_contact(name, phone):
    conn = connect()
    if conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", (name, phone))
        conn.commit()
        cur.close()
        conn.close()
        print("Контакт успешно добавлен!")

def get_contacts(filter_text=None):
    conn = connect()
    if conn:
        cur = conn.cursor()
        if filter_text:
            # Поиск по имени или номеру (регистронезависимый)
            query = "SELECT * FROM contacts WHERE name ILIKE %s OR phone LIKE %s ORDER BY id"
            cur.execute(query, (f"%{filter_text}%", f"%{filter_text}%"))
        else:
            cur.execute("SELECT * FROM contacts ORDER BY id")
        
        rows = cur.fetchall()
        if not rows:
            print("Контакты не найдены.")
        for row in rows:
            print(f"[{row[0]}] Имя: {row[1]} | Тел: {row[2]}")
        cur.close()
        conn.close()

def update_contact(id, new_name=None, new_phone=None):
    conn = connect()
    if conn:
        cur = conn.cursor()
        if new_name:
            cur.execute("UPDATE contacts SET name = %s WHERE id = %s", (new_name, id))
        if new_phone:
            cur.execute("UPDATE contacts SET phone = %s WHERE id = %s", (new_phone, id))
        conn.commit()
        cur.close()
        conn.close()
        print("Данные обновлены!")

def delete_contact(identifier):
    conn = connect()
    if conn:
        cur = conn.cursor()
        # Удаление по имени или по ID
        if identifier.isdigit():
            cur.execute("DELETE FROM contacts WHERE id = %s", (identifier,))
        else:
            cur.execute("DELETE FROM contacts WHERE name = %s", (identifier,))
        conn.commit()
        cur.close()
        conn.close()
        print("Контакт удален.")

def import_csv(filename):
    conn = connect()
    if conn:
        cur = conn.cursor()
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    cur.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", 
                                (row['name'], row['phone']))
            conn.commit()
            print("Импорт завершен!")
        except FileNotFoundError:
            print(f"Файл {filename} не найден.")
        cur.close()
        conn.close()

def menu():
    while True:
        print("\n--- PhoneBook Menu ---")
        print("1. Показать все контакты")
        print("2. Добавить новый контакт")
        print("3. Обновить контакт (по ID)")
        print("4. Удалить контакт (по имени или ID)")
        print("5. Импорт из CSV")
        print("6. Поиск (фильтр)")
        print("7. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == '1':
            get_contacts()
        elif choice == '2':
            name = input("Имя: ")
            phone = input("Телефон: ")
            insert_contact(name, phone)
        elif choice == '3':
            c_id = input("Введите ID контакта: ")
            nn = input("Новое имя (пропустите, если не нужно): ")
            np = input("Новый телефон (пропустите, если не нужно): ")
            update_contact(c_id, nn if nn else None, np if np else None)
        elif choice == '4':
            val = input("Введите имя или ID для удаления: ")
            delete_contact(val)
        elif choice == '5':
            fname = input("Имя CSV файла (напр. contacts.csv): ")
            import_csv(fname)
        elif choice == '6':
            search = input("Введите текст для поиска: ")
            get_contacts(search)
        elif choice == '7':
            break

if __name__ == "__main__":
    create_table()
    menu()