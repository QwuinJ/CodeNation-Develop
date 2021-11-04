# Simple if / elif loop to check current day and print a different statement for each

import datetime

weekno = datetime.datetime.today().weekday()

# if weekno < 5:
#     print('Can\'t wait for the weekend!')
# else: 
#     print('It\'s the weekend babey!')

if weekno == 0:
    print("Man I hate Mondays")
elif weekno == 1:
    print("Two for Tuesday!")
elif weekno == 2:
    print("Hump day am I right?")
elif weekno == 3:
    print("Thursdays are my least favourite day.")
elif weekno == 4:
    print("Thank God it's Friday")
elif weekno == 5:
    print("God my head!")
else:
    print("Ugh, work again tomorrow")
