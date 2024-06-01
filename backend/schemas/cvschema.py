from typing import Optional, List

from pydantic import BaseModel


class PersonalInfoSchema(BaseModel):
    full_name: str
    age: str
    birthdate: str
    location: str
    citizenship: str
    desired_position: str
    email: str
    phone: str
    linkedin: Optional[str]
    github: Optional[str]


class EducationSchema(BaseModel):
    institution: str
    degree: str
    graduation_year: int


class LanguageSchema(BaseModel):
    name: str
    level: str


class CompetenceProfileSchema(BaseModel):
    skills: List[str]
    technologies: List[str]
    languages: dict
    education: List[EducationSchema]


class CareerProfileSchema(BaseModel):
    company: str
    role: str
    period: str
    responsibilities: List[str]


class CVSchema(BaseModel):
    personal_info: PersonalInfoSchema
    competence_profile: CompetenceProfileSchema
    career_profile: List[CareerProfileSchema]
    score: str | None = None
