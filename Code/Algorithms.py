import time
from collections import deque


# new_list = []
#
# # import pdb;pdb.set_trace()
# def find_list(arr):
#     for item  in arr:
#         if type(item) is list:
#             return find_list(item)
#         else:
#             new_list.append(item)
#
#
# find_list([1,2,3,[4,5,[6,7]]]
# )
# print(new_list)

def sum(arr):
    if len(arr) == 1:  # 基准条件列表只有一个数
        return arr[0]
    else:  # 递归条件
        return arr[0] + sum(arr[1:])  # 每次循环，将第一个拿出来，进行相加。


# print(sum([1, 2, 3, 4]))


def quickSort(arr):
    if len(arr) < 2:  # 基准条件列表只有一个数或者列表为空
        return arr

    else:
        pivot = arr[0]  # 默认第一数为基准值
        less = [i for i in arr[1:] if i < pivot]  # 找出小于所有基准值的数
        greater = [i for i in arr[1:] if i > pivot]  # 找出大于所有基准值的数
        return quickSort(less) + [pivot] + quickSort(greater)


# print(quickSort([1, 56, 9, 23, 0, 4]))

from collections import deque
def search_queue(name):
    """
    广度优先算法
    :param name:
    :return:
    """
    col_have_search = []  # 声明一个空列表来记录已经搜索过名字
    search_queue = deque() #创建一个空队列
    search_queue.append(graph[name]) #添加第一个名字
    append = col_have_search.append
    while search_queue: #如果队列中有值，就死循环。
        person = search_queue.popleft() #从队列中弹出最左边的名字
        if person not in col_have_search: #判断是否已经检查过了
            if person_is_seller(person): #判断是否是要找的人
                return True
            else:
                append(person)
                search_queue += graph.get(person, []) #这里要用get,如果是分支尾端，就会报错。
    return False


def person_is_seller(name):
    return "S" in name


graph = {
    "Tom": ["Aaron", "Bob", "Cindy"],
    "Bob": ["Jay", "Peter", "Kevin"],
    "Aaron": ["Frank"],
    "Frank": ["Sandy"]
}

print(search_queue("Tom"))
