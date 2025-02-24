import random
import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt


def simulate_dice_rolls(num_rolls):
    """
    Симулює кидання двох кубиків задану кількість разів і повертає частоти сум.

    Args:
        num_rolls (int): Кількість симуляцій (кидків кубиків).

    Returns:
        dict: Словник з частотами кожної можливої суми (від 2 до 12).
    """
    sums = {i: 0 for i in range(2, 13)}  # Ініціалізація частот для сум від 2 до 12

    for _ in range(num_rolls):
        die1 = random.randint(1, 6)  # Кидок першого кубика
        die2 = random.randint(1, 6)  # Кидок другого кубика
        total = die1 + die2  # Обчислення суми
        sums[total] += 1  # Збільшення лічильника для цієї суми

    return sums


def calculate_probabilities(frequencies, total_rolls):
    """
    Обчислює ймовірності кожної суми на основі частот.

    Args:
        frequencies (dict): Словник з частотами сум.
        total_rolls (int): Загальна кількість кидків.

    Returns:
        dict: Словник з ймовірностями для кожної суми (у відсотках).
    """
    probabilities = {}
    for sum_value, freq in frequencies.items():
        probabilities[sum_value] = (freq / total_rolls) * 100  # Переводимо в відсотки
    return probabilities


def analytical_probabilities():
    """
    Повертає аналітичні ймовірності сум при киданні двох кубиків (з таблиці).

    Returns:
        dict: Словник з аналітичними ймовірностями для кожної суми (у відсотках).
    """
    return {
        2: 2.78,
        3: 5.56,
        4: 8.33,
        5: 11.11,
        6: 13.89,
        7: 16.67,
        8: 13.89,
        9: 11.11,
        10: 8.33,
        11: 5.56,
        12: 2.78,
    }


def create_probability_table(monte_carlo_probs, analytical_probs):
    """
    Створює таблицю для порівняння ймовірностей, отриманих методом Монте-Карло,
    та аналітичних ймовірностей.

    Args:
        monte_carlo_probs (dict): Ймовірності, отримані методом Монте-Карло.
        analytical_probs (dict): Аналітичні ймовірності.

    Returns:
        str: Форматована таблиця у вигляді рядка.
    """
    table_data = []
    for sum_value in range(2, 13):
        table_data.append(
            [
                sum_value,
                f"{monte_carlo_probs[sum_value]:.2f}%",
                f"{analytical_probs[sum_value]:.2f}%",
                f"{'✓' if abs(monte_carlo_probs[sum_value] - analytical_probs[sum_value]) < 1.0 else '✗'}",
            ]
        )

    headers = ["Сума", "Монте-Карло (%)", "Аналітичні (%)", "Відповідність"]
    return tabulate(table_data, headers=headers, tablefmt="grid")


def plot_probabilities(monte_carlo_probs, analytical_probs):
    """
    Створює графік для порівняння ймовірностей, отриманих методом Монте-Карло,
    та аналітичних ймовірностей.

    Args:
        monte_carlo_probs (dict): Ймовірності, отримані методом Монте-Карло.
        analytical_probs (dict): Аналітичні ймовірності.
    """
    sums = list(range(2, 13))
    monte_carlo = [monte_carlo_probs[s] for s in sums]
    analytical = [analytical_probs[s] for s in sums]

    plt.figure(figsize=(10, 6))
    plt.plot(sums, monte_carlo, label="Монте-Карло", marker="o")
    plt.plot(sums, analytical, label="Аналітичні", marker="o", linestyle="--")
    plt.title("Порівняння ймовірностей сум при киданні двох кубиків")
    plt.xlabel("Сума")
    plt.ylabel("Ймовірність (%)")
    plt.legend()
    plt.grid(True)
    plt.savefig("dice_probabilities.png")  # Збереження графіка у файл
    plt.close()


def generate_readme(monte_carlo_probs, analytical_probs):
    """
    Генерує файл Readme.md з висновками про порівняння ймовірностей.

    Args:
        monte_carlo_probs (dict): Ймовірності, отримані методом Монте-Карло.
        analytical_probs (dict): Аналітичні ймовірності.
    """
    with open("Readme.md", "w", encoding="utf-8") as f:
        f.write("# Висновки про симуляцію кидків кубиків\n\n")
        f.write("## Опис задачі\n")
        f.write(
            "Була проведена симуляція кидання двох кубиків за допомогою методу Монте-Карло та порівняння результатів з аналітичними ймовірностями, наведеними в таблиці.\n\n"
        )

        f.write("## Результати\n")
        f.write("Нижче наведено таблицю порівняння ймовірностей:\n\n")
        f.write("```plaintext\n")
        f.write(create_probability_table(monte_carlo_probs, analytical_probs))
        f.write("\n```\n\n")

        f.write("## Аналіз\n")
        f.write(
            "- Ймовірності, отримані методом Монте-Карло, є наближеними і можуть дещо відхилятися від аналітичних значень залежно від кількості симуляцій.\n"
        )
        f.write(
            "- Якщо відхилення між Монте-Карло та аналітичними ймовірностями менше 1%, вважаємо, що результати відповідають очікуванням (позначено символом ✓).\n"
        )
        f.write(
            "- Графік порівняння ймовірностей збережено у файлі `dice_probabilities.png`.\n\n"
        )

        f.write("## Висновки\n")
        f.write(
            "Симуляція методом Монте-Карло достовірно відтворює розподіл ймовірностей сум при киданні двох кубиків, хоча невеликі відхилення можливі через випадковість процесу. Збільшення кількості симуляцій (наприклад, до мільйона або більше) може покращити точність результатів."
        )


def main():
    """
    Головна функція для виконання симуляції, аналізу та візуалізації результатів.
    """
    num_rolls = 1000000  # Кількість симуляцій (можна змінити для точності)

    # Симуляція кидків кубиків
    frequencies = simulate_dice_rolls(num_rolls)
    monte_carlo_probs = calculate_probabilities(frequencies, num_rolls)

    # Аналітичні ймовірності
    analytical_probs = analytical_probabilities()

    # Створення таблиці
    print("Порівняння ймовірностей (Монте-Карло vs Аналітичні):")
    print(create_probability_table(monte_carlo_probs, analytical_probs))

    # Створення графіка
    plot_probabilities(monte_carlo_probs, analytical_probs)

    # Генерація Readme.md
    generate_readme(monte_carlo_probs, analytical_probs)
    print("\nФайл Readme.md та графік dice_probabilities.png створено.")


if __name__ == "__main__":
    main()
