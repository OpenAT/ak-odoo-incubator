# coding: utf-8
# © 2017 David BEAL @ Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Stock Reserve Location',
    'summary': 'Allow to feed picking locations from reserve locations',
    'version': '8.0.1.0.0',
    'author': 'Akretion',
    'description': """
- overstock implementation: exchange between: picking and reserve locations
- reserve stock locations are stored by product putaway like picking locations
""",
    'category': 'warehouse',
    'depends': [
        'stock_putaway_product',
    ],
    'website': 'http://www.akretion.com/',
    'data': [
        'views/stock_view.xml',
    ],
    'demo': [
        'demo/stock_demo.xml',
    ],
    'installable': True,
    'license': 'AGPL-3',
}
