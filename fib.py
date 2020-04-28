import argparse

parser = argparse.ArgumentParser(description='Input file name and nth term for the fibonacci sequnce which prints to a file')
parser.add_argument('file', type=str, help='User input file name')
parser.add_argument('num', type=int, help='Nth term of the fibonacci program')
args = parser.parse_args()

f = open(args.file, "x")

def fib_seq(n):
    a=0
    b=1    
    if n <=0:
        print("Enter a valid input")       
    elif n==1:
        f.write(str(a))
    else:
        f.write(str(a) + " ")
        f.write(str(b) + " ")
    for i in range(2,n):
        c = a + b
        a = b
        b = c
        f.write(str(c) + " ")
        c = int(c)
    
    


fib_seq(args.num)


f.close()