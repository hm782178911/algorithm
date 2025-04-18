import tensorflow as tf
from tensorflow.keras.layers import Input, Embedding, Dense, Concatenate, Dropout
from tensorflow.keras.models import Model

class DeepCrossing:
    def __init__(self, user_num, item_num, genre_num, embed_dim=32):
        self.user_num = user_num
        self.item_num = item_num
        self.genre_num = genre_num
        self.embed_dim = embed_dim

    def build_model(self):
        # 输入层
        user_input = Input(shape=(1,), name="UserID")
        item_input = Input(shape=(1,), name="MovieID")
        genre_input = Input(shape=(1,), name="Genres")

        # 嵌入层
        user_embed = Embedding(self.user_num, self.embed_dim)(user_input)
        item_embed = Embedding(self.item_num, self.embed_dim)(item_input)
        genre_embed = Embedding(self.genre_num, self.embed_dim)(genre_input)

        # 拼接所有特征
        concat = Concatenate()([user_embed, item_embed, genre_embed])
        flatten = tf.keras.layers.Flatten()(concat)

        # 深度交叉网络
        dense1 = Dense(64, activation="relu")(flatten)
        dense1 = Dropout(0.2)(dense1)
        dense2 = Dense(32, activation="relu")(dense1)
        output = Dense(1, activation="sigmoid")(dense2)

        # 编译模型
        model = Model(inputs=[user_input, item_input, genre_input], outputs=output)
        model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
        return model