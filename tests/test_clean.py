from mandi_ingest.clean import is_price_consistent, normalize_name, quintal_to_kg


def test_normalize_name_strips_and_titles():
    assert normalize_name(" mapusa ") == "Mapusa"


def test_normalize_name_handles_already_clean_input():
    assert normalize_name(" NORTH GOA ") == "North Goa"


def test_quintal_to_kg_converts_correctly():
    assert quintal_to_kg(2450) == 24.5


def test_quintal_to_kg_handles_zero():
    assert quintal_to_kg(0) == 0


def test_is_price_consistent_true_when_ordered_correctly():
    assert is_price_consistent(2000, 2300, 2500) is True


def test_is_price_consistent_false_when_inverted():
    assert is_price_consistent(2500, 2300, 2000) is False


def test_is_price_consistent_false_when_modal_is_zero():
    assert is_price_consistent(0, 0, 0) is False
