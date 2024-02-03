from flask import Flask, render_template,request, session
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'Upload'

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

@app.route('/', methods=['GET',"POST"])
@app.route('/home', methods=['GET',"POST"])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data # First grab the file
        f = request.files['file']
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename))) # Then save the file
        return   displayImage()
    
        print("F")

    return render_template('Login.html', form=form)

@app.route('/show_image')
def displayImage():
    # Retrieving uploaded file path from session
    Flask_Logo = os.path.join(app.config['UPLOAD_FOLDER'], 'image_2.jpeg')
    img_file_path = session.get('C:/Users/PCS/Downloads/Project/Upload', None)
    # Display image in Flask application web page
    return render_template('show_image.html', user_image =Flask_Logo)

 
if __name__=='__main__':
    app.run(debug = True)







