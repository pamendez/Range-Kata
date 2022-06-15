from genericpath import exists
from krange import Range

def test_range_contains():
    krange = Range("[2, 6)")
    exists = krange.contains(values_to_check=[2,4])
    assert (exists == True), "Values are contained in the range." 
    pass

def test_range_contains_failing_test():
    krange = Range("[2, 6)")
    exists = krange.contains(values_to_check=[-1, 1, 6, 7])
    assert (exists == False), "Values are contained in the range."
    pass

def test_getValues():
    krange = Range("[2, 4)")
    
    pass