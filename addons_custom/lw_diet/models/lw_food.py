# -*- coding: utf-8 -*-

from odoo import models, fields, api
import boto3, logging
from odoo.tools.config import config
import base64
_logger = logging.getLogger(__name__)


class LWFood(models.Model):
    _name = 'lw.food'
    _description = 'Food'
    _rec_name = 'name'

    name = fields.Char(string="Name", required=1)
    calo = fields.Float(string="Calo", required=1, default=0)
    description = fields.Text(string="Description", required=1, help="Show how to cook that and image of this food")
    total_like = fields.Integer(string="Total Likes", default=0)
    recommend_level = fields.Selection([
        ('1', '1'),
        ('1.5', '1.5'),
        ('2', '2'),
        ('2.5', '2.5'),
        ('3', '3'),
        ('3.5', '3.5'),
        ('4', '4'),
        ('4.5', '4.5'),
        ('5', '5'),
    ], string="Recommend Level")
    prepare_time = fields.Float(string="Prepare Time", help="Time for preparing in minutes")
    cooking_time = fields.Float(string="Cooking Time", help="Time for cooking in minutes")
    category_id = fields.Many2one('lw.food.category', string="Category", requried=1)
    image = fields.Char(string="Image Url")
    field_binary_import = fields.Binary(string="Image", store=False)
    field_binary_name = fields.Char(string="Image", store=False)


    @api.model
    def create(self, vals):
        file_binary = vals.get('field_binary_import')
        file_name = vals.get('field_binary_name')
        name = vals.get('name')
        calo = vals.get('calo')
        des = vals.get('description')
        category = vals.get('category_id')

        image = self.upload_file(file_binary, file_name)

        val_create = [{
            'name': name,
            'calo': calo,
            'description': des,
            'category_id': category,
            'image': image
        }]
        res = super(LWFood, self).create(val_create)

        return res


    def upload_file(self, image, name):
        try:
            bucket_name = config.get('bucket_name')
            endpoint_s3 = config.get('endpoint_s3')
            aws_access_key_id = config.get('aws_access_key_id')
            aws_secret_access_key = config.get('aws_secret_access_key')
            session = boto3.Session(aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
            s3 = session.resource('s3')
            lw_s3 = s3.Bucket(bucket_name)
            data = base64.b64decode(image)
            lw_s3.put_object(Key=name, Body=data)
            image_url = endpoint_s3 + bucket_name + '/' + name
            return image_url
        except Exception as err:
            raise err
