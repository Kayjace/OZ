import timeit
from sortedcontainers import SortedList

#list (no index, brute force)
#vs
#tree (has index, tree search)


#데이터 삽입(INSERT)
#list
print("리스트 생성 시작")
start_time_list = timeit.default_timer()
data_list = list(range(1, 320_000_001))
end_time_list = timeit.default_timer()
time_setup_list = end_time_list - start_time_list
print(f"리스트 생성 소요시간 : {time_setup_list:.6f} sec")

#tree
print("트리 생성 시작")
start_time_tree = timeit.default_timer()
data_tree = SortedList(list(range(1, 320_000_001)))
end_time_tree = timeit.default_timer()
time_setup_tree = end_time_tree - start_time_tree
print(f"트리 생성 소요시간 : {time_setup_tree:.6f} sec")

#데이터 조회 (SELECT)
#list
def fetch_from_list(target):
    for data in data_list:  #brute force
        if data == target:
            return data

#tree
def fetch_from_list(target):
    return data_tree[target]

target = 160_000_000

print("리스트 조회 시작")
start_list_fetch = timeit.default_timer()
fetch_from_list(target)
end_list_fetch = timeit.default_timer()
time_search_list = end_list_fetch-start_list_fetch
print(f"Target {target} found, searchtime : {time_search_list:.6f}")

print("트리 조회 시작")
start_tree_fetch = timeit.default_timer()
fetch_from_list(target)
end_tree_fetch = timeit.default_timer()
time_search_tree = end_tree_fetch - start_tree_fetch
print(f"Target {target} found, searchtime : {time_search_tree:.6f}")