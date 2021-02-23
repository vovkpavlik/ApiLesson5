from environs import Env
from terminaltables import AsciiTable

from head_hunter import get_hh_stats
from super_job import get_sj_stats


LANGUAGES = [
    "Python",
    "Java",
    "Javascript",
    "PHP",
    "C++",
    "CSS",
    "C#",
    "C",
]


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
    
    env = Env()
    env.read_env()
    token = env.str("TOKEN_SUPERJOB")


    print(get_table_vacancies(get_hh_stats(LANGUAGES), "Вакансии headhunter"))
    print(get_table_vacancies(get_sj_stats(LANGUAGES, token), "Вакансии superjob"))
