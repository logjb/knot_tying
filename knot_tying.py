import itertools
import numpy

with open("knots2.txt") as textFile:
    practice = [line.split() for line in textFile]
print practice
current_problem = []
problems_left = []
current_height = []
current_width = []
final_answers = []
current_height.append(practice.pop(0))
count = 0
print problems_left
#iterate through each problem
while problems_left:

    #get the height and width of the current problem
    current = problems_left.pop(0)
    current_height = current[0]
    current_width = current[1]
    for i in range(0, current_height):
        practice.append(list(practice[i]))
    #end if there is no next problem
    if current_width == "0":
        break
    #get the values of the current problem
    for i in range(0, len()):
        current_problem.append(problems_left.pop(0))
    #current problems height, width, and values
    print "height", current_height
    print "width", current_width
    print "problem", current_problem

    #find the starting value (left most "-")
    for i in range(0, len(current_problem)):
        if current_problem[i][0] == "-":
            starting_point = i
            break
    print "starting point row, y value is always 0", starting_point

    #do computation stuff (Matt) so just follow the -, you know that it starts going right, in the "starting_points"
    #row, keep track of the intersections and the direction your moving in.
    #as you can see current_problem[0] is an array of the first row, so current_problem[0][0] is the top left value
    #and current_problem[1] is the second row, right below it

    #what it looks like stack on top of each other
    for k in range(0, len(current_problem)):
        print current_problem[k]

    #reset values for the next problem
    del current_problem[:]

#print out the final answers (whether or not a knot will be formed)
for k in range(0, len(final_answers)):
    print final_answers[k]