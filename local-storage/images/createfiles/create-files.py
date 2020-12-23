#!/usr/bin/env python3
"""
Create a number of files in /vol1
"""
from os import path
from time import sleep


MOUNT = "/vol1"


def volume_mounted() -> bool:
    return path.ismount("/vol1")


def create_files() -> None:
    for x in range(0, 19):
        file = open(MOUNT + "/file-" + str(x) + ".txt", 'w+')
        file.write("Quick file")
        file.close()


def hold_container() -> None:
    print("Holding container")
    while True:
        sleep(30)


def main():
    if volume_mounted():
        print("vol1 mounted. Writing files...")
        create_files()
    else:
        print("vol1 not mounted.")
    hold_container()


if __name__ == "__main__":
    main()
