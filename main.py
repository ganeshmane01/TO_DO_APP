from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []  # list to store tasks

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        tasks.append(request.form["task"])   # naya task add karna
    return render_template("index.html", tasks=tasks)

@app.route("/delete/<int:i>")
def delete(i):
    tasks.pop(i)   # delete task
    return redirect("/")

@app.route("/edit/<int:i>", methods=["GET", "POST"])
def edit(i):
    if request.method == "POST":
        tasks[i] = request.form["task"]   # task update karna
        return redirect("/")
    return render_template("edit.html", task=tasks[i], i=i)

if __name__ == "__main__":
    app.run(debug=True)
