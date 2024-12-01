import collections
import math

if __name__ == "__main__":
    with open("day1.txt") as f:
        nums = [l.split("   ") for l in f]
    nums1 = [int(l[0]) for l in nums]
    nums2 = [int(l[1]) for l in nums]
    dist = 0
    for n1, n2 in zip(sorted(nums1), sorted(nums2)):
        dist += abs(n1 - n2)
    print(dist)
    counts2 = collections.Counter(nums2)
    s_score = 0
    for n1 in nums1:
        s_score += n1 * counts2[n1]
    print(s_score)
