# Python standard library imports
import sys

# Local imports
from utils.csv_reader import read_csv
from quiz.process_user_input import Feedback, Scoring, Statistics


def main(file_path):
    """[summary]

    Args:
        file_path ([type]): [description]
    """
    # 'quiz/data/questions_answers.csv'
    quiz = read_csv(file_path)

    user_answers = []
    for quiz_item in quiz:
        Feedback.ask_question(quiz_item)
        user_answers.append(Scoring.score_user_input(quiz_item))

    user_statistics = Statistics.calculate_user_score_statistics(user_answers)

    Statistics.report_statistics(user_statistics)


if __name__ == "__main__":
    main(sys.argv[1])
