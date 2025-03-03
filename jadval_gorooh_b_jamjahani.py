"""
تمرین برنامه‌نویسی: جدول گروه B جام جهانی

در گروه B مسابقات جام‌جهانی، تیم‌های ایران، پرتغال، اسپانیا و مراکش حضور دارند.
برنامه‌ای بنویسید که نتایج بازی‌ها را دریافت کند و نام تیم‌ها را همراه با تعداد
برد، باخت، گل‌های زده، تفاضل گل و امتیاز آن‌ها به ترتیب مشخص شده چاپ کند.

قوانین مرتب‌سازی:
1. تیم‌ها بر اساس امتیاز به ترتیب نزولی مرتب شوند.
2. در صورت برابر بودن امتیاز، تعداد برد در نظر گرفته شود.
3. اگر تعداد برد هم برابر بود، تیم‌ها به ترتیب حروف الفبا مرتب شوند.

سیستم امتیازدهی:
- برد = ۳ امتیاز
- مساوی = ۱ امتیاز
- باخت = ۰ امتیاز

تفاضل گل:
- تفاضل گل برابر است با (گل‌های زده - گل‌های خورده).

فرمت ورودی:
- نتایج بازی‌ها به ترتیب زیر خوانده می‌شوند:

    ایران - اسپانیا
    ایران - پرتغال
    ایران - مراکش
    اسپانیا - پرتغال
    اسپانیا - مراکش
    پرتغال - مراکش

- نتایج بازی‌ها به‌صورت "X-Y" دریافت می‌شوند که:
  - 'X' تعداد گل‌های تیم اول (سمت چپ) است.
  - 'Y' تعداد گل‌های تیم دوم (سمت راست) است.

مثال ورودی:
    2-2
    2-1
    1-2
    1-2
    3-1
    3-1
"""
team1 = ["Iran", "Iran", "Iran", "Spain", "Spain", "Portugal"]
team2 = ["Spain", "Portugal", "Morocco", "Portugal", "Morocco", "Morocco"]
result_dict = {}
for t1, t2 in zip(team1, team2):
    t1goal, t2goal = input("enter the result (with {int-int} template):\n").split("-")
    t1goal = int(t1goal)
    t2goal = int(t2goal)

    if t1 not in result_dict:
        result_dict[t1] = {
            "wins": 0,
            "loses": 0,
            "draws": 0,
            "entered goals": 0,
            "received goals": 0,
            "points": 0,
        }
    if t2 not in result_dict:
        result_dict[t2] = {
            "wins": 0,
            "loses": 0,
            "draws": 0,
            "entered goals": 0,
            "received goals": 0,
            "points": 0,
        }

    if t1goal > t2goal:
        result_dict[t1]["wins"] = result_dict[t1]["wins"] + 1
        result_dict[t1]["points"] = result_dict[t1]["points"] + 3
        result_dict[t1]["entered goals"] = result_dict[t1]["entered goals"] + t1goal
        result_dict[t1]["received goals"] = result_dict[t1]["received goals"] + t2goal

        result_dict[t2]["loses"] = result_dict[t2]["loses"] + 1
        result_dict[t2]["entered goals"] = result_dict[t2]["entered goals"] + t2goal
        result_dict[t2]["received goals"] = result_dict[t2]["received goals"] + t1goal

    elif t2goal > t1goal:
        result_dict[t2]["wins"] = result_dict[t2]["wins"] + 1
        result_dict[t2]["points"] = result_dict[t2]["points"] + 3
        result_dict[t2]["entered goals"] = result_dict[t2]["entered goals"] + t2goal
        result_dict[t2]["received goals"] = result_dict[t2]["received goals"] + t1goal

        result_dict[t1]["loses"] = result_dict[t1]["loses"] + 1
        result_dict[t1]["entered goals"] = result_dict[t1]["entered goals"] + t1goal
        result_dict[t1]["received goals"] = result_dict[t1]["received goals"] + t2goal

    elif t2goal == t1goal:
        result_dict[t1]["draws"] = result_dict[t1]["draws"] + 1
        result_dict[t2]["draws"] = result_dict[t2]["draws"] + 1

        result_dict[t2]["entered goals"] = result_dict[t2]["entered goals"] + t2goal
        result_dict[t2]["received goals"] = result_dict[t2]["received goals"] + t1goal
        result_dict[t1]["entered goals"] = result_dict[t1]["entered goals"] + t1goal
        result_dict[t1]["received goals"] = result_dict[t1]["received goals"] + t2goal
        result_dict[t2]["points"] = result_dict[t2]["points"] + 1
        result_dict[t1]["points"] = result_dict[t1]["points"] + 1

items = result_dict.items()
print(items)
items = reversed(sorted(items,key=lambda item: (item[1]["points"], item[1]["wins"] , item[0][0])))
for i in items:
    print(f"{i[0]}  wins:{i[1]['wins']} , loses:{i[1]['loses']} , draws:{i[1]['draws']} , goal difference:{i[1]["entered goals"] -i[1]["received goals"]} , points:{i[1]['points']}"
          )
