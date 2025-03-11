shirt_size = input("enter the size of XL shirts\n(shoulder and height, separated by space): \n").split()
person_size = input("enter the size of winner person \n(shoulder and height, separated by space): \n").split()
if shirt_size[0]>= person_size[0]:
    if shirt_size[1]>= person_size[1]:
        print("Yes")
    else:
        print("No")
else:
    print("No")