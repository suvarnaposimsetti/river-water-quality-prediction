from flask import Flask, render_template, request, flash
from form import ContactForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vanitha'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('ALL fields are required')
            return render_template('contact.html',form=form)
        else:
            return 'Form Posted Successfully'
            # Process the form data (e.g., send an email)
            #return render_template('home.html')  # Redirect to home page after successful form submission
    return render_template('contact.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)
