# -*- coding: utf-8 -*-
# © <2019> <Juan Carlos Vázquez Beas (jcarlosvazbeas@gmail.com)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api

class semantic_versioning(models.Model):
    _name = 'semantic.versioning'
    _description = 'SEMANTIC VERSIONING'

    name = fields.Char(
        string='Nombre',
        required=True
    )
