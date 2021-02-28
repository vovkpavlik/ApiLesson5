import requests

from salary import predict_rub_salary


def get_vacancies(lang, page):
    count_days = 30
    id_moscow = 1
    per_page = 100

    base_url = "https://api.hh.ru/"
    params = {
        "text": f"программист {lang}",
        "period": count_days,
        "area": id_moscow,
        "per_page": per_page,
        "page": page
    }
    response = requests.get(f"{base_url}vacancies", params=params)
    response.raise_for_status()
    return response.json()


def get_language_salaries(lang):
    salaries = []
    vacancies = []

    response = get_vacancies(lang, 0)
    vacancies += response["items"]
    pages = response["pages"]

    # Результатов не может быть более 2000(https://github.com/hhru/api/blob/master/docs/vacancies.md#запрос)
    for page in range(1, pages):
        vacancies += get_vacancies(lang, page)["items"]

    for vacancy in vacancies:
        if not vacancy["salary"] or vacancy["salary"]["currency"] != "RUR":
            continue
        if predicted_salary := predict_rub_salary(vacancy["salary"]["from"], vacancy["salary"]["to"]):
            salaries.append(predicted_salary)
    return salaries


def get_language_vacancies(lang):
    response = get_vacancies(lang, 0)
    vacancies_found = response["found"]
    return vacancies_found

def get_hh_stats(languages):
    hh_stats = {}
    for lang in languages:
        language_salaries = get_language_salaries(lang)
        lang_stat = {
            "vacancies_found": get_language_vacancies(lang),
            "vacancies_processed": len(language_salaries),
            "average_salaries": int(sum(language_salaries) / len(language_salaries))
        }
        hh_stats[lang] = lang_stat
    return hh_stats
