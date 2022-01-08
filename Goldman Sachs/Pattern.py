def findMinNumberPattern(Str):
    ans = ""  # Minimum number following pattern
    i = 0
    cur = 1  # cur val following pattern
    dCount = 0  # Count of char 'D'
    while (i < len(Str)):

        ch = Str[i]

        # If 1st ch == 'I', incr and add to ans
        if (i == 0 and ch == 'I'):
            ans += str(cur)
            cur += 1

        # If cur char == 'D', incr dCount as well, since we always start counting for dCount from i+1
        if (ch == 'D'):
            dCount += 1

        j = i + 1  # Count 'D' from i+1 index
        while (j < len(Str) and Str[j] == 'D'):
            dCount += 1
            j += 1

        k = dCount  # Store dCount
        while (dCount >= 0):
            ans += str(cur + dCount)
            dCount -= 1

        cur += (k + 1)  # Manages next cur val
        dCount = 0
        i = j

    return ans

print(findMinNumberPattern("I"))
print(findMinNumberPattern("D"))
print(findMinNumberPattern("ID"))
print(findMinNumberPattern("DI"))