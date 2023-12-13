import logging
from datetime import datetime

# Настройка логгера
logging.basicConfig(filename='test.log', level=logging.DEBUG)

def logger(log_data):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"{current_time} - {log_data}"
    logging.debug(log_message)
    
# Функция запускает тест на основе переданных вопросов и ответов.
def run_test(questions, answers):
    logger("-------ТЕСТ 1-------")
    total_questions = len(questions)
    correct_answers = 0
    num_answers = [3, 4, 2, 3, 3]

    # Проссмотр списка и вывод вопросов по порядку
    for i, question in enumerate(questions):
        print(f"Вопрос {i + 1}:")
        logger(f"Вопрос {i + 1}: {question}")
        print(question)

        #Проверка на ошибку ввода данных пользователя
        while True:
            try:
                user_answer = int(input("Введите номер правильного варианта ответа: "))
                logger(f"Введенный ответ на вопрос {i + 1}: {user_answer}")

                if user_answer < 1 or user_answer > num_answers[i]:
                    print(f"Ошибка: введите номер варианта от 1 до {num_answers[i]}.")
                    logger(f"Ошибка: введен неверный номер варианта.")
                    continue

                break
            except ValueError:
                print("Ошибка: введите целое число.")
                logger("Ошибка: введено нецелое число.")
                
        #Проверка и Вывод результата по вопросу
        if user_answer == answers[i]:
            print("Правильно!")
            logger("Ответ верный.")
            correct_answers += 1
        else:
            print(f"Неверно! Правильный ответ: {answers[i]}")
            logger(f"Неверно! Правильный ответ: {answers[i]}")

        print()
    # Расчет и Вывод результата по тесту
    score = round((correct_answers/total_questions) * 100,2)
    print(f"Результат: {correct_answers} из {total_questions} правильных ответов.")
    print(f"Выполнение теста: {score}%")
    logger(f"Результат: {correct_answers} из {total_questions} правильных ответов.")
    logger(f"Выполнение теста: {score}%")
    logger("-------КОНЕЦ 1 ТЕСТА------")

# Функция запускает тест на основе переданных вопросов и ответов
def run_test2(questions2, answers2):
    logger("-------ТЕСТ 2-------")
    total_questions2 = len(questions2)
    correct_answers2 = 0
    num_answers2 = [4, 3, 4, 4, 4, 3, 3]

    # Проссмотр списка и вывод вопросов по порядку
    for i, question in enumerate(questions2):
        print(f"Вопрос {i + 1}:")
        logger(f"Вопрос {i + 1}: {questions2}")
        print(question)

        # Проверка на ошибку ввода данных пользователя
        while True:
            try:
                user_answer2 = int(input("Введите номер правильного варианта ответа: "))
                logger(f"Введенный ответ на вопрос {i + 1}: {user_answer2}")

                if user_answer2 < 1 or user_answer2 > num_answers2[i]:
                    print(f"Ошибка: введите номер варианта от 1 до {num_answers2[i]}.")
                    logger(f"Ошибка: введен неверный номер варианта.")
                    continue

                break
            except ValueError:
                print("Ошибка: введите целое число.")
                logger("Ошибка: введено нецелое число.")
                
        # Проверка и Вывод результата по вопросу
        if user_answer2 == answers2[i]:
            print("Правильно!")
            logger("Ответ верный.")
            correct_answers2 += 1
        else:
            print(f"Неверно! Правильный ответ: {answers2[i]}")
            logger(f"Неверно! Правильный ответ: {answers2[i]}")

        print()
    # Расчет и Вывод результата по тесту
    score2 = round((correct_answers2/total_questions2) * 100, 2)
    print(f"Результат: {correct_answers2} из {total_questions2} правильных ответов.")
    print(f"Выполнение теста: {score2}%")
    logger(f"Результат: {correct_answers2} из {total_questions2} правильных ответов.")
    logger(f"Выполнение теста: {score2}%")
    logger("-------КОНЕЦ 2 ТЕСТА------")
print()

