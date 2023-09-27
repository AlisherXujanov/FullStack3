WISH_LIST = 'wish-list'


class Session:
    valid_keys = [
        WISH_LIST, 'viewed-books'
    ]

    def __init__(self, request) -> None:
        self.session = request.session

    def get(self, key: str, default=None):
        """
        Gets item(s) from session storage
        or gives default value
        """
        self._check_key(key)
        value = self.session.get(key, default)
        return value

    def set(self, key: str, value) -> None:
        """
        CAUTION: This method will override everything
        RU: Этот метод перезапишет всё
        """
        self._check_key(key)
        self.session[key] = value

    def update(self, key: str, value) -> None:
        raise NotImplementedError

    def _check_key(self, key: str) -> bool:
        if key not in self.valid_keys:
            # {key=}  =>  key=...
            raise KeyError(f"{key=} is not a valid key")
        return True


def send_to_wishlist(request, id: int, obj_name: str) -> None:
    if obj_name == "book":
        session = Session(request)
        wish_list = session.get(WISH_LIST, [])
        wish_list.book_ids.append(id)
        session.set(WISH_LIST, wish_list)
    pass
