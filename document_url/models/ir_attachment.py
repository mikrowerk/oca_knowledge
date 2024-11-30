# Copyright 2021 Tecnativa - Víctor Martínez
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, api
from odoo.exceptions import UserError
import pprint


class IrAttachmentExtended(models.Model):
    _inherit = "ir.attachment"

    def _compute_mimetype(self, values):
        if values.get("url") and values.get("type", "url") == "url":
            return "application/link"
        return super()._compute_mimetype(values)

    @api.model
    def default_get(self, default_fields):
        print(f"IrAttachmentExtended default_get")
        pprint.pprint(self._context, indent=4)
        res = super(IrAttachmentExtended, self).default_get(default_fields)
        if self._context.get('params', False):
            res.update({
                'res_model': self._context.get('params').get('model', False),
                'res_id': self._context.get('params').get('id', False)
            })
        elif self._context.get('active_model', False):
            res.update({
                'res_model': self._context.get('active_model', False),
                'res_id': self._context.get('active_id', False),

            })
        res.update({
            'type': self._context.get('attachment_type', 'binary')
        })
        pprint.pprint(res, indent=4)
        if not res.get('res_id', False) or not res.get('res_model', False):
            print(f"Missing 'res_id' or 'res_model' fields. {res}")
            # raise UserError(f"Missing 'res_id' or 'res_model' fields")
        return res
