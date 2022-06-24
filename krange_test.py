import pytest
from krange import Range

class TestRangeConstructor:     
    def test_with_empty_range_throws_syntax_error(self):
        input_range = ""
        with pytest.raises(SyntaxError):
            rng = Range(input_range)
        pass

    def test_with_invalid_symbols_throws_syntax_error(self):
        input_range = "{}"
        with pytest.raises(SyntaxError):
            rng = Range(input_range)
        pass

    def test_with_valid_input(self):
        input_range = "[3,4]"
        rng = Range(input_range)
        assert type(rng) is Range
        pass

    def test_with_invalid_input_throws_value_error(self):
        input_range = "[6,4]"
        with pytest.raises(ValueError):
            rng = Range(input_range)
        pass
