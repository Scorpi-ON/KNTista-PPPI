class GPT:
    """
    Класс GPT представляет собой модуль для работы с генеративными предобученными трансформерами (GPT).
    Он предоставляет функциональность для генерации текста, настройки модели и управления контекстом.
    """

    def __init__(self, model_name: str = "gpt-4"):
        """
        Инициализирует экземпляр GPT.

        :param model_name: Название модели GPT (по умолчанию "gpt-4").
        :type model_name: str
        """
        print("This is GPT module")
        self.model_name = model_name
        self._context = []  # Список для хранения контекста диалога
        self._temperature = 0.7  # Параметр температуры для генерации текста
        self._max_tokens = 100  # Максимальное количество токенов в ответе

    @property
    def context(self) -> list:
        """
        Возвращает текущий контекст диалога.

        :return: Список сообщений в контексте.
        :rtype: list
        """
        return self._context

    @property
    def temperature(self) -> float:
        """
        Возвращает текущее значение параметра температуры.

        :return: Значение температуры.
        :rtype: float
        """
        return self._temperature

    @temperature.setter
    def temperature(self, value: float) -> None:
        """
        Устанавливает значение параметра температуры.

        :param value: Новое значение температуры (должно быть между 0 и 1).
        :type value: float
        :raises ValueError: Если значение температуры выходит за допустимые пределы.
        """
        if 0 <= value <= 1:
            self._temperature = value
        else:
            raise ValueError("Temperature must be between 0 and 1.")

    @property
    def max_tokens(self) -> int:
        """
        Возвращает текущее значение максимального количества токенов.

        :return: Максимальное количество токенов.
        :rtype: int
        """
        return self._max_tokens

    @max_tokens.setter
    def max_tokens(self, value: int) -> None:
        """
        Устанавливает значение максимального количества токенов.

        :param value: Новое значение максимального количества токенов (должно быть положительным).
        :type value: int
        :raises ValueError: Если значение максимального количества токенов отрицательное.
        """
        if value > 0:
            self._max_tokens = value
        else:
            raise ValueError("Max tokens must be a positive integer.")

    def generate_text(self, prompt: str) -> str:
        """
        Генерирует текст на основе заданного промпта и текущего контекста.

        :param prompt: Текст запроса для генерации.
        :type prompt: str
        :return: Сгенерированный текст.
        :rtype: str
        """
        # Имитация генерации текста
        response = f"Generated response for prompt: '{prompt}' using {self.model_name}."
        self._context.append({"role": "user", "content": prompt})
        self._context.append({"role": "assistant", "content": response})
        return response

    def clear_context(self) -> None:
        """
        Очищает текущий контекст диалога.
        """
        self._context = []
        print("Context has been cleared.")

    def set_model(self, model_name: str) -> None:
        """
        Устанавливает новую модель GPT.

        :param model_name: Название модели GPT.
        :type model_name: str
        """
        self.model_name = model_name
        print(f"Model has been set to {model_name}.")
