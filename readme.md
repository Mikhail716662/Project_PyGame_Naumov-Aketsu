1. ### **Slime Platformer**
> - Игра заключается в том, что управляемый персонаж, перескакивая с одной платформы на другую, доходит до 
чекпоинта(желтого квадрата) в верхнем углу экрана. Игра состоит из 5 уровней. Служит для развлекательных целей.
> - Суммарное количество строк кода около 300
> - [Техническое задание](materials%2Ftechnical_specification.md)
2. ### **Запуск программы**
> - При запуске программы нужно установить библиотеки, указанные в requirements.txt. PyCharm предложит это сделать 
автоматически. После установки библиотек, вы можете запустить программу через файл main.py
3. ### **Поддержка проекта в рабочем состоянии**
> Добавление нового уровня в игру
> - Для добавления нового уровня необходимо создать карту этого уровня 15*20 из значков: "."(простое поле), "-"(платформа), 
"^"(шип), "@"(значок положения нашего героя) и "F"(положение портала в следующий уровень). 
Далее эту карту нужно добавить в словарь level_list в файле levels/levels.py. Чтобы уровень добавить в игру, 
необходимо дописать в главное меню этот уровень. 
Для этого в файле functions.py в функцию menu() в menu.add.selector нужно вписать название этого уровня и его 
порядковый номер.
4. ### **Описание работы для обычного пользователя в приложении**
> - После запуска приложения пользователь видит [главное меню](materials%2Fmain_menu.png) с выбором уровня, кнопками "играть" и "выход". После нажатия на кнопку "играть" запускается сама игра. После того как персонаж
достиг портала в следующий уровень он переходит на следующий по номеру уровень. После прохождения 5 уровня игра 
возвращается к начальному меню.
5. ### **Ссылка на скринкаст работы приложения**
> - https://vkvideo.ru/video742577835_456239018
