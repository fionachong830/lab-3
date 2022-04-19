import random

def bubblesort(seq):
    for i in range(len(seq)-1):
        for j in range(len(seq)-1,i,-1):
            if seq[j-1] > seq[j]:
                seq[j-1], seq[j] = seq[j], seq[j-1]
    
    return seq
            
print(bubblesort(random.sample(range(1,50),20)))