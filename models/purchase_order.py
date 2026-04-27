# -*- coding: utf-8 -*-
from datetime import datetime, date
from odoo import models, api
from odoo.http import request
from odoo.orm.fields_temporal import Date


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def po_delay(self):
        po_delv = self.search([])
        for po in po_delv:
            po_delivery = po.picking_ids.filtered(
                lambda x: x.state == 'assigned'
            )
            print(po_delivery)
            if po_delivery:
                if po_delivery.date_deadline.date() < date.today():
                    self.env['mail.activity'].create({
                        'res_model_id': self.env['ir.model']._get_id('purchase.order'),
                        'res_id': po.id,
                        'user_id': po.user_id.id,
                        'summary': 'Purchase Delay Order3',
                        'note': 'Delayed Purchase Order',
                        'activity_type_id': 4,
                        'date_deadline': datetime.today(),
                    })
                email_values = {'email_to': po.partner_id.email}
                template = self.env.ref(
                    'po_delay.email_template_po_delay')
                template.send_mail(po.id, force_send=True, email_values=email_values)

