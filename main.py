import pandas as pd
import re

# Загрузка данных из Excel файла
file_path = 'old_database.xlsx'
data = pd.read_excel(file_path)

# Функция для фильтрации дат рождения
def filter_date(date):
    if pd.isnull(date):
        return True
    cleaned_date = re.sub(r'[\t\s]', '', str(date))
    match = re.search(r'(\d{2}\.\d{2}\.(\d{4}))', cleaned_date)
    if match:
        year = int(match.group(2))
        if 1964 <= year <= 2000:
            return True
    return False


# Фильтрация данных
filtered_data = data[data['Дата рождения'].apply(filter_date)]

# Сохранение отфильтрованных данных в новый Excel файл
filtered_data.to_excel('filtered_database.xlsx', index=False)
