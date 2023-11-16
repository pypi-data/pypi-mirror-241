# stringmanipulate

![Build Status](https://github.com/software-students-fall2023/3-python-package-exercise-team-dominators-1/actions/workflows/build.yaml/badge.svg)

## Description

This Python package provides a collection of string manipulation functions, including grouping anagrams, checking string inclusions, decoding strings, and finding the length of the longest substring without repeating characters.

## Installation

To install this package, run the following command in your terminal:

```bash
pip install stringmanipulate
```
## Usage

### Group Anagrams
`groupAnagrams(strs: List[str]) -> List[List[str]]`: This function takes a list of strings and groups anagrams together. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. It returns a list where each element is a list of anagrams.

```python
from stringmanipulate import groupAnagrams
# Example usage:
print(groupAnagrams(["bat", "tab", "eat", "tea", "tan", "nat"]))  
# Output: [["bat", "tab"], ["eat", "tea"], ["tan", "nat"]]
```
### Check Inclusion
`checkInclusion(s1: str, s2: str) -> bool`: This function checks if one string (s1) is a permutation of any substring of another string (s2). It returns True if any permutation of s1 can be found as a substring in s2, otherwise False.

```python
from stringmanipulate import checkInclusion
# Example usage:
print(checkInclusion("ab", "eidbaooo"))  
# Output: True
```
### Length of Longest Substring
`lengthOfLongestSubstring(s: str) -> int`: This function finds the length of the longest substring without repeating characters in a given string (s). It returns the maximum length of such substrings.

```python
from stringmanipulate import lengthOfLongestSubstring
# Example usage:
print(lengthOfLongestSubstring("abcabcbb"))  
# Output: 3
```
### Decode String
`decodeString(s: str) -> str`: This function decodes a string that follows a specific pattern where k[encoded_string] indicates that the encoded_string within the square brackets should be repeated k times. It returns the fully decoded string.

```python
from stringmanipulate import decodeString
# Example usage:
print(decodeString("3[a]2[bc]"))  
# Output: "aaabcbc"
```

## Contributing

To contribute to this project, please follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/software-students-fall2023/3-python-package-exercise-team-dominators-1.git
   ```
2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  
   ```
3. Install dependencies using `Pipfile`:
   ```bash
   pip install pipenv
   pipenv install
   ```
4. Build and test the package:
   ```bash
   python setup.py sdist bdist_wheel
   python -m unittest discover
   ```

## Team

- [Steve Hai](https://github.com/Hyteve)
- [Ashley Luo](https://github.com/luoashley)
- [Ethan Sha](https://github.com/EthanSha111)
- [Merry Cui](https://github.com/merrylearninggithub)

## PyPI

This package is also available on PyPI:

[stringmanipulate](https://pypi.org/project/stringmanipulate/0.0.2/)
