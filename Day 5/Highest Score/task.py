student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# print(range(1, 10))

print(max(student_scores))

max_score = student_scores[0]
for m in student_scores[1:]:
    if max_score < m:
        max_score = m
print(max_score)
