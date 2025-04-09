from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9.0 / 5 + 32


@app.route('/convert/<celsius>')
def convert_celsius(celsius):
    try:
        celsius_value = float(celsius)
        fahrenheit = celsius_to_fahrenheit(celsius_value)
        return f"{celsius_value}°C is {fahrenheit:.2f}°F"
    except ValueError:
        return "Invalid temperature value. Please enter a number."


if __name__ == '__main__':
    app.run(debug=True)