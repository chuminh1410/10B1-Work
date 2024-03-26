# Program to perform a bubble sort

userName = ["Carl","Tamsin","Eric","Zoe","Alan","Mark"]
print ("list of unsorted names: ", userName)
#numItems is the length of the list
numItems = len(userName)
while numItems > 1:
    for count in range(5):
        if userName[count] > userName[count+1]:
            temp = userName[count+1] 
            userName[count] = userName[count+1] 
            userName[count+1] = temp
        print ("count = ",count, "userName[count] = ", userName[count],
               "userName[count+1] = ",userName[count+1])
    numItems = numItems - 1
    #endfor
#endwhile
print (userName)