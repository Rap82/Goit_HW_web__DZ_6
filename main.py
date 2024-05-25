import sqlite3
from prettytable import PrettyTable

# ============================= Функція опрацювння вконання запитів ==============================


def execute_query(query_file, result_handler, ):
    # Встановити з'єднання з базою даних
    with sqlite3.connect("first_db.db") as conn:
        cursor = conn.cursor()

        # Прочитати запит з файлу
        with open(query_file, "r") as file:
            query = file.read()

        # Виконати запит 
     
        cursor.execute(query)

        # Отримати результат
        result = cursor.fetchall()

        # Обробити результат за допомогою заданої функції
        result_handler(result)

        # Закрити з'єднання з базою даних
        cursor.close()


# ================================ Фунції запитів згідно завдання ДЗ =================================


def handle_query_1(result):

    table = PrettyTable()
    table.field_names = ["Name", "Average Grade"]
    table.align["Name"] = "l"  
    for row in result:
        student_id, student_name, average_grade = row
        table.add_row([student_name, average_grade])

    print(table)



def handle_query_3(result):
    table = PrettyTable()
    table.field_names = ["Group", "Subject", "Average Grade"]
    table.align["Group"] = "l"  
    prev_group = None
    group_count = 0

    for row in result:
        group_name, subject, average_grade = row
        if group_name == prev_group:
            table.add_row(["", subject, average_grade])
        else:
            if group_count > 0:
                table.add_row(["", subject, average_grade], divider=True)
            table.add_row([group_name, subject, average_grade])
            prev_group = group_name
            group_count += 1

    print(table)



def handle_query_4(result):

    table = PrettyTable()
    table.field_names = ["Average Grade"]

    for row in result:
        average_grade = row[0]
        table.add_row([average_grade])

    print(table)



def handle_query_5(result):

    table = PrettyTable()
    table.field_names = ["Teacher", "Subject"]
    table.align["Teacher"] = "l"

    for row in result:
        teacher_name, subject = row
        table.add_row([teacher_name, subject])

    print(table)



def handle_query_6(result):
    table = PrettyTable()
    table.field_names = ["Group", "Student"]
    table.align["Group"] = "l"  
    prev_group = None
    group_count = 0

    for row in result:
        group_name, _, student = row
        if group_name == prev_group:
            table.add_row(["", student])
        else:
            if group_count > 0:
                table.add_row(["", student], divider=True)
            table.add_row([group_name, student])
            prev_group = group_name
            group_count += 1

    print(table)



def handle_query_7(result):
      
    table = PrettyTable()
    table.field_names = ["Grup","Subject","Student", "Grades",]
    table.align["Student"] = "l" 
    result_new = []
    studet_names = []
    
    for row in result:
        if row[0] == "Група 2" and row[1] == "Фізика" :
        
           result_new.append(row)
           studet_names.append(row[2])
           
    studet_names = list(set(studet_names))
    result = []
    for name in studet_names :
        count = 0 
        for row in result_new:
          if name ==  row[2] and count <1:
             result.append(row)
             count+=1
    for row in result:
        _, subject, student, grades = row
        
        table.add_row([_, subject, student, grades])
  
    print(table)

    


def handle_query_8(result):

    table = PrettyTable()
    table.field_names = ["Teacher", "Subject", "Average Grade"]
    table.align["Teacher"] = "l"

    for row in result:
        teacher_name, subject, average_grade = row
        table.add_row([teacher_name, subject, average_grade])

    print(table)



def handle_query_9(result):

    table = PrettyTable()
    table.field_names = ["Student", "Subjects"]
    table.align["Teacher"] = "l"

    for row in result:
        student, subjects = row
        table.add_row([student, subjects])

    print(table)

def handle_query_10(result):
    
    table = PrettyTable()
    table.field_names = ["Student", "Subject", "Teacher"]
    table.align["Teacher"] = "l"

    for row in result:
        student, subject, teacher = row
        table.add_row([student, subject, teacher])

    print(table)



# ============================= Базові запити згідно завдання ДЗ ==============================

if __name__ == "__main__":
    query_handlers = {
        1: ["Знайти 5 студентів із найбільшим середнім балом з усіх предметів.", handle_query_1,],
        2: ["Знайти студента із найвищим середнім балом з певного предмета.", handle_query_1,],
        3: ["Знайти середній бал у групах з певного предмета.", handle_query_3],
        4: ["Знайти середній бал на потоці (по всій таблиці оцінок).", handle_query_4],
        5: ["Знайти які курси читає певний викладач.", handle_query_5],
        6: ["Знайти список студентів у певній групі.", handle_query_6],
        7: ["Знайти оцінки студентів у окремій групі з певного предмета.", handle_query_7,],
        8: ["Знайти середній бал, який ставить певний викладач зі своїх предметів.", handle_query_8,],
        9: ["Знайти список курсів, які відвідує студент.", handle_query_9,],
        10: ["Список курсів, які певному студенту читає певний викладач.", handle_query_10,],
        
    }
    for i in range(1, 11):
        print("=" * 60)
        print(f"{i}.  {query_handlers[i][0]}")
        print("=" * 60)
                
        execute_query(f"query_{i}.sql", query_handlers[i][1], )