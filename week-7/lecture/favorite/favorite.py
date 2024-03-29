# import csv

# with open("favorites.csv", "r") as file:
#     reader = csv.DictReader(file)
#     counts = dict()
#     for row in reader:
#         favorite = row["problem"]
#         if favorite in counts:
#             counts[favorite] += 1
#         else:
#             counts[favorite] = 1

# # for favorite in sorted(counts, key=lambda language: counts[language], reverse=True):
# #     print(f"{favorite}: {counts[favorite]}")

# favorite = input("Favorite: ")
# if favorite.title() in counts:
#     print(f"{favorite}: {counts[favorite.title()]}")


from cs50 import SQL

db = SQL("sqlite:///favorites.db")

favorite = input("Favorite: ")
language = 'Python'


rows = db.execute(
    "SELECT COUNT(*) AS n FROM favorites WHERE problem = ? and language = ?", favorite, language)

row = rows[0]

print(row["n"])
