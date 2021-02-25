def predict_rub_salary(salary_from, salary_to):
    if not salary_from and not salary_to:
        return None
    elif not salary_to:
        return salary_from * 1.2
    elif not salary_from:
        return salary_to * 0.8
    return (salary_from + salary_to) / 2
