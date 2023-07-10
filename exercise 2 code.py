import requests
import json
import re

def calculate_answer(problem):
    problem_parts = re.findall(r'\d+', problem)
    operator = re.findall(r'[\+\-\*\/]', problem)[0]
    num1 = int(problem_parts[0])
    num2 = int(problem_parts[1])

    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '*':
        answer = num1 * num2
    elif operator == '/':
        answer = num1 / num2

    return answer

def solve_challenges(challenges):
    answers = []
    for challenge in challenges:
        problem = challenge['problem']
        answer = calculate_answer(problem)
        answers.append(answer)
    
    return answers

def print_solutions(challenges, answers):
    print("Name: Bhavani prasad Reddy")
    print("Blazer ID: Bambati")
    for i, challenge in enumerate(challenges):
        problem = challenge['problem']
        print(f"Problem {i+1}: {problem} Answer: {answers[i]}")

def main():
    url = "https://michaelgathara.com/api/python-challenge"

    # Send a GET request to retrieve the challenge
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract the challenges from the response
        challenges = response.json()

        # Solve the challenges
        answers = solve_challenges(challenges)

        # Print the solutions
        print_solutions(challenges, answers)
    else:
        print("Failed to retrieve challenges.")

# Execute the main function
if __name__ == "__main__":
    main()
