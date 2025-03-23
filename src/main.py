from data_loader import load_data
from similarity_calculator import calculate_user_similarity
from recommender import recommend_books

def main():
    # 加载数据
    file_path = '.\\data\\ratings.csv'
    user_book_matrix = load_data(file_path)

    # 计算用户相似度
    user_similarity_df = calculate_user_similarity(user_book_matrix)

    # 为用户推荐图书
    user_id = 1
    recommendations = recommend_books(user_id, user_similarity_df, user_book_matrix)

    print(f"为用户 {user_id} 推荐的图书：")
    print(recommendations)

if __name__ == "__main__":
    main()