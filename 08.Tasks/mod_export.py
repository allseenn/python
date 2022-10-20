import datetime
import random
import json

today = datetime.datetime.now().strftime("%Y%m%d") + "_" + str(random.randint(1000, 9999)) 

def jason(res):
    json_data = []
    fields = ["СНИЛС", "Фамилия", "Имя", "Отчество", "Рождение", "Профессия", "Оклад", "Адрес", "Сотовый", "Городской"]
    for line in res:
        record = dict(zip(fields, line))
        json_data.append(record)
    json.dump( json_data, open( today + ".json", 'w' ) )
    return f'{len(res)} человек в {today}.json'

def html(res):
    html = '<html>\n<head><style> table, th, td {border: 1px solid black; border-collapse: collapse;}</style></head>\n<table><thead>\n'
    html += f'<tr><th>СНИЛС</th><th>Фамилия</th><th>Имя</th><th>Отчество</th><th>Рождение</th><th>Профессия</th><th>Оклад</th><th>Адрес</th><th>Сотовый</th><th>Городской</th></tr></thead><tbody>\n'
    for item in res:
        html += f'<tr><td>{item[0]}</td><td>{item[1]}</td><td>{item[2]}</td><td>{item[3]}</td><td>{item[4]}</td><td>{item[5]}</td><td>{item[6]}</td><td>{item[7]}</td><td>{item[8]}</td><td>{item[8]}</td></tr>\n'
    html += '<tbody>\n</table>\n</body>\n</html>'
    with open(f'{today}.html', 'w') as page:
        page.write(html)
    return f'{len(res)} человек в {today}.html'

def xml(res):
    xml = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
    for item in res:
        xml += f'<person>\n'
        xml += f'\t<SocID>{item[0]}</SocID>\n'
        xml += f'\t<LastName>{item[1]}</LastName>\n'
        xml += f'\t<FirstName>{item[2]}</FirstName>\n'
        xml += f'\t<MiddleName>{item[3]}</MiddleName>\n'
        xml += f'\t<BirthDay>{item[4]}</BirthDay>\n'
        xml += f'\t<Position>{item[5]}</Position>\n'
        xml += f'\t<Salary>{item[6]}</Salary>\n'
        xml += f'\t<Address>{item[7]}</Address>\n'
        xml += f'\t<Mobile>{item[8]}</Mobile>\n'
        xml += f'\t<Phone>{item[9]}</Phone>\n'
        xml += f'</person>\n'
    xml += '</xml>'
    with open(f'{today}.xml', 'w') as page:
        page.write(xml)
    return f'{len(res)} человек в {today}.xml'

def csv(res):
    csv = f'СНИЛС;ФИО;Дата рожд.;ВУС;Кат;Адрес;Сотовый;Городской\n'
    for item in res:
        csv += f'{item[0]};{item[1]};{item[2]};{item[3]};{item[4]};{item[5]};{item[6]};{item[7]};{item[8]};{item[9]}\n'
    with open(f'{today}.csv', 'w') as page:
        page.write(csv)
    return f'{len(res)} человек в {today}.csv'

def prints (res):
    print('{:11} {:9} {:7} {:8} {:11} {:7} {:6} {:8} {:11} {:11}'.format('СНИЛС', 'Фамилия', 'Имя', 'Отчество', 'Рождение', 'Профессия', 'Оклад', 'Адрес', 'Сотовый', 'Городской'))
    for item in res:
            print(f'{item[0][:11]} {item[1][:10]} {item[2][:7]} {item[3][:8]} {item[4][:10]} {item[5][:10]} {item[6][:8]} {item[7][:8]} {item[8][:11]} {item[9][:11]}')
