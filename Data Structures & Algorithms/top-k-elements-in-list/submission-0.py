class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count_dict = {}
        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1

        bucket = {}
        for i in range(1, len(nums)+1):
            bucket[i] = []

        for key in count_dict:
            count = count_dict[key]
            bucket[count].append(key)

        output = []
        for i in range(len(nums), 0, -1):
            if len(output) == k:
                break

            if bucket[i] != []:
                for num in bucket[i]:
                    output.append(num)
                    
                    if len(output) == k:
                        break
        return output