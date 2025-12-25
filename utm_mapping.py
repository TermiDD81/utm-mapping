# Паттерны для бесплатных поставщиков с их названиями
free_patterns = {
        "pp": "pp",
        "pesok": "Песок",
        "ndzokt5": "pp",
        "perezakokt4": "pp",       
        "replay": "Replay", 
        "replаy": "Replay",        
        "dubl": "Дубли",
        "dblvrn": "Двойная воронка",
        "otval": "Отвал",
        "mod": "pp",
        "dlsbp": "pp"
        }

# Список правил для определения поставщика
priority_rules = [
        ("dmp", "ДМП"),
        ("dmpone", "ДМП"),
        ("dmpnew", "ДМП"),       
        ("wr", "ВР"),
        ("rt", "Ростелеком"),
        ("t2", "Теле2"),
        ("lagom", "Игорь"),
        ("kokos", "Кокос"),
        ("vk", "ВКонтакте"),
        ("robot", "Robot_maks"),
        ("datacall", "Datacall"),
        ("alex", "Alex"),
        ("avito", "Avito"),
        ("reffection", "Рефекшн кинетик"),
        ("yandex", "Яндекс"),
        ("mk", "Яндекс"),
        ("spam", "Яндекс"),
        ("tg", "Telegram"),
        ("knowhow", "Ноухау"),
        ("khownow", "Ноухау"),
        ("voip", "gn_voip"),
        ("smstraf", "СМСтраф"),
        ("karl", "Карл"),
        ("andr", "Андрей"),
        ("botto", "Botto"),
        ("rasim", "Rasim"),
        ("scoring", "Скоринг"),
        ("bs", "Скоринг"),
        ("beeline", "Скоринг"),
        ("ipoteka", "Тест"),
        ("kirill", "Кирилл"),
        ("ngslb", "Нэтгроуслаб"),
        ("naumen", "Наумен"),
        ("robovoice", "Робовойс"), 
    ]

# Паттерны для направлений
project_rules = [
    ('rf', 'Недвижимость (пр)'),
    ('бп', 'Недвижимость (бп)'),
    ('bp', 'Недвижимость (бп)'),
    ('perevod', 'Перевод звонка'),
    ('jk', 'ЖК'),
    ('avto', 'Авто'),
    ('bank', 'Банковские гарантии'),
    ('spectehnika', 'Спецтехника'),
    ('lising', 'Лизинг'),
    ('arenda', 'Аренда спецтехники'),
    ('dev', 'dev'),
    ('naumen', 'dev'),
    ('robovoice', 'dev'),
]

# Паттерны для проектов
project2_rules = [
    ('avtoperevod', 'Авто Перевод звонка'),
    ('lidact', 'ЖК Лидактив'),
    ('zastr', 'ЖК Застройщики'),
    ('msk', 'Москва'),
    ('spb', 'Санкт-Петербург'),
    ('spb1', 'Санкт-Петербург'),
    ('krd', 'Краснодар'),
    ('rnd', 'Ростов'),    
    ('vld', 'Владивосток'),
    ('vladivostok', 'Владивосток'),    
    ('adygea', 'Адыгея'),
    ('arhangelsk', 'Архангельск'),
    ('arkhangelsk', 'Архангельск'),
    ('astrah', 'Астрахань'),
    ('bashkir', 'Уфа'),
    ('tatarstan', 'Уфа'),
    ('ufa', 'Уфа'),
    ('ekb', 'Екатеринбург'),    
    ('kazan', 'Казань'),
    ('kaliningrad', 'Калининград'),
    ('kaluga', 'Калуга'),
    ('krasnoyrsk', 'Красноярск'),
    ('krasnoyarsk', 'Красноярск'),
    ('crimea', 'Крым'),
    ('сrimea', 'Крым'),
    ('nn', 'Нижний Новгород'),
    ('novosib', 'Новосибирск'),
    ('novocib', 'Новосибирск'),
    ('perm', 'Пермь'),
    ('tula', 'Тула'),
    ('tyumen', 'Тюмень'),
    ('tumen', 'Тюмень'),
    ('udmurt', 'Удмуртия'),
    ('hmao', 'ХМАО'),
    ('khanty', 'ХМАО'),
    ('khabarovsk', 'Хабаровск'),
    ('cheliabinsk', 'Челябинск'),
    ('chel', 'Челябинск'),
    ('chelyabinsk', 'Челябинск'),
    ('yaroslavl', 'Ярославль'),
    ('izhevsk', 'Ижевск'),
    ('mytishchi', 'Мытищи'),
    ('narofominsk', 'Наро-Фоминск'),
    ('dubna', 'Дубна'),
    ('klin', 'Клин'),
    ('noginsk', 'Ногинск'),
    ('khotcovo', 'Хотьково'),
    ('vyborg', 'Выборг'),
    ('viborg', 'Выборг'),
    ('kirovsk', 'Кировск'),
    ('communar', 'Коммунар'),
    ('sochi', 'Сочи'),
    ('novoros', 'Новороссийск'),
]

