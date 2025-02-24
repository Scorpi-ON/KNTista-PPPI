from datetime import datetime


class Analytics:
    """
    Класс Analytics представляет собой модуль для работы с аналитикой.
    Он предоставляет методы для получения метрик и проверки времени последнего обращения к данным.
    """

    def __init__(self):
        """
        Инициализирует экземпляр Analytics.
        При создании объекта выводит сообщение о том, что модуль аналитики был инициализирован.
        """
        print("This is Analytics module")

    def get_metrics(self, metrics_name: str) -> str:
        """
        Возвращает метрики по указанному имени.

        :param metrics_name: Название метрики, которую необходимо получить.
        :type metrics_name: str
        :return: Строка с информацией о запросе метрики.
        :rtype: str
        """
        return "Getting metrics " + metrics_name

    @staticmethod
    def last_checked() -> datetime:
        """
        Возвращает текущее время как время последней проверки.

        :return: Текущее время в формате datetime.
        :rtype: datetime
        """
        return datetime.now()
