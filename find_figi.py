import pandas as pd

def find_FIGI():
    try:
        # Читаем файл с данными
        figis = pd.read_csv('source/name_figi_ticker_ru.txt', sep='\t', encoding='utf-8', on_bad_lines='skip')
    except FileNotFoundError:
        print("Файл не найден. Проверьте путь к файлу.")
        return
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
        return

    # Вывод первых 5 строк в виде таблицы
    print("Первые 5 строк из файла:")
    print(figis.head())  # Выводим первые 5 строк

    # Вводим тикер
    user_input = input("Введите тикер: ").strip()

    # Поиск по тикеру (2-й столбец)
    result_by_ticker = figis.loc[figis.iloc[:, 2].str.lower() == user_input.lower(), figis.columns[1]]  # FIGI в 1-м столбце

    if not result_by_ticker.empty:
        # Удаляем дубликаты и преобразуем в уникальный список
        figis = result_by_ticker.tolist()
        print("\nНайденные FIGI:")
        print("\n".join(figis))  # Печатаем FIGI, разделенные новой строкой
        return figis[-1]  # Возвращаем список FIGI
    else:
        print("Тикер не найден.")
        return None  # Возвращаем None, если ничего не найдено

# Пример вызова функции


