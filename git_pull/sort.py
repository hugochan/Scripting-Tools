#!usr/bin/env/python

import sys

def sort(in_file):
    names = []
    usernames = []
    try:
        with open(in_file, 'r') as f:
            for i in f:
                name, username = i.rstrip('\n').split(',')
                name = name.strip(' ')
                username = username.strip(' ')
                names.append(name)
                usernames.append(username)
    except Exception as e:
        print e
        sys.exit()
    f.close()
    sort_names = sorted(zip(names, usernames), key=lambda d:d[0].split(' ')[-1])
    return sort_names

def create_file(in_file):
    try:
        with open(in_file, 'w+') as f2:
            for each in sort_names:
                f2.write('%s, %s\n'%(each[0], each[1]))
    except Exception as e:
        print e
        sys.exit()
    f2.close()

if __name__ == '__main__':
    try:
        in_file = sys.argv[1]
    except Exception as e:
        print e
        sys.exit()
    sort_names = sort(in_file)
    print sort_names
    create_file('copy-%s'%in_file)
