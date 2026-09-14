def majority_element(nums):
    count = 0
    res = None
    for n in nums:
        if count == 0:
            res = n
        count += 1 if n == res else -1
    return res

if __name__ == "__main__":
    print(majority_element([2,2,1,1,1,2,2]))
