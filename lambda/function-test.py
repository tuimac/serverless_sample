#!/usr/bin/env python3

import os
import subprocess
import traceback
import sys

def executeHandler(functionDir):
    os.chdir(functionDir)
    command = ['docker', 'run', '--rm', '-v', os.getcwd() + ':/var/task:ro,delegated', '--network', 'lambda', 'lambci/lambda:python3.8', 'lambda_function.lambda_handler']
    subprocess.run(command)
    os.chdir('..')

def database(handler):
    os.chdir('../docker')
    if handler == 'start':
        command = ['docker-compose', 'up', '-d']
    elif handler == 'stop':
        command = ['docker-compose', 'stop']
    else:
        print('There is no handler like that.', file=sys.stderr)
    subprocess.run(command)
    os.chdir('../lambda')

if __name__ == '__main__':
    try:
        if len(sys.argv) != 2:
            print('usage: ./function-test.py <function directory>\n', file=sys.stderr)
            raise NotImplementedError
        if os.path.exists(sys.argv[1]) is False:
            print('usage: ./function-test.py <function directory>\n', file=sys.stderr)
            raise FileNotFoundError
        database('start')
        executeHandler(sys.argv[1])
        database('stop')
    except:
        #traceback.print_exc()
        sys.exit(1)
