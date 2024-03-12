from collections.abc import Generator

from htpy import Element, div, li, ul


class Test_Children:
    def test_children_as_element(self) -> None:
        child: Element = li
        ul[child]

    def test_children_as_list_element(self) -> None:
        child: list[Element] = [div]
        div[child]
