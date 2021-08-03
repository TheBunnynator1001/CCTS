# Collatz Conjecture Test Script
# By TheBunnynator1001
# Version 2.0.1
# Currently tested to 2E70
#
#
# Feel free to donate to the cause! https://streamlabs.com/nirnsroot
# Check out my stream, where I'm either coding or gaming, or both!
# http://www.twitch.tv/nirnsroot


# Define all necessary variables
steps = 0
a = int(input('From 2 to the power of: '))
b = int(input('Until 2 to the power of: '))
a0 = 2 ** a
b0 = 2 ** b
largest_step = 0
c1 = 0

# Define initial loop to iterate through all numbers
for i in range(a0, b0):
    c0 = i
    c1 = c0
    print(int(c0))
# Define loop to cycle through equation until c0 = 1
    while c0 != 1:
        if c0 % 2 == 0:
            c0 = c0 / 2
            steps += 1
            print(int(c0))
        else:
            c0 = 3 * c0 + 1
            steps += 1
            print(int(c0))
# Seeing if this step count is larger than current record
        if steps >= largest_step:
            largest_step = steps
            c2 = c1
        
# Check if the steps taken has reached the limit provided
# If it has, program breaks and shows number that failed and how many steps it took
    if steps > 999999999:
        print('Step limit reached, hypothesis proved invalid at number', c2, ', with', steps, 'tested.')
        print('Largest number of steps is:', largest_step, 'on number:', c2)
        break
    else:
        print('Steps:', steps)
        steps = 0
print('Largest number of steps is:', largest_step, 'on number:', c2)