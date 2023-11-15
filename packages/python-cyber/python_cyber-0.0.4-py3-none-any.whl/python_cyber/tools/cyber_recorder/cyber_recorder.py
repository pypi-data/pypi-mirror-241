#!/usr/bin/env python3

import os
import sys

import subprocess

import python_cyber

def main(args=sys.argv):
    wrapper_exec_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../internal', "cyber_recorder"))
    print("exec wrapper path: " + wrapper_exec_path)
    print(f"exec wrapper args: {args[1:]}" )
    os.system(wrapper_exec_path+" "+' '.join(args[1:]))


if __name__ == '__main__':
    main()
