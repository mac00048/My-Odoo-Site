from odoo import http
from odoo.http import request

class OfferController(http.Controller):
    @http.route('/send-email', type='json', auth='public', methods=['POST'])
    def send_email(self, **kwargs):
        # Extract data
        name = kwargs.get('name')
        street = kwargs.get('street')
        postcode = kwargs.get('postcode')
        phone = kwargs.get('phone')
        whatsapp = kwargs.get('whatsapp')
        total_price = kwargs.get('totalPrice')

        # Compose email details
        email_content = f"Name: {name}\nStreet: {street}\nPostcode: {postcode}\nPhone: {phone}\nTotal Price: {total_price}"

        # Create and send email
        mail = request.env['mail.mail'].create({
            'subject': 'New Offer Submission',
            'body_html': f"<p>{email_content}</p>",
            'email_to': 'admin@example.com',  # Set to your email recipient
        })
        mail.send()

        return {"status": "success", "message": "Email sent successfully"}
