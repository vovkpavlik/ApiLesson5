from terminaltables import AsciiTable


def get_vacancies_table(stats, title):
    table_data = [
        ["Язык программирования", "Вакансий найдено", "Вакансий обработано", "Средняя зарплата"],
    ]
    for lang in stats:
        table_data.append(
            [lang, stats[lang]["vacancies_found"], stats[lang]["vacancies_processed"], stats[lang]["average_salaries"]]
        )
        table = AsciiTable(table_data, title)
    return table.table