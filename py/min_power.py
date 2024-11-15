def sumOfArray(arr):
    sum = 0
    for i in arr:
        sum += i
    
    return sum

def minPower(cells):
    totalPower = 0
    cells.sort()

    for i in range(len(cells) - 1):
        totalPower += sumOfArray(cells)
        cells.pop()

    return totalPower

if __name__ == "__main__":
    result = minPower([30, 10, 20, 50, 40])

    print("Expected Answer: 30 + 60 + 100 + 150 = 340")
    print(result)