import bmi
import Lab3

def test_calculate_bmi_func_normal():
    expected = 0
    result = bmi.calculate_bmi(height=1.85,weight=65)
    assert(result ==expected)
def test_calculate_bmi_func_fat():
    expected = 1
    result = bmi.calculate_bmi(height=1.85,weight=900)
    assert(result ==expected)
def test_calculate_bmi_func_skinny():
    expected = -1
    result = bmi.calculate_bmi(height=1.85,weight=1)
    assert(result ==expected)

def test_bubble_sort_descending():
    input_array = [4,2,1,3]
    result = Lab3.bubble_sort(input_array,Lab3.SORT_DESCENDING)
    assert(result == [4,3,2,1])

def test_bubble_sort_ascending():
    input_array = [4,2,1,3]
    result = Lab3.bubble_sort(input_array,Lab3.SORT_ASCENDING)
    assert(result == [1,2,3,4])

