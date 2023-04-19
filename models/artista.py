from odoo import models, fields

class Artista(models.Model):
    _name = 'artista'
    _description = 'Modelo de artista'

    id_artista = fields.Integer(string='Id_Artista', required=True, index=True, help='Id del artista')
    nombre = fields.Char(string='Nombre', required=True, help='Nombre del artista')
    nacionalidad = fields.Char(string='Nacionalidad', help='Nacionalidad del artista')

