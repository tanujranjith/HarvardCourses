from project.project import check_correct_args, select_house, select_grade
import pytest

def test_check_correct_args():
    with pytest.raises(SystemExit):
        check_correct_args()

def test_select_house():
    assert select_house("courage") == "Oakridge House"
    assert select_house("dedication") == "Cresthaven Manor"
    assert select_house("wisdom") == "Willowbrook Cottage"
    assert select_house("ambition") == "Falconwood Estate"

def test_select_grade():
    assert select_grade(2006) == "Grade 12"
    assert select_grade(2015) == "Grade 3"