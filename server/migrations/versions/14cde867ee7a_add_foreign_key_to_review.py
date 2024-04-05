"""Add foreign key to review

Revision ID: 14cde867ee7a
Revises: ea67f3a27fa3
Create Date: 2024-04-05 13:08:09.766832

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14cde867ee7a'
down_revision = 'ea67f3a27fa3'
branch_labels = None
depends_on = None


def upgrade():
    # Create a new table with foreign key constraint
    op.create_table('tmp_reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('summary', sa.String(), nullable=True),
    sa.Column('employee_id', sa.Integer(), nullable=True),  # New column for foreign key
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id']),  # Foreign key constraint
    sa.PrimaryKeyConstraint('id')
    )

    # Copy data from old table to new table
    op.execute("INSERT INTO tmp_reviews (id, year, summary) SELECT id, year, summary FROM reviews")

    # Drop old table
    op.drop_table('reviews')

    # Rename new table to old table name
    op.rename_table('tmp_reviews', 'reviews')


def downgrade():
    # In the downgrade, you might need to reverse the process.
    pass
