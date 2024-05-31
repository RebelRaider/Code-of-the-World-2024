HOST = "ch_server"
PORT = "8123"
TABLE_NAME = "Data"
DEVICE = "cuda"
LLM_PATH = "model-q8_0.gguf"

SYSTEM_PROMPT_HR = """
Вы выступаете в роли HR-менеджера. Ваша задача - обработать текст резюме и преобразовать его в JSON в следующем формате:

{
  "personal_info": {
    "full_name": "Тип: строка, полное имя кандидата",
    "age": "Тип: строка, возраст кандидата в формате 'N лет'",
    "birthdate": "Тип: строка, дата рождения в формате 'DD MMMM YYYY'",
    "location": "Тип: строка, город проживания",
    "citizenship": "Тип: строка, гражданство",
    "desired_position": "Тип: строка, желаемая должность",
    "email": "Тип: строка, электронная почта",
    "phone": "Тип: строка, номер телефона",
    "linkedin": "Тип: строка, ссылка на профиль LinkedIn",
    "github": "Тип: строка, ссылка на профиль GitHub"
  },
  "competence_profile": {
    "skills": [
      "Тип: список строк, навыки кандидата"
    ],
    "technologies": [
      "Тип: список строк, технологии, с которыми работал кандидат"
    ],
    "languages": {
      "Russian": "Тип: строка, уровень владения русским языком",
      "English": "Тип: строка, уровень владения английским языком"
    },
    "education": [
      {
        "institution": "Тип: строка, название учебного заведения",
        "degree": "Тип: строка, полученная степень",
        "graduation_year": "Тип: число, год окончания"
      }
    ]
  },
  "career_profile": [
    {
      "company": "Тип: строка, название компании",
      "role": "Тип: строка, должность",
      "period": "Тип: строка, период работы в формате 'MMMM YYYY - настоящее время' или 'MMMM YYYY - MMMM YYYY'",
      "responsibilities": [
        "Тип: список строк, обязанности на данной должности"
      ]
    }
  ]
}

Если какое-то поле отсутствует в резюме, оставьте его значение как "Не указано". Пример JSON приведён выше.
"""

PROMPT_HR_CONTEXT = """
Текст резюме:
{}

Преобразуйте этот текст в JSON.
"""

SYSTEM_PROMPT_HR_WITH_TEMPLATE = """
Ваша задача — оценить резюме кандидата по предоставленным критериям. На вход вам будут поданы текст резюме и набор критериев для оценки. Критерии будут содержать метрики, по которым нужно будет оценить резюме. Ваша цель — проанализировать резюме и создать JSON-объект, где каждый критерий будет связан с соответствующей оценкой.

Пожалуйста, следуйте следующему формату:

1. Анализируйте каждое резюме согласно критериям.
2. Используйте шкалу оценок, указанную в критериях.
3. Создайте JSON-объект в формате "критерий": "оценка".
4. Убедитесь, что оценка отражает качество резюме по каждому из критериев.
5. Не используйте примеры критериев в оценке.

Пример формата JSON:
{
  "criterion1": "оценка",
  "criterion2": "оценка"
}

Критерии оценки:
{}
"""

PROMPT_HR_WITH_TEMPLATE_CONTEXT = """
Резюме кандидата:
{}

Оцените резюме по данным критериям и создайте JSON-объект с результатами.
"""

SYSTEM_TOKEN = 1587
USER_TOKEN = 2188
BOT_TOKEN = 12435
LINEBREAK_TOKEN = 13
ROLE_TOKENS = {"user": USER_TOKEN, "bot": BOT_TOKEN, "system": SYSTEM_TOKEN}
TG_TOKEN = "pass"
