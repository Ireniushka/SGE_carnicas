from odoo import models, fields

class animal(models.Model):
    __name = "animal"

    raza = fields.Char("Raza")
    edad = fields.Char("Edad")
    matadero = fields.Selection(selection=[("cadiz", "Cádiz"),("jerez","Jerez"),("sevilla","Sevilla")])
    fecha_sacr = fields.Date("Fecha_sacr")
    precio = fields.Float("Precio")
    ult_revision = fields.Date("Ultima revision")