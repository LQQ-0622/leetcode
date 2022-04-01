import collections


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        q = collections.deque()
        time = [-1] * n
        force = [[] for _ in range(n)]
        for i, f in enumerate(dominoes):
            if f != '.':
                q.append(i)
                time[i] = 0
                force[i].append(f)
        res = ['.'] * n
        while q:
            i = q.popleft()
            if len(force[i]) == 1:
                res[i] = f = force[i][0]
                ii = i + 1 if f == 'R' else i - 1
                if 0 <= ii < n:
                    t = time[i]
                    if time[ii] == -1:
                        q.append(ii)
                        time[ii] = t + 1
                        force[ii].append(f)
                    elif time[ii] == t + 1:
                        force[ii].append(f)
        return ''.join(res)

    def pushDominoes1(self, dominoes: str) -> str:
        dominoes = list(dominoes)
        n = len(dominoes)
        change_index = []
        for j in range(n):
            if dominoes[j] != '.':
                change_index.append(j)
        while change_index != []:
            del_list = []
            add_list = []
            for i in change_index:
                del_list.append(i)
                # if i == 0 or i == n - 1:
                #     del_list.append(i)
                if i == 1 and dominoes[i] == 'L' and dominoes[0] == '.':
                    dominoes[i - 1] = 'L'
                    # del_list.append(i)
                if i == n - 2 and dominoes[i] == 'R' and dominoes[n - 1] == '.':
                    dominoes[i + 1] = 'R'
                    # del_list.append(i)

                # if 1 < i <= n - 1 and dominoes[i] == 'L' and (i - 2 not in change_index or (
                #         i - 2 in change_index and dominoes[i - 2] != 'R')) and dominoes[i - 1] == '.':
                if 1 < i <= n - 1 and dominoes[i] == 'L' and dominoes[i - 1] == '.':
                    if (i - 2 not in change_index or (i - 2 in change_index and dominoes[i - 2] != 'R')) or \
                            (i - 1 not in change_index or (i - 1 in change_index and dominoes[i - 1] != 'R')):
                        dominoes[i - 1] = 'L'
                        add_list.append(i - 1)

                if 0 <= i < n - 2 and dominoes[i] == 'R' and dominoes[i + 1] == '.':
                    if (i + 2 not in change_index or (i + 2 in change_index and dominoes[i + 2] != 'L')) or \
                            (i + 1 not in change_index or (i + 1 in change_index and dominoes[i + 1] != 'L')):
                        dominoes[i + 1] = 'R'
                        add_list.append(i + 1)
            for i in del_list:
                change_index.remove(i)
            for i in add_list:
                change_index.append(i)
        return ''.join(dominoes)


dominoes1 = ".L.R...LR..L.."
dominoes2 = "RL"
result = Solution().pushDominoes(dominoes1)
print(result)
