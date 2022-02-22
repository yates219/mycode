#!/usr/bin/env python3
"""Small script to move two files into ceph_storage/"""

import shutil
import os

def main():
    os.chdir("/home/student/mycode") # move into working directory

    shutil.move("raynor.obj","ceph_storage/") # moves file raynor into ceph_storage directory

    xname = input("What is the new name for kerrigan.obj? ") # gets input for new filename

    shutil.move("ceph_storage/kerrigan.obj","ceph_storage/" + xname) # changes name of kerrigan file

main() # calls main function

