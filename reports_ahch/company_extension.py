from openerp import models, fields


class ResCompany(models.Model):
    """override company in order to add bvr vertical and
    Horizontal print delta"""
    _inherit = "res.company"

    bvr_delta_horz = fields.Float(
        'BVR Horz. Delta (inch)',
        help='horiz. delta in inch 1.2 will print the bvr 1.2 inch lefter, '
        'negative value is possible'
    )

    bvr_delta_vert = fields.Float(
        'BVR Vert. Delta (inch)',
        help='vert. delta in inch 1.2 will print the bvr 1.2 inch lower, '
             'negative value is possible'
    )

    bvr_scan_line_vert = fields.Float(
        'BVR vert. position for scan line (inch)',
        help='Vert. position in inch for scan line'
    )

    bvr_scan_line_horz = fields.Float(
        'BVR horiz. position for scan line(inch)',
        help='Horiz. position in inch for scan line'
    )

    bvr_add_vert = fields.Float(
        'BVR vert. position for address (inch)',
        help='Vert. position in inch for address'
    )

    bvr_add_horz = fields.Float(
        'BVR horiz. position address (inch)',
        help='Horiz. position in inch for address'
    )

    bvr_scan_line_font_size = fields.Integer(
        'BVR scan line font size (pt)'
    )

    bvr_scan_line_letter_spacing = fields.Float(
        'BVR scan line letter spacing'
    )

    merge_mode = fields.Selection(
        [('in_memory', 'Merge Slips in Memory, faster but can exhaust memory'),
         ('on_disk', 'Merge Slips on Disk, slower but safer')],
        string="Payment Slips Merge Mode",
        required=True,
        default="in_memory"
    )
    bvr_background = fields.Boolean('Insert BVR background ?')
