#Python Assignment

#Samarth H Chinivar
#1VA19IS044

from random import sample

Questions = ['What is the capital of the United States of America ?',
             'Who is called as the Peoples Champion in Boxing ?',
             'Which Cricketer has scored 100 centuries ?',
             'Who is called as The WALL of Cricket ?',
             'What is the capital of France ?',
             'Where is Amsterdam located ?',
             ]

Answers = ['Washington DC',
           'Muhammed Ali',
           'Sachin Tendulkar',
           'Rahul Dravid',
           'Paris',
           'Netherland',
           ]

n_right = 0

key = list(zip(Questions, Answers))

s = sample(key, 4)

for i in s:
    print(i[0])
    user_answer = input('Your Guess: ')
    if user_answer.lower() == i[1].lower():
        print('Correct!!!')
        n_right += 1
    else:
        print('Not Correct')
        
# Added a final fraction of correct statement
print('{}/4 Questions Correct'.format(n_right))
