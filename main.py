from flask import Flask, render_template, request

# Create a flask app
app = Flask(
  __name__,
  template_folder = "stuff"
)

# Index page
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/info', methods=['POST', 'GET'])
def grade():
  form_data = request.form
  return render_template('results.html', form = form_data)



if __name__ == '__main__':
  # Run the Flask app
  app.run(
	host='0.0.0.0',
	debug=True,
	port=8080
  )