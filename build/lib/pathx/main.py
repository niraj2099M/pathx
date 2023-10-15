"""
This module converts a WSL path into windows path and vice versa.

Only work for WSL paths in drive paths in '/mnt/[drives]'. 
These files are in windows drives.
"""

import string
#import argparse

#parser = argparse.ArgumentParser()
#parser.add_argument('--arg', help='The argument to pass to the function')
#ipath = parser.parse_args()


def wsl_win(path):
    """
    Converts a WSL path to windows path
    """
    path_split=path.split('/')
    #print(path_split)

    drive=path_split[2]
    drive=drive+':\\'

    cut_path=path_split[3:]
    #print(cut_path)
    cut_path_joined='\\'.join(cut_path) 
    
    return (drive+cut_path_joined)





def win_wsl(path):
    """
    Converts a windows path to WSL path
    """

    path_split=path.split('\\')
    #print(path_split)

    drive=path_split[0][0]
    drive=drive.swapcase()
    path_making="/mnt/"+drive+"/"

    path_split=path_split[1:]
    cut_path_joined='/'.join(path_split)

    return path_making+cut_path_joined



import argparse
import sys

def main_function():
    parser = argparse.ArgumentParser(description="Your script description")
    parser.add_argument("input_path", help="Path to the file")
    args = parser.parse_args(sys.argv[1:])  # Exclude the script name from parsing
    # Now you can use args.input_file in your function
    print(f"Processing {args.input_path}")
    print()
    path_converter(args.input_path)





def path_converter(ipath):
    
    if ipath[0]=='/':
        result=wsl_win(ipath)
        print(f'WSL to windows path: {result}')
        print()
        print('Use "spaced folder" for cd in CLIs using these paths')
    elif ipath[0] in string.ascii_letters:
        result=win_wsl(ipath)
        print(f'windows path to WSL: {result}')
        print()
        print('Use "spaced folder" for cd in CLIs using these paths')
    else:
        print("""Invalid path!!
Please enter a valid 'absolute' path.""")

if __name__=='__main__':
    inp=input("Enter a path >>")
    path_converter(inp)





