while True:
    try:
        n = int(input("please input a number:"))
        for i in range(1, n+1):
            for j in range(1, i+1):
                print("{0}*{1}={2}".format(j, i, (i*j)), end="\t")
            print()
    except:
        break