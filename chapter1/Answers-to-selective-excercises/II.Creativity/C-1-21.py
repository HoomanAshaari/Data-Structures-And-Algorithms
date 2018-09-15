textFile = open("C-1-21.txt", "w+")
print("Enter your txt, and use  ctrl+D  when you're finished: ")

while True:
    try:
        textFile.write(input() + "\n")
    except EOFError:
        print("Closing file...")
        textFile.close()
        break

textFile = open("C-1-21.txt", "r")
lst = textFile.readlines()
length = len(lst)
for i in range(length-1, -1, -1):
    print(lst[i])
textFile.close()
