from typing import Union, List

from django_actionable_messages.adaptive_card.mixins import BaseElementMixin, ElementMixin
from django_actionable_messages.adaptive_card.utils import (
    HorizontalAlignment, Color, FontType, FontSize, FontWeight, BlockElementHeight, ImageSize, ImageStyle
)
from django_actionable_messages.exceptions import CardException
from django_actionable_messages.mixins import CardElement


class TextBlock(ElementMixin):
    def __init__(self, text: str, color: Color = None, font_type: FontType = None,
                 horizontal_alignment: HorizontalAlignment = None, is_subtle: bool = None, max_lines: int = None,
                 size: FontSize = None, weight: FontWeight = None, wrap: bool = None, **kwargs) -> None:
        self._data = {
            "type": "TextBlock",
            "text": text
        }
        super().__init__(**kwargs)
        if color is not None:
            self.set_color(color)
        if font_type is not None:
            self.set_font_type(font_type)
        if horizontal_alignment is not None:
            self.set_horizontal_alignment(horizontal_alignment)
        if is_subtle is not None:
            self.set_is_subtle(is_subtle)
        if max_lines is not None:
            self.set_max_lines(max_lines)
        if size is not None:
            self.set_size(size)
        if weight is not None:
            self.set_weight(weight)
        if wrap is not None:
            self.set_wrap(wrap)

    def set_color(self, color: Color) -> None:
        self._data["color"] = color

    def set_font_type(self, font_type: FontType) -> None:
        self._data["fontType"] = font_type

    def set_horizontal_alignment(self, alignment: HorizontalAlignment) -> None:
        self._data["horizontalAlignment"] = alignment

    def set_is_subtle(self, value=True) -> None:
        self._data["isSubtle"] = value

    def set_max_lines(self, max_lines: int) -> None:
        self._data["maxLines"] = max_lines

    def set_size(self, size: FontSize) -> None:
        self._data["size"] = size

    def set_weight(self, weight: FontWeight) -> None:
        self._data["weight"] = weight

    def set_wrap(self, value=True) -> None:
        self._data["wrap"] = value


class Image(BaseElementMixin):
    def __init__(self, url: str, alternate_text: str = None, background_color: str = None,
                 height: Union[str, BlockElementHeight] = None, horizontal_alignment: HorizontalAlignment = None,
                 select_action=None, size: ImageSize = None, style: ImageStyle = None, width: str = None,
                 **kwargs) -> None:
        self._data = {
            "type": "Image",
            "url": url
        }
        super().__init__(**kwargs)
        if alternate_text is not None:
            self.set_alternate_text(alternate_text)
        if background_color is not None:
            self.set_background_color(background_color)
        if height is not None:
            self.set_height(height)
        if horizontal_alignment is not None:
            self.set_horizontal_alignment(horizontal_alignment)
        if select_action is not None:
            self.set_select_action(select_action)
        if size is not None:
            self.set_size(size)
        if style is not None:
            self.set_style(style)
        if width is not None:
            self.set_width(width)

    def set_url(self, url: str) -> None:
        self._data["url"] = url

    def set_alternate_text(self, text: str) -> None:
        self._data["altText"] = text

    def set_background_color(self, color: str) -> None:
        self._data["backgroundColor"] = color

    def set_height(self, height: Union[str, BlockElementHeight]) -> None:
        if isinstance(height, BlockElementHeight):
            self._data["height"] = height
        elif isinstance(height, str):
            self._data["height"] = height
        else:
            raise CardException("Invalid height type")

    def set_horizontal_alignment(self, alignment: HorizontalAlignment) -> None:
        self._data["horizontalAlignment"] = alignment

    def set_select_action(self, action) -> None:
        self._data["selectAction"] = action.as_data()

    def set_size(self, size: ImageSize) -> None:
        self._data["size"] = size

    def set_style(self, style: ImageStyle) -> None:
        self._data["style"] = style

    def set_width(self, width: str) -> None:
        self._data["width"] = width


class MediaSource(CardElement):
    def __init__(self, mime_type: str, url: str, **kwargs) -> None:
        self._data = {
            "mimeType": mime_type,
            "url": url
        }
        super().__init__(**kwargs)


