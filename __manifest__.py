# Part of Odoo. See LICENSE file for full copyright and licensing details.

# -*- coding: utf-8 -*-
{
    'name': "relojeria",
    'summary': "Proyecto relojeria",
    'description': "Introduccion a odoo",
    'author': "Javier",
    'website': "",
    'category': "Tools",
    'version': '0.1',
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/reloj_view.xml',
        'views/proveedores_view.xml',
        'views/servicio_cliente_view.xml',
    ],

    'installable': True,
    'application': True,
}
