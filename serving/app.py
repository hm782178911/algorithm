from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np

app = Flask(__name__)
model = tf.keras.models.load_model("./model/deepcrossing_model.h5")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        assert all(k in data for k in ["UserID", "MovieID", "Genres"])
        
        user_id = np.array([int(data["UserID"])])
        movie_id = np.array([int(data["MovieID"])])
        genre_id = np.array([hash(data["Genres"][0]) % 100])
        
        prob = model.predict([user_id, movie_id, genre_id])[0][0]
        return jsonify({"probability": float(prob)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)