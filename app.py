from flask import Flask, render_template, request, jsonify
import stripe

app = Flask(__name__)

# Initialize Stripe with your API key
stripe.api_key = "sk_test_51OouD1SEeO14Os1OKexmKjXIYj3ob0R2ptxEXsVq82RNd8uDAPNCkcHM1gAlaVq3gpYTpF91bBqbk4UTNZVX58Sw00Y1In5WpF"

@app.route('/')
def index():
    return render_template('payment.html')

@app.route('/charge', methods=['POST'])
def charge():
    amount = 500  # Amount in cents

    try:
        # Create a Stripe Payment Intent
        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency='usd',
            description='Payment for services',
            payment_method=request.form['stripeToken'],
            confirm=True
        )
        return jsonify(success=True)
    except Exception as e:
        return jsonify(error=str(e)), 403

if __name__ == '__main__':
    app.run(debug=True)
