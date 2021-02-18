import requests


def get_vacancies(lang, page):
    count_days = 30
    id_moscow = 1

    base_url = "https://api.hh.ru/"
    params = {
        "text": f"программист {lang}",
        "period": count_days,
        "area": id_moscow,
        "per_page": 100,
        "page": page
    }
    response = requests.get(f"{base_url}vacancies", params=params)
    response.raise_for_status()
    return response.json()


def predict_hh_rub_salary(vacancy):
    if not vacancy or vacancy["currency"] != "RUR":
        return None
    elif not vacancy["to"]:
        return vacancy["from"] * 1.2
    elif not vacancy["from"]:
        return vacancy["to"] * 0.8
    else:
        return (vacancy["from"] + vacancy["to"]) / 2

def get_stats_hh(languages):
    stats_hh = {}
    for lang in languages:
        salaries = []
        vacancies = []

        response = get_vacancies(lang, 0)
        found = response["found"]
        vacancies += response["items"]

        # Результатов не может быть более 2000(https://github.com/hhru/api/blob/master/docs/vacancies.md#запрос)
        for page in range(1, 20):
            vacancies += get_vacancies(lang, page)["items"]

        for vacancy in vacancies:
            if predicted_salary := predict_hh_rub_salary(vacancy["salary"]):
                salaries.append(predicted_salary)

        lang_stat = {
            "vacancies_found": found,
            "vacancies_processed": len(salaries),
            "average_salaries": int(sum(salaries) / len(salaries))
        }
        stats_hh.update({lang: lang_stat})
    return stats_hh
