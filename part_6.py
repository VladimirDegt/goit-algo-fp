def greedy_algorithm(items, budget):
    """
    Жадібний алгоритм для вибору страв з найбільшою калорійністю за одиницю вартості.

    :param items: Словник з інформацією про страви (ціна та калорії).
    :param budget: Бюджет для вибору страв.
    :return: Список обраних страв та їхня сумарна калорійність.
    """
    # Обчислюємо співвідношення калорій до вартості для кожної страви
    ratios = []
    for item, info in items.items():
        ratio = info["calories"] / info["cost"]
        ratios.append((item, info["cost"], info["calories"], ratio))

    # Сортуємо страви за співвідношенням калорій до вартості (спочатку більші)
    ratios.sort(key=lambda x: x[3], reverse=True)

    total_calories = 0
    total_cost = 0
    selected_items = []

    # Вибираємо страви поки не вичерпаємо бюджет
    for item, cost, calories, ratio in ratios:
        if total_cost + cost <= budget:
            selected_items.append(item)
            total_calories += calories
            total_cost += cost

    return selected_items, total_calories


def dynamic_programming(items, budget):
    """
    Алгоритм динамічного програмування для вибору страв з найбільшою калорійністю при заданому бюджеті.

    :param items: Словник з інформацією про страви (ціна та калорії).
    :param budget: Бюджет для вибору страв.
    :return: Список обраних страв та їхня сумарна калорійність.
    """
    # Створюємо таблицю для динамічного програмування
    n = len(items)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    selected_items = [[[] for _ in range(budget + 1)] for _ in range(n + 1)]

    # Перетворюємо словник на список страв
    item_list = [(item, info["cost"], info["calories"]) for item, info in items.items()]

    # Динамічне програмування
    for i in range(1, n + 1):
        item, cost, calories = item_list[i - 1]
        for j in range(budget + 1):
            # Якщо поточна страва не влізає в бюджет
            if cost > j:
                dp[i][j] = dp[i - 1][j]
                selected_items[i][j] = selected_items[i - 1][j]
            else:
                # Вибираємо між двома варіантами: взяти або не взяти поточну страву
                if dp[i - 1][j] > dp[i - 1][j - cost] + calories:
                    dp[i][j] = dp[i - 1][j]
                    selected_items[i][j] = selected_items[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j - cost] + calories
                    selected_items[i][j] = selected_items[i - 1][j - cost] + [item]

    # Повертаємо обрані страви та їх сумарну калорійність
    return selected_items[n][budget], dp[n][budget]


# Тестування:
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}

budget = 100

# Жадібний алгоритм
selected_items_greedy, total_calories_greedy = greedy_algorithm(items, budget)
print("Greedy Algorithm:")
print("Selected items:", selected_items_greedy)
print("Total calories:", total_calories_greedy)

# Алгоритм динамічного програмування
selected_items_dp, total_calories_dp = dynamic_programming(items, budget)
print("\nDynamic Programming:")
print("Selected items:", selected_items_dp)
print("Total calories:", total_calories_dp)
