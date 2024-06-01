import uuid
from typing import List, Optional
from uuid import uuid4

from loguru import logger
from sqlalchemy.orm import Session

from models.cv import CV, CareerProfile, Responsibility, CompetenceProfile, Education, Language, Technology, Skill, \
    PersonalInfo
from schemas.cvschema import CVSchema, CareerProfileSchema, CompetenceProfileSchema, EducationSchema, LanguageSchema, \
    PersonalInfoSchema


def convert_personal_info(p_info: PersonalInfoSchema) -> PersonalInfo:
    return PersonalInfo(
        id=uuid4(),
        full_name=p_info.full_name,
        age=p_info.age,
        birthdate=p_info.birthdate,
        location=p_info.location,
        citizenship=p_info.citizenship,
        desired_position=p_info.desired_position,
        email=p_info.email,
        phone=p_info.phone,
        linkedin=p_info.linkedin,
        github=p_info.github
    )


def convert_skill(skill: str, competence_profile_id: uuid.UUID) -> Skill:
    return Skill(id=uuid4(), competence_id=competence_profile_id, name=skill)


def convert_technology(tech: str, competence_profile_id: uuid.UUID) -> Technology:
    return Technology(id=uuid4(), competence_id=competence_profile_id, name=tech)


def convert_language(lang: LanguageSchema, competence_profile_id: uuid.UUID) -> Language:
    return Language(id=uuid4(), competence_id=competence_profile_id, name=lang.name, level=lang.level)


def convert_education(edu: EducationSchema, competence_profile_id: uuid.UUID) -> Education:
    return Education(id=uuid4(), competence_id=competence_profile_id, institution=edu.institution,
                     degree=edu.degree, graduation_year=edu.graduation_year)


def convert_competence_profile(c_profile: CompetenceProfileSchema) -> CompetenceProfile:
    competence_profile_id = uuid4()
    skills = [convert_skill(skill, competence_profile_id) for skill in c_profile.skills]
    technologies = [convert_technology(tech, competence_profile_id) for tech in c_profile.technologies]
    languages = [convert_language(lang, competence_profile_id) for lang in c_profile.languages]
    education = [convert_education(edu, competence_profile_id) for edu in c_profile.education]

    return CompetenceProfile(
        id=competence_profile_id,
        skills=skills,
        technologies=technologies,
        languages=languages,
        education=education
    )


def convert_responsibility(responsibility: str, career_profile_id: uuid.UUID) -> Responsibility:
    return Responsibility(id=uuid4(), profile_id=career_profile_id, name=responsibility)


def convert_career_profile(c_profile: CareerProfileSchema) -> CareerProfile:
    career_profile_id = uuid4()
    responsibilities = [convert_responsibility(resp, career_profile_id) for resp in c_profile.responsibilities]

    return CareerProfile(
        id=career_profile_id,
        company=c_profile.company,
        role=c_profile.role,
        period=c_profile.period,
        responsibilities=responsibilities
    )


def convert_cv(cv_schema: CVSchema, user_id: uuid.UUID) -> CV:
    personal_info = convert_personal_info(cv_schema.personal_info)
    competence_profile = convert_competence_profile(cv_schema.competence_profile)
    career_profile = [convert_career_profile(cp) for cp in cv_schema.career_profile]

    cv_id = uuid4()
    personal_info.cv_id = cv_id
    competence_profile.cv_id = cv_id
    for cp in career_profile:
        cp.cv_id = cv_id

    return CV(
        id=cv_id,
        personal_info=personal_info,
        competence_profile=competence_profile,
        career_profile=career_profile,
        # user=user_id,
    )
