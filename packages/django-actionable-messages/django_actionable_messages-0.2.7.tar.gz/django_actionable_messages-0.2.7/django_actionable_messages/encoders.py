from django.core.serializers.json import DjangoJSONEncoder
from django.utils import translation


class EncoderMixin:
    def __init__(self, *args, **kwargs):
        self.lang_code = kwargs.pop("lang_code", None)
        super().__init__(*args, **kwargs)


class BaseEncoder(EncoderMixin, DjangoJSONEncoder):
    """
    Everything that DjangoJSONEncoder can handle and translations with selected language
    """

    def default(self, o):
        with translation.override(self.lang_code):
            return super().default(o)
