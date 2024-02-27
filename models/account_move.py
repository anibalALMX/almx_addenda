# -*- coding: utf-8 -*-
from odoo import api, fields, models, SUPERUSER_ID, _

from odoo.exceptions import UserError

class AlamexAccountMove(models.Model):
    _inherit = 'account.move'
    num_provalm  = fields.Char('Número proveedor ')
    addenda_verify = fields.Char(related="partner_id.l10n_mx_edi_addenda.name")
    numPedido_al = fields.Char('Número pedido ')
    numFactura_al= fields.Char('Número factura')
    serie_al = fields.Char('Serie')
    folio_al = fields.Char('Folio')

    is_addenda = fields.Boolean(string='¿Tiene Addenda?', help='Verifica si la factura necesita el complemento de addenda en el XML')
    
    