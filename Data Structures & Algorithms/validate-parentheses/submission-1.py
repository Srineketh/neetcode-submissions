class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        def peek():
            if len(stack) > 0:
                return stack[-1]
            return None
        def pop():
            stack.pop()
        def push(x):
            stack.append(x)

        paran_map = {
            "[" : "]",
            "{" : "}",
            "(" : ")"
        }
        for i in s:
            current = peek()
            if i == paran_map.get(current):
                pop()
            else:
                push(i)
        if len(stack) > 0: 
            return False
        else: 
            return True