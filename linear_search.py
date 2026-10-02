import time
import random
import matplotlib.pyplot as plt


def linear_search(arr, target):
    """Линейный поиск. Возвращает индекс или -1."""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# === Задание 1: проверка алгоритма ===
print("=== Задание 1: Проверка алгоритма ===")
test_arr = [5, 3, 8, 1, 9, 2]
print(f"Список: {test_arr}")
print(f"Поиск 8: индекс {linear_search(test_arr, 8)}")
print(f"Поиск 1: индекс {linear_search(test_arr, 1)}")
print(f"Поиск 100: индекс {linear_search(test_arr, 100)}")


# === Задание 2: анализ сложности ===
print("\n=== Задание 2: Анализ сложности ===")
print("Временная сложность: O(n)")
print("  В худшем случае — n сравнений (элемент в конце или отсутствует).")
print("  В лучшем случае — 1 сравнение (элемент первый).")
print("  В среднем — n/2 сравнений.")
print("Пространственная сложность: O(1)")
print("  Используется только счётчик i, дополнительная память не нужна.")


# === Задание 3: список из 100 случайных чисел ===
print("\n=== Задание 3: Список из 100 случайных чисел ===")
random.seed(42)
numbers = [random.randint(1, 1000) for _ in range(100)]
print(f"Первые 10 чисел: {numbers[:10]}")

targets = [numbers[0], numbers[50], numbers[99], 9999]
for t in targets:
    idx = linear_search(numbers, t)
    print(f"Поиск {t}: индекс {idx}")


# === Задание 4: сравнение скоростей ===
print("\n=== Задание 4: Сравнение скоростей ===")
sizes = [10, 100, 1000, 10000, 100000]
times = []

for size in sizes:
    arr = [random.randint(1, 1_000_000) for _ in range(size)]
    target = arr[-1]  # худший случай — ищем последний элемент

    start = time.perf_counter()
    linear_search(arr, target)
    elapsed = time.perf_counter() - start

    times.append(elapsed)
    print(f"Размер: {size:>7} | Время: {elapsed:.6f} сек")

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(sizes, times, marker="o", color="blue", linewidth=2)
plt.title("Зависимость времени линейного поиска от размера списка")
plt.xlabel("Размер списка (n)")
plt.ylabel("Время выполнения (сек)")
plt.xscale("log")
plt.grid(True)
plt.savefig("linear_search_plot.png")
print("\nГрафик сохранён: linear_search_plot.png")