"""helloモジュールのテストを含むモジュール。"""

from hello import hello


def test_hello():
    """hello関数が4を返すことをテストする。"""
    assert hello(5) == 3
