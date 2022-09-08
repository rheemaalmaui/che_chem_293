# Generates two short sequences based on random seed

import random
import sys

def generate_matrix(seed):
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
    
    print("=================================")
    print(f"Random Seed String: {seed}")
    print("Distances")
    print("----------------")
    print(f"A to B: {random.randint(1,20)}")
    print(f"A to C: {random.randint(1,20)}")
    print(f"A to D: {random.randint(20,90)}")
    print(f"B to C: {random.randint(1,20)}")
    print(f"B to D: {random.randint(20,40)}")
    print(f"C to D: {random.randint(50,90)}")
    print("=================================")

if __name__ == '__main__':
    generate_matrix("_".join(sys.argv[1:]))