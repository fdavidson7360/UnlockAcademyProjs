'''
Write a program that takes comma separated user input and stores it in
an array.
Find the avearge of all elements
Remove all elements less than the average
'''

def remove_values(intArr, avgValue):
    for x in range(len(intArr)):
        #list comprehension to populate a new array with values less than 50
        newArr = [intArr[item] for item in range(len(intArr)) if intArr[item] < avgValue]
    return newArr

def findAvgOfArr(intArr):
    total = 0
    # print("Number of Elements: ", len(intArr))
    for x in range(len(intArr)):
        total += intArr[x]
    return (total/len(intArr)) 
        


def main():
    #Retrieve user input
    #Store in array
    intArr = []
    userStr = ""
    userStr = input("Enter a group of comma separated integers to be stored in an array: ")
    intArr = [int(i) for i in (userStr.split(","))]
    final_avg = findAvgOfArr(intArr)
    #print("Final AVG: ", final_avg)
    returnedArr = remove_values(intArr, final_avg)
    #print(intArr)
    print(returnedArr)


if __name__ == "__main__":
    main()