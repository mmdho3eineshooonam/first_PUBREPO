# احمد در حال ارسال لیست نهایی اسامی قبول شدگان المپیاد کامپیوتر برای کمیته ی بررسی نتایج می‌باشد تا
# کمیته بتواند کارت‌های ورود به مسابقات نهایی را چاپ کند. ولی به دلیل آنکه قالب مشخصی برای ثبت نام
# اسامی در هنگام آزمون تعریف نشده بود، شرکت کننده‌ها به صورت استاندارد اسامی خود را نتوانسته‌اند ثبت کنند.
# در ادامه‌ی هر اسم زبانی که با آن در مسابقات شرکت شده است، نوشته شده است و در ابتدای هر اسم نیز
# جنسیت افراد مشخص شده است. فرم استاندارد اسامی به این صورت می‌باشد که حرف اول اسم بزرگ می‌باشد
# و بقیه حروف اسم کوچک باشد. برنامه‌ای بنویسید که تعداد و اسم و جنسیت و زبان قبول شدگان را از ورودی
# بخواند و بر اساس جنسیت اسامی را تفکیک کند و آن‌ها را استاندارد سازی کند و جلوی هر اسم زبانی که با آن
# در مسابقات شرکت کرده است را بنویسد (در خروجی در ابتدا جنسیت زن و سپس جنسیت مرد چاپ شود).
# اسامی در هر جنسیت به ترتیب الفبای انگلیسی چاپ شوند.



# توجه: چنانچه قصد دارید از دیکشنری در حل مسائل خود استفاده کنید، به این نکته توجه کنید که دیکشنری
# ترتیب را حفظ نمی‌کند.

# ورودی نمونه:
# m.hossein.python
# f.miNa.C
# m.aiMad.C++
# f.Sara.java

# خروجی نمونه:
# f Mina C
# f Sara java
# m Ahmad C++
# m Hossein python
def info_getter(students_numb):
    result_dict = {}
    male_list = []
    female_list = []

    for _ in range(students_numb):
        inp = input("Enter your personal info\n(containing gender & name & language): ")
        inp = inp.split(".")

        if len(inp) != 3:
            print("Invalid input format. Please rewrite your info.")
            continue


        gender = inp[0].lower()
        student_name = inp[1].lower().capitalize()
        language = inp[2]

        student_info = [student_name, language]

        if gender == "m":
            male_list.append(student_info)
        elif gender == "f":
            female_list.append(student_info)
        else:
            print("Invalid gender. Please rewrite your info.")


    male_list = sorted(male_list, key=lambda x: x[0])
    female_list = sorted(female_list, key=lambda x: x[0])

    for itm in range(len(female_list)):
        print(f"{female_list[itm][0]}  {female_list[itm][1]}")
    for itm in range(len(male_list)):
        print(f"{male_list[itm][0]}  {male_list[itm][1]}")


def runner():
    students_numb = int(input("how many participant do we have? \n"))
    info_getter(students_numb)

runner()


