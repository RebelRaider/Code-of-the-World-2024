import uuid
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.BaseModel import EntityMeta


class PersonalInfo(EntityMeta):
    __tablename__ = "personal_info"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    cv_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('cv.id'), nullable=False)
    cv: Mapped["СV"] = relationship("CV", back_populates="personal_info")
    full_name: Mapped[str] = mapped_column(nullable=False)
    age: Mapped[str] = mapped_column(nullable=False)
    birthdate: Mapped[str] = mapped_column(nullable=False)
    location: Mapped[str] = mapped_column(nullable=False)
    citizenship: Mapped[str] = mapped_column(nullable=False)
    desired_position: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    phone: Mapped[str] = mapped_column(nullable=False)
    linkedin: Mapped[str] = mapped_column(nullable=True)
    github: Mapped[str] = mapped_column(nullable=True)


class Skill(EntityMeta):
    __tablename__ = "skill"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    competence_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('competence_profile.id'), nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)


class Technology(EntityMeta):
    __tablename__ = "technology"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    competence_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('competence_profile.id'), nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)


class Language(EntityMeta):
    __tablename__ = "language"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    competence_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('competence_profile.id'), nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    level: Mapped[str] = mapped_column(nullable=False)


class Education(EntityMeta):
    __tablename__ = "education"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    competence_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('competence_profile.id'), nullable=False)
    institution: Mapped[str] = mapped_column(nullable=True)
    degree: Mapped[str] = mapped_column(nullable=True)
    graduation_year: Mapped[int] = mapped_column(nullable=True)


class CompetenceProfile(EntityMeta):
    __tablename__ = "competence_profile"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    cv_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('cv.id'), nullable=False)
    skills: Mapped[list["Skill"]] = relationship()
    technologies: Mapped[list["Technology"]] = relationship()
    languages: Mapped[list["Language"]] = relationship()
    education: Mapped[list["Education"]] = relationship()


class Responsibility(EntityMeta):
    __tablename__ = "responsibility"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    profile_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('career_profile.id'), nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)


class CareerProfile(EntityMeta):
    __tablename__ = "career_profile"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    cv_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('cv.id'), nullable=False)
    company: Mapped[str] = mapped_column(nullable=False)
    role: Mapped[str] = mapped_column(nullable=False)
    period: Mapped[str] = mapped_column(nullable=False)
    responsibilities: Mapped[list["Responsibility"]] = relationship()


class CV(EntityMeta):
    __tablename__ = 'cv'
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    personal_info: Mapped["PersonalInfo"] = relationship("PersonalInfo", back_populates="cv")
    competence_profile: Mapped["CompetenceProfile"] = relationship()
    career_profile: Mapped[list["CareerProfile"]] = relationship()
    # user: Mapped[uuid.UUID] = mapped_column(ForeignKey("user.id"), nullable=False)
