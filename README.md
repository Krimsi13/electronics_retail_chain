# electronics_retail_chain
Test for certification
 - приложение с API-интерфейсом и админ-панелью.
 - Сеть по продаже электронники представляющая собой иерархическую структуру из трех уровней: завод, розничная сеть,
индивидуальный предприниматель.

### Требования:
1. Каждое звено сети должно обладать следующими элементами:
 - Название.
 - Контакты.
 - Продукты.
 - Поставщик.
 - Задолженность перед поставщиком в денежном выражении с точностью до копеек.
 - Время создания(заполняется автоматически при создании).
2. Сделать вывод в админ-панели созданных объектов.
3. На странице сети добавить:
 - ссылку на поставщика;
 - фильтр по названию города;
 - admin action, очищающий задолженность перед поставщиком у выбранных объектов.
4. Используя DRF, создать набор представлений:
 - CRUD для модели поставщика(запретить обновление через API поля "Задолженность перед поставщиком").
 - Добавить возможность фильтрации объектов по определенной стране.
5. Настроить права доступа к API так, чтобы только активные сотрудники имели доступ к API.

### Структура:
 - Пакет config(настройки проекта)
 - Приложение chains(модели Производителей и Продуктов)
 - Приложение users(пользователи)
 - Управляющий файл manage.py(все команды происходят через этот файл)
 - Файл с зависимостями pyproject.toml(все необходимые зависимости для работы проекта)
 - Файл README.md(описание проекта)
 - Файл .env_sample(шаблон для переменных окружения)
 - Файл .gitignore(список игнорируемых файлов)

### Инструкции:
 - Запуск проекта командой: python manage.py runserver
 - Для создания суперпользователя можно воспользоваться командой: python manage.py csu
 - Для создания активного пользователя можно воспользоваться командой: python manage.py cau
 - Для тестирования платформы можно воспользоваться административной панелью: http://127.0.0.1:8000/admin/ 
 - Также для тестирования можно воспользоваться: Postman
