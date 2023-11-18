from typing import List, Union

from django_actionable_messages.adaptive_card.mixins import InputMixin, DateTimeMixin
from django_actionable_messages.adaptive_card.utils import ChoiceInputStyle, TextInputStyle
from django_actionable_messages.mixins import CardElement


class TextInput(InputMixin):
    def __init__(self, is_multiline: bool = None, max_length: int = None, placeholder: str = None,
                 style: TextInputStyle = None, inline_action=None, value: str = None, **kwargs) -> None:
        self._data = {
            "type": "Input.Text"
        }
        super().__init__(**kwargs)
        if is_multiline is not None:
            self.set_is_multiline(is_multiline)
        if max_length is not None:
            self.set_max_length(max_length)
        if placeholder is not None:
            self.set_placeholder(placeholder)
        if style is not None:
            self.set_style(style)
        if inline_action is not None:
            self.set_inline_action(inline_action)
        if value is not None:
            self.set_value(value)

    def set_is_multiline(self, value=True) -> None:
        self._data["isMultiline"] = value

    def set_max_length(self, value: int) -> None:
        self._data["maxLength"] = value

    def set_placeholder(self, text: str) -> None:
        self._data["placeholder"] = text

    def set_style(self, style: TextInputStyle) -> None:
        self._data["style"] = style

    def set_inline_action(self, action) -> None:
        self._data["inlineAction"] = action.as_data()

    def set_value(self, value: str) -> None:
        self._data["value"] = value


class NumberInput(InputMixin):
    def __init__(self, max_value: int = None, min_value: int = None, placeholder: str = None, value: int = None,
                 **kwargs) -> None:
        self._data = {
            "type": "Input.Number"
        }
        super().__init__(**kwargs)
        if max_value is not None:
            self.set_max(max_value)
        if min_value is not None:
            self.set_min(min_value)
        if placeholder is not None:
            self.set_placeholder(placeholder)
        if value is not None:
            self.set_value(value)

    def set_max(self, value: int) -> None:
        self._data["max"] = value

    def set_min(self, value: int) -> None:
        self._data["min"] = value

    def set_placeholder(self, text: str) -> None:
        self._data["placeholder"] = text

    def set_value(self, value: int) -> None:
        self._data["value"] = value


class DateInput(DateTimeMixin):
    base_type = "Input.Date"


class TimeInput(DateTimeMixin):
    base_type = "Input.Time"


class ToggleInput(InputMixin):
    def __init__(self, title: str, value: str = None, value_off: str = None, value_on: str = None, wrap: bool = None,
                 **kwargs) -> None:
        self._data = {
            "type": "Input.Toggle",
            "title": title
        }
        super().__init__(**kwargs)
        if value is not None:
            self.set_value(value)
        if value_off is not None:
            self.set_value_off(value_off)
        if value_on is not None:
            self.set_value_on(value_on)
        if wrap is not None:
            self.set_wrap(wrap)

    def set_value(self, value: str) -> None:
        self._data["value"] = value

    def set_value_off(self, value: str) -> None:
        self._data["valueOff"] = value

    def set_value_on(self, value: str) -> None:
        self._data["valueOn"] = value

    def set_wrap(self, value=True) -> None:
        self._data["wrap"] = value


class InputChoice(CardElement):
    def __init__(self, title: str, value: Union[str, int], **kwargs) -> None:
        self._data = {
            "title": title,
            "value": value
        }
        super().__init__(**kwargs)


class ChoiceSetInput(InputMixin):
    def __init__(self, choices: List[InputChoice], is_multi_select: bool = None, style: ChoiceInputStyle = None,
                 value: str = None, wrap: bool = None, **kwargs) -> None:
        self._data = {
            "type": "Input.ChoiceSet",
            "choices": self._get_items_list(choices)
        }
        super().__init__(**kwargs)
        if is_multi_select is not None:
            self.set_is_multi_select(is_multi_select)
        if style is not None:
            self.set_style(style)
        if value is not None:
            self.set_value(value)
        if wrap is not None:
            self.set_wrap(wrap)

    def set_is_multi_select(self, value=True) -> None:
        self._data["isMultiSelect"] = value

    def set_style(self, style: ChoiceInputStyle) -> None:
        self._data["style"] = style

    def set_value(self, value: str) -> None:
        self._data["value"] = value

    def set_wrap(self, value=True) -> None:
        self._data["wrap"] = value


class DataQuery(CardElement):
    def __init__(self, dataset: str, count: int = None, skip: int = None, **kwargs) -> None:
        self._data = {
            "dataset": dataset
        }
        super().__init__(**kwargs)
        if count is not None:
            self.set_count(count)
        if skip is not None:
            self.set_skip(skip)

    def set_dataset(self, dataset: str) -> None:
        self._data["dataset"] = dataset

    def set_count(self, count: int) -> None:
        self._data["count"] = count

    def set_skip(self, skip: int) -> None:
        self._data["skip"] = skip
