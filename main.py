#Задача 1

list_of_lists_1 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f','h',False],
    [1, 2, None],
]

class FlatIterator:
    def __init__(self, lst):
        self.lst = lst
        self.cursor = -1
        self.list_len = len(self.lst)

    def __iter__(self):
        self.cursor += 1
        self.nest_cursor = 0
        return self

    def __next__(self):
        if self.nest_cursor == len(self.lst[self.cursor]):
          iter(self)
        if self.cursor == self.list_len:
          raise StopIteration
        self.nest_cursor += 1
        return self.lst[self.cursor][self.nest_cursor - 1]

if __name__ == '__main__':
  flat_list = [item for item in FlatIterator(list_of_lists_1)]
  print(flat_list)

#Задача 2

def FlatIterator(): # Создаем функцию-итератор


    for i in list_of_lists_1: # Перебераем элементы списка
        for j in i: # Перебераем элементы вложенных списков
            yield j # Возвращаем элементы




for item in FlatIterator(list_of_lists_1):
    print(item)




def flat_generator(list_of_lists):

    ...
    yield
    ...


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()