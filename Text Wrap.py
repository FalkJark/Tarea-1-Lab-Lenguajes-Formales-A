import textwrap

def wrap(string, max_width):
    cont = 0
    string = list(string)
    j = ""
    aux = ""
    for i in string:
        cont = cont + 1 
        j = j + i
        if cont == max_width:
            cont = 0
            j = j + '\n'
            
    return j

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)