from random import randrange

def myChoice(seq):
    if isinstance(seq, (set, dict)):
        raise TypeError("Sequence must support INDEXING!")
    
    length = len(seq)
    index = randrange(0, length)  #Generating a random index
    return seq[index]
