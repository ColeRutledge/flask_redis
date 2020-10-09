"""user add: about_me, last_seen

Revision ID: 2305623ff1ee
Revises: 9b72b85f969c
Create Date: 2020-10-09 09:57:52.692462

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2305623ff1ee'
down_revision = '9b72b85f969c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('users', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'last_seen')
    op.drop_column('users', 'about_me')
    # ### end Alembic commands ###
