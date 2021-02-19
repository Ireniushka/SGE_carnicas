from odoo import models, fields, api

class animal(models.Model):
    __name = "animal"

    raza = fields.Char("Raza",required=True)
    edad = fields.Integer("Edad",required=True)
    peso = fields.Integer("Peso", required=True)
    matadero = fields.Selection(selection=[("cadiz", "Cádiz"),("jerez","Jerez"),("sevilla","Sevilla")],required=True)
    fecha_sacr = fields.Date("Fecha_sacr",required=True)
    precio = fields.Float("Precio", compute="_precioTotal", store=True)
    ult_revision = fields.Date("Ultima revision")

    @api.depends("peso", "edad")
    def _precioTotal(self):
        for anm in self:
            anm.precio = anm.peso + (10*anm.edad)