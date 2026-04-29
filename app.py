from flask import Flask, render_template, request, redirect

app = Flask(__name__)

transactions = []

@app.route('/')
def home():
    income = sum(t['amount'] for t in transactions if t['amount'] > 0)
    expense = sum(t['amount'] for t in transactions if t['amount'] < 0)
    balance = income + expense

    return render_template(
        'index.html',
        txs=transactions,
        income=income,
        expense=abs(expense),
        balance=balance
    )

@app.route('/add', methods=['POST'])
def add():
    text = request.form['text']
    amount = float(request.form['amount'])

    transactions.append({
        'text': text,
        'amount': amount
    })

    return redirect('/')

@app.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(transactions):
        transactions.pop(index)
    return redirect('/')

if __name__ == '__main__':
    app.run(port=5003, debug=True)