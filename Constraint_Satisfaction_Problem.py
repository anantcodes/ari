import itertools
import re
# Function to extract unique letters from the input string
def extract_letters(equation):
    return sorted(set(re.findall(r'[A-Z]', equation)))
# Function to replace letters with digits in a word
def replace_letters(word, letter_to_digit):
    return int(''.join(str(letter_to_digit[letter]) for letter in word))
# Function to solve the cryptarithmetic puzzle based on user input
def solve_cryptarithmetic(equation):
    # Split the equation at the '=' sign
    try:
        left_part, right_part = equation.split('=')
    except ValueError:
        print("Invalid equation format! Use the format: WORD + WORD = WORD")
        return
    # Extract the individual words from both sides
    left_words = re.findall(r'[A-Z]+', left_part)
    right_word = right_part.strip()
    # Extract unique letters
    letters = extract_letters(equation)
    if len(letters) > 10:
        print("Too many unique letters! A maximum of 10 letters can be used.")
        return
    for perm in itertools.permutations(range(10), len(letters)):
        letter_to_digit = dict(zip(letters, perm))
        if any(letter_to_digit[word[0]] == 0 for word in left_words + [right_word]):
            continue
        left_sum = sum(replace_letters(word, letter_to_digit) for word in left_words)
        right_value = replace_letters(right_word, letter_to_digit)
        if left_sum == right_value:
            print("Solution found!")
            for letter, digit in letter_to_digit.items():
                print(f"{letter} = {digit}")
            print(f"{' + '.join(left_words)} = {right_word}")
            print(f"{left_sum} = {right_value}")
            return
    print("No solution found.")

if __name__ == "__main__":
    equation = input("Enter a cryptarithmetic equation (e.g., SEND + MORE = MONEY): ").upper()
    solve_cryptarithmetic(equation)
