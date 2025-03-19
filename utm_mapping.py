# Паттерны для бесплатных поставщиков с их названиями
free_patterns = {
        "pp": "_pp",
        "pesok": "_pp",
        "ndzokt5": "_pp",       
        "replay": "Replay",
        "replаy": "Replay",        
        "dubl": "Дубли",
        "dblvrn": "Двойная воронка",
        "otval": "Отвал",
        "mod": "_pp",
        "dlsbp": "_pp"
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
    ]

# Паттерны для проектов
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
]

# Паттерны для направлений
project2_rules = [
    ('lidact', 'ЖК Лидактив'),
    ('zastr', 'ЖК Застройщики'),
    ('msk', 'Москва'),
    ('spb', 'Санкт-Петербург'),
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
    ('kirovsk', 'Кировск'),
    ('communar', 'Коммунар'),
    ('sochi', 'Сочи'),
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
    Обрабатывает поставщика и фрагменты метки на явное соответствие, чтобы определить стоимость покупки.
    Построена на основе справочника https://docs.google.com/spreadsheets/d/1VCJTcPBBeMWkiKUZc6IEo0fGnOQiZmLRo4DuYayBT40/edit?gid=0#gid=0
    """
    if supplier == 'Андрей' and ('7p' in parts or 'spb' in parts):
        return 'andr_7p'
    elif supplier == 'Андрей' and ('5p' in parts or 'msk' in parts):
        return 'andr_5p'
    elif supplier == 'Андрей' and ('0p' in parts or '0р' in parts or 'free' in parts):
        return 'andr_0p'  
    elif supplier == 'Теле2' and '4.5p' in parts:
        return 't2_4.5p'
    elif supplier == 'ВР' and 'cod' in parts:
        return 'wr_cod'
    elif supplier == 'ВР' and 'meg' in parts:
        return 'wr_meg'
    elif supplier == 'Datacall' and '10p' in parts:
        return 'datacall_10p'
    elif supplier == 'Datacall' and '7.5p' in parts:
        return 'datacall_7.5p'
    elif supplier == 'Datacall' and '6p' in parts:
        return 'datacall_6p'
    elif supplier == 'Datacall' and '5p' in parts:
        return 'datacall_5p'
    elif supplier == 'Datacall' and '3p' in parts:
        return 'datacall_3p'
    elif supplier == 'Datacall' and ('0p' in parts or '0р' in parts or 'free' in parts):
        return 'datacall_0p'
    elif supplier == 'Ноухау' and ('0p' in parts or '0р' in parts or 'free' in parts):
        return 'knowhow_0p'
    elif supplier == 'ДМП' and 'cod' in parts:
        return 'dmp_cod'
    elif supplier == 'Рефекшн кинетик' and 'cod' in parts:
        return 'reffection_cod'
    elif supplier == 'Рефекшн кинетик' and ('0p' in parts or '0р' in parts or 'free' in parts):
        return 'reffection_0p'
    elif supplier == 'Игорь' and ('0p' in parts or '0р' in parts or 'free' in parts):
        return 'lagom_0p'
    elif supplier == 'Игорь' and '6p' in parts:
        return 'lagom_6p'
    elif supplier == 'Игорь' and '12p' in parts:
        return 'lagom_12p'
    elif supplier == 'Игорь' and '10p' in parts:
        return 'lagom_10p'
    elif supplier == 'Скоринг' and ('0p' in parts or '0р' in parts or 'free' in parts):
        return 'beeline_scoring_0p' 
    else:
        return supplier
    
def determine_project(parts):
    """
    Обрабатывает фрагменты метки, сначала проверяя на бесплатного поставщика '_pp'в конце метки. Если находится бесплатный поставщик, метка читается с права на лево.
    Проект назначается по первому фрагменту, который соответствует признаку
    """
    if parts[-1] == 'pp':
        parts = parts[::-1]
    
    # Словарь для хранения позиций найденных паттернов
    matches = {}

    # Перебираем элементы метки и ищем точные совпадения
    for i, part in enumerate(parts):
        for pattern, project in project_rules:
            if part == pattern:  # Строгое соответствие
                # Если совпадение уже найдено, берем более раннюю позицию
                if project not in matches or matches[project] > i:
                    matches[project] = i

    # Если есть совпадения, возвращаем проект с минимальной позицией
    if matches:
        return min(matches, key=matches.get)

    # Если совпадений нет
    return "Неизвестно"

def determine_project2(project, parts):
    """
    Обрабатывает фрагменты метки, сначала проверяя на бесплатного поставщика '_pp'в конце метки. Если находится бесплатный поставщик, метка читается с права на лево.
    Направление назначается по первому фрагменту, который соответствует признаку и корректируется в зависимости от проекта.
    """
    if parts[-1] == 'pp':
        parts = parts[::-1]

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

        elif project == 'ЖК' and project2 in {'Ростов', 'Новосибирск', 'Сочи', 'Тула', 'Санкт-Петербург', 'Москва'}:
            project2 = project + ' ' + project2

        elif project == 'Недвижимость (бп)' and project2 in {'Краснодар','Владивосток','Санкт-Петербург'}:
            project2 = project2 + ' (без прозвон)'

        elif project == 'Перевод звонка' and project2 in {'Москва', 'Санкт-Петербург', 'Мытищи', 'Уфа', 'Калининград', 'Краснодар',
                                                          'Красноярск', 'Крым', 'Нижний Новгород', 'Новосибирск', 'Ростов', 
                                                          'Екатеринбург', 'Казань', 'Тюмень', 'Выборг', 'Кировск', 'Коммунар',
                                                          'Наро-Фоминск', 'Дубна', 'Хотьково', 'Клин', 'Ногинск'}:
            project2 = project2 + ' (звонок)'  

        elif project == 'Авто' and project2 in {'Екатеринбург', 'Челябинск'}:
            project2 = 'Авто Екб и Члб'  

        elif project == 'Авто' and project2 not in {'Екатеринбург', 'Челябинск'}:
            project2 = 'Авто Мск и Спб'      
        
    else:
        if project == 'Авто':
            project2 = 'Авто Мск и Спб' 
            return project2
        
        return project  # Если совпадений нет, возвращаем название проекта

    return project2  # Возвращаем итоговое значение