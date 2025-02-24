class TGBot:
    """
    Класс TGBot представляет собой модуль для работы с Telegram-ботом.
    Он предоставляет функциональность для отправки сообщений, обработки команд и управления состоянием бота.
    """

    def __init__(self, bot_token: str):
        """
        Инициализирует экземпляр TGBot.

        :param bot_token: Токен Telegram-бота для авторизации.
        :type bot_token: str
        """
        print("This is TG Bot module")
        self.bot_token = bot_token
        self._commands = {}  # Словарь для хранения команд и их обработчиков
        self._users = {}  # Словарь для хранения данных пользователей
        self._is_running = False  # Флаг, указывающий, запущен ли бот

    @property
    def is_running(self) -> bool:
        """
        Возвращает текущее состояние бота (запущен или остановлен).

        :return: True, если бот запущен, иначе False.
        :rtype: bool
        """
        return self._is_running

    def add_command(self, command: str, handler: callable) -> None:
        """
        Добавляет новую команду и её обработчик.

        :param command: Название команды (например, "/start").
        :type command: str
        :param handler: Функция-обработчик команды.
        :type handler: callable
        """
        self._commands[command] = handler
        print(f"Command '{command}' has been added.")

    def remove_command(self, command: str) -> None:
        """
        Удаляет команду и её обработчик.

        :param command: Название команды для удаления.
        :type command: str
        """
        if command in self._commands:
            del self._commands[command]
            print(f"Command '{command}' has been removed.")
        else:
            print(f"Command '{command}' not found.")

    def start(self) -> None:
        """
        Запускает Telegram-бота.
        """
        if not self._is_running:
            self._is_running = True
            print("Bot has been started.")
        else:
            print("Bot is already running.")

    def stop(self) -> None:
        """
        Останавливает Telegram-бота.
        """
        if self._is_running:
            self._is_running = False
            print("Bot has been stopped.")
        else:
            print("Bot is already stopped.")

    def send_message(self, chat_id: int, text: str) -> None:
        """
        Отправляет сообщение в указанный чат.

        :param chat_id: Идентификатор чата.
        :type chat_id: int
        :param text: Текст сообщения.
        :type text: str
        """
        print(f"Message sent to chat {chat_id}: {text}")

    def handle_update(self, update: dict) -> None:
        """
        Обрабатывает входящее обновление от Telegram (например, сообщение или команду).

        :param update: Словарь с данными обновления.
        :type update: dict
        """
        if "message" in update and "text" in update["message"]:
            message_text = update["message"]["text"]
            chat_id = update["message"]["chat"]["id"]

            if message_text in self._commands:
                self._commands[message_text](chat_id)
            else:
                self.send_message(chat_id, "Unknown command. Type /help for a list of commands.")
        else:
            print("Unsupported update type.")

    def set_user_data(self, user_id: int, key: str, value: str) -> None:
        """
        Устанавливает данные пользователя.

        :param user_id: Идентификатор пользователя.
        :type user_id: int
        :param key: Ключ для хранения данных.
        :type key: str
        :param value: Значение данных.
        :type value: str
        """
        if user_id not in self._users:
            self._users[user_id] = {}
        self._users[user_id][key] = value
        print(f"Data for user {user_id} has been updated.")

    def get_user_data(self, user_id: int, key: str) -> str | None:
        """
        Возвращает данные пользователя по ключу.

        :param user_id: Идентификатор пользователя.
        :type user_id: int
        :param key: Ключ для получения данных.
        :type key: str
        :return: Значение данных или None, если данные не найдены.
        :rtype: str
        """
        if user_id in self._users and key in self._users[user_id]:
            return self._users[user_id][key]
        return None
