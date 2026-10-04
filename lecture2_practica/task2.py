def check_winners(scores, student_score):
    sorted_scores = sorted(scores, reverse=True)
    if sorted_scores.index(student_score) <= 2:
        print("Вы в тройке победителей!")
    else:
        print("Вы не попали в тройку победителей.")



