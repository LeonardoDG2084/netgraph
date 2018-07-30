#!/usr/bin/python3

import sys
import os
import argparse

arguments = argparse.ArgumentParser(prog='netgraph',
                                    usage=' %(prog)s -f netstat.out -p 22,80 ' \
                                          '-ep 445,3389')

arguments.add_argument('-f', '--netstat-file', required=True,
                       help='netstat output file', dest='inputNetstatFile')

arguments.add_argument('-ip', '--include-ports', required=False,
                       help='Include ports', dest='includePorts')

arguments.add_argument('-ep', '--exclude-ports', required=False,
                       help='Exclude ports', dest='includePorts')

result = arguments.parse_args()

print(result.inputNetstatFile)

