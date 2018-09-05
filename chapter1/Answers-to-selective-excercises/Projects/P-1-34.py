import random

# A function wich makes a list of different numbers with given length
def randomBox(num):
    madeNums = 0
    box = []
    while madeNums!= 8:
        rand = random.randrange(1, 101)
        if rand not in box:
            box.append(rand)
            madeNums += 1
    return box


typoLine = randomBox(8)            # number 8 passed, because we need 8 random typoes

sentence = "I will never spam my friends again."
typoes = 0
typo = ["I wil never spam mu friends again.", "I will never spam my friends agin.",
    "I will never spm my friends again.", "I will never spam my friemd again.", "I wiil never spam my friened again.",
    "I will nver spam my friends again.", "I will never spm my friends again.", "I will never spam my frids again.", 
    "I will never spam my frieends again."]
for i in range(1, 101):
    if i in typoLine:
        print (i, '. ', typo[random.randrange(0,len(typo)-1)])
        typoes += 1
    else:
        print (i, ". ", sentence)

print(typoLine)                     # Lines which typoes happened
