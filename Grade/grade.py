def get_score ():
    score = int(input ("Enter your score? "))
    return score
def calculate_grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >=50:
        return "C"
    elif score >= 45:
        return "D"
    elif score >= 40:
        return "E"
    else:
        return "F"
def display(score,grade):
    print(f"score: {score}")
    print(f"grade: {grade}")
def main():
    Score = get_score()
    Grade = calculate_grade(Score)
    display(Score,Grade)
main()