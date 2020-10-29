
user_data = [
    "YangQiang", 
    "ZhengLi",
    "ZhangYuantong",
    "ZhouYan"
    "XuQinning"
]


class UserDAO:
    def  __init__(self):
        super(UserDAO, self).__init__()
    
    def validate(self, user):
        # 今后替换成数据验证
        if user in user_data:
            return True
        else:
            return False