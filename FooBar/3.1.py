def solution(x, y):
    generation = 1
    number_to_find = (x, y)
    if x == ('1' or '2') or y == ('1' or '2'):
        return '1'
    current_list = [['1', '2']]
    while True:
        new_list = get_next_list(current_list)
        # TODO check fun here

        current_list = new_list
        new_list = list()
        print(current_list)


def get_next_list(current_list):
    new_list = list()
    for _list in current_list:
        position = 1
        for digit in _list:
            new_list.append((str(int(digit) + int(_list[position])), str(int(_list[position]))))
            position = position - 1
    return new_list


print(solution('4', '7'))