Реферат
================
Реферат в LaTeX по дисциплине «Геофизические методы контроля» на тему «Гидродинамический дебитомер».

Структура исходников
--------------------
Структура каталогов:
```
.
├── images
└── inc
```

В корневом каталоге `.` находится файл `main.tex`.
В `main.tex` подключается все, включая преамбулу, титульный лист, приложения и т.д.

В каталоге `images/` находятся рисунки, схемы.

В каталоге `inc/` находятся файлы, которые подключаются к `main.tex`:
* файлы формата `0-*.tex` являются ненумерованными секциями (например введение, заключение, список использованной литературы)
* файлы формата `[1-9]-*.tex` являются нумерованными секциями (например постановка задчи и т.д)
* файлы формата `[a-z]-app.tex` являются файлами приложений
* файлы формата `[a-z]*.tex` не являются секциями, они подключаются для полной работы документа (например преамбула)

Работа с LaTeX
--------------
Как установить LaTeX: http://blog.amet13.name/2014/06/latex.html

Пример компиляции проекта с помощью Makefile:
```bash
make
```

Пример очистки сборочных файлов после компиляции (кроме PDF):
```bash
make clean
```

Лицензия
--------
[Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](http://creativecommons.org/licenses/by-sa/4.0/deed.ru)

![CC BY SA](https://licensebuttons.net/l/by-sa/4.0/88x31.png)

Благодарности
-------------
[Амету Умерову](https://github.com/Amet13/bachelor-diploma/) за основу шаблона LaTeX