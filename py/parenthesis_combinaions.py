def backtrack(n, res, temp, open, close):
    if open == n and close == n:
        res.append(temp)
        return

    if open < n:
        backtrack(n, res, temp + "(", open + 1, close)

    if close < n and close < open:
        backtrack(n, res, temp + ")", open, close + 1)

    print(temp)


def generateBracketCombinations(n):
    res = []

    backtrack(n, res, "", 0, 0)
    return res


if __name__ == "__main__":
    res = generateBracketCombinations(3)
    print(res)
