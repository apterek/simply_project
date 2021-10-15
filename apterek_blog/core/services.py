from core.models import Post


def take_a_three_best_post():
    best_posts = Post.objects.order_by("likes")[0:3]
    return best_posts

