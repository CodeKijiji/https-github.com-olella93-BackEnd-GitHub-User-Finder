from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/user', methods=['GET'])
def get_user():
    username = request.args.get('username')
    # Logic to find GitHub user would go here
    return jsonify({"message": f"User {username} found!"})

if __name__ == '__main__':
    app.run(debug=True)