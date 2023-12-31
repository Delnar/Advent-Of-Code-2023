import sys
from Point2D import Point2D
from helpers import get_points_from_string_array, get_points_from_string_array_with_values, is_point_in_rectangle

# Open the file in read mode
# file = open('day 03\\josh\\test.txt', 'r')
file = open('day 03\\josh\\input.txt', 'r')

# Read the entire content of the file
content = file.readlines()

# Close the file
file.close()

# Create an array
symbols = get_points_from_string_array(content)
# symbols.append(Point2D(0,0))

# for i in symbols:
#      print(i)

values = get_points_from_string_array_with_values(content)

# for i in values:
#       print(i)  

for v in values:
    bbox = v.get_rectagle().expand(1, 1, 1, 1)
    #print (bbox)
    for s in symbols:
     #   print(s)
        if is_point_in_rectangle(s, bbox):
            v.add_near_point(s)
            # print (f'{v} is in {s}')
            # input()
    #input()


for yPos in range(len(content)):
    i = content[yPos]
    i = i.replace('\n', '')
    # Filter symbols for y position
    symbolsY = list(filter(lambda x: x.y == yPos, symbols)) 
    valuesY = list(filter(lambda x: x.y == yPos, values))

    # print ("Symbols:")
    # for v in symbolsY:
    #     print (v)

    # print ("Values:")
    # for v in valuesY:
    #     print (v)

    # print ("Line:")        
    # print (i)
    
    for xPos in range(len(i)):

        j = i[xPos]
        # Filter symbols for x position
        # symbolsX = list(filter(lambda x: x.x == xPos, symbolsY))
        symbolsX = list(filter(lambda x: x.point_in_rect(Point2D(xPos, yPos)), symbolsY))
        valuesX = list(filter(lambda x: x.point_in_rect(Point2D(xPos, yPos)), valuesY))


        if len(symbolsX) != 0:
            print('\033[33m', end='')  # change color of print to yellow            
        elif len(valuesX) > 1:
            print('\033[31m', end='')  # change color of print to red
        elif len(valuesX) == 1:
            if len(valuesX[0].get_near_points()) >= 1:                
                print('\033[34m', end='')  # change color of print to red
            else:
                print('\033[32m', end='')  # change color of print to red
        else:
            print('\033[37m', end='')  # change color of print to white

        # print(f'{xPos} {j}')
        print(j, end='')
    print()



sum = 0
by_symbol = False
for i in values:
    by_symbol = False

    #print (i.get_rectagle())    
    bbox = i.get_rectagle().expand(1, 1, 1, 1)
    #print (bbox)
    #input()
    for j in symbols:
        if is_point_in_rectangle(j, bbox):
            by_symbol = True
            break
    if by_symbol == False:
        # print(i)
        continue
    sum += i.v

print(sum)


