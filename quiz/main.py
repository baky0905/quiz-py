from utils.csv_reader import read_csv
from quiz.process_user_input import (
    calculate_user_score_statistics
)
from quiz.process_user_input import (
    Scoring
)


def main():
    """[summary]
    """
    questions_and_answers = read_csv('quiz/data/questions_answers.csv')

    scoring = Scoring()

    user_answers = []
    for quiz_item in questions_and_answers:
        scoring.ask_question(quiz_item)
        user_answers.append(scoring.score_user_input(quiz_item))

    user_statistics = calculate_user_score_statistics(user_answers)

    print(f"You have answered {user_statistics}% of questions correctly!")


if __name__ == '__main__':
    main()
