"""Модуль анализа топологий компьютерных сетей."""

from collections import deque
from enum import Enum
from typing import Dict, List, Set, Tuple


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


def _is_connected(v: int, adj_list: Dict[int, List[int]]) -> bool:
    """Проверяет связность графа с помощью обхода в ширину (BFS).

    :param v: Число вершин.
    :param adj_list: Список смежности графа.
    :return: True, если граф связный, иначе False.
    """
    visited: Set[int] = set()
    queue: deque = deque([1])
    visited.add(1)

    while queue:
        current_node = queue.popleft()
        for neighbor in adj_list.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return len(visited) == v


def connection_type(
    v: int,
    r: int,
    links: List[Tuple[int, int]],
) -> int:
    """Определяет тип неполносвязной топологии сети.

    :param v: Число вершин (v > 4).
    :param r: Число рёбер (r > 3).
    :param links: Список связей.
    :return: Значение перечисления ConnectionType (1, 2, 3 или 0).
    """
    # Построение списка смежности и степеней вершин
    adj_list: Dict[int, List[int]] = {i: [] for i in range(1, v + 1)}
    unique_edges: Set[Tuple[int, int]] = set()

    for node1, node2 in links:
        if not (1 <= node1 <= v and 1 <= node2 <= v):
            return ConnectionType.UNKNOWN.value
        edge: Tuple[int, int] = (min(node1, node2), max(node1, node2))
        unique_edges.add(edge)
        adj_list[node1].append(node2)
        adj_list[node2].append(node1)

    if len(unique_edges) != r:
        return ConnectionType.UNKNOWN.value

    # Проверка на связность всей сети
    if not _is_connected(v, adj_list):
        return ConnectionType.UNKNOWN.value

    degrees: List[int] = sorted([len(adj_list[i]) for i in range(1, v + 1)])

    # Топология "Кольцо" (Ring = 2): все степени равны 2, r == v
    if r == v and all(deg == 2 for deg in degrees):
        return ConnectionType.RING.value

    # Для "Шины" и "Звезды" число рёбер должно быть строго (v - 1)
    if r == v - 1:
        # "Звезда" (Star = 3): один узел степени v-1, остальные степени 1
        if degrees == [1] * (v - 1) + [v - 1]:
            return ConnectionType.STAR.value

        # "Шина" (Tire = 1): два узла степени 1, остальные степени 2
        if degrees == [1, 1] + [2] * (v - 2):
            return ConnectionType.TIRE.value

    return ConnectionType.UNKNOWN.value