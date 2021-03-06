# -*- coding: utf-8 -*-

from odoo import models, fields, api
import boto3, logging
import base64
from odoo.tools.config import config
_logger = logging.getLogger(__name__)

class LWExercise(models.Model):
    _name = 'lw.exercise'
    _description = 'Exercise'

    name = fields.Char(string="Name", required=1)
    duration = fields.Integer(string="Duration", help='Duration for 1 exercise in second')
    description = fields.Text(string="Description", help='Show how to practice this exercise')
    kcal = fields.Float(string="Kcal", help="Calories consumed after completing the exercise")
    min_weight = fields.Float(string="Min Weight", help="Min Weight that can fit exercises")
    max_weight = fields.Float(string="Max Weight", help="Max Weight that can fit exercises")
    min_height = fields.Float(string="Min Height", help="Min Height that can fit exercises")
    max_height = fields.Float(string="Max Height", help="Max Height that can fit exercises")
    fixed = fields.Boolean(string="Fixed", help="Type of exercise", required=1, default=True)
    weightloss_area_ids = fields.Many2many("lw.weightloss.area", string="WeightLoss Area")
    video_id = fields.Many2many('lw.video', string='Video')
    image = fields.Char(string="Image Url")
    video = fields.Char(string="Video Url")
    image_import = fields.Binary(string="Video", store=False)
    image_name = fields.Char(string="Field Binary Name", store=False)


    @api.model
    def create(self, vals):
        image_import = vals.get('image_import')
        name = vals.get('name')
        image_name = vals.get('image_name')
        des = vals.get('description')
        weightloss_area_ids = vals.get('weightloss_area_ids')
        area_id = weightloss_area_ids[0][2]
        video = vals.get('video_id')
        video_id = video[0][2]

        image_url = None
        if image_import:
            image_url = self.upload_file(image_import, image_name)

        val_create = [{
            'name': name,
            'description': des,
            'image': image_url,
        }]
        res = super(LWExercise, self).create(val_create)
        for item in area_id:
            res.write({
            'weightloss_area_ids': [(4, item)]
            })
        for item in video_id:

            self.env['lw.exercise.video'].create([{
                'exercise_id': res.id,
                'video_id': item
            }])
            res.write({
                'video_id': [(4, item)]
            })
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
            lw_s3.put_object(Key=name, Body=data, ACL='public-read-write')
            image_url = endpoint_s3 + name
            return image_url
        except Exception as err:
            raise err

    @api.multi
    def name_get(self):
        res = []
        for item in self:
            res.append((item.id, item.name))
        return res
