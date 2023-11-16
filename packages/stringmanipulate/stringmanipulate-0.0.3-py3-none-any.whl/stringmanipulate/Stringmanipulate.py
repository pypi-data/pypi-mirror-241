from typing import List
import collections

# Params: string list;
# Functionality: return list in which strings are anagrams, then collected in a whole list as result


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    ans = collections.defaultdict(list)
    for s in strs:
        # Expanded count to accommodate both lowercase and uppercase letters
        count = [0] * (26 + 26)  # 26 lowercase + 26 uppercase
        for c in s:
            if c.islower():
                index = ord(c) - ord('a')
            else:
                index = 26 + ord(c) - ord('A')
            count[index] += 1
            count[index] += 0 # just for test
        ans[tuple(count)].append(s)
    return list(ans.values())


# Params: 2 strings
# Functionality: return boolean checking if s2 contains the permuted version of s1


def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False

    s1Count, s2Count = [0] * 26, [0] * 26
    for i in range(len(s1)):
        s1Count[ord(s1[i]) - ord("a")] += 1
        s2Count[ord(s2[i]) - ord("a")] += 1

    matches = 0
    for i in range(26):
        matches += 1 if s1Count[i] == s2Count[i] else 0

    l = 0
    for r in range(len(s1), len(s2)):
        if matches == 26:
            return True

        index = ord(s2[r]) - ord("a")
        s2Count[index] += 1
        if s1Count[index] == s2Count[index]:
            matches += 1
        elif s1Count[index] + 1 == s2Count[index]:
            matches -= 1

        index = ord(s2[l]) - ord("a")
        s2Count[index] -= 1
        if s1Count[index] == s2Count[index]:
            matches += 1
        elif s1Count[index] - 1 == s2Count[index]:
            matches -= 1
        l += 1
    return matches == 26

# Params: 2 strings
# Functionality: return the longest longest substring without repeating chars



def lengthOfLongestSubstring(s: str) -> int:
    charSet = set()
    l = 0
    res = 0

    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        res = max(res, r - l + 1)
    return res

# Params: 1 string
# Functionality: return the decoded string 3[a] becomes aaa for instance


def decodeString(s: str) -> str:
    stack = []

    for char in s:
        if char != "]":
            stack.append(char)
        else:
            sub_str = ""
            while stack[-1] != "[":
                sub_str = stack.pop() + sub_str
            stack.pop()

            multiplier = ""
            while stack and stack[-1].isdigit():
                multiplier = stack.pop() + multiplier

            stack.append(int(multiplier) * sub_str)

    return "".join(stack)
