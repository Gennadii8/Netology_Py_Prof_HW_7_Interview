from main import Stack
BRACKETS = '()[]{}'


def check_balance(input_text, brackets=BRACKETS):
    brackets_stack = Stack()
    brackets_stack.list_of_values = []
    open_brackets = brackets[::2]
    close_brackets = brackets[1::2]
    # Проходим по каждому символу входного текста
    for symbol in input_text:
        # если символ это открывающая скобка, то добавляем его в стек
        if symbol in open_brackets:
            brackets_stack.push(open_brackets.index(symbol))
        # или если символ это закрывающая скобка
        elif symbol in close_brackets:
            # и если стек не пуст и  последняя добавленная открывающая скобка такого же типа, то удаляем
            if (not brackets_stack.is_empty()) and (brackets_stack.peek() == close_brackets.index(symbol)):
                brackets_stack.pop()
            # если не такого же типа, то сразу выводим ошибку
            else:
                return print('Несбалансированно')
    # проверяем стек, если он пустой, то возвращаем 'Сбалансированно', иначе - 'Несбалансированно'
    if not brackets_stack.list_of_values:
        return print('Сбалансированно')
    else:
        return print('Несбалансированно')


if __name__ == '__main__':
    check_balance(input_text='(((([{}]))))')
    check_balance(input_text='[([])((([[[]]])))]{()}')
    check_balance(input_text='{{[()]}}')
    check_balance(input_text='}{}')
    check_balance(input_text='{{[(])]}}')
    check_balance(input_text='[[{())}]')



