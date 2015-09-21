# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014 Eficent (<http://www.eficent.com/>)
#              <contact@eficent.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp.osv import fields, orm


class ProcurementOrder(orm.Model):
    
    _inherit = 'procurement.order'

    _columns = {
        'analytic_resource_plan_lines': fields.many2many(
            'analytic.resource.plan.line',
            'procurement_order_analytic_resource_plan_line_line_rel',
            'procurement_order_id',
            'analytic_resource_plan_line_id',
            'Analytic Resource Plan Lines', readonly=True),
        'procurement_id': fields.many2one('procurement.order', required=False),
        'procurement_state': fields.boolean('Procurement state')
    }
