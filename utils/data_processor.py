import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(data_path):
    ratings = pd.read_csv(f"{data_path}/ratings.dat", sep="::", 
                         names=["UserID", "MovieID", "Rating", "Timestamp"])
    movies = pd.read_csv(f"{data_path}/movies.dat", sep="::", 
                        names=["MovieID", "Title", "Genres"], encoding='latin1')
    
    # 合并数据，生成特征
    data = pd.merge(ratings, movies, on="MovieID")
    data["Genres"] = data["Genres"].str.split("|")
    
    # 生成标签：评分>3为正样本
    data["Label"] = (data["Rating"] > 3).astype(int)
    return data

def preprocess(data):
    # 划分训练集和测试集
    train, test = train_test_split(data, test_size=0.2, random_state=42)
    
    # 保存处理后的数据
    train.to_parquet("./data/processed/train.parquet")
    test.to_parquet("./data/processed/test.parquet")
    return train, test