## Just for Learning async programming

## LESSON 1

Прсотейший скрипт работы сервера, без асинхронного режима, пока сервер ждет запроса от одного клиента, он не может ответить другому.

## LESSON 2

Асинхронный скрипт написанный с использованием событийного цикла.

метод select распечатывает спски сокетов, и если их нет - создает их, таким образом можно каждый раз проверять, какое соединение установелнно, и кто ждет ответа.

## LESSON 3

использование функций callback

вмсето мудуля selector, используем модуль selectors - более совершенную и абстракнтуную модель того же модуля.
распакоывает сразу всю нужную информацию и отдаёт fileobj, event(служебная информация) и data(связанные данные)

##  LESSON 4

Генераторы и событийный цикл Round Robin

    1. Генераторы это функции! Они передают контроль выполнения программы

    2. Инструкций yield может быть несколько в одной функции-генераторе, код после ключевого слова yield выполняется при следующей интерации и вновь останавливается на yield (при вызове функции next())
