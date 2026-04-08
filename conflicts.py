def calculate_total(price, tax):
    total = price + (price * tax)
    total = round(total, 2)
    return total


def greet(user):
    return f"Hello {user}"