class CaptionSource(CardElement):
    def __init__(self, mime_type: str, url: str, label: str, **kwargs) -> None:
        self._data = {
            "mimeType": mime_type,
            "url": url,
            "label": label
        }
        super().__init__(**kwargs)


class Media(ElementMixin):
    def __init__(self, sources: List[MediaSource], poster: str = None, alternate_text: str = None,
                 caption_sources: List[CaptionSource] = None, **kwargs) -> None:
        self._data = {
            "type": "Media",
            "sources": self._get_items_list(sources)
        }
        super().__init__(**kwargs)
        if poster is not None:
            self.set_poster(poster)
        if alternate_text is not None:
            self.set_alternate_text(alternate_text)
        if caption_sources is not None:
            self.set_caption_sources(caption_sources)

    def add_sources(self, sources: List[MediaSource]) -> None:
        self._data["sources"].extend(self._get_items_list(sources))

    def add_source(self, source: MediaSource) -> None:
        self._data["sources"].append(source.as_data())

    def set_poster(self, poster: str) -> None:
        self._data["poster"] = poster

    def set_alternate_text(self, text: str) -> None:
        self._data["altText"] = text

    def set_caption_sources(self, caption_sources: List[CaptionSource]) -> None:
        self._data["captionSources"] = self._get_items_list(caption_sources)

    def add_caption_sources(self, caption_sources: List[CaptionSource]) -> None:
        self._data.setdefault("captionSources", [])
        self._data["captionSources"].extend(self._get_items_list(caption_sources))

    def add_caption_source(self, caption_source: CaptionSource) -> None:
        self._data.setdefault("captionSources", [])
        self._data["captionSources"].append(caption_source.as_data())


class TextRun(CardElement):
    def __init__(self, text: str, color: Color = None, font_type: FontType = None, highlight: bool = None,
                 is_subtle: bool = None, italic: bool = None, select_action=None, size: FontSize = None,
                 strike_through: bool = None, weight: FontWeight = None, **kwargs) -> None:
        self._data = {
            "type": "TextRun",
            "text": text
        }
        super().__init__(**kwargs)
        if color is not None:
            self.set_color(color)
        if font_type is not None:
            self.set_font_type(font_type)
        if highlight is not None:
            self.set_highlight(highlight)
        if is_subtle is not None:
            self.set_is_subtle(is_subtle)
        if italic is not None:
            self.set_italic(italic)
        if select_action:
            self.set_select_action(select_action)
        if size is not None:
            self.set_size(size)
        if strike_through is not None:
            self.set_strike_through(strike_through)
        if weight is not None:
            self.set_weight(weight)

    def set_color(self, color: Color) -> None:
        self._data["color"] = color

    def set_font_type(self, font_type: FontType) -> None:
        self._data["fontType"] = font_type

    def set_highlight(self, value=True) -> None:
        self._data["highlight"] = value

    def set_is_subtle(self, value=True) -> None:
        self._data["isSubtle"] = value

    def set_italic(self, value=True) -> None:
        self._data["italic"] = value

    def set_select_action(self, action) -> None:
        self._data["selectAction"] = action.as_data()

    def set_size(self, size: FontSize) -> None:
        self._data["size"] = size

    def set_strike_through(self, value=True) -> None:
        self._data["strikethrough"] = value

    def set_weight(self, weight: FontWeight) -> None:
        self._data["weight"] = weight


class RichTextBlock(ElementMixin):
    def __init__(self, inlines: List[Union[TextRun, str]], horizontal_alignment: HorizontalAlignment = None,
                 **kwargs) -> None:
        self._data = {
            "type": "RichTextBlock",
            "inlines": []
        }
        for item in inlines:
            if isinstance(item, TextRun):
                self._data["inlines"].append(item.as_data())
            elif isinstance(item, str):
                self._data["inlines"].append(item)
            else:
                raise CardException("Invalid inline type")
        super().__init__(**kwargs)
        if horizontal_alignment is not None:
            self.set_horizontal_alignment(horizontal_alignment)

    def set_horizontal_alignment(self, alignment: HorizontalAlignment) -> None:
        self._data["horizontalAlignment"] = alignment
