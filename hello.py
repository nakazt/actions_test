"""このモジュールは'Hello, world!'を出力する関数を含んでいます。"""

__version__ = "0.1.0"


def hello(n):
    """'Hello, world!'をn回出力する関数です。"""
    for i in range(n):
        print(f"{i}: Hello, world!")
    return i


if __name__ == "__main__":
    hello(3)
