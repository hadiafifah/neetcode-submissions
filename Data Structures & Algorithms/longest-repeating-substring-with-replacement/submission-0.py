class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        left = 0
        maxf = 0

        # Logic
        # Create a counter for each letter as you go through the string
        # get the max frequency between either the current letter
        # or the previous max frequency
        # and while the length of the window - maxf > k
        # we slide the window left and decrease the size of the window
        # we also decrement the count of each letter taken out
        # as we decrease the size of the window
        # then we just get the size of the window
        
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            maxf = max(maxf, count[s[right]])

            while (right - left + 1) - maxf > k:
                count[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res                                                                          