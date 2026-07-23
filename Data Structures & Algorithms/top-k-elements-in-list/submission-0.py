class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            frequency = {}
            for number in nums:
                if number not in frequency:
                    frequency[number] = 1
                else:
                    frequency[number] += 1
            
            result = []
            for i in range(k):
                max_number = max(frequency, key=frequency.get)
                result.append(max_number)
                del frequency[max_number]
            
            return result


        