```python
from flask import Flask, render_template, request
import api_integration

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.get_json()
        response = api_integration.integrate_with_toast(data)
        return render_template('response.html', response=response)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
```