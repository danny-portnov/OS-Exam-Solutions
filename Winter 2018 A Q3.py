#!/bin/python3
#! /usr/bin/env python

from subprocess import Popen, PIPE
import sys
import os


def main() -> None:
    p = Popen(["mount"], stdout=PIPE)
    folders = []
    for line in p.stdout:
        line: list[str] = line.rstrip().decode("utf-8").split()
        perm = line[4].split[','][0].replace('(', '')
        if perm == 'r':
            folders.append(os.path.join(line[2], line[3]))
    p.terminate()
    if not folders:
        print("No read-only directories")
        return
    print("Read-only directories:")
    for folder in folders:
        print(folder)


if __name__ == "__main__":
    main()
