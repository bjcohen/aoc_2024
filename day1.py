import collections

if __name__ == "__main__":
    with open("day1.txt") as f:
        nums = [line.split("   ") for line in f]
    nums1 = [int(line[0]) for line in nums]
    nums2 = [int(line[1]) for line in nums]
    dist = 0
    for n1, n2 in zip(sorted(nums1), sorted(nums2)):
        dist += abs(n1 - n2)
    print(dist)
    counts2 = collections.Counter(nums2)
    s_score = 0
    for n1 in nums1:
        s_score += n1 * counts2[n1]
    print(s_score)
