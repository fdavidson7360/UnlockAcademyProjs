'''
Write a program that receives a group of comma separates intergers
Store the input in an array
Loop through the array removing elements that are greater than 50
'''

def remove_values(intArr):
    for x in range(len(intArr)):
        #list comprehension to populate a new array with values less than 50
        newArr = [intArr[item] for item in range(len(intArr)) if intArr[item] < 50]
    return newArr


def main():
    #Retrieve user input
    #Store in array
    intArr = []
    userStr = ""
    userStr = input("Enter a group of comma separated integers to be stored in an array: ")
    intArr = [int(i) for i in (userStr.split(","))]
    #print(intArr)
    returnedArr = remove_values(intArr)
    print(returnedArr)



if __name__ == "__main__":
    main()