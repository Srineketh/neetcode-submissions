class Solution:
    def calPoints(self, operations: List[str]) -> int:
        valid = []
        operation_map = {
            "+" : lambda: valid.append(valid[-1] + valid[-2]),
            "D": lambda: valid.append(valid[-1]*2),
            "C" : lambda: valid.pop(-1)
        }
        for i in operations:
            if i not in operation_map:
                valid.append(int(i))
            else:
                operation_map[i]()
        return sum(valid)
