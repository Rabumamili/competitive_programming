class Solution(object):


    def checkInclusion(self, s1, s2):

        len_s1 = len(s1)
        len_s2 = len(s2)

        if len_s1 > len_s2:
            return False

        counter_s1 = Counter(s1)
        counter_s2 = Counter(s2[:len_s1])

        if counter_s1 == counter_s2:
            return True

        for i in range(len_s1, len_s2):
            counter_s2[s2[i]] += 1
            counter_s2[s2[i - len_s1]] -= 1

            if counter_s2[s2[i - len_s1]] == 0:
                del counter_s2[s2[i - len_s1]]

            if counter_s1 == counter_s2:
                return True

        return False


    