# Основная функция
def main():
    # Задаем вопросы и ответы для первого теста
    questions = [
        "На каком этапе разработки ПО выполняется описание алгоритмов?\n1) Детальное проектирование\n2) Разработка архитектуры системы\n3) Создание плана разработки",
        "Технический долг не является следствием чего?\n1) Отсутствия документации\n2) Отсутствия тестов\n3) Сильного зацепления компонентов\n4) Все ответы неверные",
        "Трансцендентный взгляд на качество гласит: Качество это то, что лучше подходит пользователю в контексте применения.\n1) Верно\n2) Неверно",
        "Тестирование, основанное на анализе внутренней структуры компонента или системы - это тестирование методом?\n1) Черного ящика\n2) Серого ящика\n3) Белого ящика",
        "Рефакторинг нужен когда?\n1) Программа медленно работает\n2) Программа нуждается в новой функциональности\n3) Программа нуждается в улучшении архитектуры"
    ]
    answers = [1, 4, 1, 3, 3]
    # Задаем вопросы и ответы для второго теста
    questions2 = [
        "Критерием качества программы, определяющим соответствие результатов программы ее спецификации, является?\n1) Надежность\n2) Эффективность\n3) Эргономичность \n4) Корректность",
        "Технический долг не является следствием чего?\n1) Линейной\n2) Циклической\n3) Ветвления",
        "Переменная, изменяющаясвое значение при каждом вхождении в цикл, называется\n1) Телом цикла\n2) Параметром цикла\n3) Индексом \n4) Размером",
        "Понятное  и точное предписание исполнителю выполнить конечную последовательность команд, приводящую от исходных данных к искомому результату, называется\n1) Моделью\n2) Алгоритмом\n3) Системой\n4) Технологией",
        "Алгоритмом можно назвать\n1) Описание решения квадратного уравнения\n2) Расписание уроков в колледже\n3) Технический паспорт автомобиля\n4) Список группы в журнале",
        "Многократно повторяющаяся часть алгоритма  называется\n1) Параметром цикла\n2) Телом цикла\n3) Перебором",
        "Технический долг не является следствием чего?\n1) sng\n2) int\n3) str"
    ]

    answers2 = [4, 2, 3, 2, 1, 2, 2]
    
    # Пользователь выбирает, какой тест пройти
    test_choice = input("Какой тест вы хотите пройти? Введите '1' для первого теста и '2' для второго: ")
    logger(f"Введенный ответ: {test_choice}")

    # Проверка введенного выбора пользователя
    while test_choice not in ['1', '2']:
        print("Ошибка: введите '1' или '2'.")
        logger(f"Ошибка: введен неверный вариант.")
        test_choice = input("Какой тест вы хотите пройти? Введите '1' для первого теста и '2' для второго: ")
        logger(f"Введенный ответ: {test_choice}")
        
    # Запуск выбранного теста   
    if test_choice == '1':
        run_test(questions, answers)
        
        # Пользователь может выбрать пройти ли второй тест
        choice = input("Хотите пройти второй тест? (да/нет): ")
        logger(f"Введенный ответ: {choice}")
        
        #Проверка введенного выбора пользователя
        while choice.lower() not in ['да', 'нет']:
            print("Ошибка: введите 'да' или 'нет'.")
            logger(f"Ошибка: введен неверный вариант.")
            choice = input("Хотите пройти второй тест? (да/нет): ")
            logger(f"Введенный ответ: {choice}")
            
        # Запуск второго теста, если пользователь согласился
        if choice.lower() == "да":
            run_test2(questions2, answers2)
    #    
    elif test_choice == '2':
        run_test2(questions2, answers2)
        # Пользователь может выбрать пройти ли первый тест
        choice = input("Хотите пройти первый тест? (да/нет): ")
        logger(f"Введенный ответ: {choice}")
        # Проверка введенного выбора пользователя
        while choice.lower() not in ['да', 'нет']:
            print("Ошибка: введите 'да' или 'нет'.")
            logger(f"Ошибка: введен неверный вариант.")
            choice = input("Хотите пройти первый тест? (да/нет): ")
            logger(f"Введенный ответ: {choice}")
            
        # Запуск второго теста, если пользователь согласился
        if choice.lower() == "да":
            run_test(questions, answers)

main()
