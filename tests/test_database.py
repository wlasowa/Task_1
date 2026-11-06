from unittest.mock import call, patch

import pytest

from praktikum.database import Database


class TestDatabase:
    @pytest.mark.parametrize(
        "index, name, price",
        [
            (0, "black bun", 100),
            (1, "white bun", 200),
            (2, "red bun", 300),
        ],
    )
    def test_available_buns(self, index, name, price):
        database = Database()

        bun = database.available_buns()[index]

        assert bun.get_name() == name
        assert bun.get_price() == price

    @pytest.mark.parametrize(
        "index, ingredient_type, name, price",
        [
            (0, "SAUCE", "hot sauce", 100),
            (1, "SAUCE", "sour cream", 200),
            (2, "SAUCE", "chili sauce", 300),
            (3, "FILLING", "cutlet", 100),
            (4, "FILLING", "dinosaur", 200),
            (5, "FILLING", "sausage", 300),
        ],
    )
    def test_available_ingredients(self, index, ingredient_type, name, price):
        database = Database()

        ingredient = database.available_ingredients()[index]

        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price

    @patch("praktikum.database.Ingredient")
    @patch("praktikum.database.Bun")
    def test_constructor_creates_buns_and_ingredients(self, mock_bun, mock_ingredient):
        Database()

        assert mock_bun.call_count == 3
        mock_bun.assert_has_calls(
            [
                call("black bun", 100),
                call("white bun", 200),
                call("red bun", 300),
            ]
        )

        assert mock_ingredient.call_count == 6
        mock_ingredient.assert_has_calls(
            [
                call("SAUCE", "hot sauce", 100),
                call("SAUCE", "sour cream", 200),
                call("SAUCE", "chili sauce", 300),
                call("FILLING", "cutlet", 100),
                call("FILLING", "dinosaur", 200),
                call("FILLING", "sausage", 300),
            ]
        )
