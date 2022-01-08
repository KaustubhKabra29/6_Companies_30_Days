def main():
    arr = [1 , 3 , 3 , 5 , 7 , 7 , 9 , 11 , 11 , 13 , 15 , 15 , 15 , 17  ]

    numberMap = {}

    max = len(arr)
    for i in arr:
        if not i in numberMap:
            numberMap[i] = True

        else:
            print("Repeating =", i)

    for i in range(1, max + 1):
        if not i in numberMap:
            print("Missing =", i)


main()
