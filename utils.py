import json

'''Функции'''
################################################

def get_posts_all():
    """Функция возвращает посты"""
    with open('data/posts.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_comments_all():
    """Функция возвращает комментарии"""
    with open('data/comments.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_posts_by_user(user_name):
    """Функция возвращает посты определенного пользователя."""
    posts = get_posts_all()
    posts_user = []
    try:
        for post in posts:
            if post['poster_name'].lower() == user_name.lower():
                posts_user.append(post)
        return posts_user
    except ValueError:
        return "Такого пользователя нет"



def get_comments_by_post_id(post_id):
    """Функция возвращает комментарии определенного поста."""
    comments_id = []
    comments = get_comments_all()
    for comment in comments:
        if comment['post_id'] == post_id:
            comments_id.append(comment)
    return comments_id


def get_comments_count(pk):
    """Функция возвращает количество комментариев к определенному посту"""
    comments = get_comments_all()
    count = 0
    for comment in comments:
        if comment['post_id'] == pk:
            count += 1
    return count


def search_for_posts(query):
    """Функция возвращает список постов по ключевому слову"""
    posts = get_posts_all()
    posts_query = []
    for post in posts:
        if query in post['content']:
            posts_query.append(post)
    return posts_query


def get_post_by_pk(pk):
    """Функция возвращает один пост по его идентификатору"""
    posts = get_posts_all()
    for post in posts:
        if post['pk'] == pk:
            return post
        else:
            return "нет такого поста"