# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2013-Present Tryon InfoSoft <www.tryoninfosoft.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields, api,_


class wizard_sale_target_marketing(models.TransientModel):
    _name = "wizard.sales.target.marketing"

    report_by = fields.Selection([('categ', 'By Category'),
                                  ('prod', 'By Product')], default="categ")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    category_ids = fields.Many2many('product.category', string="Category")
    product_ids = fields.Many2many('product.product', string="Products")

    @api.multi
    def action_print_sales_target_marketing(self):
        data = self.read()[0]
        datas = {
            'id': self.id,
            'form': data
        }
        return self.pool['report'].get_action(self._cr, self._uid, [],
                                              'sales_target_marketing.sale_target_marketing_report',
                                              data=datas, context=self._context)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: