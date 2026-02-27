# FILE NAME - grade_converter.py

# NAME: Nicholas Thurston
# DATE: 2/26/2026
# BRIEF DESCRIPTION: Grade Converter



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

print('===== Grade Converter =====')

# Ask user for a number
percent = int(input('Enter a numerical grade (1-100): '))

# Calculate grade
if percent > 100:
    print('A+')
elif percent >= 90 and percent <= 100:
    print('A')
elif percent in range(80,90):
    print('B')
elif percent in range(70,80):
    print('C')
elif percent in range(65,70):
    print('D')
else:
    print('F')

########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Grade Converter =====
Enter a numerical grade (1-100): 101
A+
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): -78
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 64
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 65
D
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 66
D
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is something you would tell a future student to be careful about when
   doing this lab?


Pay close attention to the logic in the lab and test it.




'''
