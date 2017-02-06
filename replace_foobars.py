#!//bin/python3
# -*- coding: utf-8 ; mode: python -*-
#
#  © Copyright 2016–2017 Roland Sieker <ospalh@gmail.com>
#
# License: GNU AGPL, version 3 or later;
#  http://www.gnu.org/licenses/agpl.html


import argparse
import io
import os
import re
import tempfile

__version__ = '0.0.2'


def do_process(args):
    with open(args.infile, 'r') as inf:
        inf_s = inf.read()
        with open(args.outfile, 'w') as outf:
            with open(args.wordfile, 'r') as wordlist:
                for wordline in wordlist.readlines():
                    word = re.search('[0-6]+\\s+([^\s]+)', wordline).group(1)
                    inf_s = inf_s.replace('foobar', word, 1)
            outf.write(inf_s)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="""Process content of file INFILE.""")
    parser.add_argument("infile", type=str, help='''The file to process''')
    parser.add_argument("outfile", type=str, help='''The output file''')
    parser.add_argument("wordfile", type=str, help='''The word list''')
    args = parser.parse_args()
    do_process(args)
