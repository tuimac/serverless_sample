#!/usr/bin/env python3

import os
import subprocess

def executeHandler():
    os.chdir('src')
    command = ['docker', 'run', '--rm', '-v', os.getcwd() + ':/var/task:ro,delegated', '--network', 'database_default', 'lambci/lambda:python3.8', 'lambda_function.lambda_handler']
    subprocess.run(command)
    os.chdir('..')

def database(handler):
    os.chdir('database')
    if handler == 'start':
        command = ['docker-compose', 'up', '-d']
    elif handler == 'stop':
        command = ['docker-compose', 'stop']
    else:
        print('There is no handler like that.', file=sys.stderr)
    subprocess.run(command)
    os.chdir('..')

if __name__ == '__main__':
    database('start')
    executeHandler()
    database('stop')
