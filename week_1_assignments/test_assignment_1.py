import pytest
import assignment_1

def test_var1_var2():
    assert assignment_1.var1 == assignment_1.var2, "var1 and var2 should have the same value."

def test_num1_num2():
    assert assignment_1.num1 * assignment_1.num2 == 16, "num1 and num2 should multiply to give 16."

