import requests
import html

categoriesURL = "https://opentdb.com/api_category.php"

categories = requests.get(categoriesURL).json()["trivia_categories"]

for c in categories:
    print(str(c["id"]) + ": " + c["name"])

category = input("\nSelect a category by number: ")

num_q = input("\nSelect number of questions: ")

newurl = f"https://opentdb.com/api.php?amount={num_q}&category={category}"

trivia = requests.get(newurl).json()

print(trivia)
