import sys

def staircase(n):
    for index in range(n):
        print(str("#"*(index+1)).rjust(n))

if __name__ == "__main__":
    n = int(input().strip())
    staircase(n)