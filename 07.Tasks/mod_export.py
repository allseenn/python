import datetime
import random

today = datetime.datetime.now().strftime("%Y%m%d") + "_" + str(random.randint(1000, 9999)) 

def html(res):
    html = '<html>\n<head><style> table, th, td {border: 1px solid black; border-collapse: collapse;}</style></head>\n<table><thead>\n'
    html += f'<tr><th>СНИЛС</th><th>ФИО</th><th>Дата рожд</th><th>ВУС</th><th>Кат</th><th>Адрес</th><th>Сотовый</th><th>Городской</th></tr></thead><tbody>\n'
    for item in res:
        html += f'<tr><td>{item[0]}</td><td>{item[1]}</td><td>{item[2]}</td><td>{item[3]}</td><td>{item[4]}</td><td>{item[5]}</td><td>{item[6]}</td><td>{item[7]}</td></tr>\n'
    html += '<tbody>\n</table>\n</body>\n</html>'
    with open(f'{today}.html', 'w') as page:
        page.write(html)
    return f'{len(res)} человек в {today}.html'

def xml(res):
    xml = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
    for item in res:
        xml += f'<person>\n'
        xml += f'\t<SocID>{item[0]}</SocID>\n'
        xml += f'\t<FullName>{item[1]}</FullName>\n'
        xml += f'\t<BirthDay>{item[2]}</BirthDay>\n'
        xml += f'\t<Position>{item[3]}</Position>\n'
        xml += f'\t<Health>{item[4]}</Health>\n'
        xml += f'\t<Address>{item[5]}</Address>\n'
        xml += f'\t<Mobile>{item[6]}</Mobile>\n'
        xml += f'\t<Phone>{item[7]}</Phone>\n'
        xml += f'</person>\n'
    xml += '</xml>'
    with open(f'{today}.xml', 'w') as page:
        page.write(xml)
    return f'{len(res)} человек в {today}.xml'

def csv(res):
    csv = f'СНИЛС;ФИО;Дата рожд.;ВУС;Кат;Адрес;Сотовый;Городской\n'
    for item in res:
        csv += f'{item[0]};{item[1]};{item[2]};{item[3]};{item[4]};{item[5]};{item[6]};{item[7]}\n'
    with open(f'{today}.csv', 'w') as page:
        page.write(csv)
    return f'{len(res)} человек в {today}.csv'

def prints (res):
    print('{:10} {:11} {:10} {:7} {:3} {:12} {:10} {:10}'.format('СНИЛС', 'ФИО', 'Дата рожд', 'ВУС', 'Кат', 'Адрес', 'Сотовый', 'Городской'))
    for item in res:
            print(f'{item[0]:10} {item[1]:11} {item[2]:10} {item[3]:7} {item[4]:3} {item[5]:12} {item[6]:10} {item[7]:10}')
