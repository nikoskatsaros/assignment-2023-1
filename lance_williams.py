import sys

ai = 0
aj = 0
b = 0
c = 0

def distance(s, t, ai, aj, b, c)
    if len(s) == 1 and len(t) == 1
    return abs (s[0]) 
    
method = sys.argv[1]
example.txt = sys.argv[2]

filename = open(example.txt, 'r' )
data = filename.read()
filename.close();


clusters = []

if method == 'single'
    ai = 1/2
    aj = 1/2
    b = 0
    c = -1/2
elif method == 'complete'
    ai = 1/2
    aj = 1/2
    b = 0
    c = 1/2
elif method == 'average'
        ai = ''
        aj = ''
        b = 0
        c = 0
elif method == 'ward'
        ai = ''
        aj = ''
        b = ''
        c = 0
