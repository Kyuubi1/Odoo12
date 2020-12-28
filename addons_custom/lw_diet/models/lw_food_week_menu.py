from odoo import models, api, fields


class FoodWeekMenu(models.TransientModel):
    _name = 'lw.food.menu.week'
    _rec_name = 'week_id'

    food_id = fields.Many2many('lw.food', string='Food')
    week_id = fields.Many2one('lw.week', string='Day of Week')
    menu_id = fields.Many2one('lw.menu', string='Meal')

    @api.model
    def create(self, vals):
        vals_list = []
        food_list = vals.get('food_id')
        list_id = food_list[0][2]
        menu_id = vals.get('menu_id')
        week_id = vals.get('week_id')
        menu = self.env['lw.menu'].sudo().search([('id', '=', menu_id)])

        val_create = {
            'menu_id': menu_id,
            'week_id': week_id
        }
        vals_list.append(val_create)

        res = super(FoodWeekMenu, self).create(vals_list=vals_list)

        diet = self.env['lw.diet'].create([{
            'lw_week_id': week_id,
            'lw_menu_id': menu_id

        }])

        for item in list_id:
            menu.write({
                'food_ids': [(4, item)]
            })
            res.write({
                'food_id': [(4, item)]
            })


            diet.write({
                'food_ids': [(4, item)]
            })

        return res