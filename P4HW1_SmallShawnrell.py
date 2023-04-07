# CTI-110

# P4HW1 - Score List

# Shawnrell Small

# 04/07/2023


# Collects amount of scores
num_scores = int(input("How many scores would you like to enter? "))
scores = []
# Loop to gather scores
for i in range(num_scores):
    while True:
        score = float(input(f"Enter score {i + 1}: "))
        if score < 0 or score > 100:
            print("INVALID Score!!! Please enter a score between 0 and 100.")
        else:
            scores.append(score)
            break
# Determining lowest score
lowest_score = min(scores)
# Removing lowest score
scores.remove(lowest_score)
# Determines average
average_score = sum(scores) / len(scores)
# Determine letter grade
if average_score >= 90:
    letter_grade = "A"
elif average_score >= 80:
    letter_grade = "B"
elif average_score >= 70:
    letter_grade = "C"
elif average_score >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

# prints "Results" list
print()
print(f'------------Results------------')
print(f"Lowest score entered    : {lowest_score}")
print(f"Modified List   : {scores}")
print(f"Average score   : {average_score:.2f}")
print(f"Letter grade    : {letter_grade}")
print(f'--------------------------------------------')
