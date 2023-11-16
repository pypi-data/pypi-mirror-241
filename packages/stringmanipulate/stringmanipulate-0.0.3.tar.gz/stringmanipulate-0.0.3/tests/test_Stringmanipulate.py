import pytest
from stringmanipulate.Stringmanipulate import groupAnagrams, checkInclusion, lengthOfLongestSubstring, decodeString


# groupAnagrams tests
def test_group_anagrams_empty():
    assert sorted(map(sorted, groupAnagrams([]))) == []


def test_group_anagrams_single():
    assert sorted(map(sorted, groupAnagrams(["abc"]))) == [["abc"]]


def test_group_anagrams_all_anagrams():
    assert sorted(map(sorted, groupAnagrams(["abc", "bca", "cab"]))) == [["abc", "bca", "cab"]]


def test_group_anagrams_mixed():
    result = groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    expected = [["bat"], ["eat", "tea", "ate"], ["tan", "nat"]]
    sorted_result = sorted([sorted(sublist) for sublist in result])
    sorted_expected = sorted([sorted(sublist) for sublist in expected])
    assert sorted_result == sorted_expected


def test_group_anagrams_case_sensitive():
    assert sorted(map(sorted, groupAnagrams(["abc", "bca", "Cba"]))) == [["Cba"], ["abc", "bca"]]


# checkInclusion tests
def test_check_inclusion_true():
    assert checkInclusion("ab", "eidbaooo") == True


def test_check_inclusion_false():
    assert checkInclusion("ab", "eidboaoo") == False


def test_check_inclusion_identical():
    assert checkInclusion("abc", "bca") == True


def test_check_inclusion_longer():
    assert checkInclusion("abc", "eidbaoooabc") == True


def test_check_inclusion_empty_s1():
    assert checkInclusion("", "eidbaooo") == True  # Assuming empty string is a permutation of any string


# lengthOfLongestSubstring tests
def test_length_of_longest_substring_simple():
    assert lengthOfLongestSubstring("abcabcbb") == 3


def test_length_of_longest_substring_single_char():
    assert lengthOfLongestSubstring("bbbbb") == 1


def test_length_of_longest_substring_empty():
    assert lengthOfLongestSubstring("") == 0


def test_length_of_longest_substring_alternating_chars():
    assert lengthOfLongestSubstring("ababab") == 2


def test_length_of_longest_substring_unique():
    assert lengthOfLongestSubstring("abcdefg") == 7


# decodeString tests
def test_decode_string_simple():
    assert decodeString("3[a]2[bc]") == "aaabcbc"


def test_decode_string_nested():
    assert decodeString("3[a2[c]]") == "accaccacc"


def test_decode_string_multiple_digits():
    assert decodeString("10[a]") == "a" * 10


def test_decode_string_complex():
    assert decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef"


def test_decode_string_empty():
    assert decodeString("") == ""
