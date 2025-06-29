import sqlite3
from art import text2art
from colorama import Fore, Style, init

init(autoreset=True)
DB_NAME = "students.db"
def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            student_id TEXT NOT NULL,
            subject TEXT,
            grade1 REAL,
            grade2 REAL,
            grade3 REAL,
            average REAL
        )
    """)
    conn.commit()
    conn.close()


def add_student():
    name = input("Enter student name: ")
    student_id = input("Student ID: ")
    subject = input("Subject: ")
    try:
        g1 = float(input("Grade 1: "))
        g2 = float(input("Grade 2: "))
        g3 = float(input("Grade 3: "))
        avg = round((g1 + g2 + g3) / 3, 2)

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO students (name, student_id,subject, grade1, grade2,grade3,average)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (name,student_id, subject,g1,g2, g3, avg))
        conn.commit()
        conn.close()

        print(Fore.GREEN+f"Student saved successfully Average: {avg}")
    except ValueError:
        print(Fore.RED +"Please enter valid numbers for grades")
def view_students():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT name, student_id, subject, average FROM students")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print(Fore.YELLOW +"No students found")
    else:
        print("\n Student List:")
        print("-" * 50)
        for r in rows:
            print(f"{r[0]:<15} | ID: {r[1]:<8} | {r[2]:<10} | Avg: {r[3]}")
        print("-" * 50)

def main_menu():
    print(Fore.CYAN +text2art("Student System",font="small"))
    while True:
        print(Fore.BLUE + "\n1. Add Student")
        print("2. View Students")
        print("3. Exit")
        choice = input(Fore.WHITE+"Choose an option: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            print(Fore.MAGENTA + "Goodbye")
            break
        else:

            print(Fore.RED + "Invalid option Try again.")
create_table()
main_menu()
