# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class StockPicking(models.Model):
    _name = "stock.picking"
    _inherit = ["stock.picking"]

    fleet_work_order_id = fields.Many2one(
        string="# Fleet Work Order",
        comodel_name="fleet_work_order",
        readonly=True,
    )
