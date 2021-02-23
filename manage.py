from environs import Env

from head_hunter import get_hh_stats
from super_job import get_sj_stats
from table import get_table_vacancies


LANGUAGES = [
    "Python",
    "Java",
    "Javascript",
    "PHP",
    "C++",
    "C#",
    "C",
]


if __name__ == '__main__':
    
    env = Env()
    env.read_env()
    token = env.str("TOKEN_SUPERJOB")


    print(get_table_vacancies(get_hh_stats(LANGUAGES), "Вакансии headhunter"))
    print(get_table_vacancies(get_sj_stats(LANGUAGES, token), "Вакансии superjob"))
