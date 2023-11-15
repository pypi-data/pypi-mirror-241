# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import api, models


class StockMove(models.Model):
    _name = "stock.move"
    _inherit = ["stock.move"]

    @api.onchange(
        "picking_type_id",
    )
    def onchange_procure_method(self):
        if self.picking_type_id:
            self.procure_method = self.picking_type_id.procure_method
