student_scores = [15,142,123,145,124,12,56,78,199,66,89]

# print(max(student_scores))
# 
# total_exa_score = sum(student_scores)
# print(total_exa_score)
 # below will work as above max function
max_score = 0

for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score) # find max num in array