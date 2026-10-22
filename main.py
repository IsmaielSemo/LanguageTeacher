
#import pandas as pd
from manual_teaching import read_excel, quiz



def main():
    choice = int(input("Welcome to the Language Teacher. Please choose what mode you would like: \n Mode 1: Manual Language Teacher \n Mode 2: Automatic Language Teacher\n"))
    if choice == 1:
        mapped_vocabulary = read_excel("ManualWords/French.xlsx")
        quiz(mapped_vocabulary)
    elif choice == 2:
        print("Still not implemented")
    else:
        print("Invalid choice")
    return 0


main()