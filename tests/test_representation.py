from src.data import generate_dei_data
from src.representation import representation

def test_representation_sums_to_one():
    df = generate_dei_data(500)
    rep = representation(df, "gender")
    assert abs(sum(rep.values()) - 1.0) < 0.01
