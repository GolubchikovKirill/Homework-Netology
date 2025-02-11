"""
Доработать параметризованный декоратор logger в коде ниже.
Должен получиться декоратор, который записывает в файл дату и время вызова функции, имя функции, аргументы,
с которыми вызвалась, и возвращаемое значение. Путь к файлу должен передаваться в аргументах декоратора.
Функция test_2 в коде ниже также должна отработать без ошибок.
TASK-2
"""

import os
import datetime
from functools import wraps


def logger(path):
    def __logger(old_function):
        @wraps(old_function)
        def new_function(*args, **kwargs):

            current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            function_name = old_function.__name__
            args_str = ', '.join([repr(arg) for arg in args])
            kwargs_str = ', '.join([f"{key}={repr(value)}" for key, value in kwargs.items()])
            all_args = ', '.join([args_str, kwargs_str]) if kwargs else args_str
            result = old_function(*args, **kwargs)
            log_entry = f"{current_time} - {function_name}({all_args}) -> {repr(result)}\n"
            # Проверим, существует ли директория
            try:
                # Если путь к файлу не существует, создаем его
                os.makedirs(os.path.dirname(path), exist_ok=True)

                # Записываем информацию в файл
                with open(path, 'a') as log_file:
                    log_file.write(log_entry)
            except Exception as e:
                print(f"Ошибка при записи в файл: {e}")
            return result
        return new_function
    return __logger


def test_2():
    paths = ('log_1.log', 'log_2.log', 'log_3.log')

    for path in paths:
        # Удаляем файл, если он уже существует
        if os.path.exists(path):
            os.remove(path)

        @logger(path)
        def hello_world():
            return 'Hello World'

        @logger(path)
        def summator(a, b=0):
            return a + b

        @logger(path)
        def div(a, b):
            return a / b

        assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
        result = summator(2, 2)
        assert isinstance(result, int), 'Должно вернуться целое число'
        assert result == 4, '2 + 2 = 4'
        result = div(6, 2)
        assert result == 3, '6 / 2 = 3'
        summator(4.3, b=2.2)

    for path in paths:
        # Проверяем, что файлы были созданы
        assert os.path.exists(path), f'файл {path} должен существовать'

        with open(path) as log_file:
            log_file_content = log_file.read()

        # Проверяем, что нужная информация записана в файл
        assert 'summator' in log_file_content, 'должно записаться имя функции'

        for item in (4.3, 2.2, 6.5):
            assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_2()

