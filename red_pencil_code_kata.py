promo_days_max = 30
sale_percent_min = .05 * 100
sale_percent_max = .30 * 100


def begin_promotion(prices):
    promotion_active = []

    days_stable = 1
    original_price = None
    on_sale = True

    for price in prices:
        on_sale = new_promo(price, original_price, days_stable) or continue_promo(on_sale, price, original_price)
        promotion_active.append(on_sale)
# stable if price value is equal to original price value
        if price == original_price:
            days_stable += 1
        else:
            days_stable = 1
            original_price = price

    return promotion_active


# If price is further reduced during promo the promo will not be prolonged.
def continue_promo(on_sale, price, original_price):
    return on_sale and not price < original_price


def new_promo(price, original_price, days_stable):
    return reduced_price(price, original_price) and not_stable(days_stable)


def reduced_price(price, original_price):
    if original_price:
        discount_amount = ((price - original_price) / original_price) * 100
        return sale_percent_min >= discount_amount <= sale_percent_max
    else:
        return True


# price should be stable for 30 days w/o intersecting promos
def not_stable(days_stable):
    return days_stable <= promo_days_max
