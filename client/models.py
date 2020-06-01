from django.db import models


class ClientScore(models.Model):
    class Meta:
        db_table = 't_client_score'
        verbose_name = '客户端分数'

    id = models.AutoField('自增主键', db_column='f_id', primary_key=True)
    client_name = models.CharField('客户端名称', db_column='f_client_name', max_length=512)
    client_score = models.IntegerField('客户端分数', db_column='f_client_score')
    state = models.BooleanField('删除状态物理标识', db_column='f_state', default=True)
    create_time = models.DateTimeField('创建时间', db_column='f_create_time', auto_now_add=True)
    update_time = models.DateTimeField('修改时间', db_column='f_update_time', auto_now=True)
