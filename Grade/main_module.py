import input_module
import logic_module
import output_module

def main():
    score = input_module.get_score()
    grade = logic_module.calculate_grade(score)
    output_module.display(score,grade)
main()