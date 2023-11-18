from django_actionable_messages.mixins import Card


class CardMixin(Card):
    content_type = ""

    def __init__(self, title: str = None, subtitle: str = None, text: str = None, images=None, buttons=None,
                 **kwargs) -> None:
        self._payload = {
             "contentType": self.content_type
        }
        super().__init__(**kwargs)
        if title is not None:
            self.set_title(title)
        if subtitle is not None:
            self.set_subtitle(subtitle)
        if text is not None:
            self.set_text(text)
        if images is not None:
            self.add_images(images)
        if buttons is not None:
            self.add_buttons(buttons)

    def set_title(self, title: str) -> None:
        self._payload.setdefault("content", {})
        self._payload["content"]["title"] = title

    def set_subtitle(self, subtitle: str) -> None:
        self._payload.setdefault("content", {})
        self._payload["content"]["subtitle"] = subtitle

    def set_text(self, text: str) -> None:
        self._payload.setdefault("content", {})
        self._payload["content"]["text"] = text

    def add_images(self, images) -> None:
        self._payload.setdefault("content", {})
        self._payload["content"].setdefault("images", [])
        if isinstance(images, (list, set, tuple)):
            self._payload["content"]["images"].extend(self._get_items_list(images))
        else:
            self._payload["content"]["images"].append(images.as_data())

    def add_buttons(self, buttons) -> None:
        self._payload.setdefault("content", {})
        self._payload["content"].setdefault("buttons", [])
        if isinstance(buttons, (list, set, tuple)):
            self._payload["content"]["buttons"].extend(self._get_items_list(buttons))
        else:
            self._payload["content"]["buttons"].append(buttons.as_data())
