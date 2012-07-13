import os
import module.uses_generated


def test_1_import_wrong_dir():
    os.chdir("..")
    assert module.uses_generated.try_import() == 0, "wrongly imported"


def test_2_import_right_dir():
    os.chdir("workdir")
    assert module.uses_generated.try_import() == 1, "failed to import"
