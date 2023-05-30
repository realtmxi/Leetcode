# 阿里巴巴饿了么机器学习推荐算法 实习
def quicksort(lst):
  # base case
  if len(lst) == 1:
    return lst
  # choose a pivot
  pivot = lst[len(lst) // 2]

  # left list
  left = [_ for _ in lst if _ < pivot]
  # right list
  right = [_ for _ in lst if _ > pivot]
  mid = [_ for _ in lst if _ == pivot]

  return quicksort(left) + middle + quicksort(right)

print(quicksort([3,1,2,5,7]))


def binary_search(lst, target):
  a = 0
  b = len(lst) - 1

  while a <= b:
    mid = (a + b) // 2

    c = lst[mid]
    if c == target:
      return mid
    elif c > target:
      b = mid - 1
    else:
      a = mid + 1
    
