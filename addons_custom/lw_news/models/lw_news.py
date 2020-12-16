# -*- coding: utf-8 -*-

from odoo import models, fields, api
import re
import boto3, logging
import base64, json
from addons_custom import const
_logger = logging.getLogger(__name__)


class LWNews(models.Model):
    _name = 'lw.news'
    _description = 'News/ Article'
    _rec_name = 'title'

    title = fields.Char(string="Title", required=1)
    description = fields.Text(string="Description")
    total_like = fields.Integer(string="Total Likes", required=1, default=0)
    total_views = fields.Integer(string="Total Views", required=1, default=0)
    image_url_list = fields.Char(string="Image URL list")
    field_binary_import = fields.Binary(string="Thumbnail", store=False)
    field_binary_name = fields.Char(string="Field Binary Name", store=False)

    @api.multi
    def name_get(self):
        res = []
        for item in self:
            res.append((item.id, ("%s") % (item.title)))
        return res

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=8):
        args = args or []
        domain_name = [('title', 'ilike', name)]
        recs = self.search(domain_name + args, limit=limit)
        return recs.name_get()

    @api.model
    def create(self, vals):

        file_binary = vals.get('field_binary_import')
        file_name = vals.get('field_binary_name')
        title = vals.get('title')
        description = vals.get('description')
        image_url = None
        if file_binary:
            image_url = self.upload_file(file_binary, file_name)

        val_create = [{
            'title': title,
            'description': description,
            'image_url_list': image_url
        }]

        res = super(LWNews, self).create(val_create)

        # update description with image
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        res.description = res.description.replace('src="/web/image', f'src="{base_url}/web/image')
        reg = r'src=".*"'
        r = re.search(reg,res.description)
        print(r)
        # get 3 or less image in html
        return res

    def upload_file(self, image, name):
        try:
            session = boto3.Session(aws_access_key_id=const.AWS_ACCESS_KEY_ID, aws_secret_access_key=const.AWS_SECRET_ACCESS_KEY)
            s3 = session.resource('s3')
            lw_s3 = s3.Bucket(const.BUCKET_NAME)
            data = base64.b64decode(image)
            lw_s3.put_object(Key=name, Body=data)
            image_url = const.ENDPOINT_S3 + const.BUCKET_NAME + '/' + name
            return image_url
        except Exception as err:
            raise err