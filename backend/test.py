import uuid

from sqlalchemy.orm import sessionmaker

from configs.Database import Engine
from models.cv import PersonalInfo
from repositories.cv import CVRepository
from schemas.cvschema import CVSchema

json_data = {
   "personal_info": {
      "full_name": "Тестович Тест Тестович",
      "age": "27 лет (31 марта 1997)",
      "birthdate": "31 марта 1997",
      "location": "Москва",
      "citizenship": "Россия",
      "desired_position": "Системный аналитик",
      "email": "Не указано",
      "phone": "Не указано",
      "linkedin": "Не указано",
      "github": "Не указано"
   },
   "competence_profile": {
      "skills": [
         "MS Excel",
         "Solid Works",
         "AutoCAD",
         "Анализ ЕСКД",
         "Adobe Photoshop",
         "MS Word",
         "Bi",
         "HTML5, JavaScript",
         "Adobe Photoshop"
      ],
      "technologies": [
         "П-Чад",
         "Redmine",
         "Kibana",
         "Postman"
      ],
      "languages": {
         "Russian": "Родной",
         "English": "Средний"
      },
      "education": [
         {
            "institution": "Московский государственный технический университет радиотехники, электроники и автоматики, Москва",
            "degree": "Институт радиотехнических и телекоммуникационных систем/Конструирование и технология электронных средств",
            "graduation_year": 2021
         },
         {
            "institution": "Московский государственный технический университет им. Н.Э. Баумана, Москва",
            "degree": "Информатика и управление/Конструирование и технология электронных средств",
            "graduation_year": 2019
         }
      ]
   },
   "career_profile": [
      {
         "company": "Вымпел, Группа компаний",
         "role": "Старший системный аналитик",
         "period": "май 2023 настоящее время (1 год)",
         "responsibilities": [
            "Писал документацию в Confluence на редизайн различных страниц.",
            "Описывал интеграционное взаимодействие загрузки данных на страницу с помощью sequence диаграммы.",
            "Составлял примерный json-файл данных для контента страницы.",
            "Проводил ревью других аналитиков.",
            "Участвовал в переезде со старого монолита на новый микросервис.",
            "Описывал маппинг полей старого функционала и нового.",
            "Проверял API в Postman.",
            "Оформлял подписки на продукт, контролировал выполнение работы."
         ]
      },
      {
         "company": "Сравни.ру, ООО",
         "role": "Младший системный аналитик",
         "period": "март 2023 - май 2023 (3 месяца)",
         "responsibilities": [
            "Был в команде реферальных программ.",
            "Частые запросы были от заказчиков, почему не начислился бонус.",
            "Искал в БД путем джойна и агрегирующих функций за кем зарегистрирован бонус.",
            "Участвовал в проектировании API по подгрузке дополнительных рекламных акций со сторонних ресурсов.",
            "Описывал интеграционное взаимодействие (параметры запросов, какими полями должен отдавать запрос, составление спецификации).",
            "Загружал данные по новым продуктам партнеров в БД, выгружал еженедельный отчет в Excel для заказчика."
         ]
      },
      {
         "company": "Доверенная среда",
         "role": "Младший системный аналитик",
         "period": "март 2022 - январь 2023 (11 месяцев)",
         "responsibilities": [
            "Интервьюирование заказчика.",
            "Работа в Bi-системе, настройка загрузки данных, составление отчетов, форм и реестров.",
            "Строительство дашбордов.",
            "Участие в ПМИ.",
            "Проведение ежедневных стендапов, обсуждение того, что делал/будет делать, какие есть блокировщики."
         ]
      },
      {
         "company": "НПО Эшелон, ЗАО",
         "role": "Технический писатель",
         "period": "ноябрь 2021 - март 2022 (5 месяцев)",
         "responsibilities": [
            "Разработка конструкторской документации: сборочные чертежи на аппаратуру, спецификации.",
            "Подготовка к испытаниям и сертификации."
         ]
      },
      {
         "company": "НПО Алмаз",
         "role": "Инженер-конструктор",
         "period": "сентябрь 2019 - ноябрь 2021 (2 года 3 месяца)",
         "responsibilities": [
            "Разработка топологии печатных плат.",
            "Составление конструкторской документации (спецификация, сборочный чертеж на ячейку и печатную плату)."
         ]
      }
   ]
}


test_schema = CVSchema(**json_data)
print(test_schema)


