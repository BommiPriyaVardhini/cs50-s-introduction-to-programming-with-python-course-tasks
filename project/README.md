MY PROJECT TITLE IS EDUCATIONAL QUIZ GAME

2 THE VIDEO DEMO'S URL IS: https://youtu.be/mPu1CTYK_Lg

# DESCRIPTION OF THE PROGRAM:

This Python program is designed as an educational quiz game that provides users with a series of questions and options, captures 5 their responses, assesses those responses for correctness, and repeatedly allows them to continue with more questions or exit the game while maintaining a running score. The detailed breakdown of the program's components and functionalities is as follows:

#Modules and Functions used:

lowercase for the lower() method and any blank space should be stripped incase the user accidencly inputs it.

After each question:

The user's answer is processed, and the score is updated accordingly.

The user is prompted on whether they wish to continue or exit. Exiting the game prints a farewell message and the final score. If the user chooses to exit the game the loop is broken and the program exits the game after displaying the number of questions he played and how many he scored correct out of them. If the user successfuly attempts all of the questions, the program print a congratulation statement and prints the score.

*Questions Function: Reads question data from a CSV file, where each row includes the question text, four options (A, B, C, D), and the correct option. I used the DictReader() because, the best way to access the questions is to use dictionary as i can easily access them using the keys of the corresponding values. This data is then formatted and returned as two lists one for the formatted questions and one for the correct answers. I used two lists so that I will be able to access the correct answers and the questions separetly which enabled me to hide the correct answer from the user.
*Choose Answer Function: Compares the user's answer (after converting it to uppercase for consistency) to the correct answer. Returns a boolean value indicating whether the answer was correct.

Update Score Function: Based on whether the answer is correct, updates and prints the user's current score in tabulate grid format which make it more user-friendly. It provides immediate feedback about the correctness of the user's answer.

*Exit Score Function: This function is called if the user decides to exit the program and stops playing the game. Displays the user's final score in a table format when they decide to exit the game.

*Print Welcome Message Function: Generates and prints an ASCII art banner welcoming users to the quiz game and informs them about the total number of prepared questions. I used the pepper format for the font table format is because I checked other font styles but most of them were out of proper size for the user to find easy to read. I came across the pepper format and it's size was much more
