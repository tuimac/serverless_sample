#!/usr/bin/env python3

import boto3
import zipfile
import os
import sys
import traceback

def zipSrcDir(path, filename):
    try:
        currentdir = os.path.dirname(os.path.realpath(__file__))
        os.chdir(path)
        zipf = zipfile.ZipFile(currentdir + '/' + filename, 'w', zipfile.ZIP_DEFLATED)
        for root, dirs, files in os.walk('.'):
            for file in files:
                zipf.write(os.path.join(root, file))
        zipf.close()
        os.chdir(currentdir)
    except Exception as e:
        raise e

def createFunction(client, iamRole, zipFile):
    try:
        response = client.create_function(
            FunctionName = 'booksearch',
            Runtime = 'python3.8',
            Role = iamRole,
            Handler = 'lambda_handler',
            Code = { 'ZipFile': open(zipFile, 'rb').read() }
        )
        print(response['FunctionArn'])
    except Exception as e:
        raise e

if __name__ == '__main__':
    srcdir = '../src/backend/book_get/'
    zipFileName = 'src.zip'

    if len(sys.argv) != 2:
        print('usage: ./createLambdaFunction.py <IAM role ARN>')
        sys.exit(1)
    iamRoleArn = sys.argv[1]

    try:
        client = boto3.client('lambda')
        zipSrcDir(srcdir, zipFileName)
        createFunction(client, iamRoleArn, zipFileName)
    except:
        traceback.print_exc()
    finally:
        os.remove(zipFileName)
