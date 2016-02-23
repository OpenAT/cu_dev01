# -*- coding: utf-8 -*-
##############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################

{
    'name': 'reports_ahch',
    'summary': """Invoice Reports AHCH""",
    'author': 'Joachim Grubelnik (joachim.grubelnik@datadialog.net), DataDialog',
    'version': '1.0',
    'website': 'https://www.datadialog.net',
    'installable': True,
    'depends': ['sale'],
    'data': [
        'report_invoice_ahch.xml',
        'report_picking_ahch.xml',
        'report_saleorder_ahch.xml',
        'report_layout_ahch_saint_header.xml',
        'report_layout_ahch_slip_footer.xml',
        'invoice_reports_ahch_extension.xml',
        'paperformat_ahch.xml'
    ],
}
