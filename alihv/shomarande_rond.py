num_list = []
is_round = dict()

count = int(input("enter the number of times you want the number to be checked: "))
for _ in range(count):
    num = input("enter a number with these conditions:\n"
                "1) Should not start with 0\n"
                "2) Has to be 8 digits\n")

    if len(num) != 8 or num[0] == '0':
        raise ValueError("You gave a wrong input")
    else:
        num_list.append(num)
        is_round[num] = 0


def is_palindrome(num_str):
    return num_str == num_str[::-1]


for num in num_list:
    repeat = 0
    print(f"being a palindrome for {num} : {is_palindrome(num)}")

    for dig in num:
        if dig in '0123456789':
            repeat += 1
    if repeat >= 4:
        is_round[num] += 1


    for index in range(2, len(num)):
        if num[index] == num[index - 1] == num[index - 2]:
            is_round[num] += 1

print(is_round)
