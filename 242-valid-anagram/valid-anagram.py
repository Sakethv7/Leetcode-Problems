class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #compare 2 strings for anagram: t is an anagram of s if if rearranging the words of string s forms the other string t
       # sort the strings first 
        # first check if the 2 strings are of the same size or else 
        if (len(s)!=len(t)):
            return False  #O(1) to check a string length

        ## Solution using sorted in built function
        # sorted_s = sorted(s) #O(nlogn) to sort a string, so its better to check the string length first
        # sorted_t = sorted(t)
        # return (sorted_s == sorted_t) #will return either true or false as it == makes it a conditional statement


        ## Sorting solution using Hashmap

        #creating 2 hashmaps to iterate with 
        countS, countT = {}, {}
 # populating the hash map with key value pairs from the s, t strings
        for i in range(len(s)):  
            countS[s[i]]= 1 + countS.get(s[i], 0) 
#using get function here to give 0 and to the value if there is nothing at s[i] or else there will be a key error
            countT[t[i]]= 1 + countT.get(t[i], 0)

        # iterating char in countS to check 
        for c in countS: 
            #if c in countS hash map is not the same as countT return false 
            if countS[c] != countT.get(c, 0): 
                return False
        return True