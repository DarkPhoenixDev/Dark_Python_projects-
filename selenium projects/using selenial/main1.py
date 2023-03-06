from flask import Flask, request, redirect, render_template

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///foodmood.db'

db = SQLAlchemy(app)


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(80), unique=True, nullable=False)

    password = db.Column(db.String(80), nullable=False)

    

    def __repr__(self):

        return '<User %r>' % self.username


@app.route('/signup', methods=['GET', 'POST'])

def signup():

    if request.method == 'POST':

        username = request.form['username']

        password = request.form['password']

        

        user = User(username=username, password=password)

        db.session.add(user)

        db.session.commit()

        

        return redirect('/')

    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])

def login():

    if request.method == 'POST':

        username = request.form['username']

        password = request.form['password']

        

        user = User.query.filter_by(username=username, password=password).first()

        if user:

            return redirect('/')

        

        return 'Invalid username or password'

import tkinter as tk

def mood_selection():
    selected_mood = var.get()
    mood_options = {1: "Romantic", 2: "Casual", 3: "Lively", 4: "Chill"}
    result_label.config(text=f"You selected: {mood_options[selected_mood]}")

root = tk.Tk()
root.title("Mood Selection")

var = tk.IntVar()

mood_frame = tk.Frame(root)
mood_frame.pack(pady=10)

tk.Radiobutton(mood_frame, text="Romantic", variable=var, value=1).pack(anchor="w")
tk.Radiobutton(mood_frame, text="Casual", variable=var, value=2).pack(anchor="w")
tk.Radiobutton(mood_frame, text="Lively", variable=var, value=3).pack(anchor="w")
tk.Radiobutton(mood_frame, text="Chill", variable=var, value=4).pack(anchor="w")

result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack(pady=10)

select_button = tk.Button(root, text="Select", command=mood_selection)
select_button.pack()



def search_and_recommend():
    mood = mood_var.get()
    location = location_var.get()
    search_history = search_history_var.get()

    # Implement your recommendation algorithm here using mood, location, and search_history inputs.
    # For demonstration purposes, hardcoded recommendations are used.
    recommendations = "Restaurant A, Cafe B, Bakery C"

    result_label.config(text=f"Recommendations for mood={mood}, location={location}, and search history={search_history}:")
    recommendation_label.config(text=recommendations)

# root = tk.Tk()
# root.title("Search and Recommendation Algorithm")

input_frame = tk.Frame(root)
input_frame.pack(pady=10)

mood_var = tk.StringVar()
tk.Label(input_frame, text="Mood:").pack(side="left")
tk.Entry(input_frame, textvariable=mood_var).pack(side="left")

location_var = tk.StringVar()
tk.Label(input_frame, text="Location:").pack(side="left", padx=10)
tk.Entry(input_frame, textvariable=location_var).pack(side="left")

search_history_var = tk.StringVar()
tk.Label(input_frame, text="Search History:").pack(side="left", padx=10)
tk.Entry(input_frame, textvariable=search_history_var).pack(side="left")

result_frame = tk.Frame(root)
result_frame.pack(pady=10)

result_label = tk.Label(result_frame, text="", font=("Helvetica", 14))
result_label.pack(pady=10)

recommendation_label = tk.Label(result_frame, text="", font=("Helvetica", 14))
recommendation_label.pack(pady=10)

search_button = tk.Button(root, text="Search and Recommend", command=search_and_recommend)
search_button.pack()





root.mainloop()




