res = 1
q = 2

num = int(input("enter the number of divisors: "))

ls = input("enter the divisors \n (with spaces between them) : ").split()
if len(ls) != num:
    raise "you gave less or extra inputs! "

for i in ls:
    res *= int(i)
    lst = [res]
while res * q <= 1000:
    x = res * q
    lst.append(x)
    q += 1
print(len(lst))
