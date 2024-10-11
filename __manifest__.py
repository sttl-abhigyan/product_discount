{
    'name': 'Product Discount',
    'version': '1.0',
    'summary': 'Base module',
    'license': 'LGPL-3',
    'depends': [
        'base',
         'sale_management',
         'product'
    ],

    'data': [

        'security/ir.model.access.csv',
        "views/product_view.xml",
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
