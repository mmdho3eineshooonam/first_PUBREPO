
n = int(input("Enter the number of channels in TV: "))
x = int(input("Enter the base channel number of TV: "))
k = int(input("Enter the number of pressing the control keys by BOB: "))

channels = []
for _ in range(n):
    channels.append(input(f"Enter the {_+1}st channel name: ").strip())


new_channel_index = (x - 1 + k) % n


print(channels[new_channel_index])
