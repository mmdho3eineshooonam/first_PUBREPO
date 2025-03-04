"""
تمرین برنامه‌نویسی: مترجم همراه

نیما به دلیل عدم تسلط به زبان انگلیسی برای حضور در مسابقات بین‌المللی مجبور است، همراه مترجم در این نشست‌ها حضور پیدا کند.
به دلیل اینکه به همراه بردن دو مترجم جهت ترجمه به زبان‌های فرانسه و آلمانی هزینه‌بر است، نیما تصمیم می‌گیرد که به دنبال راه‌حلی دیگر باشد.
حال شما باید برنامه‌ای بنویسید که نیما بتواند دیکشنری یا کلماتی مربوطه را از ورودی بخواند و جمله را با زبان‌های دیگر به‌خوبی ترجمه کند.

برنامه‌ی مترجم، ترجمه‌ی هر کلمه‌ای در دیکشنری وجود داشته باشد را در خروجی چاپ می‌کند.

ورودی برنامه شامل موارد زیر است:
1. در خط اول، یک عدد `N` وجود دارد که تعداد کلمات موجود در دیکشنری را مشخص می‌کند.
2. در `N` خط بعدی، هر خط شامل چهار کلمه است:
   - کلمه‌ی اول: فارسی
   - کلمه‌ی دوم: انگلیسی
   - کلمه‌ی سوم: فرانسوی
   - کلمه‌ی چهارم: آلمانی
3. در خط آخر، یک جمله به زبان فارسی داده شده است که باید ترجمه‌ی آن به زبان‌های دیگر چاپ شود.

نمونه ورودی:
-------------------
4
man I je ich
kheili very très sehr
alaghmand interested intéressé interessiert
barnamenevisi programming la programmation Programmierung
I am very interested in programming
-------------------

خروجی مورد انتظار:
-------------------
I am very interested in programming
je suis très intéressé par la programmation
ich bin sehr interessiert an Programmierung
-------------------
"""

n = int(input("how many words you gonna have inside dictionary?  "))
dic = {}

en_sentence = ""
fr_sentence = ""
gr_sentence = ""
for _ in range(n):
    persian_w, english, french, german = input("enter the input: \n (persian/english/german/french) \n ").split(" ")
    dic[persian_w] = (english, french, german)
    # print(dic)
    en_sentence += " " + str(list(dic[persian_w])[0])
    fr_sentence += " " + str(list(dic[persian_w])[1])
    gr_sentence += " " + str(list(dic[persian_w])[2])

persian_sentence = str(input("enter persian sentence: "))

print(f"EN sentence :{en_sentence}\nFR sentence : {fr_sentence}\nGR sentence : {gr_sentence}")
