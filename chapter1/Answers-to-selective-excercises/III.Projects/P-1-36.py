sentence = "5 11 5 5 33 44"      # enter your text here
words = sentence.split()

def nonRepeated(lst):
    result = []
    for word in lst:
        if word not in result:
            result.append(word)
    return result


main = nonRepeated(words)        # using main as non repeated words
repetitions = {}                 # creating a dictionary in order to save final results
for word in main:
    value = 0
    for rep in words:
        if word == rep:
            value += 1
    repetitions[word] = value

print(repetitions)
