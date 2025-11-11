
"""
这个gril.py 是全量复制粘贴boy.py文件的所有源码，
只是将 _pee_pose 函数中的 "站着" 改为 "蹲着"

这是极端面向过程的大缺点，只有部分不同，却需要全量复制所有代码，然后去扣字母修改部分代码。
如果男孩和女孩的吃饭公共函数改变了，那就需要去boy.py 和 gril.py 两个文件中都去修改。

例如让你实现一个分布式函数调度框架例如celery  funboost ，需要实现支持40种消息队列，但都需要支持qps控频率 并发 重试 超时杀死等功能，
如果使用极端面向过程，框架开发难度极高。
"""

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
    print(f"{name} 蹲着小便")
