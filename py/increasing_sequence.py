def calcIncSeq(sequence, k):
    sequence_count = 0
    check_count = 0
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i - 1]:
            check_count += 1
        else:
            check_count = 0

        print(f"Check Count: {check_count}")

        if check_count == k:
            sequence_count += 1
            check_count = 0

    return sequence_count


if __name__ == "__main__":
    count = calcIncSeq([2, 4, 6, 1, 0, 4, 8, 9, 6, 3, 5], 2)

    print(count)
