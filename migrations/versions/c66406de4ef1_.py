"""empty message

Revision ID: c66406de4ef1
Revises: a80e74dbc5ab
Create Date: 2017-06-10 19:17:27.607098

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c66406de4ef1'
down_revision = 'a80e74dbc5ab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reversals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=True),
    sa.Column('value', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_reversals_client_id'), 'reversals', ['client_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_reversals_client_id'), table_name='reversals')
    op.drop_table('reversals')
    # ### end Alembic commands ###
