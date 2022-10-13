from user_interface import temperature_view
from user_interface import wind_speed_view
from user_interface import pressure_view

def create(device = 1):
    xml = f'<temperature units = "c">{temperature_view(device)}</temperature>\n'
    xml += f'<wind_speed units = "m/s">{wind_speed_view(device)}</wind_speed>\n'
    xml += f'<pressure units = "mmHg">{pressure_view(device)}</pressure>\n'
    xml += '</xml>'

    with open('index.xml', 'w') as page:
        page.write(xml)
    return xml

def new_create(data, device = 1):
    t, p, w = data
    t = t * 1.8 + 32
    xml = f'<temperature units = "f">{t}</temperature>\n'
    xml += f'<wind_speed units = "m/s">{w}</wind_speed>\n'
    xml += f'<pressure units = "mmHg">{p}</pressure>\n'
    xml += '</xml>'

    with open('new_index.xml', 'w') as page:
        page.write(xml)
    return data