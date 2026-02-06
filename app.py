from flask import Flask, render_template, request, redirect, jsonify
from database import init_db, add_expense, get_expenses, delete_expense, get_expense_by_id, update_expense
from ai import categorize_expense

app = Flask(__name__)

# Initialize database
init_db()

# SINGLE PAGE DASHBOARD
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        date = request.form["date"]
        amount = request.form["amount"]
        description = request.form["description"]
        category = categorize_expense(description)

        add_expense(date, amount, description, category)
        return redirect("/")

    expenses = get_expenses()

    # Summary
    monthly, category_summary = {}, {}

    for e in expenses:
        date = e[1]
        amount = float(e[2])
        cat = e[4]

        month = date[:7]
        monthly[month] = monthly.get(month, 0) + amount
        category_summary[cat] = category_summary.get(cat, 0) + amount

    return render_template(
        "index.html",
        expenses=expenses,
        monthly=monthly,
        category_summary=category_summary
    )

# DELETE
@app.route("/delete/<int:id>")
def delete(id):
    delete_expense(id)
    return redirect("/")

# EDIT PAGE STATIC
@app.route("/edit/<int:id>")
def edit(id):
    data = get_expense_by_id(id)
    return jsonify({
        "id": data[0],
        "date": data[1],
        "amount": data[2],
        "description": data[3]
    })

# UPDATE
@app.route("/update", methods=["POST"])
def update():
    id = request.form["id"]
    date = request.form["date"]
    amount = request.form["amount"]
    description = request.form["description"]

    category = categorize_expense(description)
    update_expense(id, date, amount, description, category)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)