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

def createConfig(subnet, securitygroup, iamrole):
    try:
        config = {}
        client = boto3.client('ec2')
        config['subnetId'] = client.describe_subnets(
            Filters = [{'Name': 'tag:Name', 'Values': [subnet]}]
        )['Subnets'][0]['SubnetId']
        config['sgId'] = client.describe_security_groups(
            Filters = [{'Name': 'group-name', 'Values': [securitygroup]}]
        )['SecurityGroups'][0]['GroupId']

        resource = boto3.resource('iam')
        config['iamroleArn'] = resource.Role(iamrole).arn
        return config
    except Exception as e:
        raise e

def createFunction(config, zipFile):
    try:
        client = boto3.client('lambda')
        response = client.create_function(
            FunctionName = 'booksearch',
            Runtime = 'python3.8',
            Role = config['iamroleArn'],
            Handler = 'lambda_handler.lambda_handler',
            Code = { 'ZipFile': open(zipFile, 'rb').read() },
            VpcConfig = {
                'SubnetIds': [config['subnetId']],
                'SecurityGroupIds': [config['sgId']]
            }
        )
        print(response['FunctionArn'])
    except Exception as e:
        raise e

if __name__ == '__main__':
    srcdir = '../src/backend/book_get/'
    zipFileName = 'src.zip'
    subnet = 'VPN-Subnet-Private-01-a'
    securitygroup = 'default'
    iamrole = 'LambdaOnVPC'

    try:
        config = createConfig(subnet, securitygroup, iamrole)
        zipSrcDir(srcdir, zipFileName)
        createFunction(config, zipFileName)
    except:
        traceback.print_exc()
    finally:
        os.remove(zipFileName)
