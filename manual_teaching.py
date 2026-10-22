
import pandas as pd
import openpyxl
import random

def read_excel(file):
    print("Insert excel file: ")
    df = pd.read_excel(file)
    if df.shape[1] < 2: #Check column numbers
        print("Error: The Excel sheet must have at least two columns.")
        return None
    df = df.dropna(subset=[df.columns[0], df.columns[1]]) #Drop rows with missing data
    mapped_dict = {}
    for row in df.iloc[:, [0, 1]].itertuples(index=False):
        # Clean whitespaces and convert everything safely to strings
        col1_val = str(row[0]).strip()
        col2_val = str(row[1]).strip()

        if col1_val != "" and col2_val != "":
            mapped_dict[col1_val] = col2_val

    if not mapped_dict:
        print("Error: No valid rows found to quiz you on.")
        return None
    return mapped_dict

def quiz(mapped_dict):
    quizzed_words = list(mapped_dict.keys())
    num_of_questions = len(mapped_dict) - 1
    correct = 0
    incorrect = 0
    repeated = {}

    print("What is the translation of the following: ")
    for i in range(num_of_questions):
        quizzed_word = random.choice(quizzed_words)
        answer = input(f"French: '{quizzed_word}' -> English translation: ")
        correct_answer = mapped_dict[quizzed_word]
        if answer.strip().lower() == correct_answer.strip().lower():
            correct = correct + 1
            print("Correct!")
        else:
            incorrect = incorrect + 1
            repeated[quizzed_word] = correct_answer
            print(f"Incorrect! The correct answer is: {correct_answer}\n")

    while len(repeated) > 0:
        print("What is the answer of this: ")
        for quizzed_word in list(repeated.keys()):
                answer = input(f"Repeated French: '{quizzed_word}' -> English translation: ")
                correct_answer = repeated[quizzed_word]
                if answer.strip().lower() == correct_answer.strip().lower():
                    print("Correct now! Removed from review list.\n")
                    repeated.pop(quizzed_word)  # Remove it from mistakes
                else:
                    print(f"Still incorrect. The correct answer is: {correct_answer}\n")

    print("=== Quiz Complete ===")
    print("Number of correct answers is: ", correct)
    print("Number of correct answers is: ", incorrect)
    print("The percentage is: ", correct/num_of_questions *100.0)

