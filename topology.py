"""Модуль анализа топологий компьютерных сетей."""

from enum import Enum
from typing import List, Set, Tuple


class ConnectionType(Enum):
    """Перечисление типов сетевых топологий."""

    UNKNOWN = 0
    TIRE = 1  # Шина
    RING = 2  # Кольцо
    STAR = 3  # Звезда