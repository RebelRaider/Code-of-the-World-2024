from ml import interact_hr, interact_hr_with_template
from llama_cpp import Llama

# Шаблон для API
def template_for_upload_cv(model: Llama, file) -> str:
    """
    Функция для обработки резюме и вытягивания данных в строку (json???)

    Args:
        model (Llama):  Модель gguf под llama_cpp
        file (binary?): резюме для распаршивания и отправки в модель

    Returns:
        str: ответ от модели (json???) парсинга резюме по шаблону
    """
    resume = "Распаршенное резюме"  # file
    answer = interact_hr(model=model, content=resume)
    return answer


# Шаблон для API
def template_rate_the_candidate(model: Llama, resume_from_db: str, template: str) -> str:
    """
    шаблон для эндпоинта, который сравнивает резюме и шаблон и возвращает оценку по шаблону

    Args:
        model (Llama): Модель gguf под llama_cpp
        resume_from_db (str): резюме из бдхи конвертированное в строку
        template (str): шаблон с критериями кандидата

    Returns:
        str: оценка кандидата по шаблону
    """
    answer = interact_hr_with_template(model=model, content=resume_from_db, request=template) # По шаблону получаем оценку по критериям (template) кандидата
    return answer
