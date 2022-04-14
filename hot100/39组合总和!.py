class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        if candidates[0] > target:
            return []

        def backtrace(candidates, target):
            for i in candidates:
                if combination != [] and i < combination[-1]:
                    continue
                combination.append(i)
                sum1 = sum(combination)
                if sum1 < target:
                    backtrace(candidates, target)
                    combination.pop()
                elif sum1 == target:
                    a = combination.copy()
                    result.append(a)
                    combination.pop()
                    break
                else:
                    combination.pop()
                    break

        combination = []
        result = []
        backtrace(candidates, target)

        return result


input = [2, 7, 6, 3, 5, 1]
result = Solution().combinationSum(input, 9)
print(result)
