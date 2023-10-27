class Solution(object):
    def simplifyPath(self, path):
        stack = []
        pa = ""
        for x in path + "/":
            if x == "/":
                if pa == "..":
                    if stack:
                        stack.pop()
                elif pa != "" and pa !=".":
                    stack.append(pa)
                pa = ""
            else:
                pa += x

        return "/" + "/".join(stack)
