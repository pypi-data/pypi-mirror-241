from django_actionable_messages.exceptions import CardException
from django_actionable_messages.mixins import CardElement


class OpenUri(CardElement):
    def __init__(self, name: str, targets: list = None, **kwargs) -> None:
        self._data = {
            "@type": "OpenUri",
            "name": name
        }
        super().__init__(**kwargs)
        if targets is not None:
            self.add_targets(targets)

    def add_targets(self, targets: list) -> None:
        for target in targets:
            self.add_target(target)

    def add_target(self, target) -> None:
        targets = self._data.setdefault("targets", [])
        self._check_target(target, targets)
        self._data["targets"].append(target.as_data())

    def _check_target(self, target: list, targets: list) -> None:
        os_type = target._get_os()
        os_list = (x["os"] for x in targets)
        if os_type in os_list:
            raise CardException(f"Target already set for '{os_type}'")


class HttpPOST(CardElement):
    def __init__(self, name: str, target: str, headers: list = None, body: str = None, body_content_type: str = None,
                 **kwargs) -> None:
        self._data = {
            "@type": "HttpPOST",
            "name": name,
            "target": target
        }
        super().__init__(**kwargs)
        if headers is not None:
            self.add_headers(headers)
        if body is not None:
            self.set_body(body)
        if body_content_type is not None:
            self.set_body_content_type(body_content_type)

    def add_headers(self, headers) -> None:
        self._data.setdefault("headers", [])
        if isinstance(headers, (list, set, tuple)):
            self._data["headers"].extend(self._get_items_list(headers))
        else:
            self._data["headers"].append(headers.as_data())

    def set_body(self, body: str) -> None:
        self._data["body"] = body

    def set_body_content_type(self, content_type: str) -> None:
        self._data["bodyContentType"] = content_type


class InvokeAddInCommand(CardElement):
    def __init__(self, name: str, add_in_id: str, desktop_command_id: str, initialization_context: dict = None,
                 **kwargs) -> None:
        self._data = {
            "@type": "InvokeAddInCommand",
            "name": name,
            "addInId": add_in_id,
            "desktopCommandId": desktop_command_id
        }
        super().__init__(**kwargs)
        if initialization_context is not None:
            self.set_initialization_context(initialization_context)

    def set_add_in_id(self, add_in_id: str) -> None:
        self._data["addInId"] = add_in_id

    def set_desktop_command_id(self, cmd_it: str) -> None:
        self._data["desktopCommandId"] = cmd_it

    def set_initialization_context(self, context: dict) -> None:
        self._data["initializationContext"] = context


class ActionCard(CardElement):
    def __init__(self, name: str, inputs: list = None, actions: list = None, **kwargs) -> None:
        self._data = {
            "@type": "ActionCard",
            "name": name
        }
        super().__init__(**kwargs)
        if inputs is not None:
            self.add_inputs(inputs)
        if actions is not None:
            self.add_actions(actions)

    def add_inputs(self, inputs) -> None:
        self._data.setdefault("inputs", [])
        if isinstance(inputs, (list, set, tuple)):
            self._data["inputs"].extend(self._get_items_list(inputs))
        else:
            self._data["inputs"].append(inputs.as_data())

    def add_actions(self, actions) -> None:
        self._data.setdefault("actions", [])
        if isinstance(actions, (list, set, tuple)):
            self._data["actions"].extend(self._get_items_list(actions))
        else:
            self._data["actions"].append(actions.as_data())
