class DB:
    """
    Класс DB представляет собой модуль для работы с базой данных.
    Он предоставляет функциональность для подключения к базе данных, выполнения запросов и управления данными.
    """

    def __init__(self, db_name: str):
        """
        Инициализирует экземпляр DB.

        :param db_name: Название базы данных.
        :type db_name: str
        """
        print("This is DB module")
        self.db_name = db_name
        self._connection = None  # Подключение к базе данных
        self._tables = {}  # Словарь для хранения таблиц и их данных

    def connect(self) -> bool:
        """
        Подключается к базе данных.

        :return: True, если подключение успешно, иначе False.
        :rtype: bool
        """
        if not self._connection:
            self._connection = True  # Имитация успешного подключения
            print(f"Connected to database '{self.db_name}'.")
            return True
        print(f"Already connected to database '{self.db_name}'.")
        return False

    def disconnect(self) -> bool:
        """
        Отключается от базы данных.

        :return: True, если отключение успешно, иначе False.
        :rtype: bool
        """
        if self._connection:
            self._connection = None
            print(f"Disconnected from database '{self.db_name}'.")
            return True
        print(f"No active connection to database '{self.db_name}'.")
        return False

    def create_table(self, table_name: str, columns: list) -> bool:
        """
        Создает новую таблицу в базе данных.

        :param table_name: Название таблицы.
        :type table_name: str
        :param columns: Список колонок таблицы.
        :type columns: list
        :return: True, если таблица создана успешно, иначе False.
        :rtype: bool
        """
        if table_name in self._tables:
            print(f"Table '{table_name}' already exists.")
            return False
        self._tables[table_name] = {"columns": columns, "data": []}
        print(f"Table '{table_name}' has been created with columns: {columns}.")
        return True

    def insert(self, table_name: str, values: dict) -> bool:
        """
        Вставляет данные в указанную таблицу.

        :param table_name: Название таблицы.
        :type table_name: str
        :param values: Словарь с данными для вставки (ключи - названия колонок).
        :type values: dict
        :return: True, если данные вставлены успешно, иначе False.
        :rtype: bool
        """
        if table_name not in self._tables:
            print(f"Table '{table_name}' does not exist.")
            return False
        self._tables[table_name]["data"].append(values)
        print(f"Data inserted into table '{table_name}': {values}.")
        return True

    def select(self, table_name: str, condition: callable = None) -> list:
        """
        Выполняет выборку данных из указанной таблицы.

        :param table_name: Название таблицы.
        :type table_name: str
        :param condition: Функция-условие для фильтрации данных (опционально).
        :type condition: callable
        :return: Список данных, удовлетворяющих условию.
        :rtype: list
        """
        if table_name not in self._tables:
            print(f"Table '{table_name}' does not exist.")
            return []
        if condition:
            return [row for row in self._tables[table_name]["data"] if condition(row)]
        return self._tables[table_name]["data"]

    def update(self, table_name: str, condition: callable, new_values: dict) -> bool:
        """
        Обновляет данные в указанной таблице.

        :param table_name: Название таблицы.
        :type table_name: str
        :param condition: Функция-условие для поиска данных, которые нужно обновить.
        :type condition: callable
        :param new_values: Словарь с новыми значениями.
        :type new_values: dict
        :return: True, если данные обновлены успешно, иначе False.
        :rtype: bool
        """
        if table_name not in self._tables:
            print(f"Table '{table_name}' does not exist.")
            return False
        updated = False
        for row in self._tables[table_name]["data"]:
            if condition(row):
                row.update(new_values)
                updated = True
        if updated:
            print(f"Data in table '{table_name}' has been updated.")
        else:
            print(f"No data matching the condition in table '{table_name}'.")
        return updated

    def delete(self, table_name: str, condition: callable) -> bool:
        """
        Удаляет данные из указанной таблицы.

        :param table_name: Название таблицы.
        :type table_name: str
        :param condition: Функция-условие для поиска данных, которые нужно удалить.
        :type condition: callable
        :return: True, если данные удалены успешно, иначе False.
        :rtype: bool
        """
        if table_name not in self._tables:
            print(f"Table '{table_name}' does not exist.")
            return False
        initial_count = len(self._tables[table_name]["data"])
        self._tables[table_name]["data"] = [
            row for row in self._tables[table_name]["data"] if not condition(row)
        ]
        if len(self._tables[table_name]["data"]) < initial_count:
            print(f"Data deleted from table '{table_name}'.")
            return True
        print(f"No data matching the condition in table '{table_name}'.")
        return False

    def drop_table(self, table_name: str) -> bool:
        """
        Удаляет таблицу из базы данных.

        :param table_name: Название таблицы.
        :type table_name: str
        :return: True, если таблица удалена успешно, иначе False.
        :rtype: bool
        """
        if table_name not in self._tables:
            print(f"Table '{table_name}' does not exist.")
            return False
        del self._tables[table_name]
        print(f"Table '{table_name}' has been dropped.")
        return True
