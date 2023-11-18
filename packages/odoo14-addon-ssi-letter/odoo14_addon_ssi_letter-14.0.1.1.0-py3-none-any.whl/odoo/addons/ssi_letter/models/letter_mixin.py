# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class LetterMixin(models.Model):
    _name = "mixin.letter"
    _inherit = [
        "mixin.transaction_partner",
    ]
    _description = "Letter Mixin"

    type_id = fields.Many2one(
        string="Type",
        comodel_name="letter_type",
        required=True,
        readonly=True,
        ondelete="restrict",
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    date = fields.Date(
        string="Date",
        required=True,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    title = fields.Char(
        string="Title",
        required=True,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    digital = fields.Boolean(
        string="Digital",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    courier_id = fields.Many2one(
        string="Courier",
        comodel_name="res.partner",
        readonly=True,
        ondelete="restrict",
        domain=[
            ("parent_id", "=", False),
        ],
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    internal_partner_id = fields.Many2one(
        string="Internal Partner",
        comodel_name="res.partner",
        readonly=True,
        required=True,
        ondelete="restrict",
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
