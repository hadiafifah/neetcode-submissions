class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        result = 0

        left = 0
        maxF = 0

        # Logic
        # create a counter for each letter in the string
        # Get the max frequency between the current max and the current letter
        # if the window size - max frequency is more than k
        # we increment left and decrement the counter until it is smaller than k
        # result is just max length, or the highest frequency we've had so far
        
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            maxF = max(maxF, count[s[right]])

            while (right - left + 1) - maxF > k:
                count[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)

        return result