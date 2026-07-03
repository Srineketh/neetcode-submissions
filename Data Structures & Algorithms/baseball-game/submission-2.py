class Solution:
    def calPoints(self, operations: List[str]) -> int:

        stack = []

        def peek():
            return stack[-1]
        def pop():
            stack.pop()
        def push(x):
            stack.append(x)
        def stack_sum():
            ssum = 0
            while len(stack) !=0:
                ssum += peek()
                pop()
            return ssum
        for i in operations:
            if i == "+":
                first = peek()
                pop()
                second = peek()
                push(first)
                push(first + second)
            elif i == "D":
                push(peek()*2)
            elif i == "C":
                pop()
            else:
                push(int(i))
        return stack_sum()
