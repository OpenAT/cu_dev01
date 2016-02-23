from openerp import models, api, fields
from openerp.tools import mod10r

class invoice_reports_ahch_extension(models.Model):
    _inherit = "res.company"
    logo_report_dd = fields.Binary("Header Image", help="This field holds the image used for the logo on the prints, limited to 1024x1024px")
    website_report_dd = fields.Char("Website 2 Header Report", help="Use Website Address displayed at Header")
    email_report_dd = fields.Char("Use Second Email Address printed at Header in Report")

class ResPartnerBank(models.Model):
    """Inherit res.partner.bank class in order to add swiss specific fields
    and state controls

    """
    _inherit = 'res.partner.bank'

    bvr_customer_number = fields.Char(
        string='Bank BVR/ESR adherent number', size=11,
        help="Your Bank adherent number to be printed "
             "in references of your BVR/ESR. "
             "This is not a postal account number."
        )
    pf_acc_num = fields.Char(
        string='Postfinance Account Number', size=11,
        help="Your PF Account."
        )

def get_pz(ref_number):
    number = 0
    number += mod10r(ref_number)
    return number