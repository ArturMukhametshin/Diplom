# Diplom
Дипломная работа по курсу "Python-разработчик"
Введение.

#	Тема дипломной работы: "Анализ и сравнение написания web-приложений с использованием разных фреймворков: Django, Flask и FastAPI". 

В данной работе будет проведен анализ и сравнение трех популярных фреймворков для разработки web-приложений на языке Python: Django, Flask и FastAPI. Будет рассмотрена архитектура и принципы разработки каждого фреймворка, а также будет проведено сравнение их производительности, безопасности и масштабируемости.
	
## Обоснование выбора темы.

В современном мире, в век цифрового развития, большинство людей живут бок обок с интернетом. Будь ты на работе, дома, отдыхе, в путешествии, учёбе, везде нас сопровождает «цифровой мир». Попробуйте представить себе покупку билета, к примеру в другой город, без интернета. Сейчас это невозможно. Даже если вы скажете мне что можно купить билет через кассу, то задумайтесь, как кассир выдаёт вам билет. На данном этапе он является посредником между вами и сервисом по покупке билета. Так, что вы не вольно взаимодействуете с цифровой сетью. И это даёт множество удобств. Например, скорость поиска нужного рейса, возможность выбора места и так далее. И это только маленькая капля в океане возможностей.
Но здесь возникает вопрос, а как это работает? Существует множество языков программирования и фреймворков для создания web приложений, которые помогают взаимодействовать с различными сервисами через интернет. С каждым годом web-приложения становятся всё более сложными и требуют использования эффективных и масштабируемых фреймворков.  На мой взгляд, это достаточно интересная тема что бы её рассмотреть. В своей работе, я буду рассматривать web-приложения на языке Python: Django, Flask и FastAPI. Они являются одними из наиболее популярных фреймворков для разработки web-приложений на языке Python. Однако, каждый фреймворк имеет свои сильные и слабые стороны, и выбор правильного фреймворка для конкретного проекта может быть сложной задачей.

  # Определение цели и задачи дипломной работы.

Цели: создать web-приложения на языке Python используя 3 разных фреймворка, чтобы оценить и сравнить их эффективность и удобство применения.

Задачи дипломной работы:
1.	Обзор популярных инструментов для разработки web-приложений на Python.
2.	Изучение архитектуры каждого фреймворка.
3.	Сравнение производительности, безопасности и масштабируемости каждого фреймворка.
4.	Выявление наиболее подходящего фреймворка для разработки web-приложений в зависимости от конкретных требований.
5.	Разработка простых web-приложений с использованием Django, Flask и FastAPI, их сравнение и анализ. 




















Основные понятия и определения.

1.	Фреймворк (Framework): Программная платформа, которая предоставляет готовые компоненты и инструменты для разработки приложений. В контексте веб-приложений часто используются Django, FastAPI или Flask.
2.	Web-приложение – клиент-серверное приложение, в котором клиент взаимодействует с веб-сервером при помощи браузера. Логика веб-приложения распределена между сервером и клиентом, хранение данных осуществляется преимущественно на сервере, обмен информацией происходит по сети.
3.	ОРМ (Object-Relational Mapping, объектно-реляционное отображение) – технология программирования, которая связывает базы данных с концепциями объектно-ориентированных языков программирования, создавая «виртуальную объектную базу данных». Шаблон позволяющий связать данные с объектами в приложении.
4.	Шаблонизатор – программное обеспечение, позволяющее использовать шаблоны для генерации конечных документов с помощью декларативного языка разметки.
5.	Кэширование – это метод, используемый для повышения производительности и эффективности приложения за счет временного хранения часто используемых данных в расположении, которое быстрее извлекается, чем исходный источник. Кэширование помогает сократить время, необходимое для получения данных, и снизить нагрузку на исходный источник данных.
6.	Аутентификация — процедура проверки подлинности, например проверка подлинности пользователя путем сравнения введенного им пароля с паролем, сохраненным в базе данных.
7.	Авторизация — предоставление определенному лицу или группе лиц прав на выполнение определенных действий.
8.	Web-сокет – протокол связи поверх TCP-соединения, предназначенный для обмена сообщениями между браузером и web-сервером, используя постоянное соединение.
9.	Диспетчеризация – это процесс поиска и вызова необходимой функции или метода для уже известного типа данных.
10. API (application programming interface]) – программный интерфейс,  то есть описание способов взаимодействия одной компьютерной программы с другими (в противоположность пользовательскому интерфейсу, используемому для взаимодействия конечного пользователя с программой). Проще говоря, это способ взаимодействия какого-то программного кода с набором каких-то программных компонентов, с помощью которых одна компьютерная программа (например, бот или сайт) может использовать другую программу.
11. Масштабируемость – важный аспект электронных систем, программных комплексов, систем баз данных, маршрутизаторов, сетей и т.п., если для них требуется возможность работать под большой нагрузкой. Система называется масштабируемой, если она способна увеличивать производительность пропорционально дополнительным ресурсам.



















