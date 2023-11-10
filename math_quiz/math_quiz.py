import random


def yield_random_integers(min_value, max_value):
    """
    This function generates a random integer within the specified range.
    
    min_value sets the minimum value for the random integer
    max_value sets the maximum value for the random integer

    Returns:
    int: Random integer within the specified range
    
    """
    return random.randint(min_value, max_value)


def yield_random_operators():
    '''
    This generates the random arithmetic operator ('+', '-', '*')

    Which returns: str(string)


    '''
    return random.choice(['+', '-', '*'])


def perform_operation(num_1, num_2, operator):
    '''
    This will perform the arithmetic operation between numbers and operators

    which will return a Tuple containing a arithmetic problem as a string and the correct answer

    '''
    problem = f"{num_1} {operator} {num_2}"
    if operator == '+': 
        answer = num_1 + num_2
    elif operator == '-': 
        answer = num_1 - num_2
    else: answer = num_1 * num_2
    return problem, answer

def math_quiz():
    '''
    which will conduct a math quiz game with the user

    '''
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num_1 =  yield_random_integers(1, 10); 
        num_2 =  yield_random_integers(1, 5); 
        operator = yield_random_operators()

        PROBLEM, ANSWER = perform_operation(num_1, num_2, operator)
        print(f"\nQuestion: {PROBLEM}")
        try:
            user_answer = int(input("Your answer: "))
        except ValuError:
            print ('invalid input,Please put a valid integer')
            continue

        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
