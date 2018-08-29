def pRemover(string):
    if not isinstance(string, str):
        raise TypeError("Input must be string!")
    
    tempList = list()
    index = 0
    for i in string:
        if i not in {',', ':', "'", '"', '.', ';', '(', ')'}:
            tempList.append(string[index])             #collecting words except punctuation marks
        index += 1

    newString = "".join(tempList)                      #creating string again
    return (newString)


string = input("Enter your sentence: ")
s = pRemover(string)
print (s)
