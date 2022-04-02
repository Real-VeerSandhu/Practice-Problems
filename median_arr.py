nums1 = [1,2]
nums2 = [3,4]

def solution(nums1, nums2):
    full = (nums1 + nums2)
    full.sort()

    n = (len(full) + 1) / 2
    if n % 1 == 0:
        return full[int(n-1)]
    else:
        return (full[int(n+0.5-1)] + full[int(n-0.5-1)])/2

print(solution(nums1, nums2))