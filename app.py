from User_CRUD import app

@app.route("/")
def home():
    return "Hola Sara, Flask funciona perfectamente"

if __name__ == "__main__":
    app.run(debug=True)
