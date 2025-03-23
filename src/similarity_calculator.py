import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def calculate_user_similarity(user_book_matrix):

    # 计算用户相似度矩阵
    # :param user_book_matrix: 用户-图书评分矩阵
    # :return: 用户相似度矩阵

    user_similarity = cosine_similarity(user_book_matrix)
    user_similarity_df = pd.DataFrame(user_similarity, index=user_book_matrix.index, columns=user_book_matrix.index)
    return user_similarity_df