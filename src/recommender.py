import pandas as pd

def recommend_books(user_id, user_similarity_df, user_book_matrix, n_recommendations=5):
    """
    基于用户的协同过滤推荐图书
    :param user_id: 目标用户ID
    :param user_similarity_df: 用户相似度矩阵
    :param user_book_matrix: 用户-图书评分矩阵
    :param n_recommendations: 推荐图书数量
    :return: 推荐的图书列表
    """
    # 获取目标用户的相似用户
    similar_users = user_similarity_df[user_id].sort_values(ascending=False)[1:]

    # 获取相似用户的评分
    similar_users_ratings = user_book_matrix.loc[similar_users.index]

    # 计算加权评分
    weighted_ratings = similar_users_ratings.mul(similar_users, axis=0).sum()

    # 过滤掉目标用户已经评分的图书
    user_ratings = user_book_matrix.loc[user_id]
    unrated_books = weighted_ratings[user_ratings == 0]

    # 推荐评分最高的图书
    recommendations = unrated_books.sort_values(ascending=False).head(n_recommendations)

    return recommendations