#!/usr/bin/env python

import argparse
import os
import sys
            
def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.
    
    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
    It must be "yes" (the default), "no" or None (meaning
    an answer is required of the user).
    
    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)
    
    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")
            
def inplace_change(filename, old_string, new_string):
    # Safely read the input filename using 'with'
    with open(filename) as f:
        s = f.read()
        if old_string not in s:
            # print '"{old_string}" not found in {filename}.'.format(**locals())
            return

    # Safely write the changed content, if found in the file
    with open(filename, 'w') as f:
        print 'Changing "{old_string}" to "{new_string}" in {filename}'.format(**locals())
        s = s.replace(old_string, new_string)
        f.write(s)

def inplace_change_inform(filename, old_string, new_string):
    # Safely read the input filename using 'with'
    with open(filename) as f:
        s = f.read()
        if old_string not in s:
            # print '"{old_string}" not found in {filename}.'.format(**locals())
            return

    print 'Changing "{old_string}" to "{new_string}" in {filename}'.format(**locals())

        
def main():
        parser = argparse.ArgumentParser()
        parser.add_argument("string1", help="string to be replaced")
        parser.add_argument("string2", help="replacement string")
        args = parser.parse_args()

        FilesInDir = [fname for fname in os.listdir("./") if not os.path.isdir(fname)]

        print "the following actions will be performed:\n"
        
        for File in FilesInDir:
            inplace_change_inform(File, args.string1, args.string2)

        if query_yes_no("\nproceed?"):
            for File in FilesInDir:
                inplace_change(File, args.string1, args.string2)


if __name__ == "__main__":
        main()
