from datetime import datetime as dt

def temperature_logger(data):
    time = dt.now().strftime("%H:%M")
    with open("log.csv", "a") as file:
        file.write(f'{time},temperature,{data}')

def pressure_logger(data):
    time = dt.now().strftime("%H:%M")
    with open("log.csv", "a") as file:
        file.write(f'{time},pressure,{data}')

def wind_speed_logger(data):
    time = dt.now().strftime("%H:%M")
    with open("log.csv", "a") as file:
        file.write(f'{time},wind_speed,{data}')