# Паттерны для Марок автомабилей
avto_rules = [
    ('polar', 'Polar Stone (Полар Стоун) - китай'),
    ('lexus', 'LEXUS (Лексус) - Япония'),
    ('faw', 'FAW (Фав) - Китай'),
    ('gac', 'GAC (Гак) - Китай'),
    ('evolute', 'EVOLUTE (Эволют) - Россия'),
    ('nissan', 'NISSAN (Ниссан) - Япония'),
    ('omoda', 'OMODA (Омода) - Китай'),
    ('polestar', 'POLESTAR (Полестар) - Швеция'),
    ('jetta', 'JETTA (Джетта) - Китай'),
    ('kaiyi', 'KAIYI (Кайюй) - Китай'),
    ('kia', 'KIA (Киа) - Корея'),
    ('lynk', 'LYNK CO (Линк энд Ко) - Китай, Швеция'),
    ('renault', 'RENAULT (Рено) - Франция'),
    ('rivian', 'RIVIAN (Ривиан) - США'),
    ('skoda', 'SKODA (Шкода) - Чехия'),
    ('skywell', 'SKYWELL (Скайвел) - Китай'),
    ('ravon', 'RAVON (Равон) - Узбекистан'),
    ('suzuki', 'SUZUKI (Сузуки) - Япония'),
    ('chevrolet', 'CHEVROLET (Шевроле) - США'),
    ('citroen', 'CITROEN (Ситроен) - Франция'),
    ('datsun', 'DATSUN (Датсун) - Япония'),
    ('dongfeng', 'DONGFENG (Дунфэн) - Китай'),
    ('uaz', 'UAZ (УАЗ) - Россия'),
    ('moskvich', 'MOSKVICH (Москвич) - Россия'),
    ('changan', 'CHANGAN (Чанъянь, Шанань) - Китай'),
    ('chery', 'CHERY (Чери) - Китай'),
    ('exeed', 'CHERYEXEED (ЧериЭксид) - Китай'),
    ('isuzu', 'ISUZU (Исудзу) - Япония'),
    ('jac', 'JAC (Джак) - Китай'),
    ('jetour', 'JETOUR (ЦзеТу) - Китай'),
    ('ssang', 'SSANG_YONG (Ссан-Ён) - Корея'),
    ('toyota', 'TOYOTA (Тойота) - Япония'),
    ('volvo', 'VOLVO (Вольво) - Швеция'),
    ('volkswagen', 'VOLKSWAGEN (Фольксваген) - Германия'),
    ('lada', 'VAZ (ВАЗ) - Россия'),
    ('vaz', 'VAZ (ВАЗ) - Россия'),
    ('baic', 'BAIC (Бэй Ци) - Китай'),
    ('audi', 'AUDI (Ауди) - Германия'),
    ('bmw', 'BMW (Бэ-эм-вэ) - Германия'),
    ('byd', 'BYD (Биайди) - Китай'),
    ('porsche', 'Porsche (Порше) - Германия'),
    ('land', 'Land Rover (Ландровер) - Великобритания'),
    ('exlantix', 'Exlantix (Экслантикс) - Китай'),
    ('foton', 'Foton (Фотон) - Китай'),
    ('jmc', 'JMC (Джи Эм Си) - США'),
    ('zotye', 'Zotye (Зоти) - Китай'),
    ('brilliance', 'Brilliance (Брилианс) - Китай'),
    ('hafei', 'Hafei (Хафей) - Китай'),
    ('haval', 'HAVAL (Хавэйл) - Китай'),
    ('honda', 'HONDA (Хонда) - Япония'),
    ('hiphi', 'HIPHI (ХиПхи) - Китай'),
    ('great', 'GREAT WALL (Грейт Уолл) - Китай'),
    ('hyundai', 'HYUNDAI (Хёндэ) - Корея'),
    ('lixiang', 'LIXIANG (Лисянь) - Китай'),
    ('voyah', 'VOYAH (Войя) - Китай'),
    ('infiniti', 'INFINITI (Инфинити) - Япония'),
    ('geely', 'GEELY (Джили) - Китай'),
    ('genesis', 'GENESIS (Дженезис) - Корея'),
    ('gmc', 'GMC (Джи-Эм-Си) - США'),
    ('hongqi', 'HONGQI (Хунцы) - Китай'),
    ('lifan', 'LIFAN (Лифан) - Китай'),
    ('mazda', 'MAZDA (Мазда) - Япония'),
    ('nio', 'NIO (Нио) - Китай'),
    ('mitsubishi', 'MITSUBISHI (Мицубиси) - Япония'),
    ('mercedes', 'MERCEDES (Мерседес) - Германия'),
    ('tank', 'TANK (Тэнк) - Китай'),
    ('livan', 'Livan (Ливэн) - Китай'),
    ('jaecoo', 'Jaecoo (Джейку) - Китай'),
    ('aito', 'Aito (Эйто) - китай'),
    ('avatr', 'Avatr (Аватр) - китай'),
    ('belgee', 'Belgee (Белджи) - китай/белоруссия'),
    ('forthing', 'Forthing (Фортинг) - китай'),
    ('haima', 'Haima (Хайма) - китай'),
    ('huawei', 'Huawei (Хуавэй) - китай'),
    ('solaris', 'Solaris (Солярис) - корея'),
    ('sollers', 'Sollers (Соллерс) - россия'),
    ('m-hero', 'M-Hero (Эм-Хиро) - китай'),
    ('ora', 'Ora (Ора) - китай'),
    ('oshan', 'Oshan (Ошан) - китай'),
    ('oting', 'Oting (Отинг) - китай'),
    ('seres', 'Seres (Серес) - китай'),
    ('seres-aito', 'Seres Aito (Серес Аито) - китай'),
    ('soueast', 'Soueast (Соуист) - китай'),
    ('swm', 'SWM (Эс-Вэ-Эм) - китай'),
    ('venucia', 'Venucia (Венеция) - китай'),
    ('vgv', 'VGV (Видживи) - китай'),
    ('wey', 'Wey (Вэй) - китай'),
    ('zeekr', 'Zeekr (Зикр) - китай'),
]

