#!/usr/bin/env python

'''

Author: Bipin Bachhao (bipinbachhao@gmail.com)

Copyright 2017 Bipin Bachhao (bipinbachhao@gmail.com)

Licensed under the Apache License, Version 2.0 (the 'License');
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an 'AS IS' BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

'''

import os
import shutil
import sys
from datetime import datetime

time_now = datetime.now()
timestamp = '.%s' % (time_now.strftime('%Y_%m_%d_%H:%M:%S'),)
start_directory = '/home/bipin'
scan_report = os.path.join(os.getcwd(), 'scan_report_%s.csv' % timestamp)

def main():
    print 'Hello this is the first line from the main function'
    file_list = get_files("/home/bipin")
    print "File List is: %s" % file_list


def get_files(directory):
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_paths.append(file_path)
    return file_paths


def get_files_test(directory):
    for root, dirs, files in os.walk('.'):
        print root, "consumes",
        print sum(os.path.getsize(os.path.join(root, name)) for name in files),
        print "bytes in", len(files), "non-directory files"
        for file in files:
            fileloc = root + "/" + file
            FILE = os.open(fileloc, os.O_RDONLY)
            junk = os.fstat(FILE)
            size = junk[6]
            atime = junk[7]
            mtime = junk[8]
            ctime = junk[9]
            uid = junk[4]
            gid = junk[5]
            print "   File: %s size: %s atime: %s mtime: %s ctime: %s" % (file, size, atime, mtime, ctime)
            os.close(FILE)



if __name__ == '__main__':
    main()
