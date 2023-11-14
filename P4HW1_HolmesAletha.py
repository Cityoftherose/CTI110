# CTI-110
# P4HW1 - Score List
# Aletha Holmes
# 11/14/23
#

# Ask user to enter the number of scores they would like to enter
# Initialize an empty list to store the scores
# Create a loop to collect the number of scores the user wants to enter
# Evaluate if the score is valid, it should be between 0 and 100
# If it is not, notify the user and ask for a VALID score to be entered
# Append the valid score to the score list
# Find the lowest score
# Remove the lowest number from list
# Find the average
# Display the results



num_scores=int(input('How many scores do you want to enter? '))
print()
a = 1
score_list=[]


for a in range(num_scores):
    
    score = float(input('Enter score #{}: '.format(a+1)))
    
    while score < 0 or score > 100:
        print()
        print('INVALID Score entered!!!! ')
        print('Score should be between 0 and 100 ')
        score = float(input('Enter score #{} again: '.format(a+1)))

    else:
        score_list.append(score)
        a+=1 

lowest_score = min(score_list)
score_list.remove(lowest_score)
score_avg=sum(score_list )/len(score_list)

if score_avg >= 90:
    Grade = "A"
elif score_avg >= 80:
    Grade = "B"
elif score_avg >= 70:
    Grade = "C"
elif score_avg >= 60:
    Grade = "D"
else:
    Grade = "F"

print()
print()

print('--------------Results-----------')
print('Lowest Score  : {:.1f}'.format(lowest_score))
print('Modified List : {}'.format(score_list))
print('Scores Average: {:.2f}'.format(score_avg))
print('Grade         : {}'.format(Grade))
print('-----------------------------------')
