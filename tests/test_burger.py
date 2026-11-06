from unittest.mock import Mock

from praktikum.burger import Burger


class TestBurger:
    def test_set_buns_in_burger(self):
        burger = Burger()
        bun = Mock()

        burger.set_buns(bun)

        assert burger.bun is bun

    def test_add_ingredient_in_burger(self):
        burger = Burger()
        ingredient = Mock()

        burger.add_ingredient(ingredient)

        assert ingredient in burger.ingredients

    def test_remove_ingredient_in_burger(self):
        burger = Burger()
        ingredient1 = Mock()
        ingredient2 = Mock()
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        burger.remove_ingredient(0)

        assert ingredient1 not in burger.ingredients
        assert len(burger.ingredients) == 1

    def test_move_ingredient_in_burger(self):
        burger = Burger()
        ingredient1 = Mock()
        ingredient2 = Mock()
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        burger.move_ingredient(0, 1)

        assert burger.ingredients == [ingredient2, ingredient1]

    def test_get_price_burger(self):
        burger = Burger()
        bun = Mock()
        bun.get_price.return_value = 100
        ingredient1 = Mock()
        ingredient1.get_price.return_value = 50
        ingredient2 = Mock()
        ingredient2.get_price.return_value = 25
        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        price = burger.get_price()

        assert price == 275

    def test_get_receipt_burger(self):
        burger = Burger()
        bun = Mock()
        bun.get_name.return_value = "black bun"
        bun.get_price.return_value = 100
        ingredient = Mock()
        ingredient.get_type.return_value = "SAUCE"
        ingredient.get_name.return_value = "hot sauce"
        ingredient.get_price.return_value = 100
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)

        receipt = burger.get_receipt()

        assert receipt == (
            "(==== black bun ====)\n"
            "= sauce hot sauce =\n"
            "(==== black bun ====)\n"
            "\n"
            "Price: 300"
        )