#Паттерны для проектов ЖК
jk_project = [
('centralnyi', 'ЖК Астрахань Центральный'),
('klub25', 'ЖК Владивосток Клуб 25'),
('pogoda', 'ЖК Пермь'),
('ask', 'ЖК Краснодар АСК'),
('grani', 'ЖК Краснодар АСК'),
('we', 'ЖК Пермь'),
('belyaeva', 'ЖК Пермь'),
('sostoyanie', 'ЖК Ростов Состояние'),
('meridian', 'ЖК Тюмень Меридиан'),
('ecos', 'ЖК Санкт-Петербург Экос'),
('riviera', 'ЖК Ростов Ривьера'),

('arhitektor', 'ЖК Владивосток Архитектор'),
('kashtan', 'ЖК Владивосток Каштановый двор'),
('futurist', 'ЖК Владивосток Футурист'),
('ozero', 'ЖК Краснодар Дом у озера'),
('plaza', 'ЖК Краснодар Плаза'),
('sport', 'ЖК Краснодар Спортивная деревня'),
('rodnoy', 'ЖК Краснодар Родной дом'),
('sobytiye', 'ЖК Ростов Событие'),

('1799', 'ЖК Ростов Комфорт'),
('stolicyno', 'ЖК Ростов Комфорт'),
('serdtse2', 'ЖК Ростов Комфорт'),
('october', 'ЖК Ростов Комфорт'),
('nord', 'ЖК Ростов Комфорт'),
('levoberezhe', 'ЖК Ростов Комфорт'),
('legenda', 'ЖК Ростов Комфорт'),
('gray', 'ЖК Ростов Комфорт'),
('frame', 'ЖК Ростов Комфорт'),
('dvizhenie61', 'ЖК Ростов Комфорт'),
('donskoy', 'ЖК Ростов Комфорт'),
('flora', 'ЖК Ростов Комфорт'),
('manhjetten', 'ЖК Ростов Комфорт'),
('nasledie', 'ЖК Ростов Комфорт'),
('persona', 'ЖК Ростов Комфорт'),
('zapadnye', 'ЖК Ростов Комфорт'),
('tekuchev', 'ЖК Ростов Комфорт'),
('reki', 'ЖК Ростов Комфорт'),
('botanika', 'ЖК Ростов Комфорт'),
('sosedi', 'ЖК Ростов Комфорт'),
('pritjazhenie', 'ЖК Ростов Комфорт'),
('polet', 'ЖК Ростов Комфорт'),
('sokolniki', 'ЖК Ростов Комфорт'),
('siyanie', 'ЖК Ростов Комфорт'),
('mechta', 'ЖК Ростов Комфорт'),
('smartpolet', 'ЖК Ростов Комфорт'),
('estet', 'ЖК Ростов Комфорт'),    

('akademiya', 'ЖК Новосибирск Комфорт'),
('1956kvartaly', 'ЖК Новосибирск Комфорт'),
('vesna', 'ЖК Новосибирск Комфорт'),
('vinograd', 'ЖК Новосибирск Комфорт'),
('yasnyy', 'ЖК Новосибирск Комфорт'),
('divnogorskiy', 'ЖК Новосибирск Комфорт'),
('ezhevika', 'ЖК Новосибирск Комфорт'),
('nikolskiy', 'ЖК Новосибирск Комфорт'),
('okolica', 'ЖК Новосибирск Комфорт'),
('spektr', 'ЖК Новосибирск Комфорт'),
('stranaberegovaya', 'ЖК Новосибирск Комфорт'),

('lermontovsky', 'ЖК СПБ Бизнес'),
('promenade', 'ЖК СПБ Бизнес'),
('che', 'ЖК СПБ Бизнес'),
('novyylessner', 'ЖК СПБ Бизнес'),
('petrovskaya', 'ЖК СПБ Бизнес'),
('domino', 'ЖК СПБ Бизнес'),
('glorax', 'ЖК СПБ Бизнес'),
('view', 'ЖК СПБ Бизнес'),
('moiseenko10', 'ЖК СПБ Бизнес'),
('vidi', 'ЖК СПБ Бизнес'),
('institutskiy', 'ЖК СПБ Бизнес'),
('lisichanskaya22', 'ЖК СПБ Бизнес'),
('bolshaya', 'ЖК СПБ Бизнес'),
('sampsonievskiy', 'ЖК СПБ Бизнес'),
('korona', 'ЖК СПБ Бизнес'),
('talento', 'ЖК СПБ Бизнес'),
('manhattan', 'ЖК СПБ Бизнес'),
('pobedy', 'ЖК СПБ Бизнес'),
('modum', 'ЖК СПБ Бизнес'),
('neve', 'ЖК СПБ Бизнес'),
('bolshoj67', 'ЖК СПБ Бизнес'),
('morskaya', 'ЖК СПБ Бизнес'),
('leaves', 'ЖК СПБ Бизнес'),
('1733', 'ЖК СПБ Бизнес'),
('alpen', 'ЖК СПБ Бизнес'),
('moskovskiy', 'ЖК СПБ Бизнес'),
('regenbogen', 'ЖК СПБ Бизнес'),
('akvilonzalive', 'ЖК СПБ Бизнес'),
('avant', 'ЖК СПБ Бизнес'),
('belyi', 'ЖК СПБ Бизнес'),
('karetnogo', 'ЖК СПБ Бизнес'),
('amo', 'ЖК СПБ Бизнес'),

('respect', 'ЖК СПБ Комфорт'),
('bairon', 'ЖК СПБ Комфорт'),
('peremen', 'ЖК СПБ Комфорт'),
('friends', 'ЖК СПБ Комфорт'),
('kudrovo2', 'ЖК СПБ Комфорт'),
('newpiter', 'ЖК СПБ Комфорт'),
('kapralskiy', 'ЖК СПБ Комфорт'),
('lyubograd', 'ЖК СПБ Комфорт'),
('murino', 'ЖК СПБ Комфорт'),
('gorelovo', 'ЖК СПБ Комфорт'),
('yanila', 'ЖК СПБ Комфорт'),
('yaninskiy', 'ЖК СПБ Комфорт'),
('lesart2', 'ЖК СПБ Комфорт'),
('kantemirovskaya11', 'ЖК СПБ Комфорт'),
('chernaya', 'ЖК СПБ Комфорт'),
('chkalov', 'ЖК СПБ Комфорт'),
('FoRestakvilon', 'ЖК СПБ Комфорт'),
('novoorlovsky', 'ЖК СПБ Комфорт'),
('lubograd', 'ЖК СПБ Комфорт'),
('milya', 'ЖК СПБ Комфорт'),
('novoesertolovo', 'ЖК СПБ Комфорт'),
('parkolovo', 'ЖК СПБ Комфорт'),
('strizhy', 'ЖК СПБ Комфорт'),
('univer', 'ЖК СПБ Комфорт'),
('yasno', 'ЖК СПБ Комфорт'),
('yugtaun', 'ЖК СПБ Комфорт'),
('zeleny', 'ЖК СПБ Комфорт'),
('prinevsky', 'ЖК СПБ Комфорт'),

('river', 'ЖК Москва Премиум'),
('life', 'ЖК Москва Премиум'),
('primavera', 'ЖК Москва Премиум'),
('luzhniki', 'ЖК Москва Премиум'),
('avtory', 'ЖК Москва Премиум'),
('businovskiy', 'ЖК Москва Премиум'),
('moskvoreche', 'ЖК Москва Премиум'),
('republic', 'ЖК Москва Премиум'),
('lavrushinskiy', 'ЖК Москва Премиум'),
('slava', 'ЖК Москва Премиум'),
('pride', 'ЖК Москва Премиум'),
('hide', 'ЖК Москва Премиум'),
('zilart', 'ЖК Москва Премиум'),
('badaevsky', 'ЖК Москва Премиум'),
('frunzenskaya', 'ЖК Москва Премиум'),

('chainye', 'ЖК Сочи Комфорт'),
('alpika', 'ЖК Сочи Комфорт'),
('portugalii', 'ЖК Сочи Комфорт'),
('gorniy', 'ЖК Сочи Комфорт'),
('letniy', 'ЖК Сочи Комфорт'),
('svetsky', 'ЖК Сочи Комфорт'),
('olivia', 'ЖК Сочи Комфорт'),
('frukty', 'ЖК Сочи Комфорт'),
('lestorya', 'ЖК Сочи Комфорт'),

('vremya', 'ЖК Тула Комфорт'),
('segodnya', 'ЖК Тула Комфорт'),
('pryanichnaya', 'ЖК Тула Комфорт'),
('suvorovskiy', 'ЖК Тула Комфорт'),
('kulik', 'ЖК Тула Комфорт'),
('tula', 'ЖК Тула Комфорт'),
('karpova', 'ЖК Тула Комфорт'),
('nadezhnyy', 'ЖК Тула Комфорт'),
('platon', 'ЖК Тула Комфорт'),

('ritmy', 'ЖК Тюмень Комфорт'),

('sochipark', 'ЖК Сочи Бизнес'),
('marinegarden', 'ЖК Сочи Бизнес'),
('otrazhenie', 'ЖК Сочи Бизнес'),
('svetskiyles', 'ЖК Сочи Бизнес'),
('kislorod', 'ЖК Сочи Бизнес'),
('kiparis', 'ЖК Сочи Бизнес'),

('rezidentsiyamorey', 'ЖК Новороссийск Премиум'),
('peschaniy', 'ЖК Анапа Песчаный'),
('moregrad', 'ЖК Анапа Мореград'),
('usadbagost', 'ЖК Анапа Усадьба Гостагаевская'),
('sunhillsolginka', 'ЖК Сочи Комфорт'),
('karavellaportugalii', 'ЖК Сочи Комфорт'),
('polyanapik', 'ЖК Сочи Комфорт'),
('moretta', 'ЖК Сочи Премиум'),
]

