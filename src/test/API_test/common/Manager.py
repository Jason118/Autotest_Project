# -*- coding: utf-8 -*-
import json
from BaseModel import BaseModel


class Manager(BaseModel):
    """管理后台，包括管理后台的接口(Date:2016-07-05)"""
    def __init__(self, username='admin', password='111111'):
        self.username = username
        self.password = password

    def get_user_password_info(self):
        """接口API：
        {
          "name":"P_Human__GetUserPasswordInfo",
          "desc": "后台验证用户登录密码",
          "inParameters":[
                            {"name":"p_username","type":"varchar"},
                            {"name":"p_password", "type":"varchar"}
                          ],
          "outParameters":[
                            {"name":"p_personid", "type":"integer"}
                          ]
        }
        """
        param = {'p_username': self.username, 'p_password': self.password}
        return self._signandpost(param, 'Admin_GetUserPasswordInfo')

    def get_person_id(self):
        res = self.get_user_password_info()
        return json.loads(res)['p_personid']

    def get_menu(self):
        """接口API：
        {
          "name":"P_Global__GetMenu",
          "desc": "管理后台获取菜单api",
          "inParameters":[
                            {"name":"p_sessionid","type":"integer", "desc": "管理员id"},
                            {"name":"p_systemname", "type":"varchar", "desc": "系统模块名称"}
                          ],
          "outParameters":[
                            {"name":"res0","type":"cursor"}
                          ]
        }
        """
        param = {'p_sessionid': self.get_person_id(), 'p_systemname': ''}  # TODO 系统模块名称？
        return self._signandpost(param, 'GetMenu')

    def merchant_approve_apply(self, merchant, status=4, approvememo=''):
        """函数参数
        :param merchant:要审核的商户ID
        :param status:审核状态，4为审核通过，5为审核驳回
        :param approvememo:审核拒绝理由
        :return:返回{}表示成功，返回error message表示失败

        接口API：
        {
          "name":"P_Merchant__ApproveApply",
          "desc": "审核商户入驻申请",
          "inParameters":[
                            {"name":"p_opid","type":"integer", "desc": "管理员id"},
                            {"name":"p_merchantid", "type":"integer", "desc": "商户id"},
                            {"name":"p_status", "type":"integer", "desc": "4-审核通过，5-审核驳回"},
                            {"name":"p_approvememo", "type":"varchar", "desc": "审核拒绝原因","maxLength":500}
                          ],
          "outParameters":[
                          ]
        }
        """
        param = {'p_opid': self.get_person_id(),
                 'p_merchantid': merchant,
                 'p_status': status,
                 'p_approvememo': approvememo}
        return self._signandpost(param, 'ApproveApply')

    def merchant_get_basic_info(self, username='', merchant=0, startdate='', enddate='', mobile='', status=0, approvename=''):
        """函数参数：
        :param username:筛选条件——商户username
        :param merchant:筛选条件——商户编号，不按商户编号选则传0
        :param startdate:筛选条件——注册时间大于等于，格式yyyyMMdd
        :param enddate:筛选条件——注册时间小于等于，格式yyyyMMdd
        :param mobile:筛选条件——联系电话
        :param status:筛选条件——商户状态，默认为0
        :param approvename:筛选条件——审核人
        :return:返回筛选出的结果

        接口API：
        {
          "name":"P_Merchant__GetBasicinfo",
          "desc": "获取商户基本信息",
          "inParameters":[
                            {"name":"p_opid","type":"integer", "desc":"管理员id"},
                            {"name":"p_username","type":"varchar", "desc": "按照商户username筛选"},
                            {"name":"p_merchantid","type":"integer", "desc": "按照商户编号筛选, 不传请传0", "defaultValue":0},
                            {"name":"p_startdate","type":"date", "desc": "筛选注册时间大于等于该参数的记录, 格式yyyyMMdd"},
                            {"name":"p_enddate","type":"date", "desc": "筛选注册时间小于等于该参数的记录, 格式yyyyMMdd"},
                            {"name":"p_mobile", "type":"mobile", "desc": "按照联系电话筛选"},
                            {"name":"p_status","type":"integer", "desc": "按照商户状态筛选", "defaultValue":0},
                            {"name":"p_approvename", "type":"varchar", "desc": "按照审核人筛选"}
                          ],
          "outParameters":[
                            {"name":"res0", "type":"cursor"},
                            {"name":"res1", "type":"cursor"}
                          ]
        }
        """
        param = {'p_opid': self.get_person_id(),
                 'p_username': username,
                 'p_merchantid': merchant,
                 'p_startdate': startdate,
                 'p_enddate': enddate,
                 'p_mobile': mobile,
                 'p_status': status,
                 'p_approvename': approvename}

        return self._signandpost(param, 'GetBasicinfo')

    def purchase_transfer(self, orderid):
        """函数参数
        :param orderid:list，传入order id组成的列表
        :return:返回划款结果列表

        接口API:
        {
          "name": "R_Purchase__Transfer",
          "desc": "支付划款接口",
          "inParameters":[
                            {"name":"order_id","type":"varchar", "desc": "订单id列表，多id间用【，】分隔", "notEmpty": 1}
                          ],
          "outParameters":[
                            {"name":"ret", "type":"cursor", "desc": "划款结果的列表，每条记录的包含order_id, error_code,
                                                                    error_message，其中划款成功的订单不包括错误信息"}
                          ]
        }
        """
        orderid_str = ''
        for order in orderid:
            orderid_str += order
        param = {'order_id': orderid_str}
        return self._signandpost(param, 'PurchaseTransfer')


if __name__ == '__main__':
    print Manager().get_person_id()