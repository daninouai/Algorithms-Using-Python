import timeit

start = timeit.default_timer()


def BinDQ(n, k):
    if k == 0 or n == k:
        return 1
    else:
        # محاسبه ضریب باینومیال با استفاده از رابطه بازگشتی
        return BinDQ(n - 1, k - 1) + BinDQ(n - 1, k)


# مثال استفاده از تابع
result = BinDQ(10, 16)
print(f"result is: {result}")

stop = timeit.default_timer()

print('Time: ', stop - start)


