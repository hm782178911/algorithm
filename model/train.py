import pandas as pd
import numpy as np
from .deepcrossing import DeepCrossing
from utils.data_processor import load_data, preprocess
from utils.metrics import evaluate

# 加载数据
data = load_data("./data/raw")
train, test = preprocess(data)

# 生成训练/测试数据
def prepare_features(df):
    return (
        df["UserID"].values,
        df["MovieID"].values,
        df["Genres"].apply(lambda x: hash(x[0]) % 100).values,
        df["Label"].values
    )

train_data = prepare_features(train)
test_data = prepare_features(test)

# 初始化模型
model = DeepCrossing(
    user_num=max(train["UserID"]) + 1,
    item_num=max(train["MovieID"]) + 1,
    genre_num=100
).build_model()

# 训练
model.fit(
    train_data[:-1],  # 输入特征
    train_data[-1],   # 标签
    batch_size=64,
    epochs=10,
    validation_split=0.1
)

# 评估
test_pred = model.predict(test_data[:-1])
metrics = evaluate(test_data[-1], test_pred)
print(f"Test Metrics: {metrics}")

# 保存模型
model.save("./model/deepcrossing_model.h5")