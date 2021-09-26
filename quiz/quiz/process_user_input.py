from typing import Dict, List


def score_user_input(quiz_item: Dict) -> Dict:
    """Evaluate user input based on the quiz.

    Args:
        quiz_item (Dict): question of a csv file that contains
        following column names: 
        id,variable_a,variable_b,operator,result

    Returns:
        Dict: Returns a dictionary with a key that is
        question id and with a boolean if user input is
        equal to a stored result.
    """

    def user_feedback(message: str, user_input: str, quiz_item: Dict) -> None:

        if message == "correct_answer":
            print(f"{user_input} is correct!")
        elif message == "wrong_answer":
            print(
                f"{user_input} is INCORRECT, correct answer is {quiz_item['result']}")

    user_input = int(input())

    if user_input == int(quiz_item['result']):
        user_feedback("correct_answer", user_input, quiz_item)
        result = {"id": quiz_item["id"], "correct": True}
        return result
    else:
        user_feedback("wrong_answer", user_input, quiz_item)
        result = {"id": quiz_item["id"], "correct": False}
        return result


def calculate_user_score_statistics(user_answers: List) -> int:
    """Calculates percentage of questions correctly answered.

    Args:
        user_answers (List): Dictionary of user results.

    Returns:
        int: Percentage of correctly anwered questions.
    """

    correct_count = sum([answer["correct"] for answer in user_answers])
    score_percent = (correct_count / len(user_answers)) * 100

    return int(round(score_percent, 0))
