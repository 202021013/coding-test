score_list = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
total_score = 0
total_credit = 0

for _ in range(20):
    values = input().split()
    subject, credit, score = values[0], float(values[1]), values[2]

    if values[2] in score_list:
        total_score += credit * score_list[score]
        total_credit += credit

print(total_score / total_credit)