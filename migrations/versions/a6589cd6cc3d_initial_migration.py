"""Initial migration.

Revision ID: a6589cd6cc3d
Revises: 
Create Date: 2021-08-31 02:15:19.271930

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6589cd6cc3d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=250), nullable=True),
    sa.Column('password', sa.String(length=15), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('todolists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('Completed', sa.Boolean(), nullable=False),
    sa.Column('usermodel_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['usermodel_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('todolistname', sa.String(length=250), nullable=True),
    sa.Column('usermodel_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['usermodel_id'], ['todolists.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('items')
    op.drop_table('todolists')
    op.drop_table('users')
    # ### end Alembic commands ###
