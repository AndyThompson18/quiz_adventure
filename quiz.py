# Our quiz!

score = 0

def quiz():

    name = input("Name: ")
    print("Welcome", name)
    print("Here is a quiz to test your Knowledge!")
    question1()
   
def question1():
    global score
    print("What is uranium?")
    print("1. Pee?")
    print("2. A metal?")
    print("3. A chemical liquid?")
    answer = input("Choose an answer: ")
    if answer.lower() == "2":
        score = score + 100
        print("Correct and now quiz is done!Bye")
    else:
        print("No!")
        question1()

# Leave this at the bottom - it makes quiz run automatically when you
# run your code.
if __name__ == "__main__":
    quiz()
