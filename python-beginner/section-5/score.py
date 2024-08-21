student_scores = [1, 4, 2, 50, 23, 42, 64, 12, 3]

highest_score = 0

for score in student_scores:
    if score > highest_score:
        highest_score = score

# If you only want the highest score, you could also print it at the end
# print("The highest score is:", highest_score)
print("The highest score is: ", highest_score)
