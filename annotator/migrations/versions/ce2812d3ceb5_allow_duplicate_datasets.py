"""Allow duplicate datasets"""

# revision identifiers, used by Alembic.
revision = 'ce2812d3ceb5'
down_revision = '1ad76ad4692a'

import sqlalchemy as sa
from alembic import op



def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('uq_dataset_problem_idtable_name_entity_id', 'dataset', ['problem_id', 'table_name', 'entity_id'])
    op.drop_constraint('uq_dataset_table_name_entity_id', 'dataset', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('uq_dataset_table_name_entity_id', 'dataset', ['table_name', 'entity_id'])
    op.drop_constraint('uq_dataset_problem_idtable_name_entity_id', 'dataset', type_='unique')
    # ### end Alembic commands ###