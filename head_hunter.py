import requests
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


def get_vacancies(lang, page):
    base_url = "https://api.hh.ru/"
    params = {
        "text": f"программист {lang}",
        "period": "7",
        "area": "1",
        "per_page": 80,
        "page": page
    }
    response = requests.get(f"{base_url}vacancies", params=params)
    response.raise_for_status()
    return response.json()


def predict_rub_salary(vacancy):
    if not vacancy or vacancy["currency"] != "RUR":
        return None
    elif not vacancy["to"]:
        return vacancy["from"] * 1.2
    elif not vacancy["from"]:
        return vacancy["to"] * 0.8
    else:
        return (vacancy["from"] + vacancy["to"]) / 2

def get_stats_hh():
    stats_hh = {}
    for lang in LANGUAGES:
        salaries = []
        vacancies = []

        response = get_vacancies(lang, 0)
        pages = response["pages"]
        found = response["found"]
        vacancies += response["items"]

        for page in range(1, pages+1):
            vacancies += get_vacancies(lang, page)["items"]

        for vacancy in vacancies:
            if predicted_salary := predict_rub_salary(vacancy["salary"]):
                salaries.append(predicted_salary)

        lang_stat = {
            "vacancies_found": found,
            "vacancies_processed": len(salaries),
            "average_salaries": int(sum(salaries) / len(salaries))
        }
        stats_hh.update({lang: lang_stat})
    return stats_hh


# def get_table_hh(stats):
#     title = "Вакансии headhunter"
#     table_data = [
#         ["Язык программирования", "Вакансий найдено", "Вакансий обработано", "Средняя зарплата"],
#     ]
#     for lang in stats:
#         table_data.append(
#             [lang, stats[lang]["vacancies_found"], stats[lang]["vacancies_processed"], stats[lang]["average_salaries"]]
#         )
#         table = AsciiTable(table_data, title)
#     return table.table
