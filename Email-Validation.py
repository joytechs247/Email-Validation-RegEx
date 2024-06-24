import re
from flask import Flask, request, render_template_string, jsonify

app = Flask(__name__)

def is_valid_email(email):
    email_pattern = re.compile(
        r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    )
    return bool(email_pattern.match(email))

homepage_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Email Validation</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
</head>
<body class="bg-gray-100 flex items-center justify-center min-h-screen">
    <div class="bg-white p-8 rounded shadow-md w-full max-w-md">
        <h1 class="text-2xl font-bold mb-6 text-center">Email Validation</h1>
        <form method="POST" action="/" class="space-y-4">
            <div>
                <label for="email" class="block text-sm font-medium text-gray-700">Enter your email:</label>
                <input type="text" id="email" name="email" class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm">
            </div>
            <div class="text-center">
                <button type="submit" class="w-full py-2 px-4 bg-blue-500 text-white font-bold rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50">Validate</button>
            </div>
        </form>
        {% if result is not none %}
        <p class="mt-6 text-center text-lg font-medium 
        {% if 'valid' in result %}text-gray-800
        {% else %}text-red-500
        {% endif %}">
        {{ result }}</p>
        {% endif %}
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        email = request.form.get('email')
        if email:
            if is_valid_email(email):
                result = f"The email address '{email}' is valid."
            else:
                result = f"The email address '{email}' is invalid."
        else:
            result = "Please enter an email address."

    return render_template_string(homepage_html, result=result)

@app.route('/validation', methods=['GET'])
def validate_email():
    email = request.args.get('email')
    if not email:
        return jsonify({"error": "Email parameter is missing"}), 400

    is_valid = is_valid_email(email)
    return jsonify({"email": email, "valid": is_valid})

if __name__ == '__main__':
    app.run(debug=True)
