# 在项目根目录执行
mkdir -p data/raw
cd data/raw
wget https://files.grouplens.org/datasets/movielens/ml-1m.zip
unzip ml-1m.zip
mv ml-1m/* .
rm -r ml-1m ml-1m.zip



# 预处理数据
python -m utils.data_processor

# 训练模型
python -m model.train

# 启动服务
python -m serving.app

# 测试API（另开终端）
python -m serving.request