# 819. Most Common Word
# Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.
#
# The words in paragraph are case-insensitive and the answer should be returned in lowercase.
#
# Example 1:
#
# Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
# Output: "ball"
# Explanation:
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"),
# and that "hit" isn't the answer even though it occurs more because it is banned.
#
# Example 2:
#
# Input: paragraph = "a.", banned = []
# Output: "a"


# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
# for c in "!?',;.":
#     paragraph = paragraph.replace(c, " ")
# words = paragraph.lower().split()
# print(words)
# d ={}
# banned = set(banned)
# print(banned)
# for word in words:
#     if word not in banned:
#         if word not in d:
#             d[word] =1
#         else:
#             d[word]+=1
# print(d)
# print(max(d, key=d.get))


class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        for c in ",.!?':;":
            paragraph = paragraph.replace(c," ")
        words = paragraph.lower().split()
        d ={}
        banned = set(banned)
        for word in words:
            if word not in banned:
                if word not in d:
                    d[word] = 1
                else:
                    d[word]+=1
        return max(d, key=d.get)

