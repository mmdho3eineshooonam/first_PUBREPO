#برنامه‌ای بنویسید که ۱۰ عدد از ورودی بخواند و
#در انتها عددی که بیشترین تعداد مقسوم‌علیه عدد اول را دارد
# به همراه تعداد مقسوم‌علیه‌های اول آن، در خروجی چاپ کند.
# اگر چند عدد این حالت را داشتند، بزرگترین آن‌ها را چاپ کند.



def dv_finder(num):
    dv_list = []
    for dv in range(2, num):
        if num % dv == 0:
            dv_list.append(dv)
    return len(dv_list)


dic = {}
for _ in range(10):
    inp = int(input())
    dic[inp] = dv_finder(inp)
for k, val in dic.items():
    if val == max(dic.values()):
        print(k, max(dic.values()))