# Паттерны для объектов ЖК
jk_object = [
('centralnyi', 'ЖК Центральный'),
('klub25', 'ЖК Клуб 25'),
('pogoda', 'ЖК Погода'),
('ask', 'АСК'),
('grani', 'ЖК Грани'),
('we', 'ЖК Мы '),
('belyaeva', 'ЖК Юг на Беляева'),
('sostoyanie', 'ЖК Состояние'),
('meridian', 'ЖК Меридиан Слобода'),
('ecos', 'ЖК Экос Кузмолово'),
('riviera', 'ЖК Ривьера'),

('arhitektor', 'ЖК Архитектор'),
('kashtan', 'ЖК Каштановый двор'),
('futurist', 'ЖК Футурист'),
('ozero', 'ЖК Дом у озера'),
('plaza', 'ЖК Плаза'),
('sport', 'ЖК Спортивная деревня'),
('rodnoy', 'ЖК Родной дом'),
('sobytiye', 'ЖК Событие'),

('1799', 'ЖК 1799'),
('stolicyno', 'ЖК Сталицино'),
('serdtse2', 'ЖК Сердце Ростова 2'),
('october', 'ЖК Октябрь Парк'),
('nord', 'ЖК Норд'),
('levoberezhe', 'ЖК Левобережье'),
('legenda', 'ЖК Легенда Ростова'),
('gray', 'ЖК Gray'),
('frame', 'ЖК Frame'),
('dvizhenie61', 'ЖК Движение 61'),
('donskoy', 'ЖК Донской Арбат'),
('flora', 'ЖК Флора'),
('manhjetten', 'ЖК Манхэттен 2.0'),
('nasledie', 'ЖК Наследие'),
('persona', 'ЖК Персона'),
('zapadnye', 'ЖК Западные Аллеи'),
('tekuchev', 'ЖК Текучев'),
('reki', 'ЖК Город у реки'),
('botanika', 'ЖК Ботаника'),
('sosedi', 'ЖК Соседи'),
('pritjazhenie', 'ЖК Притяжение'),
('polet', 'ЖК Полет '),
('sokolniki', 'ЖК Сокольники'),
('siyanie', 'ЖК Сияние'),
('mechta', 'ЖК Мечта'),
('smartpolet', 'ЖК Смартполет'),
('estet', 'ЖК Эстет'),

('akademiya', 'ЖК Академия'),
('1956kvartaly', 'ЖК 1956. Кварталы Телецентра'),
('vesna', 'ЖК Весна'),
('vinograd', 'ЖК Виноград'),
('yasnyy', 'ЖК Город-парк Ясный берег'),
('divnogorskiy', 'ЖК Дивногорский'),
('ezhevika', 'ЖК Ежевика'),
('nikolskiy', 'ЖК Никольский Парк'),
('okolica', 'ЖК Околица'),
('spektr', 'ЖК Спектр'),
('stranaberegovaya', 'ЖК Страна. Береговая'),

('lermontovsky', 'ЖК Лермонтовский 54'),
('promenade', 'ЖК Promenade'),
('che', 'ЖК Квартал Che'),
('novyylessner', 'ЖК Новый Лесснер'),
('petrovskaya', 'ЖК Петровская Доминанта'),
('domino', 'ЖК Domino (Домино)'),
('glorax', 'ЖК GloraX Балтийская (Глоракс Балтийская)'),
('view', 'ЖК Grand View (Гранд Вью)'),
('moiseenko10', 'ЖК Апартаменты Моисеенко 10'),
('vidi', 'ЖК Инвест-отель VIDI (ВИДИ)'),
('institutskiy', 'ЖК Институтский'),
('lisichanskaya22', 'ЖК Лисичанская'),
('bolshaya', 'ЖК ЛСР. Большая Охта'),
('sampsonievskiy', 'ЖК Сампсониевский 32'),
('korona', 'ЖК Северная Корона'),
('talento', 'ЖК Клубный дом TALENTO'),
('manhattan', 'ЖК Клубный дом Манхэттен'),
('pobedy', 'ЖК Парк Победы'),
('modum', 'ЖК Модум'),
('neve', 'ЖК Эталон на Неве'),
('bolshoj67', 'ЖК Большой 67'),
('morskaya', 'ЖК Морская набережная'),
('leaves', 'ЖК Аквилон Leaves'),
('1733', 'ЖК 17.33'),
('alpen', 'ЖК ALPEN'),
('moskovskiy', 'ЖК ID Moskovskiy'),
('regenbogen', 'ЖК Регенбоген'),
('akvilonzalive', 'ЖК Аквилон ZALIVE'),
('avant', 'ЖК Avant'),
('belyi', 'ЖК Белый Остров'),
('karetnogo', 'ЖК Дом на Васильевском'),
('amo', 'ЖК Amo'),

('respect', 'ЖК Respect'),
('bairon', 'ЖК Байрон'),
('peremen', 'ЖК Ветер перемен 2'),
('friends', 'ЖК Friends'),
('kudrovo2', 'ЖК ID Kudrovo II'),
('newpiter', 'ЖК NewПитер'),
('kapralskiy', 'ЖК Капральский'),
('lyubograd', 'ЖК Любоград'),
('murino', 'ЖК Мурино Клаб'),
('gorelovo', 'ЖК Новое Горелово'),
('yanila', 'ЖК Янила Драйв'),
('yaninskiy', 'ЖК Янинский лес'),
('lesart2', 'ЖК ЛесART'),
('kantemirovskaya11', 'ЖК Кантемировская'),
('chernaya', 'ЖК Zoom Черная речка'),
('chkalov', 'ЖК Чкалов'),
('FoRestakvilon', 'ЖК FoRest Аквилон'),
('novoorlovsky', 'ЖК Квартал Новоорловский'),
('lubograd', 'ЖК Любоград'),
('milya', 'ЖК Морская миля'),
('novoesertolovo', 'ЖК Микрорайон Новое Сертолово'),
('parkolovo', 'ЖК Парголово'),
('strizhy', 'ЖК Стрижи в Невском'),
('univer', 'ЖК Универ Сити'),
('yasno', 'ЖК Ясно.Янино'),
('yugtaun', 'ЖК ЮгТаун. Олимпийские кварталы'),
('zeleny', 'ЖК Зелёный квартал'),
('prinevsky', 'ЖК Приневский'),

('river', 'ЖК River Park Towers Кутузовский'),
('life', 'ЖК LIFE TIME'),
('primavera', 'ЖК Клубный город на реке Primavera'),
('luzhniki', 'ЖК Luzhniki Collection'),
('avtory', 'ЖК Лаунж-дома Авторы на Большой'),
('businovskiy', 'ЖК Бусиновский парк'),
('moskvoreche', 'ЖК Москворечье'),
('republic', 'ЖК Republic'),
('lavrushinskiy', 'ЖК Дом Лаврушинский'),
('slava', 'ЖК SLAVA'),
('pride', 'ЖК Pride'),
('hide', 'ЖК HIDE'),
('zilart', 'ЖК Зиларт'),
('badaevsky', 'ЖК Бадаевский'),
('frunzenskaya', 'ЖК Фрунзенская 30'),

('chainye', 'ЖК Чайные холмы'),
('alpika', 'ЖК Новая Альпика'),
('portugalii', 'ЖК Каравелла Португалии'),
('gorniy', 'ЖК Горный Квартал'),
('letniy', 'ЖК Летний'),
('svetsky', 'ЖК Светский лес'),
('olivia', 'ЖК Olivia'),
('frukty', 'ЖК Фрукты'),
('lestorya', 'ЖК Лестория'),

('vremya', 'ЖК Время'),
('segodnya', 'ЖК Сегодня'),
('pryanichnaya', 'ЖК Пряничная Слобода'),
('suvorovskiy', 'ЖК Суворовский'),
('kulik', 'ЖК Кулик'),
('tula', 'ЖК Новая Тула'),
('karpova', 'ЖК Карпова'),
('nadezhnyy', 'ЖК Надежный'),
('platon', 'ЖК Платон парк'),

('ritmy', 'ЖК Ритмы'),

('sochipark', 'ЖК Сочи парк'),
('marinegarden', 'ЖК Марина гарден 4'),
('otrazhenie', 'ЖК Отражение'),
('svetskiyles', 'ЖК Светский лес'),
('kislorod', 'ЖК Кислород'),
('kiparis', 'ЖК Кипарис'),

('rezidentsiyamorey', 'ЖК Резиденция морей'),
('peschaniy', 'ЖК Песчаный'),
('moregrad', 'ЖК Мореград'),
('usadbagost', 'ЖК Усадьба Гостагаевская'),
('sunhillsolginka', 'ЖК Сан Хилс Ольгинка'),
('karavellaportugalii', 'ЖК Каравелла Португалии'),
('polyanapik', 'ЖК Поляна Пик'),
('moretta', 'ЖК Моретта'),
]

