def average(array):
    # your code goes here
    d = 0
    a = set(array)
    tam = len(a)
    for n in a:
        d = d + n
    avarage = d/tam
    return avarage
        
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)