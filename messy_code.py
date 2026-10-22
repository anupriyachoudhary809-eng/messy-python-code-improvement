
def calculate_total(prices):
    """Return the sum of a list of prices."""
    total = 0

    for price in prices:
        if price < 0:
            raise ValueError("Prices cannot be negative.")
        total += price

    return total


def main():
    prices = [100, 250, 75]
    total = calculate_total(prices)
    print(f"Total price: {total}")


if __name__ == "__main__":
    main()
