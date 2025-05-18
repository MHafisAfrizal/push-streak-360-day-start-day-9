from flask import Flask, jsonify
app = Flask(__name__)

testimonials = [
    {
        "name": "Dewi Sartika",
        "message": "Pelayanan sangat cepat dan ramah. Saya sangat puas!",
        "avatar": "https://i.pravatar.cc/60?img=1"
    },
    {
        "name": "Rama Dwi",
        "message": "Harga sesuai dengan kualitasnya. Sangat recommended!",
        "avatar": "https://i.pravatar.cc/60?img=2"
    },
    {
        "name": "Nina Ayu",
        "message": "Website-nya sangat mudah digunakan dan tampilannya menarik.",
        "avatar": "https://i.pravatar.cc/60?img=3"
    }
]

@app.route("/api/testimonials", methods=["GET"])
def get_testimonials():
    return jsonify({"testimonials": testimonials})

if __name__ == "__main__":
    app.run(debug=True)
