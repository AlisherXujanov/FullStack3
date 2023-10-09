from books.models import Books

WISH_LIST = 'wish-list'
VIEWED_BOOKS = 'viewed-books'
BOOK_IDS = "book_ids"


class Session:
    valid_keys = [WISH_LIST, VIEWED_BOOKS]

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


def send_to_wishlist(request, item_id: int, obj_name: str) -> None:
    """Sends item to wishlist

    Args:
        request (HttpRequest): needed to get session 
        item_id (int): id of any item
        obj_name (str): name of object (book, etc.)
    """
    session = Session(request)
    wish_list = session.get(WISH_LIST, {})

    match obj_name:
        case "book":
            if wish_list.get(BOOK_IDS):
                if item_id in wish_list[BOOK_IDS]:
                    return True
                wish_list[BOOK_IDS].append(item_id)
            else:
                wish_list[BOOK_IDS] = [item_id]
            session.set(WISH_LIST, wish_list)

    # We can add more objects here
    pass


def getItemsFromWishlist(request, item_type: str = 'all') -> list[int]:
    """
        Gets items from wishlist (all by default or by type)
    """
    session = Session(request)
    wish_list = session.get(WISH_LIST, {})

    match item_type:
        case "all":
            return wish_list
        case "book":
            return wish_list.get(BOOK_IDS, [])

    # We can add more logic here
    pass


def delete_item_from_wishlist(request, item_id: int, item_type: str) -> None:
    session = Session(request)
    wish_list = session.get(WISH_LIST, {})

    match item_type:
        case "book":
            books_ids = wish_list.get(BOOK_IDS)
            books_ids.remove(item_id)
            wish_list[BOOK_IDS] = books_ids

    session.set(WISH_LIST, wish_list)


def testpermission(user, book_id: int = None) -> bool:
    if user.is_authenticated:

        if book_id:
            if book := Books.objects.filter(id=book_id).first():
                if user == book.author:
                    return True
            return False
        else:
            return True
    else:
        return False
