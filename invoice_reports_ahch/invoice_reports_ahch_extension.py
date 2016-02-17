from openerp import models, api, fields

class invoice_reports_ahch_extension(models.Model):
    _inherit = "res.company"
    logo_report_dd = fields.Binary("Header Image", help="This field holds the image used for the logo on the prints, limited to 1024x1024px")
    website_report_dd = fields.Char("Website 2 Header Report", help="Use Website Address displayed at Header")
    email_report_dd = fields.Char("Use Second Email Address printed at Header in Report")
