def isdistinc(seq):
    if isinstance(seq, (set, dict)):
        raise TypeError("Sequence must support INDEXING!")

    length = len(seq)
    for i in range(length-1):               #Loop for choosing sequence items, except last one
        for j in range(i+1, length):        #Loop for iterating sequence items in order to comparison
          if seq[i] == seq[j]:
              return False
    
    return True
