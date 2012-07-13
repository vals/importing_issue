import os
import sys

import module_test.uses_generated


def test_1_empty_str_in_sys():
    assert "" in sys.path, "sys.path does not contains empty string"


def test_2_import_wrong_dir():
    print(sys.path)
    os.chdir("..")
    assert module_test.uses_generated.try_import() == 0, "wrongly imported"


def test_3_import_right_dir():
    os.chdir("workdir")
    assert module_test.uses_generated.try_import() == 1, "failed to import"
