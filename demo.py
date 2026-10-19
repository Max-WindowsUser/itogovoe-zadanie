"""Модуль для демонстрации работы функций анализа сетевых топологий."""

from typing import List, Tuple

from topology import ConnectionType, connection_type, is_full_connected


def run_demonstration() -> None:
    """Запускает комплексные тесты для проверки функций топологий."""
    print("=" * 65)
    print("ДЕМОНСТРАЦИЯ РАБОТЫ ФУНКЦИЙ (ВАРИАНТ 11: ТОПОЛОГИИ СЕТЕЙ)")
    print("=" * 65)

    # 1. Проверка полносвязной сети (полный граф K5)
    print("\n[ТЕСТ 1] Полносвязная сеть (V=5, R=10, полный граф K5):")
    v_full: int = 5
    r_full: int = 10
    links_full: List[Tuple[int, int]] = [
        (1, 2), (1, 3), (1, 4), (1, 5),
        (2, 3), (2, 4), (2, 5),
        (3, 4), (3, 5),
        (4, 5),
    ]
    res_full: bool = is_full_connected(v_full, r_full, links_full)
    print(f"Результат: is_full_connected = {res_full} (Ожидалось: True)")

    # 2. Проверка неполносвязной сети
    print("\n[ТЕСТ 2] Неполносвязная сеть (V=5, R=4):")
    links_incomplete: List[Tuple[int, int]] = [
        (1, 2), (2, 3), (3, 4), (4, 5)
    ]
    res_not_full: bool = is_full_connected(5, 4, links_incomplete)
    print(
        f"Результат: is_full_connected = {res_not_full} "
        "(Ожидалось: False)"
    )

    # 3. Топология "Шина" (Tire = 1)
    print("\n[ТЕСТ 3] Топология 'Шина' (Tire, V=5, R=4, путь 1-2-3-4-5):")
    links_tire: List[Tuple[int, int]] = [(1, 2), (2, 3), (3, 4), (4, 5)]
    res_tire: int = connection_type(5, 4, links_tire)
    print(
        f"Результат: {res_tire} "
        f"(Ожидалось: {ConnectionType.TIRE.value} - Шина)"
    )

    # 4. Топология "Кольцо" (Ring = 2)
    print("\n[ТЕСТ 4] Топология 'Кольцо' (Ring, V=5, R=5, цикл 1-2-3-4-5-1):")
    links_ring: List[Tuple[int, int]] = [
        (1, 2), (2, 3), (3, 4), (4, 5), (5, 1)
    ]
    res_ring: int = connection_type(5, 5, links_ring)
    print(
        f"Результат: {res_ring} "
        f"(Ожидалось: {ConnectionType.RING.value} - Кольцо)"
    )

    # 5. Топология "Звезда" (Star = 3)
    print("\n[ТЕСТ 5] Топология 'Звезда' (Star, V=5, R=4, узел 1 в центре):")
    links_star: List[Tuple[int, int]] = [(1, 2), (1, 3), (1, 4), (1, 5)]
    res_star: int = connection_type(5, 4, links_star)
    print(
        f"Результат: {res_star} "
        f"(Ожидалось: {ConnectionType.STAR.value} - Звезда)"
    )

    # 6. Произвольная сеть (Unknown = 0)
    print("\n[ТЕСТ 6] Неизвестная топология (несвязный / смешанный граф):")
    links_unknown: List[Tuple[int, int]] = [
        (1, 2), (2, 3), (3, 1), (4, 5)
    ]
    res_unknown: int = connection_type(5, 4, links_unknown)
    print(
        f"Результат: {res_unknown} "
        f"(Ожидалось: {ConnectionType.UNKNOWN.value} - Неизвестная)"
    )
    print("\n" + "=" * 65)


if __name__ == "__main__":
    run_demonstration()