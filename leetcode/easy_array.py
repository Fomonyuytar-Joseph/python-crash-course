def containsDuplicate(nums:list[int]):
    sort_nums = nums.sort()

    for index in range(0,len(sort_nums)):
        if sort_nums[index] == sort_nums[index + 1]:
            return True

    return False

def contains(nums:list[int]):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)


        # or I could still do return  len(seen) < len(nums)

    return False





# def two_sums(nums:list[int], target:int):
#     num_Map = {}
#     for index in range(0, len(nums)):
#         cur_num = nums[index]
#         difference = target - cur_num


#         if difference in num_Map:
#             return [num_Map[difference] , index]

#         num_Map[cur_num] = index


# print(two_sums(nums=[2, 7,11,15] , target=9))