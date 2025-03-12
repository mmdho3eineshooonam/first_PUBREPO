def find_nokhod_position(n, swaps):
    cups = {1: 1, 2: 0, 3: 0}

    for a, b in swaps:
        cups[a], cups[b] = cups[b], cups[a]

    for key, value in cups.items():
        if value == 1:
            return key

n = int(input("enter the number of swaps\n(a number between 1-1000):\n  "))
swaps = []
for _ in range(n):
    swap_input = input(f"enter the {_ + 1}st source and destination\nfirst source in first try should be in place1\n(separate them with space):\n ")
    swaps.append(map(int, swap_input.split()))

print(find_nokhod_position(n, swaps))