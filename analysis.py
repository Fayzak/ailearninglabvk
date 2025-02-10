import sys

import pandas as pd
from scipy import stats
from functools import partial
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


def load_file(file):
    return pd.read_csv(file, sep="\t")


def main():
    filename = sys.argv[1]

    users_df = load_file(filename)

    print(users_df.head())
    
    # Общая информация о данных
    info = users_df.info()

    # Описательная статистика
    description = users_df.describe()

    # Проверка на пропущенные значения
    missing_values = users_df.isnull().sum()

    # Гистограмма распределения возраста
    plt.figure(figsize=(8, 5))
    sns.histplot(users_df[users_df["age"] > 0]["age"], bins=30, kde=True)
    plt.title("Распределение возраста пользователей")
    plt.xlabel("Возраст")
    plt.ylabel("Количество")
    plt.show()

    # Проверка нормальности распределения возраста
    age_values = users_df[users_df["age"] > 0]["age"]
    shapiro_test = stats.shapiro(age_values.sample(min(5000, len(age_values))))

    print(info)
    print(description)
    print(missing_values)
    print(shapiro_test)

    # Анализ распределения пола
    plt.figure(figsize=(5, 5))
    sns.countplot(x="sex", data=users_df, palette="pastel")
    plt.title("Распределение пола пользователей")
    plt.xlabel("Пол (1 - Мужской, 2 - Женский)")
    plt.ylabel("Количество")
    plt.xticks(ticks=[0, 1, 2], labels=["Не указан", "Мужской", "Женский"])
    plt.show()

    # Доля пользователей с возрастом 0
    zero_age_count = (users_df["age"] == 0).sum()
    zero_age_percentage = zero_age_count / len(users_df) * 100

    # Анализ распределения пользователей по городам
    top_cities = users_df["city_id"].value_counts().head(10)  # Топ-10 городов

    plt.figure(figsize=(10, 5))
    sns.barplot(x=top_cities.index, y=top_cities.values, palette="coolwarm")
    plt.title("Топ-10 городов по числу пользователей")
    plt.xlabel("ID города")
    plt.ylabel("Количество пользователей")
    plt.show()

    print(zero_age_count)
    print(zero_age_percentage)
    print(top_cities)

    # tasks = tasks.assign(
    #     at_least_one=0,
    #     at_least_two=0,
    #     at_least_three=0,
    # )
    # tasks[['at_least_one', 'at_least_two', 'at_least_three']].to_csv(sys.stdout, sep="\t", index=False, header=True)


if __name__ == '__main__':
    main()
