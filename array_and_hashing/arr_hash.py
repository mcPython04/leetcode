
# Contains Duplicate (217)
# Time: O(n) Space: O(n)
def containsDuplicate(self, nums: List[int]) -> bool:
	
	# Create hashset
	hashset = set()
	
	# Loop through nums list
	for n in nums:
	
		# Basic Approach:
		# If value in list exists in set() return True
		# Else add value to set()
		if n in hashset:
			return True
		hashset.add(n)
	
	# No duplicates found -> return False
	return False
	

# Valid Anagram (242)
# Time: O(n) Space: O(n)
def isAnagram(self, s: str, t: str) -> bool:

	# If length of string != auto return False
	if len(s) != len(t):
		return False
	
	# Create hashmap of count
	countS, countT = {}, {}
	
	# Go through each str and count each occurence of letter
	for i in range(len(s)):
		countS[s[i]] = countS.get(s[i], 0) + 1
		countT[t[i]] = countT.get(t[i], 0) + 1
		
	# Compare the occurence of each str
	# Return False if diff
	for c in countS:
		if countS[c] != countT.get(c, 0):
			return False
			
	return True
	

# Two Sum (1)
# Time: O(n) Space: O(n)
def twoSUm(self, nums:  List[int], target: int) -> List[int]:
	map = {} # val -> index
	
	# Approach: Find the diff and see if diff is in map
	for i, n enumerate(nums):
		diff = target - n
		
		if diff in map:
			return [map[diff], i]

# Group Anagrams (49)
# Approach: Create hash map with occurence of letters as key (whole tuple) and the word as the value. Finally, simply return the values of the hash map
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        
        return res.values()
			
		# If not found add value and index pair into map
		map[n] = i
