#!/usr/bin/env python3

import os
import subprocess

def changeDir(execDir):
    srcdir = os.path.dirname(os.path.realpath(__file__)) + '/' + execDir
    os.chdir(srcdir)

def executeHandler():
    command = 'docker run --rm -v ' + os.getcwd() + ':/var/task:ro,delegated lambci/lambda:python3.8 lambda_function.lambda_handler'
    subprocess.run(command)

if __name__ == '__main__':
    changeDir('src')
    executeHandler()
    changeDir('')
