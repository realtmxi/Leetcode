# 第四范式面试
# implement merge sort
def merge_sort(lst):
    if len(lst) > 1:
        # find out the middle of the list
        mid = len(lst) // 2
        # divide the list into two parts
        left = lst[:mid]
        right = lst[mid:]
        # merge the left sublist and the right sublist
        merge_sort(left)
        merge_sort(right)
        return merge(left, right)
    # len(lst) == 1
    else:
        return lst


def merge(left, right):
    """
    merge the given left list and the right list into a sorted list
    """
    lst = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            lst.append(left[i])
            i += 1
        # left[i] >= right[j]
        else:
            lst.append(right[j])
            j += 1
    if i == len(left):
        lst.extend(right[j:])
    if j == len(right):
        lst.extend(left[i:])
    return lst


# Given a string, delete the first k elements in lexi order, return remaining.

def bucket_sort(lst):
    """
    Given a list, sort it in O(n) time by bucket sort.
    """
    # find out the max element of the given list
    size = len(lst) / max(lst)
    # initialize an empty bucket
    bucket = []
    for _ in range(len(lst)):
        bucket.append([])
    # throw corresponding element of the list into the bucket
    for i in range(len(lst)):
        if (lst[i] / size) != len(lst):
            (lst[i] / size).append(lst[i])
        else:
            bucket[len(lst)].append(lst[i])



def delete(k, lst):
    temp_1 = lst
    bucket_sort(lst) # O(n)
    temp_2 = lst[k:] # n-k
    new = []
    for _ in temp_1:
        if _ in temp_2: # if O(1) \Rightarrow O(n)
            new.append(_)
    return new





if __name__ == "__main__":