#Паттерны для операторов мобильной связи
mobile_operator = [
    ('mts', 'МТС'),
    ('meg', 'Мегафон'),
    ('rt', 'Ростелком'),
    ('rtk', 'Ростелком'),
    ('tele2', 'Теле2'),
    ('bilne', 'Билайн'),
]

def determine_supplier(parts):
    """
    Обрабатывает фрагменты метки, сначала проверяя на бесплатного поставщика в конце метки. Если находится бесплатный поставщик, функция завершается.
    Если метка не от бесплатного поставщика, то определяется платный. Поставщик назначается по первому фрагменту, который соответствует признаку 
    """
    # Проверяем, есть ли последний элемент в списке бесплатных поставщиков
    last_part = parts[-1] if parts else ""
    if last_part in free_patterns:
        return free_patterns[last_part]

    # Словарь для хранения позиций найденных паттернов
    matches = {}

    # Перебираем элементы метки и ищем точные совпадения
    for i, part in enumerate(parts):
        for pattern, supplier in priority_rules:
            if part == pattern:  # Строгое соответствие
                # Если совпадение уже найдено, берем более раннюю позицию
                if supplier not in matches or matches[supplier] > i:
                    matches[supplier] = i

    # Если есть совпадения, возвращаем поставщика с минимальной позицией
    if matches:
        return min(matches, key=matches.get)

    # Если совпадений нет
    return "Неизвестно"

