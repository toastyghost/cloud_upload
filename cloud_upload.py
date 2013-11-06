#!/bin/env python

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-container')
parser.add_argument('-filename')
args = parser.parse_args()
del parser

import os.path
filename_tail = os.path.split(args.filename)[1]

import cloudfiles
conn = cloudfiles.get_connection('[REMOVED]', '[REMOVED]')
containers = conn.get_all_containers()
container = containers[containers.index(args.container)]
new_object = container.create_object(filename_tail)
new_object.load_from_filename(args.filename)
