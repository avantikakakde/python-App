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


from flask import Flask, request
import random, os

app = Flask(__name__)

# Random number for the game
secret_number = random.randint(1, 10)

@app.route('/')
def home():
    return """
    <h2 style='color:green; text-align:center;'>🎮 Welcome to the Guessing Game!</h2>
    <p style='text-align:center;'>Guess a number between <b>1 and 10</b></p>
    <form method='GET' action='/guess' style='text-align:center;'>
        <input type='number' name='number' min='1' max='10' required>
        <button type='submit'>Guess 🔢</button>
    </form>
    """

@app.route('/guess')
def guess():
    try:
        user_number = int(request.args.get('number'))
    except (TypeError, ValueError):
        return "<h3 style='color:red; text-align:center;'>⚠️ Please enter a valid number!</h3>"
    
    if user_number == secret_number:
        result = "🎉 Correct! You guessed the secret number!"
    elif user_number < secret_number:
        result = "⬆️ Too low! Try a higher number."
    else:
        result = "⬇️ Too high! Try a lower number."

    return f"""
    <h2 style='text-align:center;'>{result}</h2>
    <div style='text-align:center; margin-top:20px;'>
        <a href='/' style='background-color:#4CAF50; color:white; padding:10px 20px;
        text-decoration:none; border-radius:8px;'>Play Again 🔁</a>
    </div>
    """

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
