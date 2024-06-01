import uuid

from sqlalchemy.orm import sessionmaker

from configs.Database import Engine
from repositories.cv import CVRepository
from schemas.cvschema import CVSchema

json_data = {
    "personal_info": {
        "full_name": "John Doe",
        "age": "30",
        "birthdate": "1990-01-01",
        "location": "New York",
        "citizenship": "USA",
        "desired_position": "Software Engineer",
        "email": "john.doe@example.com",
        "phone": "123-456-7890",
        "linkedin": "https://www.linkedin.com/in/johndoe",
        "github": "https://github.com/johndoe"
    },
    "competence_profile": {
        "skills": ["Python", "Java", "SQL"],
        "technologies": ["Django", "React", "PostgreSQL"],
        "languages": [
            {"name": "English", "level": "Native"},
            {"name": "Spanish", "level": "Fluent"}
        ],
        "education": [
            {"institution": "University of Example", "degree": "BSc Computer Science", "graduation_year": 2012},
            {"institution": "Example Institute of Technology", "degree": "MSc Software Engineering", "graduation_year": 2015}
        ]
    },
    "career_profile": [
        {
            "company": "Tech Corp",
            "role": "Senior Developer",
            "period": "2016-2020",
            "responsibilities": ["Developed software", "Led projects"]
        },
        {
            "company": "Innovative Solutions",
            "role": "Software Engineer",
            "period": "2012-2016",
            "responsibilities": ["Designed applications", "Collaborated with teams"]
        }
    ]
}

test_schema = CVSchema(**json_data)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=Engine)

repo = CVRepository(SessionLocal())

repo.create(test_schema, uuid.UUID("4dec9ffd-61cf-4008-b1de-95ed44d94cb7"))
