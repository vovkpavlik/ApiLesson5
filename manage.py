from head_hunter import get_stats_hh
from super_job import get_stats_sj
from terminaltables import AsciiTable
from environs import Env


def get_table_vacancies(stats, title):
    table_data = [
        ["Язык программирования", "Вакансий найдено", "Вакансий обработано", "Средняя зарплата"],
    ]
    for lang in stats:
        table_data.append(
            [lang, stats[lang]["vacancies_found"], stats[lang]["vacancies_processed"], stats[lang]["average_salaries"]]
        )
        table = AsciiTable(table_data, title)
    return table.table


if __name__ == '__main__':
    Env().read_env()
    print(get_table_vacancies(get_stats_hh(), "Вакансии headhunter"))
    print(get_table_vacancies(get_stats_sj(), "Вакансии superjob"))
