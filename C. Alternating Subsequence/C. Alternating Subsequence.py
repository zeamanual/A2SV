test_cases = int(input())

for i in range(test_cases):
    n = int(input())
    arr = list(map(int, input().split()))

    left = 0
    right = 0
    answer = []
    while right < n:

        max_num = arr[left]
        while right < n and (arr[left] * arr[right]) > 0:
            max_num = max(max_num, arr[right])
            right += 1

        answer.append(max_num)
        left = right

    print(sum(answer))
