import pytest
from krange import Range

class TestRangeConstructor:     
    def test_with_empty_range_throws_syntax_error(self):
        input_range = ""
        with pytest.raises(SyntaxError):
            rng = Range(input_range)
        pass

    @pytest.mark.parametrize("input_range", [("{}"), ("||"), ("//")])
    def test_with_invalid_symbols_throws_syntax_error(self, input_range):
        with pytest.raises(SyntaxError):
            rng = Range(input_range)
        pass

    @pytest.mark.parametrize("input_range", [("(4, 5, 6, 7)"), ("[555, 0, 11]"), ("[77, 12, 444]")])
    def test_with_invalid_input_throws_index_error(self, input_range):
        with pytest.raises(IndexError):
            rng = Range(input_range)
        pass

    @pytest.mark.parametrize("input_range", [("[(,)]"), ("[[,]]")])
    def test_with_invalid_numbers_throws_exception(self, input_range):
        with pytest.raises(Exception):
            rng = Range(input_range)
        pass
    
    def test_with_valid_input_return_endpoint(self):
        input_range = "(2, 4]"
        rng = Range(input_range)
        assert rng.endpoints == [3,4]
        pass

    def test_with_invalid_input_throws_value_error(self):
        input_range = "(6, 4]"
        with pytest.raises(ValueError):
            rng = Range(input_range)

    def test_with_valid_input_doesnt_throws_value_error(self):
        input_range = "[2, 4]"
        rng = Range(input_range)
        assert type(rng) is Range

        
    def test_with_valid_input(self):
        input_range = "[3, 4]"
        rng = Range(input_range)
        assert type(rng) is Range
        pass

    def test_with_valid_range_return_allpoints(Self):
        input_range = "[3, 7]"
        rng = Range(input_range)
        assert rng.allpoints == [3, 4, 5, 6, 7]
    pass

    def test_with_valid_range_return_allpoints(Self):
        input_range = "(3, 8)"
        rng = Range(input_range)
        assert rng.allpoints == [4, 5, 6, 7]
    pass

class TestRangeAsString:
    def test_show_range_as_formatted_string(self):
        input_range = "[4,               10]"
        rng = Range(input_range)
        assert rng.to_string() == "[4,10]"
        pass
    pass

class TestRangeContainsElements:
    def test_range_contains_elements(self):
        input_range= "[2,6)"
        rng = Range(input_range)
        assert rng.contains(elements=[2,4]) == True
    
    def test_range_does_not_contains_elements(self):
        input_range = "[2,6)"
        rng = Range(input_range)
        assert rng.contains(elements=[-1, 1, 6, 10]) == False
    pass

class TestRangeContainsOtherRange:
    @pytest.mark.parametrize("input_range1","input_range2", [("[2,5)","[7,10)"), ("[2,5)", "[3,10)"), ("[3,5)", "[2,10)")])
    def test_range_doesnt_contains_another_range(self,input_range1,input_range2):
        rng1 = Range(input_range1)
        rng2 = Range(input_range2)
        assert rng1.contains(range_ = rng2) == False
        pass
    pass

    @pytest.mark.parametrize("input_range1","input_range2", [("[2,10)","[3,5]"), ("[3,5]", "[3,5)")])
    def test_range_contains_another_range(self,input_range1,input_range2):
        rng1 = Range(input_range1)
        rng2 = Range(input_range2)
        assert rng1.contains(range_ = rng2) == True
        pass
    pass