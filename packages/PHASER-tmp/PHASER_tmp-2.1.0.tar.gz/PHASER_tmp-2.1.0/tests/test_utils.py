import numpy as np
from phaser.utils import bool2binstring


def test_list():
    example_bool_list = [True,False,True]
    example_int_list = [1,0,1]
    assert bool2binstring(example_bool_list) == "101"
    assert bool2binstring(example_int_list) == "101"

    assert bool2binstring(np.array(example_bool_list)) == "101"
    assert bool2binstring(np.array(example_int_list)) == "101"