# 1.	Обзор популярных инструментов для разработки web-приложений на Python.

Python — это объектно-ориентированный, интерпретируемый и интерактивный язык программирования. Его изучение считается простым и лёгким для восприятия, в связи с чем он покорил многих разработчиков. Так же он является одним из самых быстроразвивающихся языков. Так же лидирующие позиции занимает рост популярности фреймворков на его основе. Фреймворки существуют для того, чтобы упрощать жизнь программисту. Они помогают экономить время, потому что благодаря им разработчик фокусируется на логике работы приложения, а не на рутинных задачах. Много современных компаний, например: Google, Facebook, Yandex, Dropbox. И выбор достаточно большой: Django, CherryPy, Puramid, TurboGerars, Web2Py, Flask, Bottle, Tornado, Web.py, FastAPI.
	В своей работе я рассмотрю 3 фреймворка, которые входят в самые популярные.

 # Django.




![image](https://github.com/user-attachments/assets/7202e70a-7a13-4b75-9986-684884c0dde6)

Это фреймворк с открытым исходным кодом, который позволяет разработчикам создавать web-приложения практически любого уровня. Он входит в число лучших фреймворков Python и заслуженно пользуется популярностью.
Для Django доступен колоссальный набор дополнительных библиотек и поддержка огромного сообщества разработчиков, что существенно упрощает и ускоряет разработку.

Ключевые особенности Django:

•	наличие собственного ORM;
•	встроенный административный интерфейс;
•	шаблонизатор;
•	библиотека работы с формами;
•	система кэширования и интернализации;
•	система авторизации и аутентификации.


# FastAPI.

![image](https://github.com/user-attachments/assets/9b498539-35ce-44ef-8fee-e348cb8a9c83)


Это асинхронный веб-фреймворк, который появился на свет в конце 2018 года. Он предназначен для быстрой разработки API-приложений и основан на использовании стандартной аннотации типов Python.
Слово «fast» в названии указывает не только на быструю разработку приложения, но и на производительность фреймворка. Как утверждает документация, согласно результатам независимых тестов, FastAPI по скорости не уступает приложениям, написанным на NodeJS или Go, а также это один из самых быстрых фреймворков на Python.
FastAPI сразу строился как асинхронный фреймворк, в отличие от имеющих долгую историю Django и Flask, которые изначально были синхронными и лишь в последние годы начали внедрять асинхронность.
FastAPI обычно применяется для разработки API, без фронтенда, но при желании его можно дополнить стандартными шаблонами на основе шаблонизатора, например Jinja2, который применяется во Flask.

Ключевые особенности FastAPI:

•	очень высокая производительность, наравне с NodeJS и Go;
•	встроенная документация на основе Swagger;
•	использование web-сокетов;
•	лёгкая интеграция с базами данных;
•	основан на стандартах OpenAPI и полностью совместим с ними.


# Flask.

![image](https://github.com/user-attachments/assets/2f87ea02-9353-44f1-8c6d-fb8b9a9eed72)

Это фреймворк с небольшим размером исходной кодовой базы, поэтому его называют микрофреймворком. Но это не значит, что у него меньше возможностей, чем у того же Django. По умолчанию он включает в себя только обработчик запросов и шаблонизатор, а простейшее приложение на Flask может состоять всего из нескольких строк. Разработчики этого фреймворка осознанно хотели сохранить ядро простым, но расширяемым.
Тем не менее с помощью Flask можно реализовать практически любую задачу: от простого одностраничного сайта до серьёзного проекта с авторизацией, аутентификацией и другими возможностями. Flask подходит для задач, которые подразумевают гибкость в выборе компонентов. Разработчик сам принимает решение, что ему пригодится в работе.
Flask лежит в основе таких крупных сервисов как Reddit, Netflix, Pinterest, Twilio и агрегатора такси Lyft.


Ключевые особенности Flask:

•	встроенный сервер разработки и отладчик;
•	диспетчеризация запросов в RESTful-стиле;
•	встроенная поддержка модульного тестирования;
•	использование шаблонизатора Jinja2;
•	100%-ная совместимость с WSGI 1.0;
•	множество расширений, предоставляемых сообществом.

# 2.	Изучение архитектуры каждого фреймворка.

# 2.1	Архитектура web-приложений на Django.


Django - это фреймворк, использующий шаблон проектирования Model-View-Controller (MVC).
Во многих статьях приводятся объяснения что такое MVC, схемы, а так же говорится о их неточности (несколько примеров: https://habr.com/ru/articles/321050/, https://habr.com/ru/articles/175465/). 

Обычно в таких схемах MVC описывают подобным образом:

•	Model — доступ к хранилищу данных
•	View — это интерфейс, с которым взаимодействует пользователь 
•	Controller — некий связывающий объект между model и view.

Данные распространенные схемы только запутывают и мешают, когда вы хотите написать приложение, в котором есть бизнес-логика.

Стоит обратить внимание на две вещи.
Первое, часто под M в MVC подразумевают — модель данных, и говорят, что это некий класс, который отвечает за предоставление доступа к базе данных. Что неверно, и не соответствует классическому MVC и его потомкам MV*. В классическом MVC под M подразумевается domain model — объектная модель домена, объединяющая данные и поведение. Если говорить точнее, то M в MVC это интерфейс к доменной модели, так как domain model это некий слой объектов, описывающий различные стороны определенной области бизнеса. Где одни объекты призваны имитировать элементы данных, которыми оперируют в этой области, а другие должны формализовать те или иные бизнес-правила.
Второе, в Django нет выделенного слоя controller, и когда говорят, что в Django слой views — это контроллер, не стоит этому верить. Нужно обратиться к официальной документации, а точнее к FAQ, тогда можно увидеть, что этот слой вписывается в принципы слоя View в MVC, особенно, если рассматривать DRF, а как такового слоя Controller в Django нет. Как говорится в FAQ, если вам очень хочется аббревиатур, то можно использовать в контексте Django аббревиатуру MTV (Model, Template, and View). Если очень хочется рассматривать Web MVC и сравнивать Django с другими фреймворками, то для простоты можно считать view контроллером.
Несмотря на то, что Django не соответствует MVC аббревиатуре, в ней реализуется главный смысл MVC – отделение бизнес-логики от логики представления данных. Но на практике это не всегда так.

Схематично можно представить архитектуру MVT в Django следующим образом:

![image](https://github.com/user-attachments/assets/31e32b1d-9716-437c-964a-8a71b88d66e5)

Основные элементы паттерна:
URL dispatcher: при получение запроса на основании запрошенного адреса URL определяет, какой ресурс должен обрабатывать данный запрос.
View: получает запрос, обрабатывает его и отправляет в ответ пользователю некоторый ответ. Если для обработки запроса необходимо обращение к модели и базе данных, то View взаимодействует с ними. Для создания ответа может применять Template или шаблоны. В архитектуре MVC этому компоненту соответствуют контроллеры (но не представления).
Model: описывает данные, используемые в приложении. Отдельные классы, как правило, соответствуют таблицам в базе данных.
Template: представляет логику представления в виде сгенерированной разметки html. В MVC этому компоненту соответствует View, то есть представления.
Когда к приложению приходит запрос, то URL dispatcher определяет, с каким ресурсом сопоставляется данный запрос и передает этот запрос выбранному ресурсу. Ресурс фактически представляет функцию или View, который получает запрос и определенным образом обрабатывает его. В процессе обработки View может обращаться к моделям и базе данных, получать из нее данные, или, наоборот, сохранять в нее данные. Результат обработки запроса отправляется обратно, и этот результат пользователь видит в своем браузере. Как правило, результат обработки запроса представляет сгенерированный html-код, для генерации которого применяются шаблоны (Template).

# 2.2	Архитектура web-приложений на FastAPI. 

Архитектура веб-приложений на FastAPI основана на принципах современного веб-разработки, которые обеспечивают производительность, простоту в использовании и поддержку асинхронного программирования. FastAPI — это асинхронный веб-фреймворк для Python, который отлично подходит для создания API на основе стандартов OpenAPI и JSON Schema. Вот основные аспекты архитектуры веб-приложений на FastAPI:
1.	Структура проекта
Стандартная структура проекта может выглядеть следующим образом:
```
my_fastapi_app/
│
├── app/                     # Основная папка приложения
│   ├── __init__.py          # Инициализация приложения
│   ├── main.py              # Точка входа для запуска приложения
│   ├── models.py            # Модели данных
│   ├── routes.py            # Определение маршрутов (эндпоинтов)
│   ├── schemas.py           # Схемы (например, для валидации входных данных)
│   ├── services/            # Логика бизнес-уровня
│   ├── database.py          # Настройки базы данных
│   └── utilities.py         # Вспомогательные функции
│
├── tests/                   # Тесты
│   └── test_routes.py       # Тесты для маршрутов
│
├── requirements.txt         # Зависимости
└── .venv                     # Переменные окружения
```
2.	Асинхронное программирование. FastAPI поддерживает асинхронные функции, что позволяет обрабатывать большее количество запросов одновременно. 
3.	Защита и аутентификация. FastAPI поддерживает OAuth2, JWT и другие методы аутентификации. Можно использовать встроенные зависимости для защиты маршрутов. 
4.	Автоматическая документация. FastAPI автоматически генерирует документацию для вашего API на основе аннотаций типов. Она доступна по адресам /docs (Swagger UI) и /redoc (ReDoc).
5.	Тестирование. FastAPI предоставляет простые методы для тестирования приложения с помощью библиотеки pytest. Можно использовать встроенный тестовый клиент для имитации запросов к API.
6.	Разделение логики приложения. Рабочая логика (сервисы) должна быть отделена от маршрутов, что улучшает поддержку приложения и тестируемость. Например, можно создать отдельный класс или набор функций для обработки бизнес-логики.

# 2.3	Архитектура web-приложений на Flask.

Архитектура веб-приложений на Flask основана на концепциях, которые обеспечивают модульность, расширяемость и поддержку.
Основные аспекты:
1.	Модульная структура проекта. Flask позволяет организовать код в модули, что делает проект более управляемым.
2.	Маршруты и представления (Views), В Flask маршруты устанавливаются с помощью декораторов. Каждый маршрут связан с функцией (представлением), которая обрабатывает запрос и возвращает ответ.
3.	Шаблоны и рендеринг. Flask использует Jinja2 для работы с шаблонами, что позволяет динамически вставлять данные в HTML. Шаблоны хранятся в папке templates, и их можно использовать для рендеринга HTML-страниц.
4.	Форма и валидация. Flask поддерживает обработку форм через библиотеку Flask-WTF, которая интегрирует настройки для защиты от CSRF и валидации форм.
5.	Модели и базы данных. Flask часто используется с SQLAlchemy для работы с базами данных. Можно определять модели, которые представляют таблицы базы данных.
6.	Конфигурация. Конфигурация приложения может быть вынесена в отдельный файл (например, config.py) и загружена во время инициализации приложения.
7.	Статические файлы. Статические файлы (например, CSS и JavaScript) размещаются в папке static, и к ним можно получить доступ через встроенные функции Flask.
8.	Расширяемость и пакетирование. Flask имеет множество расширений, которые можно добавить для улучшения функциональности, таких как:
•	Flask-Login — для управления аутентификацией пользователей.
•	Flask-Mail — для отправки электронной почты
•	Flask-Migrate — для управления миграциями базы данных.
9.	Тестирование. Flask поддерживает написание тестов с использованием библиотеки unittest. Можно тестировать маршруты, формы, модели и другое. 

# 3.	Сравнение производительности, безопасности и масштабируемости Django, Flask и FastAPI.

Django, Flask и FastAPI имеют свои сильные и слабые стороны. 

## Сравним производительность.

Если рассматривать Django, то это полнофункциональный фреймворк, в котором много встроенных функций, что может замедлять его при обработке запросов по сравнению с более простыми фреймворками. Но данный недостаток можно изменить в лучшую сторону с помощью кэширования и оптимизации баз данных.
Flask, являясь микро-фреймворком, обладает меньшим количеством встроенных функций, что делает его более лёгким и быстрым. В нём отсутствует сложная абстракция, и возможность более эффективно контролировать производительность. Основной недостаток – это необходимость привлекать сторонние библиотеки, которые могут повлиять на производительность.
 основан на асинхронном программировании, может обрабатывать большое количество параллельных запросов, что обеспечивает высокую производительность и скорость.  Он является одним из самых быстрых фреймворков для создания API. Несмотря на это, он так же имеет ряд недостатков. Также как и Flask он имеет необходимость привлекать сторонние библиотеки. Не имеет встроенной поддержки параллельных вычислений, что может привести к замедлению.
	
## Сравним безопасность.

Django имеет встроенные механизмы безопасности, которые защищают приложение от различных типов атак и уязвимостей. В него включена защита от многих распространённых web-угроз, таких как CSRF, XSS, SQL-инъекций кликджекинга. Так же в нём предложен механизм для управления пользователями и аутентификацией.
Flask так же содержит механизмы безопасности, однако их использование не так строго регламентировано как в Django. Для поддержки безопасности может потребоваться интеграция сторонни библиотек.
FastAPI, как и Django, имеет встроенные механизмы безопасности для работы с OAuth2, JWT и API-ключами. Однако защита от CSRF и XSS может потребовать более внимательного подхода к реализации. Имеет высокую гибкость в настройке безопасности.

## Сравним масштабируемость.

Django хорошо подходит для структурированных крупных приложений и может и может эффективно масштабироваться с использованием различных инструментов и подходов. Но в свою очередь это создаёт некоторые ограничения, связанные с производительностью, так как они могут замедлить масштабирование.
Flask благодаря своей легковесности и гибкости, позволяет легко создавать масштабируемые приложения. Начать с небольшого приложения и последовательно наращивать его функционал – это сильная сторона Flask, что делает его идеальным для стартапов и небольших проектов.
FastAPI изначально ориентирован на высокую производительность и асинхронную обработку запросов, что делает его подходящим для масштабируемых приложений, особенно в облачных системах и микросервисной архитектуре. Он отлично справляется с большим количеством параллельных запросов и подходит для работы с современными веб-технологиями, включая WebSocket.

# 4.	Выявление наиболее подходящего фреймворка для разработки web-приложений в зависимости от конкретных требований.

Выбор фреймворка зависит от конкретных потребностей проекта: 
Django подходит для создания крупных и сложных веб-приложений с богатым функционалом и высокой безопасностью, в особенности, когда важна быстрая разработка с использованием готовых решений. Примеры: интернет-магазины, социальные сети и платформы для взаимодействия с пользователями. 
Flask идеально подходит для проектов, где требуется легкость и гибкость. Это хороший выбор для небольших приложений и стартапов, где важно быстрое прототипирование и возможность "собирать" приложение по частям. Примеры: сайты-визитки. 
FastAPI подходит для высокопроизводительных приложений, особенно API, работающих с большим количеством одновременных подключений. Он идеально подходит для проектов, которым необходима скорость, масштабируемость и поддержка асинхронности. Примеры: системы реального времени (чаты). 

# 5.	Разработка простых web-приложений с использованием Django, Flask и FastAPI, их сравнение и анализ. 

В своём проекте я рассмотрю создание одного приложения с использованием Django, Flask и FastAPI. За идею я взял сайт-визитку для фирмы Candy Shop. Цель сайта – ознакомить людей, интересующихся кондитерскими изделиями, с работами фирмы. 

## Структура проекта.
Рисунок 1. Главная страница. На главной странице расположено основное меню, наследуемое на все остальные страницы. Ссылки наши работы, услуги, контакты и регистрация переводят на соответствующие страницы. Логотип "Капкейк" - это ссылка на главную страницу.
![1](https://github.com/ArturMukhametshin/Diplom/blob/master/Screenshots/Главная-страница.png)

Рисунок 2. Наши работы. На странице портфолио есть дополнительное меню, для выбора темы работ фирмы.
![2](https://github.com/ArturMukhametshin/Diplom/blob/master/Screenshots/Наши-работы.png)

Рисунок 3. Торты.
![3](https://github.com/ArturMukhametshin/Diplom/blob/master/Screenshots/Торты.png)

Рисунок 4. Капкейки.
![4](https://github.com/ArturMukhametshin/Diplom/blob/master/Screenshots/Капкейки.png)


Рисунок 5.  Пончики.
![5](https://github.com/ArturMukhametshin/Diplom/blob/master/Screenshots/Пончики.png)

Рисунок 6.  Национальные сладости.
![6](https://github.com/ArturMukhametshin/Diplom/blob/master/Screenshots/Национальные-сладости.png)

На страницах Торты, Капкейки, Пончики, Национальные сладости находятся изображения работ по темам, которые являются ссылками, для перехода на соответствующую страницу для ознакомления.

Рисунок 7.  Услуги.
![7](https://github.com/ArturMukhametshin/Diplom/blob/master/Screenshots/Услуги.png)

Рисунок 8.  Контакты.
![8](https://github.com/ArturMukhametshin/Diplom/blob/master/Screenshots/Контакты.png)

Рисунок 9.  Регистрация. На странице Регистрация производится регистрация пользователя.
![9](https://github.com/ArturMukhametshin/Diplom/blob/master/Screenshots/Регистрация.png)


## Проект c использованием Django.

## Схематичное изображение структуры проекта.

```
Web_Django/               
│
├── Turtle_Django/        
│    ├── manage.py
│    ├── db.sqlite3       
│    ├── Turtle_Django/    
│    │   ├── __init__.py
│    │   ├── asgi.py 
│    │   ├── settings.py    
│    │   ├── urls.py        
│    │   └── wsgi.py        
│    │
│    └── cherepaha/         
│    │   ├── migrations/    
│    │   ├── admin.py
│    │   ├──__init__.py
│    │   ├── apps.py
│    │   ├──forms.py        
│    │   ├── models.py
│    │   ├── tests.py     
│    │   ├── views.py      
│    │   ├── urls.py               
│    │   └── static/
│    │       ├── css/         
│    │       └── img/       
│    │       
│    │
│    └── templates/         
│        ├── architecture.html
│        ├── commercial_interiors.html
│        ├── contacts.html
│        ├── home_page.html
│        ├── improvement.html
│        ├── portfolio.html
│        ├── residential_interiors.html
│        ├── services.html
│        └── user_registration.html
└──venv/

```

Список необходимых библиотек:
```
asgiref==3.8.1
Django==5.1.3
django-phonenumber-field==8.0.0
phonenumbers==8.13.52
sqlparse==0.5.2
tzdata==2024.2
```

## Проект c использованием Flask.

## Схематичное изображение структуры проекта.
```
Web-Flask/
├── instanse
│   └── cherepaha.db
├── routers/
│   ├── main_menu.py
│   └── portfolio_menu.py
├── static/
│   ├── css/                 
│   └── img/                  
└── templates/
│   ├── architecture.html      
│   ├── commercial_interiors.html 
│   ├── contacts.html          
│   ├── home_page.html         
│   ├── improvement.html       
│   ├── portfolio.html         
│   ├── residential_interiors.html
│   ├── services.html
│   └── user_registration.html
├── config.py
├── db_cherepaha.py
├── forms.py
├── main.py      
└── venv/
```


Список необходимых библиотек:

```
blinker==1.9.0
click==8.1.7
colorama==0.4.6
dnspython==2.7.0
email_validator==2.2.0
Flask==3.1.0
Flask-SQLAlchemy==3.1.1
Flask-WTF==1.2.2
greenlet==3.1.1
idna==3.10
itsdangerous==2.2.0
Jinja2==3.1.4
MarkupSafe==3.0.2
phonenumbers==8.13.52
SQLAlchemy==2.0.36
typing_extensions==4.12.2
Werkzeug==3.1.3
WTForms==3.2.1
```

## Проект c использованием FastAPI.

## Схематичное изображение структуры проекта.
```
web-fast/
├── routers/
│   ├── main_menu.py
│   ├── portfolio_menu.py
│   └── user_registration.py
├── static/
│   ├── css/                 
│   └── img/                  
└── templates/
│   ├── architecture.html      
│   ├── commercial_interiors.html 
│   ├── contacts.html          
│   ├── home_page.html         
│   ├── improvement.html       
│   ├── portfolio.html         
│   ├── residential_interiors.html
│   ├── services.html
│   └── user_registration.html
├── cherepaha.db
├── forms.py
├── main.py     
└── venv/  
``` 


Список необходимых библиотек:

```
annotated-types==0.7.0
anyio==4.7.0
click==8.1.7
colorama==0.4.6
dnspython==2.7.0
email_validator==2.2.0
exceptiongroup==1.2.2
fastapi==0.115.6
greenlet==3.1.1
h11==0.14.0
idna==3.10
Jinja2==3.1.4
MarkupSafe==3.0.2
pydantic==2.10.3
pydantic_core==2.27.1
python-multipart==0.0.20
sniffio==1.3.1
SQLAlchemy==2.0.36
starlette==0.41.3
typing_extensions==4.12.2
uvicorn==0.32.1
```
## Анализ. 

<table>
    <thead>
        <tr>
            <th>Критерии </th>
            <th>Django</th>
            <th>Flask </th>
	    <th>FastAPI</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Встроенная функциональность</td>
            <td>Множество встроенных функций</td>
            <td>Для реализации функционала может потребовать интеграцию дополнительных пакетов</td>
	    <td>Для реализации функционала требует интеграцию дополнительных пакетов</td>
        </tr>
        <tr>
            <td>Структура проекта</td>
            <td>Мене гибкая, требует большего времени для изучения</td>
            <td>Минимальная и гибкая</td>
	    <td>Минимальная и гибкая</td>
        </tr>
        <tr>
            <td>Синтаксис</td>
            <td>Использует свои шаблоны для разметки HTML Управление маршрутами осуществляется через URLconf</td>
            <td>Простой, легко читается. Для обработки запросов и маршрутизации использует Python функции</td>
	    <td>Основывается на стандартных аннотациях Python для обработки данных. Удобные декораторы для маршрутизации и валидации данных</td>
        </tr>
        <tr>
            <td>Интегрируемость с различными модулями</td>
            <td>Имеет большое число сторонних библиотек и пакетов</td>
            <td>Поддерживает множество сторонних расширений, однако может потребовать больше настроек. Благодаря гибкости может легко интегрировать сторонние расширения, однако некоторые расширения могут быть несовместимы друг с другом</td>
	    <td>Быстро интегрируется с современными библиотеками, широкая поддержка асинхронных библиотек </td>
        </tr>
	<tr>
            <td>Объём занимаемой памяти с библиотеками</td>
            <td>121 МБ</td>
            <td>111 МБ</td>
	    <td> 76 МБ</td>
        </tr>
	<tr>
            <td>Объём занимаемой памяти без библиотек</td>
            <td>25.7 МБ</td>
            <td>25.6 МБ</td>
	    <td> 25.5 МБ</td>
        </tr>

    </tbody>
</table>



