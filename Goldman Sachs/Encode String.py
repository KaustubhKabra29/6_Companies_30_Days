def encodestr(st):

    n = len(st)
    i = 0
    while i < n- 1:
        count = 1
        while (i < n - 1 and
               st[i] == st[i + 1]):
            count += 1
            i += 1
        i += 1

        # Print character and its count
        print(st[i - 1] +
              str(count),
              end = "")

# Driver code
if __name__ == "__main__":

    st = "abbcccddddeeeeeffffffggggggghhhhhhhhiiiiiiiiijjjjjjjjjjkkkkkkkkkkk"
    encodestr(st)