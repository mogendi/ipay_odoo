import hashlib, hmac, requests

from werkzeug import urls

from odoo import api, fields, models, _
from odoo.addons.payment.models.payment_acquirer import ValidationError
from odoo.tools.float_utils import float_compare

import logging

_logger = logging.getLogger(__name__)


class PaymentAcquirerIpayOdoo(models.Model):
    _inherit = 'payment.acquirer'

    provider = fields.Selection(selection_add=[('ipay', 'Ipay')])
    _ipay_key = fields.Char('Ipay Key', groups='base.group_user')
    _ipay_vendor_id = fields.Char('Vendor ID', groups='base.group_user')
    _ipay_live = fields.Boolean('Live', groups='base.group_user')

    def _get_ipay_urls(self, environment):
        if environment == 'prod':
            return 'https://payments.ipayafrica.com/v3/ke'
        else:
            return 'https://payments.ipayafrica.com/v3/ke'

    @api.multi
    def ipay_form_generate_values(self, values):
        self.ensure_one()
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        key1 = self._ipay_key
        if self._ipay_live:
            lv = 1
        else: 
            lv = 0
        ipay_values = dict(values,
                                live=str(lv),
                                txnid=values['reference'],
                                amount=values['amount'],
                                productinfo=values['reference'],
                                email=values.get('partner_email'),
                                phone=values.get('partner_phone'),
                                service_provider=self._ipay_vendor_id,
                                currency_code=values['currency'].name or '',
                                surl=urls.url_join(base_url, '/payment/ipay/ipn'),
                                cst='1',
                                crl='0',
                                )

        text = "{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}".format( ipay_values['live'], 
                                                    ipay_values['txnid'],
                                                    ipay_values['productinfo'],
                                                    ipay_values['amount'],
                                                    ipay_values['phone'],
                                                    ipay_values['email'],
                                                    ipay_values['service_provider'],
                                                    ipay_values['currency_code'],
                                                    ipay_values['surl'],
                                                    ipay_values['cst'],
                                                    ipay_values['crl'])
        hashobj = hmac.new(key1.encode(), text.encode(), hashlib.sha1)
        hashtxt = hashobj.hexdigest()
        ipay_values.update({
            'hash': hashtxt,
        })
        return ipay_values

    @api.multi
    def ipay_get_form_action_url(self):
        self.ensure_one()
        return self._get_ipay_urls(self.environment)


class PaymentTransactionIpayOdoo(models.Model):
    _inherit = 'payment.transaction'

    @api.multi
    def _ipay_form_validate(self,data):
        val1 = data.get('id') 
        val2 = data.get('ivm') 
        val3 = data.get('qwh') 
        val4 = data.get('afd') 
        val5 = data.get('poi') 
        val6 = data.get('uyt') 
        val7 = data.get('ifd')
        ipn_url = "{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}{13}{14}".format( 'https://www.ipayafrica.com/ipn/?vendor=demo',
                                                                    '&id',val1,'&ivm',val2,'&qwh',val3,'&afd',val4,'&poi',val5,'&uyt',val6,'ifd',val7 )
        r = requests.get(ipn_url)
        if r.status_code == 200:
            self._set_transaction_done()
            return True
        else:
            return False
