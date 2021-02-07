if __name__ == '__main__':
    n = int(input())
    integer_list = list(map(int, input().split()))
    #print(type(integer_list))
    t = tuple(integer_list)
    print(hash(t))