def determine_supplier2(supplier, parts):
    """
    Обрабатывает фрагменты метки, проверяя наличие доп условий, для уже определенного поставщика.
    """
    # Приводим фрагменты к единому формату: заменяем , -> . и русскую р -> латинскую p
    normalized_parts = [p.replace(',', '.').replace('р', 'p') for p in parts]

    zero_price = {'0p', 'free'}

    # Словарь с правилами
    rules = {
        'Андрей': {'7p': 'andr_7p', '5p': 'andr_5p', '5.5p': 'andr_5.5p', '4p': 'andr_4p', 
                   '3p': 'andr_3p', '4.5p': 'andr_4.5p', **{k: 'andr_0p' for k in zero_price}},
        'Теле2': {'4.5p': 't2_4.5p'},
        'ВР': {'cod': 'wr_cod', 'meg': 'wr_meg', 'mts': 'wr_mts', 'bilne': 'wr_beeline'},
        'Datacall': {'10p': 'datacall_10p', '7.5p': 'datacall_7.5p', '6p': 'datacall_6p',
                     '5p': 'datacall_5p', '3p': 'datacall_3p', **{k: 'datacall_0p' for k in zero_price}},
        'Ноухау': {'newkval': 'knowhow_newkval', '16p': 'knowhow_16p', **{k: 'knowhow_0p' for k in zero_price}},
        'ДМП': {'cod': 'dmp_cod', 'bilne': 'dmp_beeline'},
        'Рефекшн кинетик': {'cod': 'reffection_cod', '3.5p': 'reffection_3,5p', **{k: 'reffection_0p' for k in zero_price}},
        'Игорь': {'6p': 'lagom_6p', '12p': 'lagom_12p', '10p': 'lagom_10p', '4.5p': 'lagom_4.5p', **{k: 'lagom_0p' for k in zero_price}},
        'Скоринг': {k: 'beeline_scoring_0p' for k in zero_price},
        'Кирилл': {'80p': 'kirill_80p', '12p': 'kirill_12p', '10p': 'kirill_10p', '2p': 'kirill_2p', '3p': 'kirill_3p', **{k: 'lagom_0p' for k in zero_price}},
        'Нэтгроуслаб': {**{k: 'ngslb_0p' for k in zero_price}}  
    }

    # Значения по умолчанию для поставщиков
    default_supplier = {
        'ВР': 'wr',
        'ДМП': 'dmp',
        'Скоринг': 'beeline scoring',
        'Теле2': 't2',
        'Рефекшн кинетик': 'reffection',
        'Ноухау': 'knowhow',
        'Кокос': 'kokos',
        'Ростелеком': 'RT ростелеком',
        'Replay': 'replay',
        'Песок': 'pesok',
        'Дубли': 'DUBL',
    }

    # Получаем правила для текущего поставщика
    supplier_rules = rules.get(supplier, {})

    # Словарь для хранения позиций найденных паттернов
    matches = {}

    # Перебираем элементы метки и ищем точные совпадения с паттернами поставщика
    for i, part in enumerate(normalized_parts):
        for pattern, supplier_pattern in supplier_rules.items():
            if part == pattern:  # Строгое соответствие
                # Если совпадение уже найдено, берем более раннюю позицию
                if supplier_pattern not in matches or matches[supplier_pattern] > i:
                    matches[supplier_pattern] = i

    # Если есть совпадения, возвращаем поставщика с минимальной позицией
    if matches:
        return min(matches, key=matches.get)

    # Если ничего не нашли, возвращаем дефолтное значение
    return default_supplier.get(supplier, 'pp')
    
