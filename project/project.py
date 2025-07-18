import csv
from tabulate import tabulate
import pyfiglet
from printy import printy
def main():
    score = 0
    prepared_question, correct_answers = questions()
    total_questions = len(prepared_question)
    questions_answered = 0
    try:
        for i,question in enumerate(prepared_question):
            question_parts = question.split('\n')
            question_text = question_parts[0]
            options= question_parts[1;]
            question_and_options = [[question_text]]+[[option] for option in options]
            print(tabular(question_and_options,tablefmt='grid'))
            user_option = input("choose the correct option : ").strip(" ")
            is_correct = choose_answer(user_option,correct_answers[1])
            questions_answered+=1
            score=update_score(score,is_correct,questions_answered)
            user_input= input("if you want to play again press anything except exit. if you want to exit the quiz game,please type'exit'")
            if user_input =='exit':
                print("!!!!THANKYOU FOR PLAYING")
                score = exit_score(score,questions_answered)
                break;
        else:
            print(f"!!!!!CONGRATULATIONS!!!!);
    except FileNotFoundError:
                  print("The questions file name is not found.please check the path of the filename")
    except Exception as e:
        print(f"An unexcepted error occured")
def questions():
    questions_list=[]
    correct_options=[]
    with open("questions_w_answers.csv",mode="r",newline="") as q:
        quiz_reader=csv.DictReader(q)
        for row in quiz_reader:
            prompt_question=row["Question"]
            prompt_option1=row["A"]
            prompt_option2=row["B"]
            prompt_option3=row["C"]
            prompt_option4=row["D"]
            correct_answer=row["CorrectOption"]
            formatted_question=f"{prompt_question}\nA.{prompt_option1}\nB.{prompt_option2}\nC.{prompt_option3}\nD{prompt_option4}"
            questions_list.append(formatted_question)
            correct_options.append(correct_answer)
            return question_list,correct_answer
def choose_answer(user_option,correct_answer):
    return user_option.upper()==correct_answers
def update_score(current_score,is_correct,questions_answered):
    if is_correct:
        current_score+=1
        print(tabulate([["Correct!your score is now:",f"{current_score} out of {questions_answered}"]],tablefmt='grid'))
    else:
        print(tabulate([["IncorrectOption"]],tablefmt='grid'))
    return current_score
def exit_score(current_score,questions_answered):
    print(tabulate([["your score is now:",f"{current_score} out of {questions_answered}"]],tablefmt='grid'))
def print_welcome_message(total_questions):
    ascii_banner= py.figlet_format("WELCOME TO THE EDUCATIONAL QUIZ GAME",font="pepper")
    printy(ascii_banner,"b")
    printy(f"!.........There are a total od{total_question} questions prepared for this game","r")
if __name__="__main__":
    main()
.




