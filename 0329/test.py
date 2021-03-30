# arr = [[] for _ in range(2)]
#
# for k in range(2):
#     for j in range(3):
#         tmp = list(map(int,input().split()))
#         arr[k].append(tmp)
# print(arr)

arr = [[[0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0]]]
if not arr:
    print('yes')
else:
    print('no')