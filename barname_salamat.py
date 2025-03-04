# تمرین برنامهنویسی: برنامهی سلامت

# در دو مدرسه A و B، برنامهی سلامت در نظر گرفته شده است و در یک مدرسه شیر توزیع می‌شود و در مدرسه دیگر
# شیر توزیع نمی‌شود. کارشناسان تغذیه با بررسی قد، وزن و سن دانش‌آموزان این دو مدرسه را با یکدیگر مقایسه می‌کنند.
# برنامه‌ای بنویسید که تعداد دانش‌آموزان هر کلاس را بگیرد و اطلاعات سن، قد و وزن آن‌ها را ذخیره کند و میانگین سن،
# قد و وزن هر کلاس را محاسبه و در خروجی چاپ کند. اطلاعات هر کلاس در یک خط جداگانه و به ترتیب چاپ شود
# (به صورت float). در ادامه، کلاسی که میانگین قد آن بیشتر است را در خروجی چاپ کنید. در صورتی که میانگین
# قد برابر بود، کلاسی که میانگین وزن کمتری دارد چاپ شود. اگر میانگین قد و وزن برابر بود، عبارت "Same" چاپ شود.

# در ابتدا اطلاعات کلاس A و سپس اطلاعات کلاس B را وارد کنید. خروجی نیز به ترتیب اطلاعات ورودی چاپ شود.

# استفاده از class در حل تمرین تصویری توصیه می‌شود.

# نمونه ورودی:
# 16 17 15 16 17
# 180 175 172 170 165
# 67 72 59 62 55
# 15 17 16 15 16
# 166 156 168 170 162
# 60 58 59 57 56

# نمونه خروجی:
# 16.4 172.4 63.0
# 15.8 164.4 58.0
def get_student_data(school_name, num_students):
    total_age, total_height, total_weight = 0, 0, 0

    for _ in range(num_students):
        age = int(input(f"Enter the age of the student for {school_name}: "))
        height = int(input(f"Enter the height of the student for {school_name}: "))
        weight = int(input(f"Enter the weight of the student for {school_name}: "))

        total_age += age
        total_height += height
        total_weight += weight

    return {
        "av_age": total_age / num_students,
        "av_height": total_height / num_students,
        "av_weight": total_weight / num_students
    }


def run():
    num_students = int(input("How many students do we have in each class? "))

    result_dict = {
        "cls_a": get_student_data(str(input("enter the  first school name: ")), num_students),
        "cls_b": get_student_data(str(input("enter the  second school name: ")), num_students)
    }

    print(f"\nResults:\nA School: {result_dict['cls_a']}\nB School: {result_dict['cls_b']}")

    if result_dict["cls_a"]["av_height"] > result_dict["cls_b"]["av_height"]:
        print("Class A has taller students on average.")
    elif result_dict["cls_a"]["av_height"] < result_dict["cls_b"]["av_height"]:
        print("Class B has taller students on average.")
    else:
        print("Both classes have the same average height.")



run()
