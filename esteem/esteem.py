def get_score(response, is_positive):
    """ Returns the score of a given response based on
        whether the question is a positive or negative one.

        Parameters:
        str response - a single character that should be either
            a capital or lowercase A or D
        bool is_positive - True if the question is positive, false
            if it's negative
    """
    if response not in ["D", "d", "a", "A"]:
        return None
    if is_positive:
        score = {"D" : 0,
                 "d" : 1,
                 "a" : 2,
                 "A" : 3}
    else:
        score = {"D" : 3,
                 "d" : 2,
                 "a" : 1,
                 "A" : 0}

    return score[response]

def main():
    print("""This program is an implementation of the Rosenberg
Self-Esteem Scale. This program will show you ten
statements that you could possibly apply to yourself.
Please rate how much you agree with each of the
statements by responding with one of these four letters:

D means you strongly disagree with the statement.
d means you disagree with the statement.
a means you agree with the statement.
A means you strongly agree with the statement.
          """)
    
    total_score = 0
    questions = [
        ["""I feel that I am a person of worth, at least on an
equal plane with others.""", True],
        ["I feel that I have a number of good qualities.", True],
        ["All in all, I am inclined to feel that I am a failure.", False],
        ["I am able to do things as well as most other people.", True],
        ["I feel I do not have much to be proud of.", False],
        ["I take a positive attitude toward myself.", True],
        ["On the whole, I am satisfied with myself.", True],
        ["I wish I could have more respect for myself.", False],
        ["I certainly feel useless at times.", False],
        ["At times I think I am no good at all.", False]
    ]

    for i in range(len(questions)):
        print(f"{i + 1}. {questions[i][0]}")
        answer = input("    Enter D, d, a, or A: ")
        while answer not in ["D", "d", "a", "A"]:
            answer = input("Invalid answer. Please try again: ")
        total_score += get_score(answer, questions[i][1])

    print(f"""\nYour score is {total_score}.
A score below 15 may indicate problematic low self-esteem.""")

    return 0


main()