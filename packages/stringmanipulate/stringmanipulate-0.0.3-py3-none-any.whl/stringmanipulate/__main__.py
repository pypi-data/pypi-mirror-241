# __main__.py
import argparse
from stringmanipulate.Stringmanipulate import groupAnagrams, checkInclusion, decodeString,lengthOfLongestSubstring

def main():
    parser = argparse.ArgumentParser(description='String Manipulation operations.')
    parser.add_argument('operation', choices=['anagrams', 'inclusion', 'longest_substring', 'decode_string'], help='The operation to perform.')
    parser.add_argument('--strings', nargs='+', help='A list of strings for the operation.')
    parser.add_argument('--file', type=str, help='A file path to read strings from.')
 
    args = parser.parse_args()

    if args.file:
        with open(args.file, 'r') as f:
            strings = f.read().splitlines()
    elif args.strings:
        strings = args.strings
    else:
        raise ValueError("No strings provided for operation.")


    if args.operation == 'anagrams':
        print(groupAnagrams(strings))
    elif args.operation == 'inclusion':
        if len(strings) != 2:
            raise ValueError("Inclusion operation requires exactly two strings.")
        print(checkInclusion( strings[0], strings[1]))
    elif args.operation == 'longest_substring':
        for string in strings:
            print(lengthOfLongestSubstring(string))
    elif args.operation == 'decode_string':
        for string in strings:
            print(decodeString( string))

if __name__ == '__main__':
    main()
