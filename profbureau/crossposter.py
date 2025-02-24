from datetime import datetime


class Crossposter:
    """
    Класс Crossposter представляет собой модуль для публикации постов во всех соцсетях ИКНТ (ВК и Telegram).
    Он предоставляет функциональность для одновременной публикации постов, управления атрибутами (хештеги, оформление)
    и контроля прав доступа для публикации.
    """

    def __init__(self):
        """
        Инициализирует экземпляр Crossposter.
        При создании объекта выводит сообщение о том, что модуль кросс-постинга был инициализирован.
        Также инициализирует пустые структуры для хранения постов, черновиков и прав доступа.
        """
        print("This is Crossposter module")
        self._posts = []  # Список для хранения опубликованных постов
        self._drafts = []  # Список для хранения черновиков
        self._users = {}  # Словарь для хранения прав доступа пользователей

    def add_user(self, user_id: int, can_publish: bool) -> None:
        """
        Добавляет пользователя в систему с указанием прав на публикацию.

        :param user_id: Идентификатор пользователя.
        :type user_id: int
        :param can_publish: Имеет ли пользователь право на публикацию.
        :type can_publish: bool
        """
        self._users[user_id] = {"can_publish": can_publish}
        print(f"User {user_id} added with publish rights: {can_publish}.")

    def create_post(self, user_id: int, content: str, hashtags: list[str], images: list[str]) -> None:
        """
        Создает пост. Если пользователь имеет право на публикацию, пост публикуется сразу.
        В противном случае пост сохраняется как черновик для одобрения.

        :param user_id: Идентификатор пользователя, создающего пост.
        :type user_id: int
        :param content: Текст поста.
        :type content: str
        :param hashtags: Список хештегов для поста.
        :type hashtags: list[str]
        :param images: Список путей к изображениям для поста.
        :type images: list[str]
        """
        post = {
            "user_id": user_id,
            "content": content,
            "hashtags": hashtags,
            "images": images,
            "timestamp": datetime.now()
        }

        if user_id in self._users and self._users[user_id]["can_publish"]:
            self._publish_post(post)
        else:
            self._drafts.append(post)
            print(f"Post by user {user_id} saved as draft for approval.")

    def _publish_post(self, post: dict) -> None:
        """
        Публикует пост во всех соцсетях (ВК и Telegram).

        :param post: Данные поста для публикации.
        :type post: dict
        """
        self._posts.append(post)
        print(f"Post published on VK and Telegram: {post['content']}")
        print(f"Hashtags: {', '.join(post['hashtags'])}")
        print(f"Images: {', '.join(post['images'])}")

    def approve_draft(self, draft_id: int, approver_id: int) -> None:
        """
        Одобряет черновик для публикации, если пользователь имеет право на одобрение.

        :param draft_id: Индекс черновика в списке черновиков.
        :type draft_id: int
        :param approver_id: Идентификатор пользователя, одобряющего черновик.
        :type approver_id: int
        """
        if 0 <= draft_id < len(self._drafts):
            if approver_id in self._users and self._users[approver_id]["can_publish"]:
                post = self._drafts.pop(draft_id)
                self._publish_post(post)
            else:
                print(f"User {approver_id} does not have permission to approve drafts.")
        else:
            print(f"Draft {draft_id} not found.")

    def list_posts(self) -> list:
        """
        Возвращает список всех опубликованных постов.

        :return: Список опубликованных постов.
        :rtype: list
        """
        return self._posts

    def list_drafts(self) -> list:
        """
        Возвращает список всех черновиков.

        :return: Список черновиков.
        :rtype: list
        """
        return self._drafts

    def list_users(self) -> list:
        """
        Возвращает список всех пользователей и их прав на публикацию.

        :return: Список пользователей и их прав.
        :rtype: list
        """
        return [{"user_id": uid, "can_publish": data["can_publish"]} for uid, data in self._users.items()]
