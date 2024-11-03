import pandas as pd

# Загрузка данных (замените на ваш путь к файлу, если необходимо)
df = pd.read_csv("C:\\Users\\abbos\\Desktop\\student-scores.csv")

# Создаем новый столбец для общего балла (среднее арифметическое оценок)
df['test_score'] = df[['math_score', 'history_score', 'physics_score',
                        'chemistry_score', 'biology_score',
                        'english_score', 'geography_score']].mean(axis=1)

# Разбиваем оценки на указанные диапазоны
df['bucket'] = pd.cut(df['test_score'], bins=[0, 50, 75, 90, 100], labels=['<50', '<75', '<90', '<100'])

# Считаем накопительный процент студентов в каждом диапазоне
cumulative_percentage = df['bucket'].value_counts(normalize=True).sort_index().cumsum()

# Приводим к удобному формату для отображения
result = cumulative_percentage.reset_index()
result.columns = ['bucket', 'cumulative_percentage']

# Выводим результаты
print(result)
