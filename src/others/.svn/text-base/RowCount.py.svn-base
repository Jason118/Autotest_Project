# -*- coding: utf-8 -*-

import os


def count_line(path):
    count = 0
    for root, dirs, files in os.walk(path):
        # print("Root = ", root, "dirs = ", dirs, "files = ", files)
        for fi in files:
            if fi[-3:] == '.py':
                with open(root + '/' + fi, 'r') as f:
                    for line in f:
                        if line.strip() == '':
                            continue
                        elif line.lstrip()[0] == '#':
                            continue
                        else:
                            count += 1
    return count

if __name__ == '__main__':
    path = 'D:/zhigou/zhigou_framework/'
    path1 = 'D:/'

    print count_line(path)
