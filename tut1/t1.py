n = 10
count = 0
f0 = 0
f1 = 1
for count in range(n):
    print(f0)
    fn = f1 + f0
    f0 = f1
    f1 = fn