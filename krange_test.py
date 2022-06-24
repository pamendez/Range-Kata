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