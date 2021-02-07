def minion_game(string):
    vocales = 'AEIOU'
    Stuart_p, Kevin_p = 0, 0
    l = len(string)
    for start_idx in range(l):
        score = l - start_idx
        if string[start_idx] in vocales:
            Kevin_p = Kevin_p + score
        else:
            Stuart_p = Stuart_p + score
    if Stuart_p == Kevin_p:
        print('Draw')
    if Stuart_p > Kevin_p:
        print('Stuart {}'.format(Stuart_p))
    if Stuart_p < Kevin_p:
        print('Kevin {}'.format(Kevin_p))
    
    
if __name__ == '__main__':
    s = input()
    minion_game(s)