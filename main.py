#!/usr/bin/env python3
with open('out.csv') as fin, open('out.txt','w') as fout:
    stripline = lambda line: map(str.strip, line.split(','))
    lenline = lambda line: map(len,line)
    formatfield = lambda col,width: f'{col:^{width}}'

    rows = map(stripline, filter(lambda line: line!='\n',fin))
    lenrows = map(lenline,rows)
    maxlens = tuple(map(max,zip(*lenrows))) # tuple consumes generator
    fin.seek(0) # rows is a map of map on generator
    frows = map(lambda row: '| '+' | '.join(map(formatfield,row,maxlens))+' |',rows)

    for row in frows:
        fout.write(row)
        fout.write('\n')
        #print(row)
    print('rows = ',maxlens)
