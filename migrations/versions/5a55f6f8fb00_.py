"""empty message

Revision ID: 5a55f6f8fb00
Revises: b94cb8a4c400
Create Date: 2022-05-10 14:54:56.362371

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a55f6f8fb00'
down_revision = 'b94cb8a4c400'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('goal', sa.Column('title', sa.String(), nullable=True))
    op.drop_column('goal', 'goal_title')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('goal', sa.Column('goal_title', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('goal', 'title')
    # ### end Alembic commands ###
