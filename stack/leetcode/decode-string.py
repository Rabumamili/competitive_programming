class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_num = 0
        decoded = ""

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == "[":
                stack.append((decoded, current_num))
                decoded = ""
                current_num = 0
            elif char == "]":
                prev_str, num = stack.pop()
                decoded = prev_str + decoded * num
            else:
                decoded += char

        return decoded

                            


                        


                    


                    
