class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height  # 身高，单位：厘米
        self.weight = weight  # 体重，单位：千克

    def eat(self, food_weight):
        """吃饭：增加体重和身高"""
        self.weight += food_weight
        self.height += food_weight * 0.01
        print(f"{self.name} 吃了 {food_weight} 千克食物，体重: {self.weight} 千克，身高: {self.height} 厘米")

    def pee(self, pee_weight):
        """拉尿：减少体重"""
        self._pee_pose()
        if pee_weight > self.weight:
            pee_weight = self.weight
        self.weight -= pee_weight
        print(f"{self.name} 拉了 {pee_weight} 千克尿，体重: {self.weight} 千克，身高: {self.height} 厘米")

    def _pee_pose(self):
        """拉尿姿势："""
        raise NotImplementedError("子类必须实现 _pee_pose 方法")


class Boy(Person):
    """
    男孩类：继承自Person类
    """

    def _pee_pose(self):
        """拉尿姿势："""
        print(f"{self.name} 站着小便")


class Girl(Person):
    """
    女孩类：继承自Person类
    """

    def _pee_pose(self):
        """拉尿姿势："""
        print(f"{self.name} 蹲着小便")


if __name__ == "__main__":
    xiaomin = Boy("小明", 100, 50)
    xiaohong = Girl("小红", 95, 45)
    xiaohua = Girl("小花", 98, 48)

    person_list :list[Person] = [xiaomin, xiaohong, xiaohua] # 多态

    for person in person_list:
        person.eat(10)
        person.pee(5)
        print("="*30 + '\n')


    """
小明 吃了 10 千克食物，体重: 60 千克，身高: 100.1 厘米
小明 站着小便
小明 拉了 5 千克尿，体重: 55 千克，身高: 100.1 厘米
==============================

小红 吃了 10 千克食物，体重: 55 千克，身高: 95.1 厘米
小红 蹲着小便
小红 拉了 5 千克尿，体重: 50 千克，身高: 95.1 厘米
==============================

小花 吃了 10 千克食物，体重: 58 千克，身高: 98.1 厘米
小花 蹲着小便
小花 拉了 5 千克尿，体重: 53 千克，身高: 98.1 厘米
==============================
    """

