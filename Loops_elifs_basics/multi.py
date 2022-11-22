#multiplication tables upto 9
for j in range(1, 10):
    for i in range(1, 11, 1):
        # 2 *i (current number)
        product = j * i
        print(product, end = " ")
    print()


