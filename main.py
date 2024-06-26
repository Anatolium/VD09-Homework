from app import app, db
import os

if not os.path.exists(os.path.join(app.instance_path, 'clicker.db')):
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
