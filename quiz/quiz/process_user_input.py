from typing import Dict, List
from quiz.validations import validate_user_input


class Scoring:

    def feedback_on_answers(self, message: str, user_input: str, quiz_item: Dict) -> None:

        if message == "correct_answer":
            print(f"{user_input} is correct!")
        elif message == "wrong_answer":
            print(
                f"{user_input} is INCORRECT, correct answer is {quiz_item['result']}")

    def ask_question(self, quiz_item: Dict) -> None:
        print(
            f"How much is {quiz_item['variable_a']} {quiz_item['operator']} {quiz_item['variable_b']}?")

    def score_user_input(self, quiz_item: Dict) -> Dict:
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
        # is_number = True
        # while is_number:
        #     user_input = validate_user_input(input())
        #     if isinstance(user_input, int):
        #         break
        #     continue
        user_input = int(input())
        if user_input == int(quiz_item['result']):
            self.feedback_on_answers("correct_answer", user_input, quiz_item)
            result = {"id": quiz_item["id"], "correct": True}
            return result
        else:
            self.feedback_on_answers("wrong_answer", user_input, quiz_item)
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
