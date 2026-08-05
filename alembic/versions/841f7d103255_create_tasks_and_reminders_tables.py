"""create tasks and reminders tables

Revision ID: 841f7d103255
Revises: 
Create Date: 2026-08-05 13:44:04.281333

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '841f7d103255'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    """Upgrade schema."""

    op.create_table(
        'tasks',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('task_type', sa.String(), nullable=False),
        sa.Column('priority', sa.String(), nullable=False),
        sa.Column('start_date', sa.DateTime(), nullable=True),
        sa.Column('due_date', sa.DateTime(), nullable=True),
        sa.Column('recurrence_type', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('status', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_index(
        op.f('ix_tasks_id'),
        'tasks',
        ['id'],
        unique=False
    )


    op.create_table(
        'reminders',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('task_id', sa.Integer(), nullable=False),
        sa.Column('remind_at', sa.DateTime(), nullable=False),
        sa.Column('is_sent', sa.Boolean(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['task_id'], ['tasks.id']),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_index(
        op.f('ix_reminders_id'),
        'reminders',
        ['id'],
        unique=False
    )

def downgrade() -> None:
    """Downgrade schema."""

    op.drop_index(
        op.f('ix_reminders_id'),
        table_name='reminders'
    )

    op.drop_table('reminders')

    op.drop_index(
        op.f('ix_tasks_id'),
        table_name='tasks'
    )

    op.drop_table('tasks')