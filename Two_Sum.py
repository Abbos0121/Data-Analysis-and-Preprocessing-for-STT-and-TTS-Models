def two_sum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[num] = i
    return None

# Пример использования
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # Ожидаемый результат: [0, 1]
