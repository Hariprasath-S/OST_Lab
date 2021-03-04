from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/prime', methods=['GET', 'POST'])
def prime():
    num = int(request.form['number'])
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if (num % i) == 0:
                flag = 0
                print(num)
                return render_template('index.html', output='{} is not a prime number'.format(num))
        else:
            return render_template('index.html', output='{} is a prime number'.format(num))


if __name__ == "__main__":
    app.run(debug=True)

