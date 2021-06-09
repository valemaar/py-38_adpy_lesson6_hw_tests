# КАТАЛОГ ДОКУМЕНТОВ ХРАНИТЬСЯ В СЛЕДУЮЩЕМ ВИДЕ:

documents = [
    {'type': 'passport', 'number': '2207 876123', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

# Перечень полок, на которых находяться документы, хранится в следующем виде:
directories = {
    '1': ['2207 876123'],
    '2': ['11-2'],
    '3': ['10006']
}


def find_client_by_doc(docs_list, doc_input='0'):  # command p
    print('Поиск владельца документа')
    result = ''
    print('Введен номер докумета: {}'.format(doc_input))
    for doc in docs_list:
        if doc['number'] == doc_input:
            result = doc["name"]
            print(f'Имя владельца документа: {doc["name"]}')
    if result == '':
        print(f'Документа с номером "{doc_input}" нет в архиве!')
    return result


def find_shelf_by_doc(shelf_list, doc_input='0'):  # command s
    print('Поиск номера полки хранения')
    print('Введен номер докумета: {}'.format(doc_input))
    counter = 0
    result = ''
    for shelf, docs in shelf_list.items():
        if doc_input in docs:
            result = shelf
            print(f'Документ хранится на полке: {shelf}')
            counter += 1
    if counter == 0:
        print('Документа с таким номером нет в архиве!')
    return result


def give_all_docs_list(docs_list):  # command l
    print('Список документов в архиве:')
    my_list = list()
    list_index = 0
    for docs in docs_list:
        my_list.extend([value for key, value in docs.items()])
    for item in my_list:
        try:
            print(f'{my_list[list_index]} "{my_list[list_index + 1]}" "{my_list[list_index + 2]}"')
            list_index += 3
        except IndexError:
            pass
    return my_list


def add_new_doc(docs_list, shelf_list, doc_input='', type_doc_input='', name_input='', shelf_input=''):  # command a
    print(f'Добавление нового документа')
    my_dict = dict()
    my_list = list()
    temp_list = list()
    print('Введен номер докумета: {}'.format(doc_input))

    # добавим в список temp_list все номера существующих документов
    for docs in docs_list:
        temp_list.append(docs['number'])

    if doc_input in set(temp_list):
        print('Документ с номером "{}" уже создан'.format(doc_input))
    else:
        print('Введен тип докумета: {}'.format(type_doc_input))
        print('Введены Имя и Фамилия владельца: {}'.format(name_input))
        print('Введен номер полки для хранения: {}'.format(shelf_input))

        if shelf_input in shelf_list.keys():
            my_dict['type'] = type_doc_input
            my_dict['number'] = doc_input
            my_dict['name'] = name_input
            docs_list.append(my_dict)
            my_list = shelf_list[shelf_input]
            my_list.append(doc_input)
            shelf_list[shelf_input] = my_list
            print(f'Документ номер "{doc_input}" добавлен на полку "{shelf_input}".')
        else:
            print(f'Полки с номером "{shelf_input}" нет в архиве!')

    return docs_list


def del_doc(docs_list, shelf_list, doc_input=''):  # command d
    print('Удаление документа')
    my_list = list()
    print('Введен номер докумета: {}'.format(doc_input))
    counter = 0
    for shelf, docs in shelf_list.items():  # delete doc from shelf
        if doc_input in docs:
            my_list = docs
            my_list.remove(doc_input)
            shelf_list[shelf] = my_list
            for doc in docs_list:  # delete doc from docs_list
                if doc_input in doc.values():
                    docs_list.remove(doc)
                    print(f'Документ "{doc_input}" удален!')
                counter += 1
    if counter == 0:
        print(f'Документа с номером "{doc_input}" нет в архиве!')
    print('docs_list:', docs_list)
    return docs_list, shelf_list


def move_doc(docs_list, shelf_list):  # command m
    print('Перенос документа на другую полку')
    my_list = list()
    new_list = list()
    numb_doc = input('Введите номер документа: ')
    numb_shelf = input('Введите номер полки для переноса документа: ')
    count_list = 0
    result = ''
    if numb_shelf in shelf_list.keys():
        for shelf, docs in shelf_list.items():  # delete doc from shelf
            if numb_doc in docs and numb_shelf != shelf:
                my_list = docs
                my_list.remove(numb_doc)
                shelf_list[shelf] = my_list
                new_list = shelf_list[numb_shelf]
                new_list.append(numb_doc)
                shelf_list[numb_shelf] = new_list
                count_list += 1
                result = f'Документ "{numb_doc}" перенесён на полку "{numb_shelf}"'
        if count_list == 0:
            result = f'Документа с номером "{numb_doc}" нет в архиве!'
    else:
        result = f'Полки с номером "{numb_shelf}" нет в архиве! Введите другой номер или добавьте новую' \
                 f' полку командой "as".'
    return result


def add_new_shelf(shelf_list):  # command as
    print(f'Добавление новой полки')
    user_input = input('Введите номер новой полки: ')
    result = ''
    if user_input not in shelf_list.keys():
        shelf_list[user_input] = []
        result = f'Добавлена полка номер "{user_input}"!'
    else:
        result = f'Полка номер "{user_input}" уже существует!'
    return result


def give_list_shelf(shelf_list):  # command ls
    print('Список полок в архиве:')
    return shelf_list


def my_main():
    '''
    p - people - команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
    s - shelf - команда, которая спросит номер документа и выведет номер полки, на которой он находится;
    l - list - команда, которая выведет список всех документов в формате passport "2207 876123" "Василий Гупкин";
    a - add - команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя
    владельца и номер полки, на которой он будет храниться.
    d - delete - команда, которая спросит номер документа и удалит его из каталога и из перечня полок.
    '''
    while True:
        user_input = input('Введите команду: ').lower()
        command_list = ['p', 's', 'l', 'a', 'd', 'm', 'as', 'ls', 'q']
        if user_input in command_list:
            if user_input == 'p':
                find_client_by_doc(documents, '11-2')
            elif user_input == 's':
                find_shelf_by_doc(directories, '2207 876123')
            elif user_input == 'l':
                give_all_docs_list(documents)
            elif user_input == 'a':
                add_new_doc(documents, directories, '1234 567890', 'passport', 'Иван Крузенштерн', '3')
            elif user_input == 'd':
                del_doc(documents, directories, '10006')
            elif user_input == 'm':
                print(move_doc(documents, directories))
            elif user_input == 'as':
                print(add_new_shelf(directories))
            elif user_input == 'ls':
                print(give_list_shelf(directories))
            elif user_input == 'q':
                print('Завершение работы программы ...')
                break
            print()
        else:
            print(f'Ошибка! Такой команды нет!\nСписок допустимых команд:')
            print(my_main.__doc__)
    return


if __name__ == '__main__':
    my_main()
