class FinancialHelp:
    """
    Класс FinancialHelp представляет собой модуль для работы с финансовой помощью.
    Он предоставляет функциональность для управления запросами на финансовую помощь,
    отслеживания статуса заявок и обработки платежей.
    """

    def __init__(self):
        """
        Инициализирует экземпляр FinancialHelp.
        При создании объекта выводит сообщение о том, что модуль финансовой помощи был инициализирован.
        Также инициализирует пустой список для хранения заявок на финансовую помощь.
        """
        print("This is Financial Help module")
        self._requests = []  # Список для хранения заявок на финансовую помощь

    @property
    def total_requests(self) -> int:
        """
        Возвращает общее количество заявок на финансовую помощь.

        :return: Количество заявок.
        :rtype: int
        """
        return len(self._requests)

    def add_request(self, user_id: int, amount: float, description: str) -> None:
        """
        Добавляет новую заявку на финансовую помощь.

        :param user_id: Идентификатор пользователя, подающего заявку.
        :type user_id: int
        :param amount: Сумма запрашиваемой финансовой помощи.
        :type amount: float
        :param description: Описание причины запроса финансовой помощи.
        :type description: str
        :return: None
        """
        request = {
            "user_id": user_id,
            "amount": amount,
            "description": description,
            "status": "pending",  # Статус заявки по умолчанию
            "created_at": datetime.now(),
        }
        self._requests.append(request)
        print(f"New financial help request added by user {user_id} for amount {amount}.")

    def approve_request(self, request_id: int) -> None:
        """
        Одобряет заявку на финансовую помощь по её идентификатору.

        :param request_id: Индекс заявки в списке заявок.
        :type request_id: int
        :return: None
        """
        if 0 <= request_id < len(self._requests):
            self._requests[request_id]["status"] = "approved"
            print(f"Request {request_id} has been approved.")
        else:
            print(f"Request {request_id} not found.")

    def reject_request(self, request_id: int) -> None:
        """
        Отклоняет заявку на финансовую помощь по её идентификатору.

        :param request_id: Индекс заявки в списке заявок.
        :type request_id: int
        :return: None
        """
        if 0 <= request_id < len(self._requests):
            self._requests[request_id]["status"] = "rejected"
            print(f"Request {request_id} has been rejected.")
        else:
            print(f"Request {request_id} not found.")

    def get_request_status(self, request_id: int) -> str:
        """
        Возвращает статус заявки на финансовую помощь по её идентификатору.

        :param request_id: Индекс заявки в списке заявок.
        :type request_id: int
        :return: Статус заявки.
        :rtype: str
        """
        if 0 <= request_id < len(self._requests):
            return self._requests[request_id]["status"]
        else:
            return "Request not found."

    def list_requests(self) -> list:
        """
        Возвращает список всех заявок на финансовую помощь.

        :return: Список заявок.
        :rtype: list
        """
        return self._requests
