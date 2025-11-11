
def eat(name, height, weight, food_weight):
    """吃饭：增加体重和身高"""
    new_weight = weight + food_weight
    new_height = height + food_weight * 0.01
    print(f"{name} 吃了 {food_weight} 千克食物，体重: {new_weight} 千克，身高: {new_height} 厘米")
    return new_height, new_weight

# 拉尿函数
def pee(name, height, weight, pee_weight):
    """拉尿：减少体重"""
    if pee_weight > weight:
        pee_weight = weight
    new_weight = weight - pee_weight
    print(f"{name} 拉了 {pee_weight} 千克尿，体重: {new_weight} 千克，身高: {height} 厘米")
    return height, new_weight


def _pee_pose(name):
    """拉尿姿势："""
    print(f"{name} 站着小便")
