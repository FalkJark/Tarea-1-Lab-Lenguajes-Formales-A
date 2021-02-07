
# Complete the solve function below.
def solve(s):
    s = s.title()
    t = len(s)-1
    print(t)
    if (s[t]=="G"):
        print("Pasa por el if")
        s = s.replace("G","g")
    return s
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()