from dataclasses import dataclass


@dataclass
class Routes:
    """Содержит адреса страниц."""
    url: str = "https://www.avito.ru/"


@dataclass
class ElementAttributes:
    """Содержит названия аттрибутов."""
    marker: str = "data-marker"
    title: str = "title"
