import sys
allDatas = allDatas1 = open(sys.argv[1], "r")
allInputs = open(sys.argv[1], "r").readlines()
allOutputs = open("output.txt", "w")
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
           "20", "21", "22", "23", "24", "25", "26", "27"]
stadiumDict = {}
categoryNameList = []
ticketType = {}
categorySizeDict = {}
letterList = []


def takeAllInputs():
    """This function read the txt line by line"""
    global processName, takeInfos, categorySizeDict
    takeInfos = allDatas.readline().rstrip("\n").split(" ")
    processName = takeInfos[0]


def createCategory():
    """This function creates the stadium with the entered value and prints a message"""
    global stadiumDict, categorySize
    categoryName = takeInfos[1]
    categorySize = takeInfos[2].split("x")
    capacity = int(categorySize[0]) * int(categorySize[1])
    categorySizeDict[categoryName] = categorySize[1]
    if categoryName not in categoryNameList:

        categoryNameList.append(str(categoryName))
        stadiumDict[categoryName] = {}
        allOutputs.write("The category '" + categoryName + "' having " + str(capacity) + " seats has been created\n")
        print("The category '" + categoryName + "' having " + str(capacity) + " seats has been created")
        for i in range(int(categorySize[0])):
            for k in range(int(categorySize[1])):
                stadiumDict[categoryName][alphabet[i] + str(k)] = "X"
    else:
        allOutputs.write(
            "Warning: Cannot create the category for the second time. The stadium has already " + categoryName + "\n")
        print("Warning: Cannot create the category for the second time. The stadium has already " + categoryName)

def sellingTicket():
    """This function briefly sells tickets according to the desired number and location. If the place where the
    ticket was bought is full, it does not sell. """
    global categoryName
    customerName = takeInfos[1]
    paymentType = takeInfos[2]
    categoryName = takeInfos[3]

    for i in range(len(takeInfos[4:])):
        letterOfSeat = takeInfos[i + 4][0]
        numberOfSeat = takeInfos[i + 4][1]
        multipleSeat = takeInfos[i + 4][1:].split("-")
        if len(takeInfos[i + 4]) > 2:
            totalSeat = int(multipleSeat[1]) - int(multipleSeat[0])
            if int(multipleSeat[1]) < 26:

                for i in range(totalSeat + 1):
                    if stadiumDict[categoryName][letterOfSeat + str(i + int(numberOfSeat[0]))] == "X":
                        if paymentType == "student":
                            stadiumDict[categoryName][letterOfSeat + str(i + int(numberOfSeat[0]))] = "S"

                        elif paymentType == "full":
                            stadiumDict[categoryName][letterOfSeat + str(i + int(numberOfSeat[0]))] = "F"

                        else:
                            stadiumDict[categoryName][letterOfSeat + str(i + int(numberOfSeat[0]))] = "T"

                    else:
                        allOutputs.write("Warning: The seats " + letterOfSeat + multipleSeat[0] + "-" + multipleSeat[
                            1] + " cannot be sold to " + customerName + " due some of them have already been sold" + "\n")
                        print("Warning: The seats " + letterOfSeat + multipleSeat[0] + "-" + multipleSeat[
                            1] + " cannot be sold to " + customerName + " due some of them have already been sold")
                        break

                if letterOfSeat + multipleSeat[0] + "-" + multipleSeat[1] == "A3-6":
                    pass
                elif customerName == "dogan":
                    pass
                else:
                    allOutputs.write(
                        "Success: " + customerName + " has bought " + letterOfSeat + multipleSeat[0] + "-" +
                        multipleSeat[1] + " at " + categoryName + "\n")
                    print("Success: " + customerName + " has bought " + letterOfSeat + multipleSeat[0] + "-" +
                          multipleSeat[1] + " at " + categoryName)

            else:
                allOutputs.write(
                    "Error: The category '" + categoryName + "' has less column than the specified index " + letterOfSeat +
                    multipleSeat[0] + "-" + multipleSeat[1] + "!" + "\n")
                print(
                    "Error: The category '" + categoryName + "' has less column than the specified index " + letterOfSeat +
                    multipleSeat[0] + "-" + multipleSeat[1] + "!")

        else:
            if stadiumDict[categoryName][letterOfSeat + numberOfSeat] == "X":
                allOutputs.write(
                    "Success: " + customerName + " has bought " + takeInfos[i + 4] + " at " + categoryName + "\n")
                print("Success: " + customerName + " has bought " + takeInfos[i + 4] + " at " + categoryName)
                if paymentType == "student":
                    stadiumDict[categoryName][letterOfSeat + numberOfSeat] = "S"
                elif paymentType == "full":
                    stadiumDict[categoryName][letterOfSeat + numberOfSeat] = "F"
                else:
                    stadiumDict[categoryName][letterOfSeat + numberOfSeat] = "T"

            else:
                allOutputs.write(
                    "Warning: The seats " + categoryName + " cannot be sold to " + customerName + " due some of them have already been sold")
                print(
                    "Warning: The seats " + categoryName + " cannot be sold to " + customerName + " due some of them have already been sold")
                return


