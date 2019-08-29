import logging
import pprint
import werkzeug

from odoo import http
from odoo.http import request
from odoo.addons.payment.controllers.portal import PaymentProcessing

_logger = logging.getLogger(__name__)


class IpayOdooController(http.Controller):

    @http.route('/payment/ipay/ipn', type='http', auth="none", methods=['POST', 'GET'], csrf=False)
    def ipay_ipn(self, **post):
        TX = request.env['payment.transaction']
        tx = None

        if post.get('id'):
            tx = TX.sudo().search([('reference', '=', post['id'])])
        if not tx:
            tx_id = (post.get('id') or request.session.get('sale_transaction_id') or
                     request.session.get('website_payment_tx_id'))
            tx = TX.sudo().browse(int(tx_id))
        if not tx:
            raise werkzeug.exceptions.NotFound()

        if tx._ipay_form_validate(post):
            PaymentProcessing.add_payment_transaction(tx)
            return werkzeug.utils.redirect("/payment/process")
        else:
            return werkzeug.exceptions.NotAcceptable()