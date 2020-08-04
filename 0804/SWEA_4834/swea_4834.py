import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    _input = input()

    _max = 0
    num_list = [0] * 10

    for char in _input:
        num = int(char)
        num_list[num] += 1

    freq_num = -1
    for i in range(len(num_list)):
        if num_list[i] >= freq_num and i > _max:
            freq_num = num_list[i]
            _max = i

    print('#{} {} {}'.format(test_case, _max, freq_num))