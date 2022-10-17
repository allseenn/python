import random
import datetime
import os
BASE = "base.csv"

def generate(size):
    if int(size) <=0:
        return "Не задан размер базы"
    elif int(size) > 0:
        syllables = ['ба', 'бо', 'бу', 'бы', 'би', 'бя', 'бю', 'бе', 'ва', 'во', 'ву', 'вы', 'вэ', 'ви', 'вя', 'вю', 'ве', 'да', 'до', 'ду', 'ды', 'ди', 'дя', 'дю', 'де', 'га', 'го', 'гу', 'ги', 'гя', 'гю', 'ге', 'за', 'зо', 'зу', 'зи', 'зя', 'зю', 'зе', 'ка', 'ко', 'ку', 'ки', 'кя', 'кю', 'ке', 'са', 'со', 'су', 'сы', 'си', 'ся', 'сю', 'се', 'па', 'по', 'пу', 'пы', 'пи', 'пя', 'пю', 'пе', 'жа', 'жо', 'жу', 'жи', 'жю', 'же', 'ла', 'ло', 'лу', 'лы', 'ли', 'ля', 'лю', 'ле', 'ма', 'мо', 'му', 'мы', 'ми', 'мя', 'мю', 'ме', 'на', 'но', 'ну', 'ны', 'ни', 'ня', 'ню', 'не', 'ра', 'ро', 'ру', 'ри', 'ря', 'рю', 'ре', 'та', 'то', 'ту', 'ти', 'тя', 'тю', 'те', 'ха', 'хо', 'ху', 'хи', 'хя', 'хю', 'хе', 'ца', 'цо', 'цу', 'ци', 'це', 'ша', 'шо', 'шу', 'ши', 'ше', 'ща', 'що', 'щу', 'щи', 'ще', 'ча', 'чо', 'чу', 'чи', 'че', 'фа', 'фо', 'фу', 'фи', 'фя', 'фе', 'аб', 'об', 'уб', 'иб', 'яб', 'юб', 'ав', 'ов', 'ув', 'ив', 'яв', 'юв', 'ев', 'ад', 'од', 'уд', 'ид', 'яд', 'юд', 'ед', 'аг', 'ог', 'уг', 'иг', 'яг', 'юг', 'ег', 'аз', 'оз', 'уз', 'из', 'яз', 'юз', 'ез', 'ак', 'ок', 'ук', 'ик', 'як', 'юк', 'ек', 'ас', 'ос', 'ус', 'ис', 'яс', 'юс', 'ес', 'ап', 'оп', 'уп', 'ип', 'яп', 'юп', 'аж', 'ож', 'уж', 'иж', 'юж', 'еж', 'ал', 'ол', 'ул', 'ил', 'ял', 'юл', 'ел', 'ам', 'ом', 'ум', 'им', 'ям', 'юм', 'ем', 'ан', 'он', 'ун', 'ин', 'ян', 'юн', 'ен', 'ар', 'ор', 'ур', 'ир', 'яр', 'юр', 'ер', 'ат', 'от', 'ут', 'ит', 'ят', 'ют', 'ет', 'ах', 'ох', 'ух', 'их', 'ях', 'юх', 'ех', 'ац', 'оц', 'уц', 'иц', 'яц', 'юц', 'ец', 'аш', 'ош', 'уш', 'иш', 'яш', 'юш', 'еш', 'ач', 'оч', 'уч', 'ич', 'яч', 'юч', 'еч', 'аф', 'оф', 'уф', 'иф', 'яф', 'юф', 'еф']
        endings = ['лин', 'лов', 'нин', 'нов', 'шин', 'шов', 'рин', 'ров', 'пин', 'пов', 'ков', 'кин', 'ко', 'кий', 'ций', 'вич', 'цев', 'цов', 'цин']
        initials = ['А.', 'Б.', 'В.', 'Г.', 'Д.', 'Е.', 'Ж.', 'З.', 'И.', 'Й.', 'К.', 'Л.', 'М.', 'Н.', 'О.', 'П.', 'Р.', 'С.', 'Т.', 'Ш.', 'У.', 'Ц.', 'Ф.', 'Х.', 'Э.', 'Ю.', 'Я.']
        positions = ['без какой-либо должности', 'авиационный механик', 'дежурный', 'заместитель командира взвода', 'инструктор', 'командир взвода', 'командир отделения', 'командир танка', 'контролер', 'водитель-крановщик', 'механик по реактивным моторам самолётов', 'рядовой механик технической роты', 'механик-водитель', 'музыкант', 'наводчик-оператор', 'эксперт по подрывным работам под водой', 'огнемётчик', 'оленевод', 'оператор', 'операционная медицинская сестра', 'парикмахер', 'писарь', 'повар', 'почтальон', 'помощник начальника', 'помощник командира', 'помощник солиста', 'радиотелеграфист', 'разведчик', 'сапёр', 'слесарь', 'снайпер', 'солист', 'старший механик', 'старший механик-водитель', 'старший оператор', 'старший оптик', 'старший разведчик', 'пулемётчик', 'старший электрик', 'стрелок', 'телеграфист', 'авиационный техник', 'укладчик парашютов', 'фармацевт', 'фельдшер', 'фельдшер-спасатель', 'химик', 'чертежник', 'экскаваторщик', 'электрик', 'электромонтёр']
        categories = ['1', '2', '3', '4', '5']
        streets = ['Авиационная улица', 'Алёшкинский проезд', 'Ангелов переулок', 'Аэродромная улица', 'Барышиха, улица', 'Береговая улица', 'Большая Набережная улица', 'Большой Волоколамский проезд', 'Братцевская улица', 'Вишнёвая улица', 'Волоколамский проезд', 'Волоколамское шоссе', 'Волоцкой переулок', 'Воротынская улица', 'Врачебный проезд', 'ГДубравная улица', 'Живописная улица', 'Захарьинская улица', 'Звенигородское шоссе', 'Иваньковское шоссе', 'Карамышевская набережная', 'Карамышевский проезд', 'Крылатская улица', 'Крылатский мост', 'Куркинское шоссе', 'Ландышевая улица', 'Лодочная улица', 'Лыковский проезд', 'Лётная улица', 'Максимова, улица', 'Малая Набережная улица', 'Машкинское шоссе', 'Мещерякова, улица', 'Митинская улица', 'Мнёвники, улица', 'Муравская улица', 'Мякининский проезд', 'Нелидовская улица', 'Неманский проезд', 'Нижние Мнёвники, посёлок', 'Нижние Мнёвники, улица', 'Никольский тупик', 'Новогорская улица', 'Новокуркинское шоссе', 'Новопоселковая улица', 'Новотушинская улица', 'Новотушинский проезд', 'Новохорошевский проезд', 'Новощукинская улица', 'Одинцовская улица', 'Окружная улица', 'Парусный проезд', 'Пенягинская улица', 'Пехотная улица', 'Планерная улица', 'Подмосковная улица', 'Полесский проезд', 'Походный проезд', 'Причальный проезд', 'Путилковское шоссе', 'Пятницкое шоссе', 'Родионовская улица', 'Светлогорский проезд', 'Сосновая аллея', 'Сосновая улица', 'Староспасская улица', 'Строгинский бульвар', 'Строгинский мост', 'Строгинское шоссе', 'Строительный проезд', 'Сходненская улица', 'Сходненский проезд', 'Сходненский тупик', 'Таллинская улица', 'Таманская улица', 'Твардовского, улица', 'Тепличный переулок', 'Трикотажный проезд', 'Туристская улица', 'Туркменский проезд', 'Тушинская улица', 'Уваровский переулок', 'Фабричная улица', 'Фабричный проезд', 'Химкинский бульвар', 'Цариков переулок', 'Цветочный проезд', 'Шелепихинская набережная', 'Щукинская улица', 'Юровская улица']
        mobile_prefix = ['910', '915', '916', '917', '919', '985', '986', '903', '905', '906', '909', '962', '963', '964', '965', '966', '967', '968', '969', '980', '983', '986', '925', '926', '929', '936', '999', '901', '958', '977', '999', '995', '996', '999']
        phone_prefix = ['495', '499', '498']
        for i in range(int(size)):
            soc_id = str(random.randint(11111111111, 99999999999))
            full_name = ''.join(random.sample(syllables, random.randint(2, 3)) + random.sample(endings, 1)).title() + ' '+''.join(random.sample(initials, 1) + random.sample(initials, 1))
            birth_day =  datetime.date.fromtimestamp(random.randint(0, 1000000000)).strftime("%Y-%m-%d")
            vus = "".join(random.sample(positions, 1))
            health = "".join(random.sample(categories, 1))
            address = " ".join(random.sample(streets, 1))
            address += " д." + str(random.randint(1, 99)) + " кв." + str(random.randint(1, 300))
            mobile = '8' + ''.join(random.sample(mobile_prefix, 1)) + str(random.randint(1111111, 9999999))
            phone = '8' + ''.join(random.sample(phone_prefix, 1)) + str(random.randint(1111111, 9999999))
            with open("base.csv", "a") as file:
                file.write(f'{soc_id};{full_name};{birth_day};{vus};{health};{address};{mobile};{phone}\n')
        return f"База размером {size} записей создана"
    else:
        return "Ошибка"

def drop(base=BASE):
    if os.path.isfile(base):
        os.remove(base)
        #os.system("cls")
        return f"{base} удалена!"
    else:
        # os.system("cls")
        return  f"Ошибка: {base} не найдена!"

def save(data):
    with open("base.csv", "a") as file:
        file.writelines(f'{data[0]};{data[1]};{data[2]};{data[3]};{data[4]};{data[5]};{data[6]};{data[7]}\n')
    return "Запись сохранена"

def search(data):
    res = []
    with open(BASE, "r") as file:
        base = file.read().split('\n') 
        for item in base:
            line = item.split(';')
            lists = list(filter(None, data))
            if set(lists).issubset(line) and len(line) > 1:
                res.append(line)
    return res

def delete(data):
    res = []
    with open(BASE, "r") as file:
        base = file.read().split('\n') 
        for item in base:
            line = item.split(';')
            lists = list(filter(None, data))
            if not set(lists).issubset(line) and len(line) > 1:
                res.append(line)
    drop()
    with open("base.csv", "a") as file:
        for item in res:
            file.write(f'{item[0]};{item[1]};{item[2]};{item[3]};{item[4]};{item[5]};{item[6]};{item[7]}\n')
    return f'Удалено {len(base)-len(res)-1} зап.'

