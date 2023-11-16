# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Fleet Work Order - Stock Integration",
    "version": "14.0.2.1.0",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "ssi_fleet_work_order",
        "ssi_stock"
    ],
    "data": [
        "views/fleet_work_order_type_views.xml",
        "views/fleet_work_order_views.xml",
    ],
    "images": [],
}
