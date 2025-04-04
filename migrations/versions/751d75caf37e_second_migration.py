"""Second migration

Revision ID: 751d75caf37e
Revises: 501764ad04d4
Create Date: 2025-04-04 14:25:43.755313

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '751d75caf37e'
down_revision = '501764ad04d4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('today_weather', schema=None) as batch_op:
        batch_op.alter_column('highest_temp',
               existing_type=sa.VARCHAR(length=10),
               type_=sa.String(length=50),
               existing_nullable=True)
        batch_op.alter_column('lowest_temp',
               existing_type=sa.VARCHAR(length=10),
               type_=sa.String(length=50),
               existing_nullable=True)
        batch_op.alter_column('humidity',
               existing_type=sa.VARCHAR(length=10),
               type_=sa.String(length=50),
               existing_nullable=True)
        batch_op.alter_column('dew_point',
               existing_type=sa.VARCHAR(length=10),
               type_=sa.String(length=50),
               existing_nullable=True)
        batch_op.alter_column('pressure',
               existing_type=sa.VARCHAR(length=10),
               type_=sa.String(length=50),
               existing_nullable=True)
        batch_op.alter_column('uv_index',
               existing_type=sa.VARCHAR(length=10),
               type_=sa.String(length=50),
               existing_nullable=True)
        batch_op.alter_column('visibility',
               existing_type=sa.VARCHAR(length=10),
               type_=sa.String(length=50),
               existing_nullable=True)

    with op.batch_alter_table('weather_forecast', schema=None) as batch_op:
        batch_op.alter_column('high_temp',
               existing_type=sa.VARCHAR(length=10),
               type_=sa.String(length=50),
               existing_nullable=True)
        batch_op.alter_column('low_temp',
               existing_type=sa.VARCHAR(length=10),
               type_=sa.String(length=50),
               existing_nullable=True)
        batch_op.alter_column('rain_percentage',
               existing_type=sa.VARCHAR(length=10),
               type_=sa.String(length=50),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('weather_forecast', schema=None) as batch_op:
        batch_op.alter_column('rain_percentage',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=10),
               existing_nullable=True)
        batch_op.alter_column('low_temp',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=10),
               existing_nullable=True)
        batch_op.alter_column('high_temp',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=10),
               existing_nullable=True)

    with op.batch_alter_table('today_weather', schema=None) as batch_op:
        batch_op.alter_column('visibility',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=10),
               existing_nullable=True)
        batch_op.alter_column('uv_index',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=10),
               existing_nullable=True)
        batch_op.alter_column('pressure',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=10),
               existing_nullable=True)
        batch_op.alter_column('dew_point',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=10),
               existing_nullable=True)
        batch_op.alter_column('humidity',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=10),
               existing_nullable=True)
        batch_op.alter_column('lowest_temp',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=10),
               existing_nullable=True)
        batch_op.alter_column('highest_temp',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=10),
               existing_nullable=True)

    # ### end Alembic commands ###
