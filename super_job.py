import requests

from salary import predict_rub_salary


def get_superjob_professions(lang, page, token):
    moscow_id = 4
    per_page = 15
    headers = {
        "X-Api-App-Id": token,
    }

    params = {
        "town": moscow_id,
        "keyword": f"Программист {lang}",
        "page": page,
        "count": per_page
    }

    base_url = "https://api.superjob.ru/2.33/"
    response = requests.get(f"{base_url}vacancies/", headers=headers, params=params)
    response.raise_for_status()
    return response.json()


def get_language_salaries(lang, token):
    vacancies = []
    salaries = []

    page = 1
    response = get_superjob_professions(lang, page, token)
    more_page = response["more"]

    vacancies += response["objects"]

    while more_page:
        page += 1
        response = get_superjob_professions(lang, page, token)
        more_page = response["more"]
        vacancies += response["objects"]

    for vacancy in vacancies:
        if vacancy["currency"] != "rub":
            continue
        if predicted_salary := predict_rub_salary(vacancy["payment_from"], vacancy["payment_to"]):
            salaries.append(predicted_salary)
    return salaries


def get_language_found(lang, page, token):
    response = get_superjob_professions(lang, page, token)
    found = response["total"]
    return found


def get_sj_stats(languages, page, token):
    sj_stats = {}
    for lang in languages:
        language_salaries = get_language_salaries(lang, token)
        lang_stat = {
            "vacancies_found": get_language_found(lang, page, token),
            "vacancies_processed": len(language_salaries),
            "average_salaries": int(sum(language_salaries) / len(language_salaries))
        }
        sj_stats[lang] = lang_stat
    return sj_stats
