# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:

#         l, r = 0, 0

#         lists1 = list(s1)
#         lists2 = list(s2)

#         while l <= len(s2) - len(s1):
#             if lists2[r] in lists1:
#                 lists1.remove(lists2[r])
#                 if len(lists1) == 0:
#                     return True
#                     break
#                 else:
#                     r += 1
#             else:
#                 lists1 = list(s1)
#                 l += 1
#                 r = l
#         return False


# s1 = "ab"  # True
# s2 = "eidbaooo"

# s1 = "ab" # False
# s2 = "eidboaoo"

# s1 = "adc" # True
# s2 = "dcda"


# Output: false

# sol = Solution()
# print(sol.checkInclusion(s1, s2))


### try two


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        while s1[0] in list(s2):

            lists1 = list(s1)
            lists2 = list(s2)

            for letter in lists1[1:]:

                l, r = 1, 1

                if letter == lists2.index(s1[0] - l):
                    l += 1
                    continue

                elif letter == lists2.index(s1[0] + r):
                    r += 1
                    continue

                else:
                    lists2.remove(s1[0])
                    l, r = 1, 1

        return False


# s1 = "ab"  # True
# s2 = "eidbaooo"

# s1 = "ab" # False
# s2 = "eidboaoo"

s1 = "adc"  # True
s2 = "dcda"


# Output: false

sol = Solution()
print(sol.checkInclusion(s1, s2))
