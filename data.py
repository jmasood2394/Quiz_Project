import requests

categories = {
    "General Knowledge": 9,
    "Science & Nature": 17,
    "Science: Computers": 18,
    "Science: Mathematics": 19,
    "Sports": 21,
    "Geography": 22,
    "Vehicles": 28,
}


def quiz_data(q_category, q_amount, q_difficulty):
    api_url = (f"https://opentdb.com/api.php?amount={q_amount}&category={categories[q_category]}"
               f"&difficulty={q_difficulty}&type=boolean")
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        questions = data["results"]
        return questions
