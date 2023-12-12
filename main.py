# Задание 2
# При помощи инструмента Streamlit проведите разведочный анализ данных. В него может входить:

# построение графиков распределений признаков
# построение матрицы корреляций
# построение графиков зависимостей целевой переменной и признаков
# вычисление числовых характеристик распределения числовых столбцов (среднее, min, max, медиана и так далее)
# любые другие ваши идеи приветствуются!

import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
#import plotly.express as px

df = pd.read_csv('dataset.csv')
df_coded = df.copy()

df_coded['EDUCATION'] = pd.Categorical(df_coded['EDUCATION']).codes
df_coded['FAMILY_INCOME'] = pd.Categorical(df_coded['FAMILY_INCOME_x']).codes
df_coded.drop('FAMILY_INCOME_x', axis=1, inplace=True)

columns = list(df.columns)
columns = [x for x in columns if x != "TARGET"]


st.title('Разведочный анализ данных')

st.title('1. Числовые характеристик распределения числовых столбцов:')
st.dataframe(df.describe())

st.title('2. Графики зависимостей целевой переменной и признаков')

column = st.selectbox(
    "Выбери по какому признаку смотрим от чего зависит отклик на маркетинговую кампанию", columns
)

fig, ax = plt.subplots(figsize=(15,5))
sns.barplot(x=column, y='TARGET', data=df)
st.title(f"График зависимости отклика на маркетинговую кампанию от {column}")
st.pyplot(fig)

st.title('3. Матрица корреляций')

fig = plt.figure(figsize=(10, 10))
fig.suptitle("Heatmap")
sns.heatmap(df_coded.corr(), annot=False, vmin=-1, vmax=1, center=0, cmap='coolwarm')
st.pyplot(fig)


st.title('4. График распределения признаков')

feature = st.selectbox('Выберите признак', df.columns)


fig, ax = plt.subplots(figsize=(8, 6))
plt.hist(df[feature], bins=10)
plt.xlabel('Значение признака')
plt.ylabel('Частота')
plt.title('Распределение признака')
st.write(fig)

