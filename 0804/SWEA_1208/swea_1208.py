import sys
sys.stdin = open("input.txt", "r")

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    d = int(input())
    blocks = list(map(int, input().split()))

    while d > 0:
        max_idx = 0
        min_idx = 0
        for i in range(len(blocks)):
            if blocks[i] > blocks[max_idx]:
                max_idx = i

            if blocks[i] < blocks[min_idx]:
                min_idx = i

        blocks[max_idx] -= 1
        blocks[min_idx] += 1
        d -= 1

    for i in range(len(blocks)):
        if blocks[i] > blocks[max_idx]:
            max_idx = i

        if blocks[i] < blocks[min_idx]:
            min_idx = i

    print('#{} {}'.format(test_case, blocks[max_idx] - blocks[min_idx]))