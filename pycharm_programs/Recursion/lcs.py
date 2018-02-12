
def lcs(s1, s2):
    #base case
    if len(s1) == len(s2) == 0:
        return 0

    if s1[len(s1)-1] == s2[len(s2)-1]:
        return 1 + lcs(s1[:len(s1)-1], s2[:len(s2)-1])

    #recursion case
    max(lcs(s1,s2[:len(s2)-1]), lcs(s1,s2[:len(s2)-1]))