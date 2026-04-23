# -*- coding: utf-8 -*-
from datetime import datetime

from odoo import models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def po_delay(self):
        po_delv = self.search([])
        res_model_id = self.env['ir.model'].search([('name', '=', 'Purchase Order')])
        # print(res_model_id.model)
        print(self.env['ir.model']._get_id('res.partner'))
        for po in po_delv:
            if po.date_order < datetime.now():
                print(po.id)
                activity = self.env['mail.activity'].create({
                    'res_id': po.id,
                    'res_model_id': self.env['ir.model']._get_id('res.partner'),
                    'user_id': 2,
                    'summary': 'Purchase Delay',
                    'note': 'Delayed Purchase Order',
                    'activity_type_id': 4,
                    'date_deadline': datetime.today(),
                })
        print(activity)
        # user_id = self.env['res.users'].search([]).mapped('id')
        # print(user_id)
        # print(self.env.user.id)
        # res_model_id = self.env['mail.activity'].search([]).mapped('res_model_id')
        # print(res_model_id)
        # res_id = self.env['mail.activity'].search([]).mapped('res_model_id')
        # print(res_id)
        # res_model_id = self.env['ir.model'].search([]).mapped('name')
        print(res_model_id)
