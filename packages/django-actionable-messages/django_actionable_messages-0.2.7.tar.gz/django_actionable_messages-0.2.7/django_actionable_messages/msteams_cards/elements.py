from django_actionable_messages.mixins import CardElement


class OpenUrl(CardElement):
    def __init__(self, title: str, url: str, **kwargs) -> None:
        self._data = {
            "type": "openUrl",
            "title": title,
            "value": url
        }
        super().__init__(**kwargs)


class Image(CardElement):
    def __init__(self, url: str, alt: str = None, **kwargs) -> None:
        self._data = {
            "url": url
        }
        super().__init__(**kwargs)
        if alt is not None:
            self.set_alt(alt)

    def set_alt(self, alt: str) -> None:
        self._data["alt"] = alt
