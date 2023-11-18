from django_actionable_messages.mixins import CardElement


class ElementMixin(CardElement):
    def __init__(self, is_visible: bool = None, **kwargs) -> None:
        super().__init__(**kwargs)
        if is_visible is not None:
            self.set_is_visible(is_visible)

    def set_is_visible(self, visible=True) -> None:
        self._data["isVisible"] = visible


class DisplayFormMixin(ElementMixin):
    base_type = ""

    def __init__(self, title: str = None, item_id=None, **kwargs) -> None:
        self._data = {
            "type": self.base_type
        }
        super().__init__(**kwargs)
        if title is not None:
            self.set_title(title)
        if item_id is not None:
            self.set_item_id(item_id)

    def set_title(self, title: str) -> None:
        self._data["title"] = title

    def set_item_id(self, item_id) -> None:
        self._data["itemId"] = item_id
