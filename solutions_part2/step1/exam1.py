import grading
    
student_results = {
               'John': 3,
               'Mary': 9,
               'Peter': 5
               }

for s_name, s_grade in student_results.items():
    s_feedback = grading.comment_grade(s_grade, mode='negative_reinforcement')
    print(f'Feedback for {s_name}: {s_feedback}')
