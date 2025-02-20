"""Create phone number for user column

Revision ID: c067454158b1
Revises: 
Create Date: 2025-02-19 17:08:12.513852

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c067454158b1'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade() -> None:
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))


def downgrade() -> None:
    pass
