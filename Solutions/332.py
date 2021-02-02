"""
Problem:

Given integers M and N, write a program that counts how many positive integer pairs
(a, b) satisfy the following conditions:

a + b = M
a XOR b = N
"""


def get_count(M: int, N: int) -> int:
    count = 0
    for i in range(1, M):
        # (a, b) and (b, a) are considered different entities.
        # To consider them only once, use range(1, M // 2)
        if i ^ (M - i) == N:
            count += 1
    return count


if __name__ == "__main__":
    print(get_count(100, 4))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
"""
