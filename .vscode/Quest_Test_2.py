import string #импортируем строки для последующей работы с ними

text = input("Введите текст: ") # переменная для ввод текста

def remove_extra_spaces(text): # функция в которой будут удаляться лишние пробелов в начале и конце текста
    
    # удаляем повторяющиеся пробелы между словами
    text = text.strip() # переменная для удаления начальных и конечных символов
    words = text.split() # переменная для разделения строки
    text = " ".join(words) # переменная для проставления одного пробела
    
    for punctuation in string.punctuation: # удаляем пробелы перед знаками препинания

        text = text.replace(" " + punctuation, punctuation) # переменная где удаляются пробелы перед знаками препинания

    return text

def count_removed_spaces(text): # функция для подсчет количества удаленных пробелов

    total_spaces = text.count(" ") # переменная для подсчета общего количества пробелов
    removed_spaces = total_spaces - len(text.split()) + 1 # переменная для подсчета удаленных пробелов
    
    return removed_spaces

def count_remaining_spaces(text): # функция для подсчета количества оставшихся пробелов
    
    remaining_spaces = text.count(" ") # считает количнство оставшихся пробелов
    
    return remaining_spaces

processed_text = remove_extra_spaces(text) # обработанный текст без лишних пробелов

# вывод необходимых результатов
print("Обработанный текст: ", processed_text) 
print("Количество удаленных пробелов: ", count_removed_spaces(processed_text))
print("Количество оставшихся пробелов: ", count_remaining_spaces(processed_text))