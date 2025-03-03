# ژانرهای موجود: Horror, Romance, Comedy, History, Adventure, Action

# برنامه ای بنویسید که تعداد افراد را بگیرد سپس اسم هر فرد را با زانرهای مورد عالقش بگیرد و اسم هر زانر و
# در صورتی که میزان عالقهمندی در زانرهای مختلف یکسان شد، به ترتیب الفبای انگلیسی در خروجی چاپ کنید.
# در صورتی که زانری انتخاب نشد، مقدار آن را صفر در نظر بگیرید و در خروجی اسم و عدد را چاپ کنید.


# نمونه خروجی:
# Action : 3
# Comedy : 2
# History : 2
# Horror : 2
# Romance : 2
# Adventure : 1
genres_dict = {"Horror": 0, "Romance": 0, "Comedy": 0, "Adventure": 0, "Action": 0, "History": 0}

keys_list = list(genres_dict.keys())

count = int(input("Enter the number of people: "))
for _ in range(count):
    name = input("Enter the name: ")
    print("Here are the genres (enter the corresponding number):")

    for index, key in enumerate(keys_list):
        print(f"{index}: {key}")

    genre1 = int(input("Enter your first genre index: "))
    genre2 = int(input("Enter your second genre index: "))
    genre3 = int(input("Enter your third genre index: "))

    for genre_index in (genre1, genre2, genre3):
        genres_dict[keys_list[genre_index]] += 1

print(genres_dict)