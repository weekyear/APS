import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    _data = list(map(int, input().split()))
    K = _data[0]
    N = _data[1]
    M = _data[2]

    charge_list = list(map(int, input().split()))
    charge_list.append(N)

    num_charge = 0
    c = 0
    cur_battery = K

    for i in range(1, N+1):
        cur_battery -= 1

        if i == charge_list[c] and i != N:
            c += 1
            if cur_battery < charge_list[c] - i:
                cur_battery = K
                num_charge += 1
                
        if cur_battery < 1 and i != N:
            num_charge = 0
            break

    print('#{} {}'.format(test_case, num_charge))