from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# General professional everyday tasks
todos = ["Review project specifications", "Fix outstanding bugs", "Update documentation", "Team sync meeting at 10 AM"]

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    todo = request.form.get('todo')
    if todo:
        todos.append(todo)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)