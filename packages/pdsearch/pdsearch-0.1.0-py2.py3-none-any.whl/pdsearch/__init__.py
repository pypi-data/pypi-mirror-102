"""Let's find some podcasts!"""
from typing import Optional
from dataclasses import dataclass

from requests import get as _get

__version__ = "0.1.0"

SEARCH_URL = 'https://itunes.apple.com/search'


@dataclass
class Podcast:
    """Podcast metada."""

    id: str
    name: str
    author: str
    feed: Optional[str] = None
    category: Optional[str] = None
    image: Optional[str] = None


def search(name: str, count: int = 5) -> list[Podcast]:
    """Search podcast by name."""
    params = {"name": name, "limit": limit, "media": "podcast"}
    response = _get(url=SEARCH_URL, params=params)
    return _parse(response)
