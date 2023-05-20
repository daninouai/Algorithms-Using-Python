import timeit

start = timeit.default_timer()


def BinDP(n, k):
    # ایجاد یک جدول برای ذخیره ضرایب
    # ساخت یک آرایه دو بعدی با ابعاد داینامیک
    table = [[0] * (k + 1) for _ in range(n + 1)]

    # پر کردن جدول به صورت پایین به بالا
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            # ضریب باینومیال برابر با ۱ در صورتی که j برابر با ۰ یا j برابر با i باشد
            if j == 0 or j == i:
                table[i][j] = 1
            # محاسبه ضریب باینومیال با استفاده از رابطه بازگشتی
            else:
                table[i][j] = table[i - 1][j - 1] + table[i - 1][j]

    return table[n][k]


# مثال استفاده از تابع
result = BinDP(10, 16)
print(f"result is: {result}")

stop = timeit.default_timer()

print('Time: ', stop - start)


