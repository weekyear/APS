import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    input_data = list(map(int, input().split()))
    N = input_data[0] # 10
    M = input_data[1] # 3

    num_data = list(map(int, input().split()))

    _min = 9999999999
    _max = -9999999999
    for i in range(N+1-M):
        _sum = 0
        for k in range(i, i+M):
            _sum += num_data[k]

        if _min > _sum:
            _min = _sum
        if _max < _sum:
            _max = _sum

    print('#{} {}'.format(test_case, _max-_min))