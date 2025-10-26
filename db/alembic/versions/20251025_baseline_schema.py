import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "20251025_baseline_schema"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "example",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(50), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("example")
