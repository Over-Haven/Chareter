#Take
string = input("Please enter your own words :")
#take
char = input("Please enter your own character :")
i = 0
count = 0
#loop
while(i < len(string)):
     if(string[i] == char):
          count = count + 1
     i = i + 1
print("The total number of time", char,"has Occurred =",count)
