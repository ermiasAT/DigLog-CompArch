from flask import Flask, render_template, request
from src.converter import (
    decimal_to_binary,
    binary_to_decimal,
    hex_to_binary,
    binary_to_hex,
    hex_to_decimal,
    decimal_to_hex,
    is_valid_decimal,
    is_valid_binary,
    is_valid_hex
)
import os

app = Flask(__name__, template_folder=os.path.join("src", "templates"))

@app.route('/', methods=['GET', 'POST'])
def index():
    comments = ''
    result = ''
    number = ''
    from_base = ''
    to_base = ''

    if request.method == 'POST':
        number = request.form.get('number')
        from_base = request.form.get('from_base')
        to_base = request.form.get('to_base')

        # First, validate the number for its base
        is_valid = True
        if from_base == 'decimal':
            is_valid = is_valid_decimal(number)
        elif from_base == 'binary':
            is_valid = is_valid_binary(number)
        elif from_base == 'hexadecimal':
            is_valid = is_valid_hex(number)

        if not is_valid:
            comments = f'Invalid {from_base} number'
            result = ''
        elif from_base == to_base:
            comments = 'Invalid conversion: source and target base are the same'
            result = ''
        else:
            try:
                # Perform conversion
                if from_base == 'decimal' and to_base == 'binary':
                    comments, result = decimal_to_binary(float(number))
                elif from_base == 'binary' and to_base == 'decimal':
                    comments, result = binary_to_decimal(number)
                elif from_base == 'hexadecimal' and to_base == 'binary':
                    comments, result = hex_to_binary(number)
                elif from_base == 'binary' and to_base == 'hexadecimal':
                    comments, result = binary_to_hex(number)
                elif from_base == 'hexadecimal' and to_base == 'decimal':
                    comments, result = hex_to_decimal(number)
                elif from_base == 'decimal' and to_base == 'hexadecimal':
                    comments, result = decimal_to_hex(float(number))
                else:
                    comments = 'Conversion not supported'
                    result = ''
            except Exception as e:
                comments = f'Error: {str(e)}'
                result = ''

        # Replace semicolons with newlines for step-by-step display
        if comments:
            comments = comments.replace(';', '\n')

    return render_template('index.html', result=result, comments=comments,
                           number=number, from_base=from_base, to_base=to_base)

if __name__ == '__main__':
    app.run(debug=True)
