from collections import deque
def solution(s):
    arr = list(s)
    q = deque()
    for c in arr:
        if c == "(":
            q.append("(")
        else:
            if not q:
                return False
            q.pop()
    return not q