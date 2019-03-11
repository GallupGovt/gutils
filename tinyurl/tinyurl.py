#!/usr/local/Cellar/python/3.6.5/bin
# -*- coding: utf-8 -*-
import argparse
import pandas as pd
import os
import requests


def run(args_dict):
    # define base url for tinyurl.com
    URL = 'http://tinyurl.com/api-create.php'

    # read in data
    links = pd.read_csv(args_dict['data'], sep=None, engine='python')

    # iterate through each link
    tinys = [requests.get(URL, params={'url': link}).text for link in
             links['Link']]

    # match tinyurls to data
    links['tinyurl'] = tinys

    # write to disk
    fpath = os.path.splitext(args_dict['data'])
    links.to_csv('{}_tiny{}'.format(fpath[0], fpath[1]), index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run a series of URLs through '
                                     'a link shortening program.')
    parser.add_argument('-d', '--data', required=True, help='Path/name of file '
                        'with URLs to shorten.')
    args_dict = vars(parser.parse_args())

    run(args_dict)
