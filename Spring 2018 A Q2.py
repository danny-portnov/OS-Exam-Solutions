#!/bin/python3
#! /usr/bin/env python

from subprocess import Popen, PIPE
import sys
import os


def main() -> None:
    dir: str = sys.argv[2] if len(sys.argv) == 3 else os.path.curdir
    name: str = sys.argv[1]
    p = Popen(["find", dir, "-name", name], stdout=PIPE, stderr=PIPE)
    found = False
    for line in p.stdout:
        line: str = line.rstrip().decode("utf-8")
        if "Permission denied" in line:
            continue
        print(os.path.dirname(line))
        found = True
    if not found:
        print("No such file found")
    p.terminate()


if __name__ == "__main__":
    main()
