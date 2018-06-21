# _*_ encoding: utf-8 _*_
__author__ = 'Admin'
__date__ = '2018/6/12 0:44'


import xadmin
from xadmin.views import BaseAdminPlugin, ListAdminView
from django.template import loader

class ListImporExcelPlugin(BaseAdminPlugin):
    import_excel = False

    def init_request(self, *args, **kwargs):
        return bool(self.import_excel)

    def block_top_toolbar(self, context, nodes):
        nodes.append(loader.render_to_string('xadmin/excel/model_list.top_toolbar.import.html', context_instance=context))


xadmin.site.register_plugin(ListImporExcelPlugin, ListAdminView)