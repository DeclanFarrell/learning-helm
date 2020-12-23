#!/usr/bin/env python3
"""
Delete all files in /vol1
"""
from os import path, unlink, walk
from sys import exit
from shutil import rmtree

MOUNT = "/vol1"


def volume_mounted() -> bool:
    return path.ismount("/vol1")


def clean_dir() -> None:
    for root, dirs, files in walk(MOUNT):
        for f in files:
            unlink(path.join(root, f))
        for d in dirs:
            rmtree(path.join(root, d))


def main() -> None:
    if volume_mounted():
        print("vol1 mounted. Cleaning Volume")
        clean_dir()
    else:
        print("vol1 not mounted.")
        exit(2)


if __name__ == "__main__":
    main()
