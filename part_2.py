import turtle


def draw_pythagorean_tree(branch_length, level):
    """
    Рекурсивна функція для малювання фрактала "дерево Піфагора".

    Args:
        branch_length (int): Довжина поточної гілки.
        level (int): Поточний рівень рекурсії.
    """
    if level == 0:
        return

    # Малюємо основну гілку
    turtle.forward(branch_length)
    turtle.left(45)

    # Рекурсивний виклик для лівої гілки
    draw_pythagorean_tree(branch_length * 0.7, level - 1)

    turtle.right(90)

    # Рекурсивний виклик для правої гілки
    draw_pythagorean_tree(branch_length * 0.7, level - 1)

    # Повертаємось назад
    turtle.left(45)
    turtle.backward(branch_length)


def main():
    """
    Головна функція для ініціалізації та запуску малювання.
    """
    level = int(input("Введіть рівень рекурсії (рекомендується 5-10): "))

    turtle.speed("fastest")
    turtle.left(90)
    turtle.up()
    turtle.backward(300)
    turtle.down()
    draw_pythagorean_tree(100, level)
    turtle.done()


if __name__ == "__main__":
    main()
