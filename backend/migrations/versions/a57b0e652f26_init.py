"""init

Revision ID: a57b0e652f26
Revises: 
Create Date: 2024-06-01 08:29:30.224250

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a57b0e652f26'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cv',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('career_profile',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('cv', sa.Uuid(), nullable=False),
    sa.Column('company', sa.String(), nullable=False),
    sa.Column('role', sa.String(), nullable=False),
    sa.Column('period', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['cv'], ['cv.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('competence_profile',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('cv', sa.Uuid(), nullable=False),
    sa.ForeignKeyConstraint(['cv'], ['cv.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('personal_info',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('cv', sa.Uuid(), nullable=False),
    sa.Column('full_name', sa.String(), nullable=False),
    sa.Column('age', sa.String(), nullable=False),
    sa.Column('birthdate', sa.String(), nullable=False),
    sa.Column('location', sa.String(), nullable=False),
    sa.Column('citizenship', sa.String(), nullable=False),
    sa.Column('desired_position', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('phone', sa.String(), nullable=False),
    sa.Column('linkedin', sa.String(), nullable=True),
    sa.Column('github', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['cv'], ['cv.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('education',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('competence', sa.Uuid(), nullable=False),
    sa.Column('institution', sa.String(), nullable=True),
    sa.Column('degree', sa.String(), nullable=True),
    sa.Column('graduation_year', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['competence'], ['competence_profile.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('language',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('competence', sa.Uuid(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['competence'], ['competence_profile.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('responsibility',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('profile', sa.Uuid(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['profile'], ['competence_profile.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('skill',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('competence', sa.Uuid(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['competence'], ['competence_profile.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('technology',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('competence', sa.Uuid(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['competence'], ['competence_profile.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('technology')
    op.drop_table('skill')
    op.drop_table('responsibility')
    op.drop_table('language')
    op.drop_table('education')
    op.drop_table('personal_info')
    op.drop_table('competence_profile')
    op.drop_table('career_profile')
    op.drop_table('cv')
    # ### end Alembic commands ###
