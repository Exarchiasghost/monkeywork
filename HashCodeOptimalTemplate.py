import fileinput

itIsTheFirstLine = True     #This variable is about the input line. If the line is the first the variable itIsTheFirstLine is True.
T=0     #The number of lines with usefull Data. the number of tierations.
result = "Not any result right now" #this is used for the result wich is printed in the end of the code with the default value.
countForT = 0 #this is the count vairiable that helps to check that the iterations are not more than the predefined T variable.
f = open('output.txt','w')


#the mainCheckFunction() function is doing the necessary checking before the mainCalculativFunction().
#there is always something to check
def mainCheckFunction(checkFunctionsProperty):
        if checkFunctionsProperty == True:
                return True

#The function mainCalculativFunction() solves the logical problem of the exercise.         
def mainCalculativFunction(inputProperty):
    if mainCheckFunction(True):
        return inputProperty

#The function firstLineCorrection() changes the itIsTheFirstLine to False and stores the N to the variable T
def firstLineCorrection(inputForNInitiation):
    global itIsTheFirstLine
    global T
    itIsTheFirstLine = False
    T = inputForNInitiation
    
#this is the function that uses the countForT to check up that the iterations are not more than what the T variable defines    
def iterationsCheck(hereGoesTheCountForTParameter):
    if hereGoesTheCountForTParameter >= int(T):
        return True
    
    
#The main iteration, (AKA the main loop), now is the main() function. 
#The separation of code to functions blocks keeps the template simple and clear.    
def main():
    global countForT
    for line in fileinput.input("happyinput.in"):
        print("itIsTheFirstLine now is " + str(itIsTheFirstLine))
        print("itIsTheFirstLine now is " + str(itIsTheFirstLine) end='\n' file=f)
        if itIsTheFirstLine == True:
            firstLineCorrection(N)
        else:
            result = mainCalculativFunction(N)
            countForT += 1
            print("the T which represent the number of lines with input data, now is " + str(T))        
            if iterationsCheck(countForT):
                print("the result of the main calculative fuction know as mainCalculativFunction() now is " + result)
            else:
                print ("the N now which is the value of the last input now is " + str(N))
                
if __name__ == "__main__": main()



#Optimal print example
#print("Case #", str(unregisteredcase), ": ", number_string2, " ",sep="", end='\n', file=f)


f.close()
print("That's all folks!")
