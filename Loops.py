if __name__ == '__main__':
    n = int(input())
    
    number = []
    for x in range(n):
        square = x**2
        number.append(square)
    for i in range(len(number)):
        print (number[i])        
    
