"""add description

Revision ID: 9ad49c28d6dc
Revises: 127404c96448
Create Date: 2023-04-13 14:32:24.839205

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = '9ad49c28d6dc'
down_revision = '127404c96448'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('meetingroom', sa.Column('description', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('meetingroom', 'description')
    # ### end Alembic commands ###