def determine_project(parts):
    """
    Обрабатывает фрагменты метки, сначала проверяя на бесплатного поставщика 'pp'в конце метки. Если находится бесплатный поставщик, метка читается справа налево.
    Направление назначается по первому фрагменту, который соответствует признаку
    """
    # Перезакидки читаем с конца
    if 'pp' in parts[-2:]:
        parts.reverse()
    
    # Словарь для хранения позиций найденных паттернов
    matches = {}

    # Перебираем элементы метки и ищем точные совпадения
    for i, part in enumerate(parts):
        for pattern, project in project_rules:
            if part == pattern:  # Строгое соответствие
                # Если совпадение уже найдено, берем более раннюю позицию
                if project not in matches or matches[project] > i:
                    matches[project] = i

    # Если нашли конкретный проект (включая уточнённые ЖК)
    if matches:
        project = min(matches, key=matches.get)
        # Если это общий "ЖК", пытаемся уточнить
        if project == 'ЖК':
            # Проверяем на специальные типы ЖК
            for part in parts:
                if part == 'zastr':
                    return 'ЖК Застройщики'
                elif part == 'lidact':
                    return 'ЖК Лидактив'
            
            # Если нет специальных типов, проверяем города
            city_matches = {}
            for i, part in enumerate(parts):
                for pattern, city in project2_rules:
                    if part == pattern:
                        if city not in city_matches or city_matches[city] > i:
                            city_matches[city] = i
            
            if city_matches:
                city = min(city_matches, key=city_matches.get)
                return f'ЖК {city}'
            
            # Если ничего не нашли, возвращаем "ЖК Застройщики" по умолчанию
            return 'ЖК'
        
        return project

    # Если совпадений нет
    return "Неизвестно"

