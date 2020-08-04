import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    a = list(map(int, input().split()))
    _min = 9999999999
    _max = -9999999999
    for num in a:
        if _min > num:
            _min = num
        if _max < num:
            _max = num

    print('#{} {}'.format(test_case, _max - _min))