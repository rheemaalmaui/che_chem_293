# Generates two short sequences based on random seed

import random
import sys

def generate_sequences(seed):
    """
    Generates two short sequences based on random seed
    :param seed:
    :return:
    """
    # Generate two short sequences
    random.seed(seed)

    LETTERS = list("AAAAATCG")
    sequence_1 = str()
    sequence_2 = str()

    for _ in range(4):
        sequence_1 += random.choice(LETTERS)
        sequence_2 += random.choice(LETTERS)
    
    print(f"Random Seed String: {seed}")
    print(f"Sequence 1: {sequence_1}")
    print(f"Sequence 2: {sequence_2[0:3]}") # only return part of the second sequence

if __name__ == '__main__':
    generate_sequences("_".join(sys.argv[1:]))