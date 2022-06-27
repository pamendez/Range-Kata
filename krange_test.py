import pytest
from krange_dev import Range

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

    def test_with_spaced_input_returns_instance(self):
        input_range = " [3, 4] "
        rng = Range(input_range)
        assert type(rng) is Range
        pass
    pass

class TestRangeEndPoints:
    @pytest.mark.parametrize("input_range, result", [("(2, 4]", [3,4]), ("[-3,5]", [-3,5]), ("[4,7)", [4,6]), ("(4,8)", [5,7]), ("[2,3)", [2,2])]) 
    def test_with_valid_input_return_endpoint(self,input_range,result):
        rng = Range(input_range)
        assert rng.endpoints == result
        pass
    pass

class TestRangeAllPoints:
    def test_with_valid_range_return_allpoints(Self):
        input_range = "[3, 7]"
        rng = Range(input_range)
        assert rng.getAllPoints() == [3, 4, 5, 6, 7]
    pass

class TestRangeAsString:
    @pytest.mark.parametrize("input_range, result", [("[4,               10]", "[4,10]"), (" (7,10] ", "(7,10]")]) 
    def test_with_closed_range_show_as_formatted_string(self, input_range, result):
        rng = Range(input_range)
        assert rng.to_string() == result

class TestRangeContainsElements:
    def test_with_range_contains_elements_returns_true(self):
        input_range= "[2,6)"
        rng = Range(input_range)
        assert rng.contains(range_or_elements=set([2,4])) == True
    
    def test_with_range_does_not_contains_elements_returns_false(self):
        input_range = "[2,6)"
        rng = Range(input_range)
        assert rng.contains(range_or_elements = set([-1, 1, 6, 10])) == False
    
    def test_with_range_contains_empty_throws_value_error(self):
        input_range = "[1, 4]"
        rng = Range(input_range)
        with pytest.raises(ValueError):
            rng.contains(range_or_elements=set([]))
    
    def test_with_range_contains_invalid_type_throws_type_error(self):
        input_range = "[1, 4]"
        rng = Range(input_range)
        with pytest.raises(TypeError):
            rng.contains(range_or_elements=["j"])
    
    def test_with_range_contains_valid_type_but_invalid_carather_throws_exception(self):
        input_range = "[1, 4]"
        rng = Range(input_range)
        with pytest.raises(Exception):
            rng.contains(range_or_elements="2,3,4,j")

    def test_with_range_contains_valid_but_spaced_inputs_returns_true(self):
        input_range = "[2, 11)"
        rng = Range(input_range)
        elements = "3, 6,    8,  9,    10"
        assert rng.contains(elements) == True 
        pass
    pass

class TestRangeContainsOtherRange:
    @pytest.mark.parametrize("input_range1, input_range2", [("[2,5)", "[7,10)"), ("[2,5)", "[3,10)"), ("[3,5)", "[2,10)")])
    def test_range_doesnt_contains_another_range(self,input_range1,input_range2):
        rng1 = Range(input_range1)
        rng2 = Range(input_range2)
        assert rng1.contains(range_or_elements=rng2) == False
        pass
    pass

    @pytest.mark.parametrize("input_range1, input_range2", [("[2,10)","[3,5]"), ("[3,5]", "[3,5)")])
    def test_range_contains_another_range(self,input_range1,input_range2):
        rng1 = Range(input_range1)
        rng2 = Range(input_range2)
        assert rng1.contains(range_or_elements=rng2) == True
        pass
    pass

class TestRangeEqualsOtherRange:
    @pytest.mark.parametrize("input_range1, input_range2", [("[3,5) ", "[3,5) ")])
    def test_range_equals_another_range(self,input_range1,input_range2):
        rng1 = Range(input_range1)
        rng2 = Range(input_range2)
        assert rng1.equals(range_to_compare=rng2) == True
        pass

    @pytest.mark.parametrize("input_range1, input_range2", [("[2,10) ", "[3,5)"), ("[2,5) ", "[3,10)"), ("[3,5) ", "[2,10)")])
    def test_range_not_equals_another_range(self,input_range1,input_range2):
        rng1 = Range(input_range1)
        rng2 = Range(input_range2)
        assert rng1.equals(range_to_compare=rng2) == False
        pass
    pass

class TestRangeOverlapsRange:
    @pytest.mark.parametrize("input_range1, input_range2", [("[2,5)", "[7,10)")])
    def test_range_doesnt_overlaps_another_range(self,input_range1,input_range2):
        rng1 = Range(input_range1)
        rng2 = Range(input_range2)
        assert rng1.overlapsRange(range_to_compare=rng2) == False
        pass

    @pytest.mark.parametrize("input_range1, input_range2", [("[2,10)", "[3,5)"), ("[3,5)", "[3,5)"), ("[2,5)", "[3,10)"), ("[3,5)", "[2,10)")])
    def test_range_overlaps_another_range(self,input_range1,input_range2):
        rng1 = Range(input_range1)
        rng2 = Range(input_range2)
        assert rng1.overlapsRange(range_to_compare=rng2) == True
        pass
    pass
