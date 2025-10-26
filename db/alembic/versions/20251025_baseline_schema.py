"""baseline schema

Revision ID: 20251025_baseline_schema
Revises:
Create Date: 2025-10-25 12:00:00.000000
"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "20251025_baseline_schema"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String, nullable=False),
        sa.Column("role", sa.String, nullable=False),
        sa.Column("active", sa.Boolean, default=True),
    )


def downgrade():
    op.drop_table("users")
