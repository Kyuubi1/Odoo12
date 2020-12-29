# -*- coding: utf-8 -*-

from odoo import models, fields, api
import boto3, logging
import base64
from odoo.tools.config import config
_logger = logging.getLogger(__name__)


class LWVideo(models.Model):
    _name = 'lw.video'
    _description = 'Exercise\'s Video'

    field_binary_import = fields.Binary(string="Video", store=False)
    field_binary_name = fields.Char(string="Video name", store=False)
    image_import = fields.Binary(string="Video", store=False)
    image_name = fields.Char(string="Field Binary Name", store=False)
    video_name = fields.Char(string="Video Name", required=1)
    image = fields.Char(string="Image")
    url = fields.Char(string="URL")
    description = fields.Char(string="Description", required=1)
    calo = fields.Float(string="Calo", required=1)
    category_ids = fields.Many2many(comodel_name='lw.category', column1='lw_video_id', column2='lw_category_id', string='Category')

    @api.model
    def create(self, vals):
        file_binary = vals.get('field_binary_import')
        file_name = vals.get('field_binary_name')
        image_import = vals.get('image_import')
        video_name = vals.get('video_name')
        image_name = vals.get('image_name')
        calo = vals.get('calo')
        des = vals.get('description')

        video_url = None
        image_url = None
        if file_binary:
            video_url = self.upload_file(file_binary, file_name)
        if image_import:
            image_url = self.upload_file(image_import, image_name)

        vals_create = [{
            'video_name': video_name,
            'url': video_url,
            'image': image_url,
            'description': des,
            'calo': calo
        }]

        res = super(LWVideo, self).create(vals_list=vals_create)
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

    @api.multi
    def name_get(self):
        res = []
        for item in self:
            res.append((item.id, item.video_name))
        return res