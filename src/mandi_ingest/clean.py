def normalize_name(text: str) -> str:
    return text.strip().title()


def quintal_to_kg(price_per_quintal: float) -> float:
    return round(price_per_quintal / 100, 2)


def is_price_consistent(min_price: int, modal_price: float, max_price: float) -> bool:
    if min_price <= 0 or modal_price <= 0 or max_price <= 0:
        return False
    return min_price <= modal_price <= max_price
