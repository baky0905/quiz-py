from utils.csv_reader import read_csv

from quiz.process_user_input import (
    Feedback,
    Scoring,
    Statistics
)


def main():
    """[summary]
    """
    quiz = read_csv('quiz/data/questions_answers.csv')

    user_answers = []
    for quiz_item in quiz:
        Feedback.ask_question(quiz_item)
        user_answers.append(Scoring.score_user_input(quiz_item))

    user_statistics = calculate_user_score_statistics(user_answers)

    Statistics.report_statistics(user_statistics)


if __name__ == '__main__':
    main()
