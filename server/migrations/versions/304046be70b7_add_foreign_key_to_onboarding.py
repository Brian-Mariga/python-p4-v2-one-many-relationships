"""add foreign key to onboarding

Revision ID: 304046be70b7
Revises: 14cde867ee7a
Create Date: 2024-04-05 13:45:50.182217

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '304046be70b7'
down_revision = '14cde867ee7a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('onboardings') as batch_op:
        batch_op.create_foreign_key(op.f('fk_onboardings_employee_id_employees'), 'employees', ['employee_id'], ['id'])
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('onboardings') as batch_op:
        batch_op.drop_constraint(op.f('fk_onboardings_employee_id_employees'), type_='foreignkey')
    # ### end Alembic commands ###