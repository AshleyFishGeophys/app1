import json

with open("../files/quesitons.json", "r") as file:
    content = file.read()

    data = json.loads(content)

score = 0
for question in data:
    print(question["question_text"])
    for idx, alternative in enumerate(question["alternatives"]):
        print(f"{idx + 1}) {alternative}")
    user_choice = int(input("Enter your answer: "))
    question["user_choice"] = user_choice

for question in data:
    if question["user_choice"] == question["correct_answer"]:
        score += 1
        result = "Correct Answer!"
    else:
        result = "Wrong Answer!"
    message = f" {result} Your answer is: {question['user_choice']}," \
              f" Correct answer is: {question['correct_answer']}"
    print(message)

print("you got", score, "out of", len(data), "questions correct.")