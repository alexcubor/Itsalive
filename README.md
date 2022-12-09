[![Python 2.6 2.7 3.7](https://img.shields.io/badge/python-2.6%20%7C%202.7%20%7C%203.7-blue.svg)](https://www.python.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Описание пакета разработчика

Это небольшое введение даст вам понимание, почему здесь организована 
именно такая структура папок и по какой логике расположены скрипты.

### Интеграция с Cerebro

На студии в качестве основного менеджера задач выбран Cerebro, однако пакет разработчика 
построен таким образом, что бы скрипты могли работать как с Cerebro, так и без него, по скольку 
не всем художникам будет доступен Cerebro.

## Корень папки `tools` и её содержание

В ней находятся репозитории отдельных приложений, независимых от других программ. Это должны быть именно приложения, 
а не их установщики. Они служат для поддержания инфраструктуры студии.

*Для установщиков предусмотрена папка `soft` рядом с папкой `tools`*

- Приложение `ffmpeg` напрямую используется скриптами для запуска конвертации видео и изображений.

- `OCIO` так же является приложением в этом пакете разработчика, так как поддерживает 
инфраструктуру студии по части цветокоррекции.
- `Itsalive` здесь является отдельным приложением и поддерживает инфраструктуру студии на фундаментальном уровне и связывает 
все вышеописанные приложения единую экосистему. По мере разработки оно будет интегрироваться 
в `Unreal Engine`, `Maya`, `Nuke` и другие программы. Подробнее об этом в следующем разделе.
- Папка `utility` не является приложением и содержит в себе служебные файлы, которые помогут настроить корректную работу 
приложений на своём компьютере.

## Структура папки `Itsalive`

Содержит универсальные скрипты и конфигурации, которые работают на базовом уровне. 
К примеру обеспечивают файловую структуру, которая построена по единым правилам для всех программ.

*Файл `path_config.json` является конфигурацией Cerebro и является единым правилом для всех программ, 
по этому лежит в корне папки `Itsalive`*

Так же содержит в себе папку для каждой программы отдельно, так как каждая программа имеет свою структуру 
для связи со скриптами. К тому же скрипты чаще всего уникальны и выполняет задачу конкретной программы.

К примеру структура папки `maya` повторяет структуру родной папки `prefs`. Это позволяет Maya 
автоматически распознавать папки `scripts`, `icons` и др. и понимать, что в них находится.

У Houdini тоже есть подобный пример со своей структурой, но он будет реализован позже по мере необходимости.
