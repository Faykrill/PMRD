import numpy as np
import pandas as pd

# Фиксируем сид для воспроизводимости результатов
np.random.seed(42)

n_samples = 10000

# Создаем словарь с 10 признаками разного типа
data = {
    # Числовые признаки (float)
    'feature_num_1': np.random.uniform(0, 100, n_samples),
    'feature_num_2': np.random.normal(50, 15, n_samples),
    'feature_num_3': np.random.exponential(1, n_samples),
    'feature_num_4': np.random.uniform(-10, 10, n_samples),
    'feature_num_5': np.random.lognormal(0, 1, n_samples),
    
    # Целочисленные признаки (int)
    'feature_int_1': np.random.randint(1, 100, n_samples),
    'feature_int_2': np.random.randint(0, 2, n_samples),  # Бинарный признак
    'feature_int_3': np.random.choice([10, 20, 30, 40, 50], n_samples),
    
    # Категориальные признаки (object)
    'feature_cat_1': np.random.choice(['Category_A', 'Category_B', 'Category_C', 'Category_D'], n_samples),
    'feature_cat_2': np.random.choice(['Type_X', 'Type_Y'], n_samples)
}

# Преобразуем в DataFrame и сохраняем в CSV
df = pd.DataFrame(data)
df.to_csv('data.csv', index=False)

print(f"Файл 'data.csv' успешно сгенерирован! Размер: {df.shape[0]} строк, {df.shape[1]} признаков.")