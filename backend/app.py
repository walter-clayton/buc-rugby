from flaskblog import create_app
from dotenv import load_dotenv
load_dotenv()

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
