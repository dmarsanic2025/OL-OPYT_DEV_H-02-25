import math_operations as math
import data_fetcher


def add(a, b, c):
    return a + b + c


def main() -> None:
    print(math.add(5, 5), math.subtract(5, 5), sep="\n")
    print(math.multiply(5, 5))
    print(math.divide(5, 1))
    print(add(5, 5, 5))
    url = r"https://jsonplaceholder.typicode.com/users"
    print(data_fetcher.fetch_data(url))
    url = r"https://example.com/highlights"
    print(data_fetcher.fetch_data(url))


if __name__ == "__main__":
    main()
