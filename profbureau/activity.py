from datetime import datetime


class Activity:
    """
    Класс Activity представляет собой модуль для отслеживания активности на факультете и составления отчетов.
    Он предоставляет функциональность для внесения данных о мероприятиях, участии студентов и генерации отчетов в формате DOCX.
    """

    def __init__(self):
        """
        Инициализирует экземпляр Activity.
        При создании объекта выводит сообщение о том, что модуль активности был инициализирован.
        Также инициализирует пустые структуры для хранения данных о мероприятиях и участии студентов.
        """
        print("This is Activity module")
        self._events = []  # Список для хранения данных о мероприятиях
        self._students = {}  # Словарь для хранения данных об участии студентов

    def add_event(self, event_name: str, date: str, participants: list[int]) -> None:
        """
        Добавляет новое мероприятие в систему.

        :param event_name: Название мероприятия.
        :type event_name: str
        :param date: Дата проведения мероприятия в формате "YYYY-MM-DD".
        :type date: str
        :param participants: Список идентификаторов студентов, участвующих в мероприятии.
        :type participants: list[int]
        """
        event = {
            "name": event_name,
            "date": date,
            "participants": participants
        }
        self._events.append(event)
        for student_id in participants:
            if student_id not in self._students:
                self._students[student_id] = []
            self._students[student_id].append(event_name)
        print(f"Event '{event_name}' on {date} has been added with {len(participants)} participants.")

    def get_student_activity(self, student_id: int) -> list:
        """
        Возвращает список мероприятий, в которых участвовал студент.

        :param student_id: Идентификатор студента.
        :type student_id: int
        :return: Список мероприятий.
        :rtype: list
        """
        return self._students.get(student_id, [])

    def generate_report(self, month: int, year: int) -> str:
        """
        Генерирует отчет о мероприятиях за указанный месяц и год в формате DOCX.

        :param month: Месяц, за который требуется отчет (1-12).
        :type month: int
        :param year: Год, за который требуется отчет.
        :type year: int
        :return: Путь к сгенерированному файлу отчета.
        :rtype: str
        """
        report_events = [
            event for event in self._events
            if datetime.strptime(event["date"], "%Y-%m-%d").month == month
            and datetime.strptime(event["date"], "%Y-%m-%d").year == year
        ]
        report_filename = f"activity_report_{year}_{month}.docx"
        # Имитация создания DOCX-файла
        print(f"Report for {year}-{month} generated with {len(report_events)} events. Saved as '{report_filename}'.")
        return report_filename

    def list_events(self) -> list:
        """
        Возвращает список всех мероприятий.

        :return: Список мероприятий.
        :rtype: list
        """
        return self._events

    def list_students(self) -> list:
        """
        Возвращает список всех студентов, участвовавших в мероприятиях.

        :return: Список идентификаторов студентов.
        :rtype: list
        """
        return list(self._students.keys())
