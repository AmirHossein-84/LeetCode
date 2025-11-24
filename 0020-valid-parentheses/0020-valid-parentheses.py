class Solution:
    def isValid(self, s: str) -> bool:
        dict = {'(':')', '[':']','{':'}',}
        opens = "([{"
        close = ")]}"
        order = []
        for i in s:
            if i in dict.keys():
                order.append(i)
            else:
                if order:
                    if dict[order[-1]] == i:
                        order.pop()
                    elif dict[order[-1]] != i:
                        return False
                else:
                    return False
        return True if not order else False