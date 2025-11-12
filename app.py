# from flask import Flask
# import os
# app = Flask(__name__)

# @app.route('/')
# def hello_geek():
#     return 'successfully deployed python application through jenkins!!!!!!!!!, added webhook'
# @app.route('/hi')
# def hell():
#     return '<h1>Hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii from Flask & Docker</h1>'

# if __name__ == "__main__":
#     port = int(os.environ.get('PORT', 5000))
#     app.run(debug=True, host='0.0.0.0', port=port)


from  flask  import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
        <head>
            <title>🚀 Flask CI/CD Deployment</title>
            <style>
                body {
                    font-family: 'Poppins', sans-serif;
                    background: linear-gradient(135deg, #667eea, #764ba2);
                    color: white;
                    text-align: center;
                    padding-top: 100px;
                }
                h1 {
                    font-size: 2.8em;
                    margin-bottom: 10px;
                }
                p {
                    font-size: 1.3em;
                }
                .btn {
                    display: inline-block;
                    padding: 10px 25px;
                    margin-top: 20px;
                    font-size: 1.1em;
                    background-color: #ff9f43;
                    color: #fff;
                    text-decoration: none;
                    border-radius: 8px;
                    transition: background 0.3s ease;
                }
                .btn:hover {
                    background-color: #ff6b6b;
                }
            </style>
        </head>
        <body>
            <h1>✅ Successfully Deployed Flask App through Jenkins!</h1>
            <p>Automated with <b>CI/CD Pipeline</b> 💻 using <b>Jenkins + Docker</b> 🚀</p>
            <a href="/hi" class="btn">Say Hi 👋</a>
        </body>
    </html>
    '''

@app.route('/hi')
def hi():
    return '''
    <html>
        <head>
            <title>👋 Flask Greetings</title>
            <style>
                body {
                    font-family: 'Poppins', sans-serif;
                    background: linear-gradient(135deg, #43cea2, #185a9d);
                    color: white;
                    text-align: center;
                    padding-top: 120px;
                }
                h1 {
                    font-size: 3em;
                }
                p {
                    font-size: 1.2em;
                }
                a {
                    color: #fff;
                    text-decoration: underline;
                    font-size: 1.1em;
                }
            </style>
        </head>
        <body>
            <h1>👋 Hi There!</h1>
            <p>Welcome to your Flask + Jenkins + Docker environment 🌍</p>
            <p><a href="/">Back to Home</a></p>
        </body>
    </html>
    '''

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

