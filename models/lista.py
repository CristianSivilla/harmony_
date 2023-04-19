from odoo import models, fields

class Lista(models.Model):
    _name = 'lista'
    _description = 'Modelo de lista'

    id_lista = fields.Integer(string='Id_Lista', required=True, index=True, help='Id de la lista')
    nom = fields.Char(string='Nom', help='Nombre de la lista')
    lista = fields.Many2one('empleat', string='Lista', required=True, help='Empleado de la lista')
