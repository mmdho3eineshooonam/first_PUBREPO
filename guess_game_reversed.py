import random

guess_lst = []
count = 0


def new_guess(start_of_bound, end_of_bound):
    return random.randint(start_of_bound, end_of_bound)


num = int(input("input the number [and AI gonna guess that!] :  "))
end_of_bound = 100
start_of_bound = 0
guess = new_guess(start_of_bound, end_of_bound)

while guess != num:
    try:
        if guess in guess_lst:
            guess = new_guess(start_of_bound, end_of_bound)

        print(f"I think your number is {guess}")
        guess_lst.append(guess)
        print("I think I messed up.... ")
        count += 1

        txt = input("what should I do? go higher or lower? (h/l): ")

        if txt == "l":
            end_of_bound = guess - 1
            guess = new_guess(start_of_bound, end_of_bound)

        elif txt == "h":
            start_of_bound = guess + 1
            guess = new_guess(start_of_bound, end_of_bound)

        else:
            print("you entered a wrong input. try again")

    except ValueError:
        print(f"I think you are bothering me :(  \n  I am done with you... ")
        break
else:
    print(f"your number was {guess}!!")

