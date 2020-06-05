#两种打印乘法口决表的方法
for m in range(1,10):
    for n in range(1,m+1):
        print(f'{m}*{n}={m*n}',end=' ')
    print()
print('-'*70)
x = 1
while x <= 9:
    y = 1
    while y < x + 1:
        print(f'{x}*{y}={x * y}', end=' ')
        y += 1
    x += 1
    print()
