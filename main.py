#!/usr/bin/env python3
import sys

def format_csv(file):
    def splitline(line):
    ''' splits the line into row with columns and shit '''
        return map(str.strip, line.split(',')) 

    def lenrow(row):
    ''' turns elements in a row into their lengths '''
        return map(len,row)

    def formatfield(field,width):
        return f'{field:^{width}}'

    def formatrow(row,widths):
        return '| '+' | '.join(map(formatfield,row,widths))+' |'

    rows = map(splitline, filter(lambda line: line!='\n',file))
    lenrows = map(lenrow,rows)
    maxlens = tuple(map(max,zip(*lenrows))) # tuple consumes file generator
    file.seek(0) # rows is a map of map on generator
    frows = map(lambda row: formatrow(row,maxlens),rows) # currying formatrow is required
    return frows, maxlens

def format_csv_new(file):
    splitline = lambda line: (field.strip() for field in line.split(','))
    lenrow = lambda row: (len(field) for field in row)
    formatfield = lambda field,width: f'{field:^{width}}'
    formatrow = lambda row, widths: '| '+' | '.join(formatfield(field,width) for field,width in zip(row,widths))+' |'

    rows = (splitline(line) for line in file if line!='\n')
    lenrows = (lenrow(row) for row in rows)
    maxlens = tuple(max(column) for column in zip(*lenrows))
    file.seek(0) # rows is a map of map on generator
    rows = (splitline(line) for line in file if line!='\n')
    frows = (formatrow(row,maxlens) for row in rows)
    return frows, maxlens

if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit(f'usage: {sys.argv[0]} <input file> [<output file>]')
    with open(sys.argv[1]) as fin,open(sys.argv[2],'w') if len(sys.argv)==3 else sys.stdout as fout:
        table, colwidths = format_csv_new(fin)
        for row in table:
            fout.write(row+'\n')
        print(f'max column widths = {colwidths}')
