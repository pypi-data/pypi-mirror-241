from typing import Union

from django_actionable_messages.message_card.utils import OSType
from django_actionable_messages.mixins import CardElement


class Fact(CardElement):
    def __init__(self, name: str, value: Union[str, int], **kwargs) -> None:
        self._data = {
            "name": name,
            "value": value
        }
        super().__init__(**kwargs)


class HeroImage(CardElement):
    def __init__(self, url: str, title: str = None, **kwargs) -> None:
        self._data = {
            "image": url
        }
        super().__init__(**kwargs)
        if title is not None:
            self.set_title(title)

    def set_title(self, title: str) -> None:
        self._data["title"] = title


class InputChoice(CardElement):
    def __init__(self, name: str, value: Union[str, int], **kwargs) -> None:
        self._data = {
            "value": value,
            "display": name
        }
        super().__init__(**kwargs)

    def _get_value(self) -> Union[str, int]:
        return self._data["value"]


class ActionTarget(CardElement):
    def __init__(self, os_type: OSType, url: str, **kwargs) -> None:
        self._data = {
            "os": os_type,
            "uri": url
        }
        super().__init__(**kwargs)

    def _get_os(self) -> OSType:
        return self._data["os"]
