from .data_loader import load_data
from .similarity_calculator import calculate_user_similarity
from .recommender import recommend_books

# 定义包的公共接口
__all__ = ['load_data', 'calculate_user_similarity', 'recommend_books']