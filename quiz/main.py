from utils.csv_reader import read_csv
from quiz.process_user_input import (
    calculate_user_score_statistics,
    score_user_input
)


def main():
    """[summary]
    """
    questions_and_answers = read_csv('quiz/data/questions_answers.csv')

    user_answers = []
    for quiz_item in questions_and_answers:
        question = f"How much is {quiz_item['variable_a']} {quiz_item['operator']} {quiz_item['variable_b']}?"
        print(question)
        user_answers.append(score_user_input(quiz_item))

    user_statistics = calculate_user_score_statistics(user_answers)

    print(f"You have answered {user_statistics}% of questions correctly!")


if __name__ == '__main__':
    main()
