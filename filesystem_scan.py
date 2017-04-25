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
import csv
import sys
from datetime import datetime
from pwd import getpwuid
from grp import getgrgid


time_now = datetime.now()
timestamp = '%s' % (time_now.strftime('%Y_%m_%d_%H:%M:%S'),)
start_directory = '/home/bipin/Workspace'
scan_report_dir = os.path.join(os.getcwd(), 'temp')

def main():
    if os.path.exists(start_directory):
        print 'Starting the Filesystem Scanning Configured Starting directory is : %s' % start_directory
        print "It will take a long time to complete large filesystems, seat tight"
        user_dir(start_directory)
        print "Scanning completed!!!!"
    else:
        print "Parent Directory to Start scan from, does not Exists. Exiting!!!"
        sys.exit()


def user_dir(parent_dir):
    child_dirs = os.listdir(parent_dir)
    for child_dir in child_dirs:
        if os.path.exists(scan_report_dir):
            scan_report = os.path.join(scan_report_dir, '%s_scan_report_%s.csv' % (child_dir, timestamp))
            child_dir_path = os.path.join(parent_dir, child_dir)
            get_files(child_dir_path, scan_report)
        else:
            print "Scan Report Directory does not exists so Exiting!!"
            sys.exit()


def get_files(directory, scan_report):
    with open(scan_report, 'wb') as csvfile:
        field_names = ['Directory', 'No of Files', 'File name', 'UID', 'GID', 'File Size', 'Creation Time', 'Access Time', 'Modification Time']
        csv_writer = csv.writer(csvfile, delimiter=',', lineterminator='\n')
        csv_writer.writerow(field_names)
        for root, dirs, files in os.walk(directory):
            directory_info = [root, len(files), '', getpwuid(os.stat(root).st_uid).pw_name, getgrgid(os.stat(root).st_gid).gr_name, os.stat(root).st_size, datetime.fromtimestamp(os.stat(root).st_ctime), datetime.fromtimestamp(os.stat(root).st_atime), datetime.fromtimestamp(os.stat(root).st_mtime)]
            csv_writer.writerow(directory_info)
            for filename in files:
                file_path = os.path.join(root, filename)
                if os.path.isfile(file_path):
                    file_info = ['', '', file_path, getpwuid(os.stat(file_path).st_uid).pw_name, getgrgid(os.stat(file_path).st_gid).gr_name, os.stat(file_path).st_size, datetime.fromtimestamp(os.stat(file_path).st_ctime), datetime.fromtimestamp(os.stat(file_path).st_atime), datetime.fromtimestamp(os.stat(file_path).st_mtime)]
                    csv_writer.writerow(file_info)
        csvfile.close()


if __name__ == '__main__':
    main()
