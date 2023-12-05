class Solution(object):
    def restoreString(self, s, indices):
          
    # Character array to form final string
        mystr = [''] * len(s)

        # Do what the question says
        for i in range(len(s)):
            mystr[indices[i]] = s[i]

        # Return the restored string
        return ''.join(mystr)
