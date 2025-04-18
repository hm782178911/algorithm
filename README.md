# 基于deepcrossing模型的电影推荐系统

# 工程结构

## 目录

```sh
deepcrossing_recommender/
├── data/                   # 原始数据和预处理结果
│   ├── raw/                # 原始数据（如MovieLens）
│   └── processed/          # 预处理后的数据
├── model/                  # 模型相关
│   ├── __init__.py			# 空文件
│   ├── deepcrossing.py     # DeepCrossing模型实现
│   └── train.py            # 训练脚本
├── serving/                # 模型服务化
│   ├── __init__.py			# 空文件
│   ├── app.py              # Flask API服务
│   └── request.py          # API请求示例
├── utils/                  # 工具函数
│   ├── __init__.py			# 空文件
│   ├── data_processor.py   # 数据预处理
│   └── metrics.py          # 评估指标
└── requirements.txt        # 依赖库
```



# 运行步骤

## 0.创建工程

```sh
mkdir -p deepcrossing_recommender/{data/{raw,processed},model,serving,utils} && touch deepcrossing_recommender/{model/{__init__.py,deepcrossing.py,train.py},serving/{__init__.py,app.py,request.py},utils/{__init__.py,data_processor.py,metrics.py},requirements.txt}
```



## 1.配置环境

```sh
#创建conda环境
conda create -n deepcrossing python=3.11
conda activate deepcrossing

#进入项目根目录
cd deepcrossing_recommender

#使用pip安装依赖
pip install -r requirements.txt
```



## 2.运行

在项目根目录运行下列命令

```sh
# 预处理数据
python -m utils.data_processor

# 训练模型
python -m model.train

# 启动服务
python -m serving.app

# 测试API（另开终端）
python -m serving.request
```



# Q&A

```python -m utils.data_processor```未成功加载数据集，建议手动加载数据集

```sh
# 在项目根目录执行
mkdir -p data/raw
cd data/raw
wget https://files.grouplens.org/datasets/movielens/ml-1m.zip
unzip ml-1m.zip
mv ml-1m/* .
rm -r ml-1m ml-1m.zip

```

