#Print out all colors from color-list1 not contained in color-list2.

color_list1=list(input("enter some colors for list 1:").split(","))     #input list of colors
a=set(color_list1)          #store as set in 'a'
print("color_list1",a)      #print  set color_list1

color_list2=list(input("enter some colors for list 2:").split(","))     
b=set(color_list2)
print("color_list2",b)
p=a-b                       #remove colors of 'b' present in 'a' and store  the lefted colors of 'a' in p
print("colors from color list1 not contained in color list2:",p)        #print colors in 'p'


'''output

enter some colors for list 1:red,blue
color_list1 {'red', 'blue'}
enter some colors for list 2:green,red
color_list2 {'red', 'green'}
colors from color list1 not contained in color list2: {'blue'}

'''
