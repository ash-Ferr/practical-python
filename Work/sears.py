#sears.py
bill_thickness=0.11*0.001  #convert .11mm to meters
sears_height=442 # height in meters
num_bills=1  #initalize the bill variable
day=1  #day count

while (num_bills*bill_thickness < sears_height):
    print(day,num_bills, num_bills*bill_thickness)
    day=day+1
    num_bills = num_bills*2

print('Number of days',day)
print('Number of bills',num_bills)
print('Final height',num_bills*bill_thickness)
