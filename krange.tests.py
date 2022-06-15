from krange import Range

def test_range_contains():
    krange = Range(2, 6)
    exists = krange.contains(values_to_check=[2,4])
    assert (exists == True), "Values are contained in the range." 
    pass