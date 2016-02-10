#!/usr/bin/env/python

import sys
from subprocess import call

def git_pull(names, urls, workspace='work'):
    call(['mkdir', workspace])
    print "mkdir %s"%workspace
    print "git pull ..."
    for name, url in zip(names, urls):
        try:
            call(['mkdir', name], cwd=workspace)
            call(['git', 'init'], cwd='%s/%s'%(workspace, name))
            call(['git', 'pull', url, 'master'], cwd='%s/%s'%(workspace, name))
            print name, url
        except Exception as e:
            print e
            sys.exit()

def get_names_urls(in_file, hw_idx):
    names = []
    urls = []
    default_url = 'https://github.com/RPI-CSCI-2500-2016-Spring/assignment%s-%s.git'
    try:
        with open(in_file, 'r') as f:
            for i in f:
                name, username = i.rstrip('\n').split(',')
                name = name.strip(' ')
                username = username.strip(' ')
                if name == 'X':
                    continue
                names.append(name)
                urls.append(default_url%(hw_idx, username))
    except Exception as e:
        print e
        sys.exit()
    return [names, urls]

if __name__ == '__main__':
    try:
        in_file = sys.argv[1]
        hw_idx = int(sys.argv[2])
    except Exception as e:
        print e
        sys.exit()
    names, urls = get_names_urls(in_file, hw_idx)
    # print names
    # print urls
    git_pull(names, urls)

