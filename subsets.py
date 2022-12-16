def subsets(integers):
    lenIntegers = len(integers)
    for i in range(2**lenIntegers):
        mask = bin(i)[2:].zfill(lenIntegers)
        subset = [integers[j] for j in range(lenIntegers) if mask[j] == "1"]
        print(f"{int(mask, 2)} -> {subset}")


# Watch it working
if __name__ == "__main__":
    subsets([1, 2, 3, 4, 5, 6, 7, 8])
