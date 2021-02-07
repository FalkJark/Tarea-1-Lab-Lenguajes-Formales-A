if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    vmax = max(arr)
    arr = set(arr)
    arr.remove(vmax)
    
    smax = max(arr)
    print (smax)
    
        
