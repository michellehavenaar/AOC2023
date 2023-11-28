import operator as op

operator_dict = {
    '==': op.eq,
    '!=': op.ne,
    '<': op.lt,
    '<=': op.le,
    '>': op.gt,
    '>=': op.ge,
    '+': op.add,
    '-': op.sub,
    '*': op.mul,
    '/': op.truediv,
    '//': op.floordiv
    }

def compare_list_int(list, compare_op: str):
    # compares elements in a list of integers, looking one element ahead, counts if comparison equals to true
    # compare operators: >, <, >=, <=, ==, !=
    # stops looking after the previous to last item has been compared to last
    count = 0
    for index, elem, in enumerate(list):
        if index < len(list)-1:
            if operator_dict[compare_op](elem, list[index+1]):
                count+=1

    return count

def get_first_index(list:list, value):
    i = list.index(value)
    return i

def get_last_index(list: list, value):
    list.reverse()
    i = list.index(value)
    list.reverse()
    return (len(list) - i) - 1