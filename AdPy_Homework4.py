import datetime
import os

p = os.path.abspath('file.txt ')
print(p)

documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

def logger (final_file):
    file_path=0
    def parametric_decorator(old_function):
        def new_function(*args, **kwargs):
            result=old_function(*args,**kwargs)
            print(result)
            file = open("logger_decorator.txt", "w")
            nonlocal final_file
            final_file = os.path.abspath('logger_decorator.txt')
            file.write('Путь к файлу: '+'\n'+'\n')
            file.write(final_file+'\n'+'\n')
            time=datetime.datetime.utcnow()
            file.write('Время открытия функции: '+'\n'+'\n')
            file.write(str(time)+'\n'+'\n')
            file.write('Имя функции: '+'\n'+'\n')
            file.write(old_function.__name__+'\n'+'\n')
            file.write('Аргументы функции'+'\n'+'\n')
            file.write(str(*args)+str(**kwargs)+'\n'+'\n')
            file.write('Возвращаемое значение функции:' + '\n'+'\n')
            for elems in result:
                file.write(str(elems)+'\n')
            file.close()
        return new_function
    return parametric_decorator

@logger('logger_decorator.txt')
def documents_list(documents):
    list=[]
    i=0
    for docs in documents:
        person = ('Тип документа', docs['type'], 'Номер документа', docs['number'], 'Имя держателя', docs['name'])
        list.append (person)
        i+=1
    for elements in list:
        print (elements)
    return (list)

documents_list(documents)