from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = '9b461588cebbef380f27767d9896fdcaf43c6d6e165650e9323c0c3afa9a94e9'

# Configure Flask-Mail settings
app.config['MAIL_SERVER'] = 'smtp.hostinger.com'
app.config['MAIL_PORT'] = 465 
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'admin@tradetreex.com'
app.config['MAIL_PASSWORD'] = ''

class ContactForm(FlaskForm):
    name = StringField('Your Name', validators=[InputRequired()])
    email = StringField('Your Email', validators=[InputRequired(), Email()])
    message = TextAreaField('Your Message', validators=[InputRequired()])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')  


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST' and form.validate_on_submit():
        # Process the form data (you can add your own logic here)
        flash('Message received! We will get back to you soon.', 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html', form=form) 

def send_email(name, email, message):
    subject = 'New Form Submission'
    body = f"Name: {name}\nEmail: {email}\nMessage: {message}"

    # Create a message object
    msg = Message(subject, sender=email, recipients=['admin@tradetreex.com'])
    msg.body = body

    # Send the email
    mail.send(msg)


