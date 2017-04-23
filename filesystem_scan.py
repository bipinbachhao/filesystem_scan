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
import csv
from datetime import datetime
from pwd import getpwuid
from grp import getgrgid


time_now = datetime.now()
timestamp = '.%s' % (time_now.strftime('%Y_%m_%d_%H:%M:%S'),)
start_directory = '/home/bipin/Workspace/'
#scan_report = os.path.join(os.getcwd(), 'scan_report_%s.csv' % timestamp)
scan_report = os.path.join(os.getcwd(), 'scan_report.csv')

def main():
    print 'Hello this is the first line from the main function'
    file_list = get_files(start_directory)
    get_files_test(start_directory)
    print "File List is: %s" % file_list


def get_files(directory):
    file_paths = []
    with open(scan_report, 'wb') as csvfile:
        field_names = ['Directory', 'No of Files', 'File name', 'UID', 'GID', 'File Size', 'Creation Time', 'Access Time', 'Modification Time']
        csv_writer = csv.writer(csvfile, delimiter=',', lineterminator='\n')
        csv_writer.writerow(field_names)
        for root, dirs, files in os.walk(directory):
            directory_info = [root, len(files), '', getpwuid(os.stat(root).st_uid).pw_name, getgrgid(os.stat(root).st_gid).gr_name, os.stat(root).st_size, datetime.fromtimestamp(os.stat(root).st_ctime), datetime.fromtimestamp(os.stat(root).st_atime), datetime.fromtimestamp(os.stat(root).st_mtime)]
            csv_writer.writerow(directory_info)
            for filename in files:
                file_path = os.path.join(root, filename)
                file_info = ['', '', file_path, getpwuid(os.stat(file_path).st_uid).pw_name, getgrgid(os.stat(file_path).st_gid).gr_name, os.stat(file_path).st_size, datetime.fromtimestamp(os.stat(file_path).st_ctime), datetime.fromtimestamp(os.stat(file_path).st_atime), datetime.fromtimestamp(os.stat(file_path).st_mtime)]
                csv_writer.writerow(file_info)
                file_paths.append(file_path)
        csvfile.close()
    return file_paths


def get_files_test(directory):
    for root, dirs, files in os.walk(directory):
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
