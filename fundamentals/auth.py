class Auth:
    """
    Класс Auth представляет собой модуль для работы с аутентификацией и авторизацией пользователей.
    Он предоставляет функциональность для регистрации, входа, выхода и управления пользовательскими сессиями.
    """

    def __init__(self):
        """
        Инициализирует экземпляр Auth.
        При создании объекта выводит сообщение о том, что модуль аутентификации был инициализирован.
        Также инициализирует пустой словарь для хранения зарегистрированных пользователей и текущих сессий.
        """
        print("This is Auth module")
        self._users = {}  # Словарь для хранения зарегистрированных пользователей
        self._sessions = {}  # Словарь для хранения активных сессий

    def register(self, username: str, password: str) -> bool:
        """
        Регистрирует нового пользователя.

        :param username: Имя пользователя.
        :type username: str
        :param password: Пароль пользователя.
        :type password: str
        :return: True, если регистрация прошла успешно, иначе False.
        :rtype: bool
        """
        if username in self._users:
            print(f"User '{username}' already exists.")
            return False
        self._users[username] = {"password": password}
        print(f"User '{username}' has been registered.")
        return True

    def login(self, username: str, password: str) -> bool:
        """
        Выполняет вход пользователя в систему.

        :param username: Имя пользователя.
        :type username: str
        :param password: Пароль пользователя.
        :type password: str
        :return: True, если вход выполнен успешно, иначе False.
        :rtype: bool
        """
        if username in self._users and self._users[username]["password"] == password:
            self._sessions[username] = True
            print(f"User '{username}' has logged in.")
            return True
        print(f"Invalid credentials for user '{username}'.")
        return False

    def logout(self, username: str) -> bool:
        """
        Выполняет выход пользователя из системы.

        :param username: Имя пользователя.
        :type username: str
        :return: True, если выход выполнен успешно, иначе False.
        :rtype: bool
        """
        if username in self._sessions:
            del self._sessions[username]
            print(f"User '{username}' has logged out.")
            return True
        print(f"User '{username}' is not logged in.")
        return False

    def is_authenticated(self, username: str) -> bool:
        """
        Проверяет, аутентифицирован ли пользователь.

        :param username: Имя пользователя.
        :type username: str
        :return: True, если пользователь аутентифицирован, иначе False.
        :rtype: bool
        """
        return username in self._sessions

    def change_password(self, username: str, old_password: str, new_password: str) -> bool:
        """
        Изменяет пароль пользователя.

        :param username: Имя пользователя.
        :type username: str
        :param old_password: Текущий пароль пользователя.
        :type old_password: str
        :param new_password: Новый пароль пользователя.
        :type new_password: str
        :return: True, если пароль изменен успешно, иначе False.
        :rtype: bool
        """
        if username in self._users and self._users[username]["password"] == old_password:
            self._users[username]["password"] = new_password
            print(f"Password for user '{username}' has been changed.")
            return True
        print(f"Failed to change password for user '{username}'.")
        return False

    def delete_user(self, username: str) -> bool:
        """
        Удаляет пользователя из системы.

        :param username: Имя пользователя.
        :type username: str
        :return: True, если пользователь удален успешно, иначе False.
        :rtype: bool
        """
        if username in self._users:
            del self._users[username]
            if username in self._sessions:
                del self._sessions[username]
            print(f"User '{username}' has been deleted.")
            return True
        print(f"User '{username}' not found.")
        return False
