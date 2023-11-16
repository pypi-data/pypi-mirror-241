# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.tools.safe_eval import safe_eval


class FleetWorkOrderType(models.Model):
    _name = "fleet_work_order_type"
    _inherit = ["fleet_work_order_type"]

    picking_type_selection_method = fields.Selection(
        string="Picking Type Selection Method",
        selection=[("manual", "Manual"), ("domain", "Domain")],
        default="manual",
    )
    picking_type_ids = fields.Many2many(
        comodel_name="stock.picking.type",
        relation="rel_fleet_wo_type_2_picking_type",
        column1="type_id",
        column2="picking_type_id",
        string="Picking Types",
    )
    picking_type_domain = fields.Text(
        string="Picking Type Domain",
        default=[],
    )
    allowed_picking_type_ids = fields.Many2many(
        comodel_name="stock.picking.type",
        string="Allowed Picking Types",
        compute="_compute_allowed_picking_type_ids",
        store=False,
        compute_sudo=True,
    )

    @api.depends(
        "picking_type_selection_method",
        "picking_type_ids",
        "picking_type_domain",
    )
    def _compute_allowed_picking_type_ids(self):
        for record in self:
            result = []
            if record.picking_type_selection_method == "manual":
                result = record.picking_type_ids.ids
            elif record.picking_type_selection_method == "domain":
                criteria = safe_eval(record.picking_type_domain, {})
                result = (
                    self.env["stock.picking.type"].search(criteria).ids
                )
            record.allowed_picking_type_ids = result
