# pip install -r requirements.txt
from flask import Flask, request, render_template, flash
import sql_module


app = Flask(__name__)


@app.route('/')
def start_page_of_blog():
    """ Function returns all records hat we have in our database"""
    all_records = sql_module.all_records()
    return render_template("index.html", title="All Records in the Blog are:", all_records=all_records)


@app.route('/new_record', methods=['POST', 'GET'])
def create_record():
    """Function for adding new record"""
    if request.method == "POST":
        title = request.form['new_record_title']
        description = request.form['new_record_description']
        sql_module.add_record(title, description)
        flash("New record was added to the blog")
    return render_template("new_record.html")


@app.route('/edit', methods=['POST', 'GET'])
def edit_records():
    if request.method == "POST":
        try:
            identifier = int(request.form["id_for_edit"])
        except ValueError:
            flash("Please use numbers for the ID value")

        title = request.form['editing_title']
        description = request.form['editing_description']
        sql_module.edit_record(identifier, title, description)
        flash("The record was updated")

    return render_template("edit_record.html")


@app.route('/delete', methods=['POST', 'GET'])
def delete_record():
    if request.method == "POST":
        try:
            identifier = int(request.form["record_id_for_deleting"])
        except ValueError:
            flash("Please use numbers for the ID value")

        sql_module.delete_record(identifier)
        flash("Record was deleted")

    return render_template("delete_record.html", identifier=id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
