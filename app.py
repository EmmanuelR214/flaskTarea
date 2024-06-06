from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_content = request.form['content']
    tasks.append(task_content)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
