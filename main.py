from flask import Flask, render_template, request
import subprocess
import os

app = Flask(__name__, template_folder = "templates")

@app.route("/", methods = ["GET", "POST"])
def home():
	output = ""
	error = ""
	if request.method == "POST":
		code = request.form["code"]
		with open("tempCode.py", "w") as f:
			f.write(code)

		os.chmod('process.sh', 0o755)

		subprocess.call("./process.sh")
		with open("output.txt") as f:
			output = f.read()

		with open("error.txt") as f:
			error = f.read()


	return render_template("index.html", output = output, error = error)
if __name__ == "__main__":
	app.run(debug = True)