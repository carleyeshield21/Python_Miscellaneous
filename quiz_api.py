import requests

parangmeter = {
    "amount": 1,
    "difficulty": 'easy',
    "type": 'multiple',
}

quiz_api_req = requests.get('https://opentdb.com/api.php?amount=50&difficulty=medium&type=multiple',params=parangmeter)
quiz_api_req.raise_for_status()
print(quiz_api_req)
print(quiz_api_req.json())
print(quiz_api_req.json()['results'][0]['category'])
print(quiz_api_req.json()['results'][0]['type'])
print(quiz_api_req.json()['results'][0]['difficulty'])
print(quiz_api_req.json()['results'][0]['question'])
print(quiz_api_req.json()['results'][0]['correct_answer'])
print(quiz_api_req.json()['results'][0]['incorrect_answers'])