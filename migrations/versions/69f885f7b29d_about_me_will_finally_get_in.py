"""about_me will finally get in

Revision ID: 69f885f7b29d
Revises: 1157cdeb7396
Create Date: 2018-07-18 15:56:47.942912

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69f885f7b29d'
down_revision = '1157cdeb7396'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###