#!/usr/bin/env python3

import boto3
import zipfile
import os
import traceback

def zipSrcDir(path, filename):
    try:
        zipf = zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED)
        for root, dirs, files in os.walk(path):
            for file in files:
                zipf.write(os.path.join(root, file))
        zipf.close()
    except Exception as e:
        raise e

if __name__ == '__main__':
    srcdir = '../src/backend/book_get'
    zipFileName = 'src.zip'
    try:
        client = boto3.client('lambda')
        zipSrcDir(srcdir, zipFileName)


    except:
        traceback.print_exc()

