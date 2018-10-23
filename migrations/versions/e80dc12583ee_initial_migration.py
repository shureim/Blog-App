"""Initial Migration

Revision ID: e80dc12583ee
Revises: b2265ea4159a
Create Date: 2018-10-23 10:31:31.082547

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e80dc12583ee'
down_revision = 'b2265ea4159a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment_name', sa.String(length=255), nullable=True),
    sa.Column('date_posted', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('blog_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['blog_id'], ['blogs.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('comments')
    op.add_column('blogs', sa.Column('Blog_post', sa.String(), nullable=True))
    op.add_column('blogs', sa.Column('category', sa.String(), nullable=True))
    op.add_column('blogs', sa.Column('date_posted', sa.DateTime(), nullable=True))
    op.drop_column('blogs', 'posted')
    op.drop_column('blogs', 'blog')
    op.drop_column('blogs', 'title')
    op.drop_column('blogs', 'blog_id')
    op.add_column('subscribers', sa.Column('name', sa.String(length=255), nullable=True))
    op.add_column('subscribers', sa.Column('title', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('password_hash', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('password_secure', sa.String(length=255), nullable=True))
    op.drop_column('users', 'pass_secure')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_secure', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('users', 'password_secure')
    op.drop_column('users', 'password_hash')
    op.drop_column('subscribers', 'title')
    op.drop_column('subscribers', 'name')
    op.add_column('blogs', sa.Column('blog_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('blogs', sa.Column('title', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('blogs', sa.Column('blog', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('blogs', sa.Column('posted', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_column('blogs', 'date_posted')
    op.drop_column('blogs', 'category')
    op.drop_column('blogs', 'Blog_post')
    op.create_table('comments',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('comment', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('posted', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('blog_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['blog_id'], ['blogs.id'], name='comments_blog_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='comments_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='comments_pkey')
    )
    op.drop_table('comment')
    # ### end Alembic commands ###