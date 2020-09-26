## /core/views.py
## Home and Info View

from flask import render_template, request, Blueprint
from companyblog.models import BlogPost
## register the blueprint in __init__ file
core = Blueprint('core', __name__) ## (Name of Blurprint)


@core.route('/')
def index():
    ## Query for blog posts
    page = request.args.get('page', 1, type=int)
    blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page, per_page=5)
    return render_template('index.html', blog_posts = blog_posts)

@core.route('/info')
def info():
    return render_template('info.html')