class Stack:
    def __init__(self,  list_of_values=[], depth=32):
        self.depth = depth
        self.list_of_values = list_of_values

    def is_empty(self):
        """проверка стека на пустоту. Метод возвращает True, если он пустой или False, если в нём что-то есть"""
        if not self.list_of_values:
            return True
        else:
            return False

    def push(self, new_elem):
        """добавляет новый элемент на вершину стека. Метод ничего не возвращает"""
        length = self.size()
        if length != self.depth:
            self.list_of_values.insert(0, new_elem)
            # print(self.list_of_values)
        else:
            return print("Stack is full, not able to add element")

    def pop(self):
        """удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека"""
        if not self.is_empty():
            self.list_of_values.pop(0)
            if not self.is_empty():
                return self.list_of_values[0]
        else:
            return print('Stack is empty')

    def peek(self):
        """возвращает верхний элемент стека, но не удаляет его. Стек не меняется"""
        if not self.is_empty():
            return self.list_of_values[0]
        else:
            return print('Stack is empty')

    def size(self):
        """возвращает количество элементов в стеке"""
        return len(self.list_of_values)


if __name__ == '__main__':
    example_stack = Stack(list_of_values=[3, 7, 5])
    print(example_stack.list_of_values)
    print(example_stack.is_empty())
    # print(example_stack.size())
    # example_stack.push(77)
    # example_stack.aaa()
    # print(example_stack.pop())
    # print(example_stack.peek())
