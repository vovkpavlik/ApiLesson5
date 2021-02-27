from environs import Env

from head_hunter import get_hh_stats
from super_job import get_sj_stats
from table import get_vacancies_table


LANGUAGES = [
    "Python",
    "Java",
    "Javascript",
    "PHP",
    "C++",
    "C#",
    "C",
]


if __name__ == "__main__":
    
    env = Env()
    env.read_env()
    token = env.str("TOKEN_SUPERJOB")


    print(get_vacancies_table(get_hh_stats(LANGUAGES), "Вакансии headhunter"))
    print(get_vacancies_table(get_sj_stats(LANGUAGES, 1, token), "Вакансии superjob"))
