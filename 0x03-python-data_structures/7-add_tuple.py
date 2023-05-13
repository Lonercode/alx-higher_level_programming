#!/usr/bin/python3
if __name__ == "__main__":
    def add_tuple(tuple_a=(), tuple_b=()):
        list_morph = []
        list_a = []
        list_b = []
        if len(tuple_a) < 2:
            list_a.append(tuple_a[0])
            list_a.append(0)
            tuple_a = tuple(list_a)

        if len(tuple_b) < 2:
            list_b.append(tuple_b[0])
            list_b.append(0)
            tuple_b = tuple(list_b)

        if len(tuple_a) > 2 or len(tuple_b) > 2:
            for i in range(2):
                result = tuple_a[i] + tuple_b[i]
                list_morph.append(result)
            tuple_c = tuple(list_morph)
            print(tuple_c)

        if len(tuple_a) == len(tuple_b):
            for i in range(len(tuple_a)):
                result = tuple_a[i] + tuple_b[i]
                list_morph.append(result)
            tuple_c = tuple(list_morph)
            print(tuple_c)

