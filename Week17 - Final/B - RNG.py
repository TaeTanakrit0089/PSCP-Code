"""Saul Goodman"""
import json
def b_rng(data, num_n, num_s, result):
    """Saul Goodman"""
    for i in range(255):
        temp, memo = 0, []
        for j in range(i, num_n*num_s+i, num_s):
            if j % 256 in memo:
                break
            memo.append(j % 256)
            temp += data[j % 256]
        result.append(temp * max(1, num_n // len(memo)) +
                      sum([data[i] for i in memo[:num_n % len(memo)]]))
    return max(result)
print(b_rng(json.loads(input()), int(input()), int(input()), []))
