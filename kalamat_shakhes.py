# **تمرین برنامهنویسی: کلمات شاخص**
import re


# برنامه‌ای بنویسید که از یک متن کلمات شاخص (کلماتی که با حروف بزرگ شروع می‌شوند) را به همراه شماره کلمه
# (چندمین کلمه می‌باشد) را در خروجی چاپ کند. در صورتی که در متن، کلمه‌ای با این ویژگی یافت نشد، در خروجی
# None چاپ کند. کلماتی که در ابتدای جمله می‌باشند به عنوان کلمه شاخص در نظر نباید بگیرید. (شماره کلمات را از یک شروع کنید)


# اعداد جز کلمات شاخص حساب نمی‌شوند. تنها نشانه مورد استفاده در جمله به جز نقطه، ویژگول می‌باشد. حتما دقت شود
# که در صورتی که نقطه یا ویژگول در آخر کلمه بود، حذف شود.         replace " "


# ورودی نمونه:
text="""The Persian League is the largest sport event dedicated to the
 deprived areas of Iran. The Persian League promotes peace and
 friendship. This video was captured by one of our heroes who wishes peace.
"""
# خروجی نمونه:
# 2:Persian
# 3:League
# 15:Iran
# 17:Persian
# 18:League

# **توجه:** چنانچه قصد دارید از دیکشنری در حل مسائل خود استفاده کنید، به این نکته توجه کنید که دیکشنری ترتیب را حفظ نمی‌کند.

text2 = text.replace("."," ").strip().split(" ")

for itm in text:
    print(text2)
    if re.split(r"\b /n$",text) or [] or ['']:
        text2.remove(itm)
print(text)