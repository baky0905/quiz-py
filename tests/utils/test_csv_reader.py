# Third party
import pytest

# Local imports
from quiz.utils.csv_reader import read_csv


@pytest.mark.unittest
def test_csv_reader_should_return_dictionary():
    # arrange
    expected = [
        {
            "id": "1",
            "variable_a": "2",
            "variable_b": "2",
            "operator": "+",
            "result": "4",
        },
        {
            "id": "2",
            "variable_a": "2",
            "variable_b": "2",
            "operator": "-",
            "result": "0",
        },
    ]

    # act

    actual = read_csv("quiz/data/questions_answers.csv")[0:2]

    # assert
    assert actual == expected
