# Задача_4
# Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1


list_string = ["123", "234", 123, "567"]
search_string = "123"
if type(search_string) == int:
    print(f"список: {list_string}, ищем: {search_string}, ответ: -1")
else:  
    new_list_string = list(enumerate(list_string))

    if search_string in list_string:
        second_occurrence_str = list(filter(lambda x: x[1] == search_string , new_list_string))
        if  second_occurrence_str[-1][0] == 0 :
            print(f"список: {list_string}, ищем: '{search_string}', ответ: -1")
        else:
            print(f"список: {list_string}, ищем: '{search_string}', ответ: {second_occurrence_str[-1][0]}")
    else:
        print(f"список: {list_string}, Искомой строки '{search_string}'' нет в этом списке.")        