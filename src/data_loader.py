import pandas as pd

def load_data(file_path):
    """
    加载评分数据
    :param file_path: 数据文件路径
    :return: 用户-图书评分矩阵
    """
    # 读取CSV文件
    ratings = pd.read_csv(file_path)
    
    # 检查数据是否包含所需的列
    if not all(col in ratings.columns for col in ['user_id', 'book_id', 'rating']):
        raise ValueError("CSV文件必须包含 'user_id', 'book_id', 'rating' 列")
    
    # 创建用户-图书评分矩阵
    user_book_matrix = ratings.pivot_table(index='user_id', columns='book_id', values='rating', fill_value=0)
    
    return user_book_matrix