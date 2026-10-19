"""Модуль анализа топологий компьютерных сетей."""

from enum import Enum
from typing import List, Set, Tuple


class ConnectionType(Enum):
    """Перечисление типов сетевых топологий."""

    UNKNOWN = 0
    TIRE = 1  # Шина
    RING = 2  # Кольцо
    STAR = 3  # Звезда


def is_full_connected(
    v: int,
    r: int,
    links: List[Tuple[int, int]],
) -> bool:
    """Определяет, является ли заданная сеть полносвязной (полным графом).

    :param v: Число вершин (компьютеров).
    :param r: Число рёбер (связей).
    :param links: Список связей между вершинами.
    :return: True, если сеть полносвязная, иначе False.
    """
    # В полном графе число ребер строго равно v * (v - 1) // 2
    expected_edges_count: int = (v * (v - 1)) // 2
    if r != expected_edges_count or len(links) != r:
        return False

    # Проверка уникальности связей без учета направления и петель
    unique_edges: Set[Tuple[int, int]] = set()
    for node1, node2 in links:
        if node1 == node2:
            return False
        edge: Tuple[int, int] = (min(node1, node2), max(node1, node2))
        unique_edges.add(edge)

    return len(unique_edges) == expected_edges_count