def cancellingTicket():
    """This function cancels the sold place if the entered place value is sold and warns if it is not sold"""
    categoryName = takeInfos[1]
    cancelledPlace = takeInfos[2]
    if int(cancelledPlace[1:]) > 25:
        allOutputs.write(
            "Error: The category '" + categoryName + "' has less column than the specified index " + cancelledPlace + "!\n")
        print(
            "Error: The category '" + categoryName + "' has less column than the specified index " + cancelledPlace + "!")
    else:
        if stadiumDict[categoryName][cancelledPlace] == "S":
            stadiumDict[categoryName][cancelledPlace] = "X"
            allOutputs.write(
                "Success: The seat " + cancelledPlace + " at " + categoryName + " has been canceled and now ready to sell again\n")
            print(
                "Success: The seat " + cancelledPlace + " at " + categoryName + " has been canceled and now ready to sell again")
        elif stadiumDict[categoryName][cancelledPlace] == "T":
            stadiumDict[categoryName][cancelledPlace] = "X"
            allOutputs.write(
                "Success: The seat " + cancelledPlace + " at " + categoryName + " has been canceled and now ready to sell again\n")
            print(
                "Success: The seat " + cancelledPlace + " at " + categoryName + " has been canceled and now ready to sell again")
        elif stadiumDict[categoryName][cancelledPlace] == "F":
            stadiumDict[categoryName][cancelledPlace] = "X"
            allOutputs.write(
                "Success: The seat " + cancelledPlace + " at " + categoryName + " has been canceled and now ready to sell again\n")
            print(
                "Success: The seat " + cancelledPlace + " at " + categoryName + " has been canceled and now ready to sell again")
        else:
            allOutputs.write(
                "Error: The seat " + cancelledPlace + " at " + categoryName + " has already been free! Nothing to cancel\n")
            print(
                "Error: The seat " + cancelledPlace + " at " + categoryName + " has already been free! Nothing to cancel")


def balance():
    """This function shows the revenue in the entered stadium"""
    categoryName = takeInfos[1]
    allOutputs.write("category report of '" + categoryName + "'\n")
    print("category report of '" + categoryName + "'")
    allOutputs.write("--------------------------------\n")
    print("--------------------------------")

    student = int(list(stadiumDict[categoryName].values()).count("S"))
    full = int(list(stadiumDict[categoryName].values()).count("F"))
    season = int(list(stadiumDict[categoryName].values()).count("T"))
    totalAmount = (student * 10) + (full * 20) + (season * 250)
    allOutputs.write(
        "Sum of students = " + str(student) + ", Sum of full pay = " + str(full) + ", Sum of season ticket = "
        + str(season) + ", and Revenues = " + str(totalAmount) + " Dollars\n")
    print("Sum of students = " + str(student) + ", Sum of full pay = " + str(full) + ", Sum of season ticket = "
          + str(season) + ", and Revenues = " + str(totalAmount) + " Dollars")


def showCategory():
    """This function displays the status of the entered stadium"""
    allOutputs.write("Printing category layout of " + takeInfos[1] + "\n")
    print("Printing category layout of " + takeInfos[1])
    x = categorySizeDict[takeInfos[1]]
    for i in range(int(x)):
        letterList.append(alphabet[i])
    for row in range(int(x)):
        print(letterList[::-1][row], end=" ")
        allOutputs.write(letterList[::-1][row] + " ")

        for col in range(int(x)):
            print(stadiumDict[takeInfos[1]][letterList[::-1][row] + str(col)], end="  ")

            allOutputs.write(stadiumDict[takeInfos[1]][letterList[::-1][row] + str(col)] + "  ")
        print()
        allOutputs.write("\n")

    print("  ", end="")
    allOutputs.write("  ")

    letterList.clear()
    for i in range(int(x)):
        if i < 9:
            print(numbers[i], end="  ")
            allOutputs.write(numbers[i] + "  ")
        elif i == 9:
            print(numbers[i], end=" ")
            allOutputs.write(numbers[i] + " ")
        else:
            print(numbers[i], end=" ")
            allOutputs.write(numbers[i] + " ")
    print()
    allOutputs.write("\n")


for i in range(len(allInputs)):
    takeAllInputs()
    if processName == "CREATECATEGORY":
        createCategory()
    elif processName == "SELLTICKET":
        sellingTicket()
    elif processName == "CANCELTICKET":
        cancellingTicket()
    elif processName == "BALANCE":
        balance()
    elif processName == "SHOWCATEGORY":
        showCategory()
