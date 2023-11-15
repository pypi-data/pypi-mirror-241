#!/usr/bin/env python3

import subprocess
import os
import sys
import python_cyber


def main(args=sys.argv):
    if os.getenv('TERM') is None:
        os.environ['TERM'] = "xterm-256color"
    if os.getenv('TERMINFO') is None:
        os.environ['TERMINFO'] = "/lib/terminfo"
    wrapper_exec_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../internal', "cyber_monitor"))
    print("exec wrapper path: " + wrapper_exec_path)
    os.system(wrapper_exec_path+" "+' '.join(args))


if __name__ == '__main__':
    main()
