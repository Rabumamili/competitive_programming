class Solution(object):
    def compress(self,chars):
         
        read = write = 0
        count = 1

        while read < len(chars):
            if read + 1 == len(chars) or chars[read] != chars[read + 1]:
                chars[write] = chars[read]
                write += 1

                if count > 1:
                    for digit in str(count):
                        chars[write] = digit
                        write += 1

                count = 1
            else:
                count += 1

            read += 1

        return write
