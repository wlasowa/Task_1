from praktikum.ingredient import Ingredient


class TestIngredient:
    def test_type_of_ingredient(self):
        ingredient = Ingredient("SAUCE", "hot sauce", 100)

        assert ingredient.type == "SAUCE"

    def test_name_of_ingredient(self):
        ingredient = Ingredient("SAUCE", "hot sauce", 100)

        assert ingredient.name == "hot sauce"

    def test_price_of_ingredient(self):
        ingredient = Ingredient("SAUCE", "hot sauce", 100)

        assert ingredient.price == 100

    def test_get_type_of_ingredient(self):
        ingredient = Ingredient("FILLING", "cutlet", 200)

        assert ingredient.get_type() == "FILLING"

    def test_get_name_of_ingredient(self):
        ingredient = Ingredient("FILLING", "cutlet", 200)

        assert ingredient.get_name() == "cutlet"

    def test_get_price_of_ingredient(self):
        ingredient = Ingredient("FILLING", "cutlet", 200)

        assert ingredient.get_price() == 200
