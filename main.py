from flask import Flask, jsonify, abort, make_response
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('dineease.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/test', methods=['GET'])
def test():
    return "Hello World!"

@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    users = conn.execute('SELECT id, firstName, lastName, email, isActive FROM users').fetchall()
    conn.close()
    return jsonify([dict(user) for user in users])

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    conn = get_db_connection()
    user = conn.execute('SELECT id, firstName, lastName, email, isActive FROM users WHERE id = ?',
                        (user_id,)).fetchone()
    conn.close()
    if user is None:
        return make_response(jsonify({'message': 'User not found'}), 404)
    return jsonify(dict(user))

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'message': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
