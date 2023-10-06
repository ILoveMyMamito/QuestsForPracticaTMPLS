import string # импортируем строки для последующей работы с ними
import re # импортируем библиотеку для работы с пробелами перед пунктуацией (прошлый метод решил перестать работать)

text = input("Введите текст: ") # переменная для ввод текста

def remove_extra_spaces(text): # функция в которой будут удаляться лишние пробелов в начале и конце текста
    new_text = re.sub(r'\s*([,.\?!:;])', r'\1', text) # удлаяем пробелы толлько перед пунктуацией (не после)
    modified_text = ' '.join(new_text.split()) # удаляем повторяющиеся пробелы между словами
    print("Обработанный текст: ", modified_text) # выводим текст без повторяющихся пробелов
    
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
print("Количество удаленных пробелов: ", count_removed_spaces(processed_text))
print("Количество оставшихся пробелов: ", count_remaining_spaces(processed_text))
