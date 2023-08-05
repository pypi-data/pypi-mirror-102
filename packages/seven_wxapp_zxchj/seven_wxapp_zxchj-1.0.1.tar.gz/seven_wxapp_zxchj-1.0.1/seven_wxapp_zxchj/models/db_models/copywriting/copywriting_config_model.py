
#此文件由rigger自动生成
from seven_framework.mysql import MySQLHelper
from seven_framework.base_model import *


class CopywritingConfigModel(BaseModel):
    def __init__(self, db_connect_key='db_wxapp', sub_table=None, db_transaction=None, context=None):
        super(CopywritingConfigModel, self).__init__(CopywritingConfig, sub_table)
        self.db = MySQLHelper(config.get_value(db_connect_key))
        self.db_connect_key = db_connect_key
        self.db_transaction = db_transaction
        self.db.context = context

    #方法扩展请继承此类
    
class CopywritingConfig:

    def __init__(self):
        super(CopywritingConfig, self).__init__()
        self.id = 0  # id
        self.act_id = 0  # 活动id
        self.title = ""  # 标题
        self.content = ""  # 内容
        self.copywriting_type = 0  # 文案类型(枚举CopywritingType：1问题及帮助配置2关于我们3用户默认发货地址协议4抽盒规则)
        self.create_date = "1900-01-01 00:00:00"  # 创建时间
        self.modify_date = "1900-01-01 00:00:00"  # 更新时间

    @classmethod
    def get_field_list(self):
        return ['id', 'act_id', 'title', 'content', 'copywriting_type', 'create_date', 'modify_date']
        
    @classmethod
    def get_primary_key(self):
        return "id"

    def __str__(self):
        return "copywriting_config_tb"
    