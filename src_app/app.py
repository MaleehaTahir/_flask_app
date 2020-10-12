from flask import Flask, jsonify

app = Flask(__name__)


def sum_list_range(_list, start, end):
    total = 0
    for i in range(start, end+1, 1):
        total += _list[i]
    return total


@app.route("/total")
def list_total():
    numbers_to_add = list(range(10000001))
    return jsonify(total=sum_list_range(numbers_to_add, numbers_to_add[0], numbers_to_add[-1]))


if __name__ == '__main__':
    app.run(debug=True)
