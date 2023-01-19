def fib(n):
    count = 0
    f0 = 0
    f1 = 1
    seq = []
    for count in range(n):
        seq.append(f0)
        fn = f1 + f0
        f0 = f1
        f1 = fn
    return seq

def main():
    with open('./fibonacci_n.txt') as f:
        count = int(f.readlines()[0])
        seq = fib(count)
        f.close()
    with open('fibonacci_output.txt', 'w') as fw:
        for i in seq:
            fw.write(str(i)+'\n')

main()