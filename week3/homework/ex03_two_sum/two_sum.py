def two_sum(nums, target):
    hashmap = {}
    for idx, num in enumerate(nums):
        need = target - num
        if need in hashmap:
            return [hashmap[need], idx]
        hashmap[num] = idx
    return []

if __name__ == "__main__":
    # 测试样例
    print(two_sum([2,7,11,15],9))
