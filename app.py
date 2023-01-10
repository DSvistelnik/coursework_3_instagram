from flask import Flask, render_template, request, jsonify
from utils import get_posts_all, get_comments_by_post_id, get_comments_count, search_for_posts, get_posts_by_user, \
    get_post_by_pk

app = Flask(__name__)

''' Вьюшки'''

@app.route('/')
def index_page():
    posts = get_posts_all()
    return render_template('index.html', posts=posts)


@app.route('/posts/<int:postid>')
def post_page(postid):
    comments = get_comments_by_post_id(postid)
    posts = get_posts_all()
    count_comments = get_comments_count(postid)
    return render_template('post.html', posts=posts, comments=comments, pk=postid, count_comments=count_comments)


@app.route('/search/')
def search_page():
    query = request.args["s"]
    found_posts = search_for_posts(query)
    count_posts = len(found_posts)
    print(found_posts)
    return render_template('search.html', count_posts=count_posts, posts=found_posts, query=query)


@app.route('/user/<username>')
def user_page(username):
    posts_user = get_posts_by_user(username)
    return render_template('user-feed.html', posts_user=posts_user, username=username)

''' Вьюшки ошибок'''

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_server_error(error):
    return render_template('500.html'), 500

''' Вьюшки API'''

@app.route('/api/posts')
def page_api_all_posts(logger_api=None):
    """Страница API с всеми постами"""
    posts = get_posts_all()
    logger_api.info("Запрос /api/posts")
    return jsonify(posts)

@app.route('/api/posts/<int:post_id>')
def page_api_post_id(post_id, logger_api=None):
    """Страница API с постом по id"""
    post = get_post_by_pk(post_id)
    logger_api.info(f"Запрос /api/posts/{post_id}")
    return jsonify(post)

if __name__ == '__main__':
    app.run(debug=True)
