from typing import Dict, List

# from quiz.validations import validate_user_input


class Feedback:
    def give_feedback_to_input(message: str, user_input: str, quiz_item: Dict) -> None:
        """[summary]

        Args:
            message (str): [description]
            user_input (str): [description]
            quiz_item (Dict): [description]
        """

        if message == "correct_answer":
            print(f"{user_input} is correct!")
        elif message == "wrong_answer":
            print(f"{user_input} is INCORRECT, correct answer is {quiz_item['result']}")

    def ask_question(quiz_item: Dict) -> None:
        """[summary]

        Args:
            quiz_item (Dict): [description]
        """
        print(
            f"How much is {quiz_item['variable_a']} {quiz_item['operator']} {quiz_item['variable_b']}?"
        )


class Scoring:
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
        while True:
            try:
                user_input = int(input())
                break
            except ValueError:
                print("Type in a number!")
                continue

        if user_input == int(quiz_item["result"]):
            Feedback.give_feedback_to_input("correct_answer", user_input, quiz_item)
            result = {"id": quiz_item["id"], "correct": True}
            return result
        else:
            Feedback.give_feedback_to_input("wrong_answer", user_input, quiz_item)
            result = {"id": quiz_item["id"], "correct": False}
            return result


class Statistics:
    def calculate_user_score_statistics(user_answers: List) -> int:
        """Calculates percentage of questions correctly answered.

        Args:
            user_answers (List): Dictionary of user results..

        Returns:
            int: Percentage of correctly anwered questions.
        """

        correct_count = sum([answer["correct"] for answer in user_answers])
        score_percent = (correct_count / len(user_answers)) * 100

        return int(round(score_percent, 0))

    def report_statistics(user_statistics):
        """Gives a message to the user about the score stats.

        Args:
            user_statistics ([type]): Percentage of succesfully
            answered questions.
        """
        print(f"You have answered {user_statistics}% of questions correctly!")
