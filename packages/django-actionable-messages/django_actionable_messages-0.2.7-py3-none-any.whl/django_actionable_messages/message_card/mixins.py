from django_actionable_messages.mixins import CardElement


class InputMixin(CardElement):
    input_type = None

    def __init__(self, input_id: str = None, title: str = None, value: str = None, is_required: bool = None,
                 **kwargs) -> None:
        self._data = {
            "@type": self.input_type
        }
        super().__init__(**kwargs)
        if input_id is not None:
            self.set_id(input_id)
        if title is not None:
            self.set_title(title)
        if value is not None:
            self.set_value(value)
        if is_required is not None:
            self.set_is_required(is_required)

    def set_id(self, input_id: str) -> None:
        self._data["id"] = input_id

    def set_title(self, title: str) -> None:
        self._data["title"] = title

    def set_value(self, value: str) -> None:
        self._data["value"] = value

    def set_is_required(self, is_required=True) -> None:
        self._data["isRequired"] = is_required