def determine_project2(project, parts):
    """
    Обрабатывает фрагменты метки, сначала проверяя на бесплатного поставщика 'pp' в конце метки. Если находится бесплатный поставщик, метка читается справа налево.
    Проект назначается по первому фрагменту, который соответствует признаку и корректируется в зависимости от проекта.
    """
    # Перезакидки читаем с конца
    if 'pp' in parts[-2:]:
        parts.reverse()

    # Если направление - ЖК, ищем конкретный проект
    if project.startswith('ЖК'):
        for part in parts:
            for pattern, jk_name in jk_project:
                if part == pattern:
                    return jk_name
        return project  # Если не нашли, возвращаем направление (ЖК Застройщики/Лидактив)

    # Направления которые не делятся на проекты внутри себя
    if project in {'Банковские гарантии', 'Спецтехника', 'Лизинг', 'Аренда спецтехники'}:
        project2 = project
        return project2

    # Словарь для хранения позиций найденных паттернов
    matches = {}

    # Перебираем элементы метки и ищем точные совпадения
    for i, part in enumerate(parts):
        for pattern, project2 in project2_rules:
            if part == pattern:  # Строгое соответствие
                # Если совпадение уже найдено, берем более раннюю позицию
                if project2 not in matches or matches[project2] > i:
                    matches[project2] = i

    # Если есть совпадения, возвращаем направление с минимальной позицией
    if matches:
        project2 = min(matches, key=matches.get)
        # Проверяем проект и корректируем направление
        if project2 == 'ЖК Застройщики' and 'test' in parts:
            project2 = 'ЖК Застройщики тест'

        # elif project.startswith('ЖК'):
        #         # Перебираем элементы метки и ищем точные совпадения
        #         for i, part in enumerate(parts):
        #             for pattern, project2 in jk_project:
        #                 if part == pattern:  # Строгое соответствие
        #                     # Если совпадение уже найдено, берем более раннюю позицию
        #                     if project2 not in matches or matches[project2] > i:
        #                         matches[project2] = i
        #                         # Если нашли конкретный проект (включая уточнённые ЖК)
        #                         if matches:
        #                             project2 = min(matches, key=matches.get)
            
        elif project == 'Недвижимость (бп)' and project2 in {'Краснодар','Владивосток','Санкт-Петербург'}:
            project2 = project2 + ' (без прозвон)'

        elif project == 'Перевод звонка' and project2 in {'Мытищи', 'Санкт-Петербург', 'Москва'}:
            project2 = project2 + ' (звонок)'

        elif project == 'Перевод звонка' and project2 in {'Уфа', 'Калининград', 'Краснодар', 'Красноярск', 'Крым', 'Тюмень',
                                                          'Нижний Новгород', 'Новосибирск', 'Екатеринбург', 'Ростов', 'Казань', 
                                                          'ХМАО', 'Калуга', 'Челябинск', 'Владивосток', 'Тула', 
                                                          'Ижевск', 'Пермь', 'Хабаровск', 'Архангельск', 'Адыгея', 'Ярославль'}:
            project2 = 'Перевод КЦ Регионы'

        elif project == 'Перевод звонка' and project2 in {'Ногинск', 'Клин', 'Хотьково', 'Дубна', 'Наро-Фоминск'}:
            project2 = 'Перевод КЦ ДМО'

        elif project == 'Перевод звонка' and project2 in {'Выборг', 'Кировск', 'Коммунар'}:
            project2 = 'Перевод КЦ ДЛО'

        elif project == 'Недвижимость (пр)' and project2 in {'Москва', 'Санкт-Петербург'}:
            project2 = 'Яндекс Т0'

        elif project == 'Недвижимость (пр)' and project2 in {'Краснодар', 'Екатеринбург', 'Казань', 'Новосибирск', 'Ростов', 'Тюмень'}:
            project2 = 'Яндекс Т1'

        elif project == 'Недвижимость (пр)' and project2 in {'Ярославль', 'ХМАО', 'Нижний Новгород', 'Калининград', 'Калуга', 'Уфа', 'Красноярск', 'Челябинск',
                                                             'Тула', 'Ижевск', 'Пермь', 'Хабаровск', 'Архангельск', 'Адыгея', 'Крым'}:
            project2 = 'Яндекс Т2'          

        elif project == 'Авто' and project2 in {'Екатеринбург', 'Челябинск'}:
            project2 = 'Авто Екб и Члб'  

        elif project == 'Авто' and project2 == {'Авто Перевод звонка'}:
            project2 = 'Авто Перевод звонка'    

        elif project == 'Авто' and project2 not in {'Екатеринбург', 'Челябинск', 'Авто Перевод звонка'}:
            project2 = 'Авто Мск и Спб'       
        
    else:
        if project == 'Авто': #Старые метки Авто не имели приписки 'spb' или 'msk', но относились туда
            project2 = 'Авто Мск и Спб' 
            return project2
        
        return project  # Если совпадений нет, возвращаем название проекта

    return project2  # Возвращаем итоговое значение

def determine_city(project, project2, parts):
    """
    Обрабатывает фрагменты метки, сначала проверяя на бесплатного поставщика '_pp'в конце метки. Если находится бесплатный поставщик, метка читается справа налево.
    Город назначается по первому фрагменту, который соответствует признаку и корректируется в зависимости от проекта.
    Объекты ЖК определяются по отдельному списку.
    """
    if 'pp' in parts[-2:]:
        parts.reverse()

    if project in {'Банковские гарантии', 'Спецтехника', 'Лизинг', 'Аренда спецтехники', 'Авто'}:
        return project2
    
    if project2 == 'ЖК Застройщики тест':
        return project2
         
    # Проверяем на объекты ЖК
    if project.startswith('ЖК'):
        for part in parts:
            for pattern, city_object in jk_object:
                if part == pattern:
                    return city_object
                
    # Словарь для хранения позиций найденных паттернов
    matches = {}

    # Перебираем элементы метки и ищем точные совпадения
    for i, part in enumerate(parts):
        for pattern, city in project2_rules:
            if part == pattern:  # Строгое соответствие
                # Если совпадение уже найдено, берем более раннюю позицию
                if city not in matches or matches[city] > i:
                    matches[city] = i

    # Если есть совпадения, возвращаем направление с минимальной позицией
    if matches:
        city = min(matches, key=matches.get)
        # Проверяем проект и корректируем направление
        if project == 'Перевод звонка':
            city += ' (звонок)'  
        elif project == 'Недвижимость (бп)':
            city += ' (без прозвон)'   

        return city  # Возвращаем итоговое значение
    
    return project2

def determine_department(parts):

    if 'traf' in parts:
        return 'Реклама'
    else:
        return 'Базы'
    
def determine_avto(project, parts):

    # Проверяем на марки Авто
    if project == 'Авто':
        for part in parts:
            for pattern, avto_mark in avto_rules:
                if part == pattern:
                    return avto_mark
        else:
            return 'Другое'
        
def determine_mobile_operator(parts):

    # Проверяем наличие оператора сотовой связи из метки
    for part in parts:
        for pattern, operator in mobile_operator:
            if part == pattern:
                return operator
    else:
        return 'Не определен'