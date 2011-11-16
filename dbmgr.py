#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2011-11-16
@author: shell.xu
'''
import os, sys, getopt
import segment

dbname = 'frq.db'

def load(filepath):
    ddb = segment.dictdb(dbname, 'n')
    ddb.loadtxt(filepath)
    ddb.flush()

def export(filepath):
    with open(filepath, 'w') as fo: ddb.export(fo)

def trans_cedict(infile, outfile):
    words = set()
    with open(infile, 'r') as fi:
        for line in fi:
            if line.startswith('#'): continue
            word = line.split()[1].decode('utf-8')
            if len(word) > 1: words.add(word)
    with open(outfile, 'w') as fo:
        for word in list(words):
            fo.write((u'%s 1\n' % word).encode('utf-8'))

def main():
    opts, args = getopt.getopt(sys.argv[1:], 'd:')
    for opt, val in opts:
        if opt == '-d':
            global dbname
            dbname = val
    if len(args) == 0:
        print 'loadtxt or exporttxt'
    elif args[0] == 'load': load(args[1])
    elif args[0] == 'export': export(args[1])
    elif args[0] == 'trans_cedict': trans_cedict(args[1], args[2])

if __name__ == '__main__': main()
