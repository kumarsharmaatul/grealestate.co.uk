'''
1. Group Anagrams
Problem:
Given a list of strings, group words that are anagrams of each other. For example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

Solution:
I used a hash map (dictionary) to group the anagrams. 
By sorting each string, we obtain a consistent key for all words that are anagrams of each other. 
We then append the original words to the list corresponding to that sorted key.'''


from collections import defaultdict

def groupAnagrams(strs):
    anagrams = defaultdict(list)
    
    for word in strs:
        # Sort the word to create a common key for anagrams
        sorted_word = tuple(sorted(word))
        anagrams[sorted_word].append(word)
        
    return list(anagrams.values())

# Test
print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))