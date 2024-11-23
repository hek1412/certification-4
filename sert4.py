import pandas as pd

df = pd.read_csv('data.csv')

average_salary = df[['salary']].mean().item() # Вычисляем среднюю зп
print(f"Средняя зарплата сотрудников:{average_salary}")

age = df[df['age'] > 30] # Вычисляем у кого возраст старше 30 лет
print("Сотрудники старше 30 лет:")
print(age)
