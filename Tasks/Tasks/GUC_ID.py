import re
from turtle import back


class GUC_ID:
    def __init__(self, id):
        self.id = id

    def Valid_id(self) -> bool:
        regex = re.compile(r'^(\d{1,2})\-(\d{4,5})$')
        match = regex.search(self.id)
        if not match:
            return False

        self.batch = int(match.group(1))
        app_num = int(match.group(2))

        batch_valid = (self.batch - 1) % 3 == 0
        app_num_valid = app_num != 0
        return app_num_valid and batch_valid

    def Entrance_Year(self):
        return int(2003 + (self.batch - 1) / 3)

    # def check(self):
    #     dash =-1
    #     for i in range(0,len(id)):
    #         if not isnumeric(id[i]) and id[i]=='-' and dash == -1:
    #             dash=i
    #         else:
    #             return False
    #     return True
