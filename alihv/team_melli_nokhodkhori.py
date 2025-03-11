result = 0
time_elapsed_list = []
team_members = int(input("enter the number of team members inside the shop\n(number should be 1/2/3): "))

price : int = input("please enter the prices\n(separate a & b & c prices with space)\n").split()

for _ in range(team_members):
    time = input(
        f"enter the Check-in and check-out times for person {_ + 1} \n(separate Check-in and check-out times with space)\n").split()
    elapsed = int(time[1]) - int(time[0])
    time_elapsed_list.append(elapsed)

for index in range(len(time_elapsed_list)):
    result += int(price[index]) * int(time_elapsed_list[index])

print(result)