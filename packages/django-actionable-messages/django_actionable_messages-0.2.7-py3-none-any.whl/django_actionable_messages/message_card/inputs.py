from django_actionable_messages.exceptions import CardException
from django_actionable_messages.message_card.mixins import InputMixin
from django_actionable_messages.message_card.utils import ChoiceStyle


class TextInput(InputMixin):
    input_type = "TextInput"

    def __init__(self, max_length: int = None, is_multiline: bool = False, **kwargs) -> None:
        super().__init__(**kwargs)
        if max_length is not None:
            self.set_max_length(max_length)
        self.set_is_multiline(is_multiline)

    def set_max_length(self, max_length: int) -> None:
        self._data["maxLength"] = max_length

    def set_is_multiline(self, is_multiline=True) -> None:
        self._data["isMultiline"] = is_multiline


class DateInput(InputMixin):
    input_type = "DateInput"

    def __init__(self, include_time: bool = None, **kwargs) -> None:
        super().__init__(**kwargs)
        if include_time is not None:
            self.set_include_time(include_time)

    def set_include_time(self, include_time=True) -> None:
        self._data["includeTime"] = include_time


class MultiChoiceInput(InputMixin):
    input_type = "MultichoiceInput"

    def __init__(self, choices: list = None, is_multi_select: bool = None, style: ChoiceStyle = None, **kwargs) -> None:
        super().__init__(**kwargs)
        if choices is not None:
            self.add_choices(choices)
        if is_multi_select is not None:
            self.set_is_multi_select(is_multi_select)
        if style is not None:
            self.set_style(style)

    def add_choices(self, choices: list) -> None:
        for choice in choices:
            self.add_choice(choice)

    def add_choice(self, choice) -> None:
        choices = self._data.setdefault("choices", [])
        self._check_choice(choice, choices)
        self._data["choices"].append(choice.as_data())

    def set_is_multi_select(self, is_multi_select=True) -> None:
        self._data["isMultiSelect"] = is_multi_select

    def set_style(self, style: ChoiceStyle) -> None:
        self._data["style"] = style

    def _check_choice(self, choice, choices) -> None:
        choice_value = choice._get_value()
        values_list = (c["value"] for c in choices)
        if choice_value in values_list:
            raise CardException(f"Choice with this 'value' [{choice_value}] already added")
