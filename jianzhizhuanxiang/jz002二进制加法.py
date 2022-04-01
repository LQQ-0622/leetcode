def addBinary(a: str, b: str) -> str:
    i, j = len(a) - 1, len(b) - 1
    is_carry = 0
    result = []
    while i >= 0 or j >= 0:
        x, y = int(a[i]), int(b[j])
        i -= 1
        j -= 1
        sum = x + y + is_carry
        is_carry = 1 if sum > 1 else 0
        pos = sum - 2 if sum > 1 else sum
        result.append(str(pos))
    if is_carry == 1:
        result.append(1)
    re_str = ''
    for i in range(len(result)-1, 0, -1):
        re_str += re_str + str(result[i])
    return re_str


a = addBinary('11', '10')
print(a)
