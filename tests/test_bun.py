from praktikum.bun import Bun


class TestBun:
    def test_name_of_bun(self):
        bun = Bun("Pink Bun", 200)

        assert bun.name == "Pink Bun"

    def test_price_of_bun(self):
        bun = Bun("One Bun", 400)

        assert bun.price == 400

    def test_get_name_of_bun(self):
        bun = Bun("Black Bun", 100)

        assert bun.get_name() == "Black Bun"

    def test_get_price_of_bun(self):
        bun = Bun("Green Bun", 300)

        assert bun.get_price() == 300
