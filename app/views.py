"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""
import os
from app import app
from app.forms import AddProperty
from flask import render_template, request, redirect, url_for, flash, send_from_directory
from app.models import Property
from werkzeug.utils import secure_filename
from . import db

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/properties/create', methods=['POST', 'GET'])
def createproperty():
    form = AddProperty()
    if request.method == 'POST':
        title = form.title.data
        location = form.location.data
        bathroom_no = form.bathroom_no.data
        bedroom_no = form.bedroom_no.data
        type = form.type.data
        description = form.description.data
        price = form.price.data
        pic = request.files['pic']
        filename = secure_filename(pic.filename)
        pic.save(os.path.join(app.config['UPLOAD_FOLDER'],filename)) 
        property = Property(title, location, bathroom_no, bedroom_no, type, description, price, filename)
        db.session.add(property)
        db.session.commit()
        flash('Property was successfully added')
        return redirect(url_for('properties'))
    return render_template('createproperty.html', form = form)
    

@app.route('/properties')
def properties():
    return render_template('properties.html', properties = Property.query.all())


@app.route('/properties/<propertyid>')
def viewproperty():
    return render_template('viewproperty.html')

@app.route('/app/uploads/<filename>')
def get_image(filename):
    return send_from_directory(os.path.join(os.getcwd(),app.config['UPLOAD_FOLDER']), filename)

###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
