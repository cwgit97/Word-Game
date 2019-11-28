import math

def get_above(index):
    new_index = index - 4
    if new_index < 0:
        return -1
    else:
        return new_index

def get_below(index):
    new_index = index + 4
    if new_index > 15:
        return -1
    else:
        return new_index

def get_right(index):
    if (index + 1) % 4 == 0:
        return -1
    else:
        return index + 1

def get_left(index):
    if index % 4 == 0:
        return -1;
    else:
        return index - 1

def get_bot_right(index):
    if get_below(index) == -1 or get_right(index) == -1:
        return -1
    else:
        return index + 5

def get_top_left(index):
    if get_above(index) == -1 or get_right(index) == -1:
        return -1
    else:
        return index - 5

def get_top_right(index):
    if get_above(index) == -1 or get_right(index) == -1:
        return -1
    else:
        return index - 3

def get_bot_left(index):
    if get_below(index) == -1 or get_left(index) == -1:
        return -1
    else:
        return index + 3

def push_a_thing(some_list):
    some_list.append("test element")

def get_adj(index):
    adj_set = set()
    if get_above(index) != -1:
        adj_set.add(get_above(index))
    if get_below(index) != -1:
        adj_set.add(get_below(index))
    if get_left(index) != -1:
        adj_set.add(get_left(index))
    if get_right(index) != -1:
        adj_set.add(get_right(index))
    if get_top_left(index) != -1:
        adj_set.add(get_top_left(index))
    if get_top_right(index) != -1:
        adj_set.add(get_top_right(index))
    if get_bot_left(index) != -1:
        adj_set.add(get_bot_left(index))
    if get_bot_right(index) != -1:
        adj_set.add(get_bot_right(index))
    return adj_set

def traverse(index, cur_word, visited_set):
    if len(cur_word) > 4:
        return

    visited_set.add(index)

    cur_letter = string_arr[index]
    cur_word = cur_word + cur_letter
    word_list.append(cur_word)

    # print("index + adj")
    # print(index)
    # print(get_adj(index))

    for adj in get_adj(index):
        if adj not in visited_set:
            traverse(adj, cur_word, visited_set)
    visited_set.remove(index)


vowels = ["a", "e", "i", "o", "u", "y"]

input_string = "abcdefghijklmnop"

string_arr = [char for char in input_string]

path_dict = {index: set() for index in range(len(string_arr))}

# path_dict[0].add("test")
# path_dict[0].add("test2")
# path_dict[0].add("test")


print(path_dict)

word_list = list()
visited_set = set()
visited = set()

print(string_arr)

traverse(0, "", visited_set)

# print(get_adj(1))

print("word list")
print(word_list)
print("word list length")
print(len(word_list))




print("hello")