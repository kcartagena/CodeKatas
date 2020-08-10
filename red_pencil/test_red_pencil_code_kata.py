import unittest
from red_pencil_code_kata import begin_promotion


class BeginPromotionTest(unittest.TestCase):
    def test_begin_promotion__price_not_stable_returns_true(self):
        prices = [75, 75, 75, 75, 65]
        promotions = [True] * len(prices)
        self.assertEqual(begin_promotion(prices), promotions,
                         "Not stable is always true if price is reduced after less than 30 days of stable prices.")

    def test_begin_promotion__price_not_stable_returns_false(self):
        prices = [50] * 30
        promotions = [True] * len(prices)
        self.assertEqual(begin_promotion(prices), promotions,
                         "30 days of consistent prices is always considered stable.")

    # (not_stable = false) == (begin_promotion = true)
    def test_begin_promotion__price_max_discount__not_stable_returns_false(self):
        prices = [50] * 30
        promotions = [True] * len(prices)
        # 30 days of stable prices has to be followed by price reduction for begin_promotion to be true
        prices.append(35)
        promotions.append(True)
        self.assertEqual(begin_promotion(prices), promotions,
                         "Not stable is always false if 30 days of stable prices are followed by promotion of 30% off.")

    def test_begin_promotion__price_min_discount__not_stable_returns_false(self):
        prices = [50] * 30
        promotions = [True] * len(prices)
        prices.append(47.50)
        promotions.append(True)
        self.assertEqual(begin_promotion(prices), promotions,
                         "Not stable is always false if 30 days of stable prices are followed by promotion of 5% off.")

    def test_begin_promotion__price_less_than_min_discount_not_stable_returns_true(self):
        prices = [50] * 30
        promotions = [True] * len(prices)
        prices.append(48)
        promotions.append(True)
        self.assertEqual(begin_promotion(prices), promotions,
                         "Not stable is always true if price is reduced less than minimum amount.")

    def test_begin_promotion__price_more_than_min_discount_not_stable_returns_true(self):
        prices = [50] * 30
        promotions = [True] * len(prices)
        prices.append(25)
        promotions.append(True)
        self.assertEqual(begin_promotion(prices), promotions,
                         "Not stable is always true if price is reduced more than maximum amount.")

    def test_begin_promotion__promotion_stops_on_price_increase(self):
        prices = [50] * 30
        promotions = [True] * len(prices)
        prices.extend([35, 35, 45])
# iterable  argument ends at 45.
        promotions.extend([True, True, True])
        self.assertEqual(begin_promotion(prices), promotions,
                         "If prices increase at any point during the red pencil promotion, then the promotion stops.")


if __name__ == '__main__':
    unittest.main()
