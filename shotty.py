# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 13:32:26 2018

@author: Jim
"""

import boto3

if __name__ == '__main__':
    session = boto3.Session(profile_name='shotty')
    ec2 = session.resource('ec2')

    for i in ec2.instances.all():
        print(i)
