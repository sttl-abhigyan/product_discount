from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    discount_percentage = fields.Float(string="Discount Percentage", default=0.0)

    @api.depends('list_price', 'discount_percentage')
    def _compute_discounted_price(self):
        for product in self:
            if product.discount_percentage:
                discount = product.list_price * (product.discount_percentage / 100)
                product.discounted_price = product.list_price - discount
            else:
                product.discounted_price = product.list_price

    discounted_price = fields.Monetary(
        string="Discounted Price",
        compute="_compute_discounted_price",
        store=True,
    )


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.onchange('product_id', 'product_uom_qty')
    def _apply_discount(self):
        for line in self:
            if line.product_id.discount_percentage:
                discount = line.product_id.list_price * (line.product_id.discount_percentage / 100)
                line.price_unit = line.product_id.list_price - discount
            else:
                line.price_unit = line.product_id.list_price
