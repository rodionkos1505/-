while True:
    import sys
    from tkinter import *
    from PIL import ImageTk

    canvas = Canvas(width = 2560, height = 1600, bg = 'blue')
    canvas.pack(expand = YES, fill = BOTH)

    image = ImageTk.PhotoImage(file = "Фон.png")
    canvas.create_image(0.5, 1, image = image, anchor = NW)

    print('Привет! Ты попал в игру "Города"! Называй название города, а я тебе введу другой город с названием, начинающимся на последнюю букву твоего. Ты тоже должен следовать этим правилам. Но повторять один и тот же город дважды нельзя! Погнали!')
    print('P.s.:Игра создана Родионом Косковым. Техподдржка по номеру: +7-916-373-08-79(Звонки или SMS)')
    input('Нажми "enter", чтобы начать! \n')
    last_sities=[]
    sities_a=["Абакан","Арзамас", "Астана", "Алматы", "Архангельск","Астрахань","Абу-Даби","Анапа","Анадырь","Армавир",'Анкара',"Адлер","Анагарск","Ашхабад","Альметьевск","Афины","Анталья","Ачинск","Артём","Алексин","Алушта","Алупка","Александрия","Авдеевка"]
    sities_b=['Барнаул',"Брянск","Благовещенск","Белград","Бишкек","Берлин","Баку","Бангкок","Балашиха","Братск","Бийск","Будапешт","Буэнос-Айрес","Брест","Батайск","Багдад","Биробаджан","Батуми","Бердянск"]
    sities_v=["Владивосток","Воронеж","Волгоград","Великий Новгород","Великий Устюг","Владимир","Воркута","Владикавказ","Вавилон","Вологда","Выборг","Вильнюс","Волжский","Витебск","Варшава","Вена","Венеция","Видное","Волгодонск","Великие Луки","Воскресенск","Валдай"]
    sities_g=['Грозный',"Геленджик","Гуанчжоу","Гомель","Горно-Алтайск","Гатчина","Гродно","Губкинский","Глазов","Гагра","Гавана","Гусь-Хрустальный","Галич","Гамбург","Губаха","Горячий Ключ","Губкин","Городец","Гаага","Гусев","Гай","Георгиевск","Гурзуф","Генуя","Глазго","Гудермес","Гжель"]
    sities_d=["Дубай","Душанбе","Дербент","Дзержинск","Дели","Детройт","Джакарта","Дубна","Дмитров","Дублин","Диксон","Дмитровград","Доха","Дамаск","Дудинка","Дакка","Джанкой","Дзержинский","Дивеево","Дагомыс","Дивногоск","Даллас","Донецк"]
    sities_e=["Екатеринбург","Ереван","Ейск","Ессентуки","Елабуга","Елец","Евпатория","Егорьевск","Енисейск","Елизово","Ефремов","Елань","Емажелинск","Ельня","Ермолино","Ерофей Павлович","Ершов","Елизаветинская","Емва","Елгава","Ермаковское","Егорлыкская","Еруда","Еткуль","Есентукская","Емельяново"]
    sities_zhe=["Железногоск","Железнодорожный","Жуковский","Жирона","Женева","Железноводск","Жигулёвск","Жостово","Жезказган","Жлобин","Жодино","Железногорск-Илимский","Жанаозен","Жирновск","Жуков","Жуковка","Жаркент"]
    sities_z=["Златоуст","Зеленоградск","Звенигород","Зеленодольск","Зеленогорск","Забайкальск","Зарайск","Заринск","Загреб","Зеленоград","Заречный","Зальцбург","Зея","Знаменск","Зима","Зугрэс","Заволжье","Заречный","Заполярный","Заводоуковск"]
    sities_i=["Ижевск","Иркутск","Иваново","Иерусалим","Иннополис","Ивантеевка","Исламбад","Ишим","Инта","Измир","Иерихон","Искитим","Ирбит","Ивангород","Играка","Ишимбай","Избербаш","Иу","Иокогама","Ивдель","Инкерман","Изобильный","Итиль"]
    sities_y=["Йошкар-Ола","Йоханнесбург","Йорк","Йена","Йыхви","Йезд","Йоэнсуу","Йеллоунайф","Йозгат","Йёнчёпинг","Йютербог","Йонъин"]
    sities_k=["Казань","Краснодар","Калининград","Красноярск","Киров","Калуга","Кострома","Кемерово","Курган","Курск","Канберра","Кисловодск","Караганда","Коломна","Кызыл","Керчь","Кингисепп","Копенгаген","Кишинёв","Кронштадт","Красная Поляна","Кировск","Кейптаун","Когалым","Королёв","Каменск-Уральский","Ковров","Клин","Костанай"]
    sities_l=["Лондон","Лос-Анджелес","Липецк","Лиссабон","Люберцы","Ливны","Лобня","Лыткарино","Лысьва","Львовский","Львовский","Лодьзь","Лас-Вегас","Лимасол","Лиский","Лангепас","Лима","Лион","Луга","Лабинск","Лесосибирск","Любляна","Ленинск-Кузнецкий","Луховицкий","Луганск"]
    sities_m=["Москва","Минск","Мурманск","Махачкала","Магадан","Магнитогоск","Майами","Минеральные Воды","Майкоп","Мытищи","Мадрид","Миасс","Муром","Милан","Мехико","Мекка","Мюнхен","Мирный","Мумбаи","Мурино","Можайск","Манила","Минусинск","Мичуринск","Мончегорск","Мельбурн"]
    sities_n=['Новосибирск',"Нижний Новгорд","Нью-Йорк","Норильск","Новороссийск","Новочеркасск","Набережные Челны","Новокузнецк","Новый Уренгой","Нижневартовск","Нижний Тагил","Невиномысск","Нальчик","Нижнекамск","Ногинск","Ноябрьск","Нарьян-Мар","Наро-Фоминск","Находка"]
    sities_o=["Омск","Оренбург","Орёл","Орск","Оймякон","Обнинск","Оттава","Одинцово","Осло","Орехово-Зуево","Обухово","Озёрск","Октябрьский","Оксфорд","Орша","Осака","Оленегорск","Окленд","Острогоржск","Отрадный","Онега","Осташков","Оха","Орландо","Оса","Остин","Отрадное","Озёры","Олонец","Олбани","Остров","Окуловка","Обь"]
    sities_p=["Пермь","Пекин","Петропавловск-Камчатский","Париж","Псков","Петрозаводск","Пенза","Пятигорск","Подольск","Прага","Переславль-Залесский","Паттайя","Припять","Пушкино","Павлодар","Первоуральск","Певек","Прокопьевск","Пхеньян","Помпеи","Пушкин","Петропавловск","Печора","Павловский Посад"]
    sities_r=["Ростов-на-Дону","Рязань","Рим","Рыбинск","Рига","Ростов","Ржев","Раменское","Реутов","Рио-Де-Жанейро","Рубцовск","Рейкьявик","Россошь","Руан","Радумля","Ревда","Рабат","Руза","Радужный","Рославль","Разметелево","Роттердам","Рузаевко","Риттер"]
    sities_s=["Санкт-Петербург","Самара","Саратов","Сочи","Сургут","Севастополь","Ставрополь","Стамбул","Смоленск","Сыктывкар","Симферополь","Саранск","Суздаль","Самарканд","Салехард","Стокгольм","Сергиев Посад","Стерлитамак","Старый Оскол","Северодвинск","Серпухов","Сан-Франциско","Сидней","Сортавала"]
    sities_t=["Тюмень","Ташкент","Тольятти","Томск","Тверь","Тула","Таганрог","Тбилиси","Тамбов","Тобольск","Таллин","Териберка","Торонто","Туапсе","Тегеран","Троицк","Троя","Тараз","Тында","Трёхгорный","Торжок","Тель-Авив","Тихвин","Тихорецк","Тарко-Сале"]
    sities_u=["Уфа","Улан-Уде","Ульяновск","Уссурийск","Ухта","Усть-Кут","Улан-Батор","Уральск","Усть-Каменогорск","Углич","Усинск","Усть-Илимск","Усть-Луга","Урай","Усолье-Сибирское","Урюпинск","Усть-Лабинск","Уренгой","Удомля","Умаг","Ургенч","Ужгород","Учалы"]
    sities_f=["Феодосия","Фанкфурт-на-Майне","Флоренция","Фуджейра","Филадельфия","Фрязино","Фергана","Фетихе","Финикс","Фивы","Фурманов","Фролово","Фокино","Форос","Фантхьет","Фукуока","Фряново","Фес","Форшань","Февральск","Фаниполь","Фамагуста"]
    sities_h=["Хабаровск","Харп","Хургада","Ханты-Мансийск","Химки","Хельсинки","Харбин","Хошимин","Ханой","Худжанд","Херсонес Таврический","Хасавюрт","Хьюстон","Ханчжоу","Хэйхэ","Хайфа","Хайфа","Хиросима","Хвалынск","Хиккадува","Хотьково","Хива","Хатанга"]
    sities_c=["Циндао","Цюрих","Цхинвал","Цзинань","Циолковский","Цинциннати","Цимилянск","Цивильск","Цахкадзор","Цандрыпш","Цзиньхуа","Цыган Аман","Цибанобалка","Целина","Цесис","Цицикар","Цхалтубо","Цетине","Цуг","Цзясин","Цзыбо","Цзинин"]
    sities_che=["Челябинск","Чебоксары","Чита","Чернобыль","Череповец","Чикаго","Чайковский","Чекалин","Черкесск","Чуницин","Чехов","Часов Яр","Черногоск","Черноголовка","Чэнду","Чебаркуль","Чистополь","Черкассы","Чусовой","Черняховск","Чернушка","Черновцы"]
    sities_sha=["Шарм-эш-Шейх","Шанхай","Шушары","Шымкент","Шахты","Шэньчжень","Шарджа","Шуя","Шлиссербург","Шадринск","Шебекино","Шарья","Штутгарт","Шумерля","Шатура","Шэньян","Шарыпово","Шелехов","Шерегеш","Шексна","Шахунья"]
    sities_sca=["Щёлково","Щербинка","Щёкино","Щёлкино","Щецыин","Щигры","Щучинск","Щельяюр","Щучин","Щучье","Щапово","Щеглово","Щелкун","Щебетовка"]
    sities_ee=["Электросталь","Элиста","Энгельс","Эр-Рияд","Экибазур","Эрбиль","Эдинбург","Электроугли","Эль-Фуджайра","Эстосадок","Эфес","Электрогорск","Эгвекинот"]
    sities_yu=["Южно-Сахалинск","Югра","Югорск","Юрьев-Польский","Южноуральск","Юрмала","Юкки","Южно-Курильск","Юрьевец","Юрюзань","Южный","Юхнов","Юбилейный","Южа","Юсьва","Юма","Юрамыш"]
    sities_ya=["Ярославль","Якутск","Ялта","Яблоново","Яблоново","Ярцево","Яя","Яхрома","Ялуторовск","Янтарный","Ямбург","Яблоновский","Янгон","Янаул","Яровое","Яшкино"]
    sites_vse=["Абакан","Арзамас", "Астана", "Алматы", "Архангельск","Астрахань","Абу-Даби","Анапа","Анадырь","Армавир",'Анкара',"Адлер","Анагарск","Ашхабад","Альметьевск","Афины","Анталья","Ачинск","Артём","Алексин","Алушта","Алупка","Александрия",'Барнаул',"Брянск","Благовещенск","Белград","Бишкек","Берлин","Баку","Бангкок","Балашиха","Братск","Бийск","Будапешт","Буэнос-Айрес","Брест","Батайск","Багдад","Биробаджан","Батуми","Владивосток","Воронеж","Волгоград","Великий Новгород","Великий Устюг","Владимир","Воркута","Владикавказ","Вавилон","Вологда","Выборг","Вильнюс","Волжский","Витебск","Варшава","Вена","Венеция","Видное","Волгодонск","Великие Луки","Воскресенск","Валдай",'Грозный',"Геленджик","Гуанчжоу","Гомель","Горно-Алтайск","Гатчина","Гродно","Губкинский","Глазов","Гагра","Гавана","Гусь-Хрустальный","Галич","Гамбург","Губаха","Горячий Ключ","Губкин","Городец","Гаага","Гусев","Гай","Георгиевск","Гурзуф","Генуя","Глазго","Гудермес","Гжель","Дубай","Душанбе","Дербент","Дзержинск","Дели","Детройт","Джакарта","Дубна","Дмитров","Дублин","Диксон","Дмитровград","Доха","Дамаск","Дудинка","Дакка","Джанкой","Дзержинский","Дивеево","Дагомыс","Дивногоск","Даллас","Екатеринбург","Ереван","Ейск","Ессентуки","Елабуга","Елец","Евпатория","Егорьевск","Енисейск","Елизово","Ефремов","Елань","Емажелинск","Ельня","Ермолино","Ерофей Павлович","Ершов","Елизаветинская","Емва","Елгава","Ермаковское","Егорлыкская","Еруда","Еткуль","Есентукская","Емельяново","Железногоск","Железнодорожный","Жуковский","Жирона","Женева","Железноводск","Жигулёвск","Жостово","Жезказган","Жлобин","Жодино","Железногорск-Илимский","Жанаозен","Жирновск","Жуков","Жуковка","Жаркент","Златоуст","Зеленоградск","Звенигород","Зеленодольск","Зеленогорск","Забайкальск","Зарайск","Заринск","Загреб","Зеленоград","Заречный","Зальцбург","Зея","Знаменск","Зима","Зугрэс","Заволжье","Заречный","Заполярный","Заводоуковск","Ижевск","Иркутск","Иваново","Иерусалим","Иннополис","Ивантеевка","Исламбад","Ишим","Инта","Измир","Иерихон","Искитим","Ирбит","Ивангород","Играка","Ишимбай","Избербаш","Иу","Иокогама","Ивдель","Инкерман","Изобильный","Итиль","Йошкар-Ола","Йоханнесбург","Йорк","Йена","Йыхви","Йезд","Йоэнсуу","Йеллоунайф","Йозгат","Йёнчёпинг","Йютербог","Йонъин","Казань","Краснодар","Калининград","Красноярск","Киров","Калуга","Кострома","Кемерово","Курган","Курск","Канберра","Кисловодск","Караганда","Коломна","Кызыл","Керчь","Кингисепп","Копенгаген","Кишинёв","Кронштадт","Красная Поляна","Кировск","Кейптаун","Когалым","Королёв","Каменск-Уральский","Ковров","Клин","Костанай","Киев","Лондон","Лос-Анджелес","Липецк","Лиссабон","Люберцы","Ливны","Лобня","Лыткарино","Лысьва","Львовский","Львовский","Лодьзь","Лас-Вегас","Лимасол","Лиский","Лангепас","Лима","Лион","Луга","Лабинск","Лесосибирск","Любляна","Ленинск-Кузнецкий","Луховицкий","Луганск","Москва","Минск","Мурманск","Махачкала","Магадан","Магнитогоск","Майами","Минеральные Воды","Майкоп","Мытищи","Мадрид","Миасс","Муром","Милан","Мехико","Мекка","Мюнхен","Мирный","Мумбаи","Мурино","Можайск","Манила","Минусинск","Мичуринск","Мончегорск","Мельбурн",'Новосибирск',"Нижний Новгорд","Нью-Йорк","Норильск","Новороссийск","Новочеркасск","Набережные Челны","Новокузнецк","Новый Уренгой","Нижневартовск","Нижний Тагил","Невиномысск","Нальчик","Нижнекамск","Ногинск","Ноябрьск","Нарьян-Мар","Наро-Фоминск","Находка","Неаполь","Нурлан","Нижний Новгород","Омск","Оренбург","Орёл","Орск","Оймякон","Обнинск","Оттава","Одинцово","Осло","Орехово-Зуево","Обухово","Озёрск","Октябрьский","Оксфорд","Орша","Осака","Оленегорск","Окленд","Острогоржск","Отрадный","Онега","Осташков","Оха","Орландо","Оса","Остин","Отрадное","Озёры","Олонец","Олбани","Остров","Окуловка","Обь","Пермь","Пекин","Петропавловск-Камчатский","Париж","Псков","Петрозаводск","Пенза","Пятигорск","Подольск","Прага","Переславль-Залесский","Паттайя","Припять","Пушкино","Павлодар","Первоуральск","Певек","Прокопьевск","Пхеньян","Помпеи","Пушкин","Петропавловск","Печора","Павловский Посад","Ростов-на-Дону","Рязань","Рим","Рыбинск","Рига","Ростов","Ржев","Раменское","Реутов","Рио-Де-Жанейро","Рубцовск","Рейкьявик","Россошь","Руан","Радумля","Ревда","Рабат","Руза","Радужный","Рославль","Разметелево","Роттердам","Рузаевко","Риттер","Санкт-Петербург","Самара","Саратов","Сочи","Сургут","Севастополь","Ставрополь","Стамбул","Смоленск","Сыктывкар","Симферополь","Саранск","Суздаль","Самарканд","Салехард","Стокгольм","Сергиев Посад","Стерлитамак","Старый Оскол","Северодвинск","Серпухов","Сан-Франциско","Сидней","Тюмень","Ташкент","Тольятти","Томск","Тверь","Тула","Таганрог","Тбилиси","Тамбов","Тобольск","Таллин","Териберка","Торонто","Туапсе","Тегеран","Троицк","Троя","Тараз","Тында","Трёхгорный","Торжок","Тель-Авив","Тихвин","Тихорецк","Тарко-Сале","Уфа","Улан-Уде","Ульяновск","Уссурийск","Ухта","Усть-Кут","Улан-Батор","Уральск","Усть-Каменогорск","Углич","Усинск","Усть-Илимск","Усть-Луга","Урай","Усолье-Сибирское","Урюпинск","Усть-Лабинск","Уренгой","Удомля","Умаг","Ургенч","Ужгород","Учалы","Феодосия","Фанкфурт-на-Майне","Флоренция","Фуджейра","Филадельфия","Фрязино","Фергана","Фетихе","Финикс","Фивы","Фурманов","Фролово","Фокино","Форос","Фантхьет","Фукуока","Фряново","Фес","Форшань","Февральск","Фаниполь","Фамагуста","Хабаровск","Харп","Хургада","Ханты-Мансийск","Химки","Хельсинки","Харбин","Хошимин","Ханой","Худжанд","Херсонес Таврический","Хасавюрт","Хьюстон","Ханчжоу","Хэйхэ","Хайфа","Хайфа","Хиросима","Хвалынск","Хиккадува","Хотьково","Хива","Хатанга","Циндао","Цюрих","Цхинвал","Цзинань","Циолковский","Цинциннати","Цимилянск","Цивильск","Цахкадзор","Цандрыпш","Цзиньхуа","Цыган Аман","Цибанобалка","Целина","Цесис","Цицикар","Цхалтубо","Цетине","Цуг","Цзясин","Цзыбо","Цзинин","Челябинск","Чебоксары","Чита","Чернобыль","Череповец","Чикаго","Чайковский","Чекалин","Черкесск","Чуницин","Чехов","Часов Яр","Черногоск","Черноголовка","Чэнду","Чебаркуль","Чистополь","Черкассы","Чусовой","Черняховск","Чернушка","Черновцы","Шарм-эш-Шейх","Шанхай","Шушары","Шымкент","Шахты","Шэньчжень","Шарджа","Шуя","Шлиссербург","Шадринск","Шебекино","Шарья","Штутгарт","Шумерля","Шатура","Шэньян","Шарыпово","Шелехов","Шерегеш","Шексна","Шахунья","Щёлково","Щербинка","Щёкино","Щёлкино","Щецыин","Щигры","Щучинск","Щельяюр","Щучин","Щучье","Щапово","Щеглово","Щелкун","Щебетовка","Электросталь","Элиста","Энгельс","Эр-Рияд","Экибазур","Эрбиль","Эдинбург","Электроугли","Эль-Фуджайра","Эстосадок","Эфес","Электрогорск","Эгвекинот","Южно-Сахалинск","Югра","Югорск","Юрьев-Польский","Южноуральск","Юрмала","Юкки","Южно-Курильск","Юрьевец","Юрюзань","Южный","Юхнов","Юбилейный","Южа","Юсьва","Юма","Юрамыш","Ярославль","Якутск","Ялта","Яблоново","Яблоново","Ярцево","Яя","Яхрома","Ялуторовск","Янтарный","Ямбург","Яблоновский","Янгон","Янаул","Яровое","Яшкино","Донецк","Авдеевка","Бердянск","Луганск"]    
    while True:
        gorod_igroka=input('Введите город!\n')
        nado_bukvu=gorod_igroka[-1]
        nado_bukvu=nado_bukvu.lower()
        gorod_igroka=gorod_igroka.title()
        if gorod_igroka== 'Сдаюсь':
            print("Ты круто играл! Молодец! Пока!")
            sys.exit(0) 
        if gorod_igroka in last_sities:
            print('Такой город уже был! ')
            continue
        last_sities.append(gorod_igroka)
        if  gorod_igroka in sites_vse:
            if nado_bukvu=='а' :
                print(sities_a[0])
                del sities_a[0]
            elif nado_bukvu=='б':
                print(sities_b[0])
                del sities_b[0]
            elif nado_bukvu=='в':
                print(sities_v[0])
                del sities_v[0]
            elif nado_bukvu=='г':
                print(sities_g[0])
                del sities_g[0]
            elif nado_bukvu=='д':
                print(sities_d[0])
                del sities_d[0]
            elif nado_bukvu=='е':
                print(sities_e[0])
                del sities_e[0]
            elif nado_bukvu=='ж':
                print(sities_zhe[0])
                del sities_zhe[0]
            elif nado_bukvu=='з':
                print(sities_z[0])
                del sities_z[0]
            elif nado_bukvu=='и':
                print(sities_i[0])
                del sities_i[0]
            elif nado_bukvu=='й':
                print(sities_y[0])
                del sities_y[0]
            elif nado_bukvu=='к':
                print(sities_k[0])
                del sities_k[0]
            elif nado_bukvu=='л':
                print(sities_l[0])
                del sities_l[0]
            elif nado_bukvu=='м':
                print(sities_m[0])
                del sities_m[0]
            elif nado_bukvu=='н':
                print(sities_n[0])
                del sities_n[0]
            elif nado_bukvu=='о':
                print(sities_o[0])
                del sities_o[0]
            elif nado_bukvu=='п':
                print(sities_p[0])
                del sities_p[0]
            elif nado_bukvu=='р':
                print(sities_r[0])
                del sities_r[0]
            elif nado_bukvu=='с':
                print(sities_s[0])
                del sities_s[0]
            elif nado_bukvu=='т':
                print(sities_t[0])
                del sities_t[0]
            elif nado_bukvu=='у':
                print(sities_u[0])
                del sities_u[0]
            elif nado_bukvu=='ф':
                print(sities_f[0])
                del sities_f[0]
            elif nado_bukvu=='х':
                print(sities_h[0])
                del sities_h[0]
            elif nado_bukvu=='ц':
                print(sities_c[0])
                del sities_c[0]
            elif nado_bukvu=='ч':
                print(sities_che[0])
                del sities_che[0]
            elif nado_bukvu=='щ':
                print(sities_sca[0])
                del sities_sca[0]
            elif nado_bukvu=='э':
                print(sities_ee[0])
                del sities_ee[0]
            elif nado_bukvu=='ю':
                print(sities_yu[0])
                del sities_yu[0]
            elif nado_bukvu=='я':
                print(sities_ya[0])
                del sities_ya[0]
            elif nado_bukvu=='ь' or nado_bukvu=='ы' or nado_bukvu=='ъ':
                nado_bukvu=gorod_igroka[-2]
                nado_bukvu=nado_bukvu.lower()
                gorod_igroka=gorod_igroka.lower()
                if nado_bukvu=='а':
                    print(sities_a[0])
                    del sities_a[0]
                elif nado_bukvu=='б':
                    print(sities_b[0])
                    del sities_b[0]
                elif nado_bukvu=='в':
                    print(sities_v[0])
                    del sities_v[0]
                elif nado_bukvu=='г':
                    print(sities_g[0])
                    del sities_g[0]
                elif nado_bukvu=='д':
                    print(sities_d[0])
                    del sities_d[0]
                elif nado_bukvu=='е':
                    print(sities_e[0])
                    del sities_e[0]
                elif nado_bukvu=='ж':
                    print(sities_zhe[0])
                    del sities_zhe[0]
                elif nado_bukvu=='з':
                    print(sities_z[0])
                    del sities_z[0]
                elif nado_bukvu=='и':
                    print(sities_i[0])
                    del sities_i[0]
                elif nado_bukvu=='й':
                    print(sities_y[0])
                    del sities_y[0]
                elif nado_bukvu=='к':
                    print(sities_k[0])
                    del sities_k[0]
                elif nado_bukvu=='л':
                    print(sities_l[0])
                    del sities_l[0]
                elif nado_bukvu=='м':
                    print(sities_m[0])
                    del sities_m[0]
                elif nado_bukvu=='н':
                    print(sities_n[0])
                    del sities_n[0]
                elif nado_bukvu=='о':
                    print(sities_o[0])
                    del sities_o[0]
                elif nado_bukvu=='п':
                    print(sities_p[0])
                    del sities_p[0]
                elif nado_bukvu=='р':
                    print(sities_r[0])
                    del sities_r[0]
                elif nado_bukvu=='с':
                    print(sities_s[0])
                    del sities_s[0]
                elif nado_bukvu=='т':
                    print(sities_t[0])
                    del sities_t[0]
                elif nado_bukvu=='у':
                    print(sities_u[0])
                    del sities_u[0]
                elif nado_bukvu=='ф':
                    print(sities_f[0])
                    del sities_f[0]
                elif nado_bukvu=='х':
                    print(sities_h[0])
                    del sities_h[0]
                elif nado_bukvu=='ц':
                    print(sities_c[0])
                    del sities_c[0]
                elif nado_bukvu=='ч':
                    print(sities_che[0])
                    del sities_che[0]
                elif nado_bukvu=='щ':
                    print(sities_sca[0])
                    del sities_sca[0]
                elif nado_bukvu=='э':
                    print(sities_ee[0])
                    del sities_ee[0]
                elif nado_bukvu=='ю':
                    print(sities_yu[0])
                    del sities_yu[0]
                elif nado_bukvu=='я':
                    print(sities_ya[0])
                    del sities_ya[0]

                else:
                    print("Бро, у тебя русская раскладка?!")
        else:
            print('Такого города нет! Попробуй другой! \nP.s.Если хочешь доказать, что такой город существует, напиши в техподдержку!')
