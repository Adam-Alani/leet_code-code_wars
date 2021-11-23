def findNumbers(nums):
  count = 0
  for num in nums:
    if len(str(num)) % 2 == 0:
      count += 1
  return count

print(findNumbers([12,345,2,6,7896]))