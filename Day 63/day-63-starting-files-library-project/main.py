from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST': 
        name = request.form['name'] 
        author = request.form['author'] 
        rating = request.form['rating'] 
        all_books.append({"title":name, "author":author, "rating":rating})
        
        return redirect(url_for('home'))
   
    return render_template('add.html') 



if __name__ == "__main__":
    app.run(debug=True)


# NOTE
# read the document rather than stack over flow or chatgpt, try to read for few minutes before going deep

