import array
def main():    
    file = open('s1.txt','r')
    lines = file.readlines()
    X = array.array
    Y = array.array
    for i in range(30):
        frag = lines[i].split('    ')
        X[i] = frag[1]
        frag1 = frag[2].replace('\n','')
        Y[i] = frag1    
    for i in range(30):
        print(X[i],Y[i])
main()