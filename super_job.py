import requests
from environs import Env
from terminaltables import AsciiTable


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


def get_professions_superjob(lang, page):
    id_town = 4
    headers = {
        "X-Api-App-Id": Env().str("TOKEN_SUPERJOB"),
    }

    params = {
        "town": id_town,
        "keyword": f"Программист {lang}",
        "page": page,
        "count": 15
    }

    base_url = "https://api.superjob.ru/2.33/"
    response = requests.get(f"{base_url}vacancies/", headers=headers, params=params)
    return response.json()


def predict_rub_salary(vacancy):
    if not vacancy["payment_from"] and not vacancy["payment_to"] or vacancy["currency"] != "rub":
        return None
    if not vacancy["payment_to"]:
        return vacancy["payment_from"] * 1.2
    elif not vacancy["payment_from"]:
        return vacancy["payment_to"] * 0.8
    else:
        return (vacancy["payment_from"] + vacancy["payment_to"]) / 2


def get_stats_sj():
    stats_sj = {}
    for lang in LANGUAGES:
        vacancies = []
        salaries = []

        page = 1
        response = get_professions_superjob(lang, page)
        more_page = response["more"]

        found = response["total"]
        vacancies += response["objects"]

        while more_page:
            page += 1
            response = get_professions_superjob(lang, page)
            more_page = response["more"]
            vacancies += response["objects"]

        for vacancy in vacancies:
            if predicted_salary := predict_rub_salary(vacancy):
                salaries.append(predicted_salary)

        lang_stat = {
            "vacancies_found": found,
            "vacancies_processed": len(salaries),
            "average_salaries": int(sum(salaries) / len(salaries))
        }
        stats_sj.update({lang: lang_stat})
    return stats_sj


# def get_table_superjob(stats):
#     title = "Вакансии superjob"
#     table_data = [
#         ["Язык программирования", "Вакансий найдено", "Вакансий обработано", "Средняя зарплата"],
#     ]
#     for lang in stats:
#         table_data.append(
#             [lang, stats[lang]["vacancies_found"], stats[lang]["vacancies_processed"], stats[lang]["average_salaries"]]
#         )
#         table = AsciiTable(table_data, title)
#     return table.table
