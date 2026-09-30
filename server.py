from flask import Flask, render_template, request, redirect # type: ignore
import csv

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


# @app.route("/contact.html")
# def contact():
#     return render_template("contact.html")

# @app.route("/works.html")
# def works():
#     return render_template("works.html")

# @app.route("/work.html")
# def work():
#     return render_template("work.html")


# def write_to_file(data):
#     with open('database.txt', mode='a') as database:
#         email = data["email"]
#         subject = data["subject"]
#         message = data["message"]
#         file = database.write(f'\n {email}, {subject}, {message}')

def write_to_csv(data):
    with open('database.csv', 'a', newline='') as csvfile:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(csvfile, delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("/thankyou.html")
        except Exception as e:
            return "Did not save to database. Error: " + str(e)
    else:
        return "Something went wrong. Try Again!!"

