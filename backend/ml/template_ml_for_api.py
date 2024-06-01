from ml import interact_hr, interact_hr_with_template
from llama_cpp import Llama

from ml.init import llm_model
from parsing.omega_parser import read_any_doc
import os


# Шаблон для API
def template_for_upload_cv(path_to_temp_file: os.PathLike, model: Llama = llm_model,) -> str:
    """
    Функция для обработки резюме и вытягивания данных в строку (json???) (json кста не напиздел)

    Args:
        model (Llama):  Модель gguf под llama_cpp
        file (binary?): резюме для распаршивания и отправки в модель

    Returns:
        str: ответ от модели (json???) парсинга резюме по шаблону (json кста не напиздел)
    """
    resume = read_any_doc(path_to_temp_file)
    answer = interact_hr(model=model, content=resume)
    return answer


# Шаблон для API
def template_rate_the_candidate(model: Llama, resume_from_db: str, template: str) -> str:
    """
    шаблон для эндпоинта, который сравнивает резюме и шаблон и возвращает оценку по шаблону (json брат...)

    Args:
        model (Llama): Модель gguf под llama_cpp
        resume_from_db (str): резюме из бдхи конвертированное в строку (что хочешь посчитаешь полезным в оценке компетенций то и пихай, наверное навыки и работу конверть, остальное пох)
        template (str): шаблон с критериями кандидата Максим присылает вместе с id чела чьё резюме мы чекаем (json))))

    Returns:
        str: оценка кандидата по шаблону
    """
    answer = interact_hr_with_template(model=model, content=resume_from_db,
                                       request=template)  # По шаблону получаем оценку по критериям (template) кандидата
    return answer
