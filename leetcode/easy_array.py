def two_sums(nums:list[int], target:int):
    num_Map = {}
    for index in range(0, len(nums)):
        cur_num = nums[index]
        difference = target - cur_num


        if difference in num_Map:
            return [num_Map[difference] , index]

        num_Map[cur_num] = index


print(two_sums(nums=[2, 7,11,15] , target=9))