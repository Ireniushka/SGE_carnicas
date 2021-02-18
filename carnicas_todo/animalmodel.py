from odoo import models, fields

class animal(models.Model):
    __name = "animal"

    raza = fields.Char("Raza")
    edad = fields.Char("Edad")
    matadero = fields.Char("Matadero")
    fecha_sacr = fields.Date("Fecha_sacr")