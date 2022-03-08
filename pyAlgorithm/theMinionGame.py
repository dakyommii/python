def minion_game(string):

    st=0
    kv=0
    l=len(string)
    for i in range(l):
        if s[i] in "AEIOU": kv += l-i
        else: st += l-i

    if st>kv: print("Stuart %d"%(st))
    elif st==kv: print("Draw")
    else: print("Kevin %d"%(kv))

if __name__ == '__main__':
    s = input()
    minion_game(s)