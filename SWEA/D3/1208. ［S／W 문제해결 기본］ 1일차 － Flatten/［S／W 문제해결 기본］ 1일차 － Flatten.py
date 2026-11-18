for test_case in range(1, 11):
    dump_count = int(input())
    height_list = list(map(int, input().split()))
    height_list.sort(reverse=True)

    for i in range(dump_count):
        height_list[0] -= 1
        height_list[99] += 1
        height_list.sort(reverse=True)

    print(f'#{test_case} {height_list[0] - height_list[99]}')
