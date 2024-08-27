# This is ICE 13
# Name : Bhawana Maswa
# Date: July 26,2023
# App name: Feedback Survey
# Description: App that displays a feedback survey and collects the user's answer

# Import the GUI module
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox


# Constants
QUESTION1 = "How satisfied are you with our company?"
QUESTION1_ANSWER1 = "Satisfied"
QUESTION1_ANSWER2 = "Not Sure!"
QUESTION1_ANSWER3 = "Surely...NOT!"

QUESTION2 = "How well do our products meet your needs"
QUESTION2_ANSWER1 = "Satistfied"
QUESTION2_ANSWER2 = "Neutral"
QUESTION2_ANSWER3 = "Dissatisfied"

QUESTION3 = "Would you recommend our product to friends"
QUESTION3_ANSWER1 = "For sure"
QUESTION3_ANSWER2 = "Not sure..."
QUESTION3_ANSWER3 = "Surely...NOT!"

def submit_answers():
    """
    Function that's called when the user clicks the submit button
    Display an error message incase any question is left un answered
    Display a report with the question and the their answers
    reset the form
    """

    # Check if the answers are empty
    if answer_question1.get() == "" or answer_question2.get() == "" or answer_question3.get () == "" :
        messagebox.showerror(message= "please answer all question",title= "Error")

        # If above is false, which means we have an answered all questiond
    else:
        # Variable that hold the report text
        report = QUESTION1 +"\n" + answer_question1.get() + "\n\n"
        report += QUESTION2 + "\n" + answer_question2.get() + "\n\n"
        report += QUESTION3 + "\n" +answer_question3.get() + "\n\n"

        # Display the report
        messagebox.showinfo(message=report,title="Survey report")

        # Uncheck all the answers
        answer_question1.set("")
        answer_question2.set("")
        answer_question3.set("")

# Create window
window =Tk()    #Create a new window
window.title("Feedback Survey - Bhawana Maswa")    #Set title
window.iconbitmap("Survey.ico")    #Set window icon
window.resizable(width=False,height=False)

# Label frame holding the questions
question1frame = LabelFrame (text=QUESTION1)
question2frame = LabelFrame (text=QUESTION2)
question3frame = LabelFrame (text=QUESTION3)

# Question 1 radio button
# Variable that holds the answer for question 1
answer_question1 = Variable()
q1a1_radiobutton = Radiobutton (question1frame, text=QUESTION1_ANSWER1,variable=answer_question1,value= QUESTION1_ANSWER1)
q1a2_radiobutton = Radiobutton (question1frame, text=QUESTION1_ANSWER2,variable=answer_question1,value= QUESTION1_ANSWER2)
q1a3_radiobutton = Radiobutton (question1frame, text=QUESTION1_ANSWER3,variable=answer_question1,value= QUESTION1_ANSWER3)
#-----------------------------------------------------------------------------------------------------------------------

# Question 2 radio button
# Variable that holds the answer for question 1
answer_question2 = Variable()
q2a1_radiobutton = Radiobutton (question2frame, text=QUESTION2_ANSWER1,variable=answer_question2,value= QUESTION2_ANSWER1)
q2a2_radiobutton = Radiobutton (question2frame, text=QUESTION2_ANSWER2,variable=answer_question2,value= QUESTION2_ANSWER2)
q2a3_radiobutton = Radiobutton (question2frame, text=QUESTION2_ANSWER3,variable=answer_question2,value= QUESTION2_ANSWER3)
#-----------------------------------------------------------------------------------------------------------------------

# Question 3 radio button
# Variable that holds the answer for question 1
answer_question3 = Variable()
q3a1_radiobutton = Radiobutton (question3frame, text=QUESTION3_ANSWER1,variable=answer_question3,value= QUESTION3_ANSWER1)
q3a2_radiobutton = Radiobutton (question3frame, text=QUESTION3_ANSWER2,variable=answer_question3,value= QUESTION3_ANSWER2)
q3a3_radiobutton = Radiobutton (question3frame, text=QUESTION3_ANSWER3,variable=answer_question3,value= QUESTION3_ANSWER3)
#-----------------------------------------------------------------------------------------------------------------------


# Submit button
submit_button = Button(window,text="Submit Answers",command= submit_answers)# call the function when called

# Place the widget
question1frame.grid(sticky="we",padx =10)
q1a1_radiobutton.grid(sticky="w")
q1a2_radiobutton.grid(sticky="w")
q1a3_radiobutton.grid(sticky="w")
#--------------------------------------------------------------------------------------------------------------------------------------
question2frame.grid(sticky="we",padx =10)
q2a1_radiobutton.grid(sticky="w")
q2a2_radiobutton.grid(sticky="w")
q2a3_radiobutton.grid(sticky="w")
#--------------------------------------------------------------------------------------------------------------------------------------
question3frame.grid(sticky="we",padx =10)
q3a1_radiobutton.grid(sticky="w")
q3a2_radiobutton.grid(sticky="w")
q3a3_radiobutton.grid(sticky="w")
#--------------------------------------------------------------------------------------------------------------------------------------
submit_button.grid(pady=10)



# Start the app
window.mainloop()

