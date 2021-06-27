import os  # 系统模块，有操作文件的功能
import time  # 时间模块
import random  # 随机数模块


def one():
    """遍历目录"""
    dir_lists = os.listdir(r'C:\Program Files (x86)')  # win系统的软件目录，返回目录的列表
    cnt = 0  # 计数
    print("前10个软件：")
    print('-' * 30)
    for dir_l in dir_lists:  # 遍历前10个目录
        cnt += 1
        if cnt > 10:
            break
        print(dir_l)
    print("-" * 30)
    print("统计含有Windows的软件：")
    keyword = "Windows"
    for dir_l in dir_lists:
        if keyword in dir_l:
            print(dir_l, end=', ')
    print('')


def two():
    """列表去重与排序"""
    li = [3, 6, 1, 7, 2, 8]  # 使用列表推导式
    li.extend([5, 6, 10, 11])  # 列表的元素扩充区别于append
    print("已知列表：", li)
    print("使用set去重后：", list(set(li)))  # set集合的使用以及类型转换
    print("使用sort排序：", sorted(li, reverse=False))
    print("使用切片排序：", tuple(li[::-1]))  # 同时使用tuple转为元组


def three():
    """求斐波那契数列"""
    fib = {1: 1, 2: 1}  # 初始化fib
    print("斐波那契数列前20项为：")
    for i in range(1, 20 + 1):
        if i not in fib.keys():
            fib[i] = fib[i - 1] + fib[i - 2]
        print(fib[i], end=', ')  # 使用end参数控制结尾的字符
    print('')


def four():
    """获取时间"""
    now = time.time()  # 获取当前时间戳，需要格式化
    print(
        "当前时间为：%d-%d-%d %d:%d:%d" %
        (time.localtime(now).tm_year, time.localtime(now).tm_mon,
         time.localtime(now).tm_mday, time.localtime(now).tm_hour,
         time.localtime(now).tm_min,
         time.localtime(now).tm_sec))  # 时间模块的使用以及字符串的格式化, tm_开头的是localtime的属性


def five():
    """计算阶乘"""
    num = input("请输入一个20以内的数（阶乘结果很大）：")
    assert 0 <= int(num) <= 20, "！！数字不合理, 程序终结。"  # 断言操作 条件表达式为false时，触发异常
    ans = cal(int(num))
    print("结果为：", ans)


def cal(n):
    """
    递归计算n的阶乘
    :param n:
    :return:
    """
    if n <= 1:
        return 1
    else:
        return n * cal(n - 1)  # 函数递归运行


def six():
    """lambda 表达式"""
    square = lambda x: x * x  # 使用lambda表达式作为函数
    print("计算平方：", square(12))


def seven():
    f1 = Friend("小明", "男", 12)  # 创建两个人物对象
    f2 = Friend("小红", "女", 20)
    print("这两个人一样吗：", f1 is f2)  # is运算符，判断是否是同一个对象，通过地址判断
    print("现在有几个人：", get_nums())
    f1.alloc_friends()  # 调用函数
    f2.alloc_friends()


def get_nums():
    return Friend.friend


class Friend:
    """建立Friend类"""
    friend = 0  # 类变量，不属于对象

    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age
        Friend.friend += 1

    def alloc_friends(self):
        if self.age < 18:
            print("抱歉！{}，你未成年".format(self.name))  # 使用format格式化字符串
        else:
            print("你好！{}".format(self.name), end=' ')
            alloc = {
                '男': "looking for a girl friend for you",  # 含蓄点，用英文
                '女': "looking for a boy friend for you"
            }
            print(alloc[self.sex], "from 1 - 100")
            no = random.randint(1, 100 + 1)  # 产生1-100内的随机整数
            print("for you:  No.", no)


def eight():
    """捕获异常"""
    a = [i for i in range(4, 12)]  # a长度为8: 12-4=8
    print(
        "列表a：",
        [("a[{}]".format(index), value) for index, value in enumerate(a)
         ],  # enumerate解析列表为：索引-值 的形式, 同时又使用列表推导式
        "长度：",
        len(a))  # len函数的使用
    print("a[2]~a[6]: ", a[2:6 + 1])  # 列表的切片：左闭右开区间
    try:
        print("a[9]", a[9])  # 下标越界错误
    except IndexError as e:  # 捕获异常
        print("【错误信息：", e, "】")


def nine():
    """迭代器和生成器"""
    li = 'I-am-a-iterator.'  # 字符串本身就是一个迭代器
    print("使用迭代器：")
    for c in li:
        print(c, end=', ')
    print('')
    print("使用生成器：")
    for num in genera(10):  # 生成器返回的结果就是一个迭代器
        print(num, end=', ')
    print('')
    li = [i for i in range(100 + 1)]
    ans = []
    for v in filter(filter_func, li):  # 过滤器返回的是一个迭代器, 所以用for遍历
        ans.extend([v])  # 使用extend函数会将列表解析成单个值
    print("被2,4,6都整除的正整数：", ans)


def genera(n):
    for i in range(n):
        yield i  # 使用yield关键字使用生成器


def filter_func(n):
    """大于等于0，且被2,4,6整除的数"""
    # 使用了常用的的算术运算符和逻辑运算符and
    ans = True
    ans = (n > 0) and ans
    ans = (n % 2 == 0) and ans  # 取余 10 % 2 = 0， 11 % 2 = 1
    ans = (n % 4 == 0) and ans
    ans = (n % 6 == 0) and ans
    return ans


def my_dec(func):
    def inner():
        print(">>> 明月装饰了我的窗子，你装饰了我的函数 -- 《断zhang》")  # func执行前执行
        func()
        print(my_dec.__name__, "装饰了你的梦")  # func执行后执行  __name__为函数的名称

    return inner


@my_dec
def ten():
    """使用装饰器"""
    print(">>> 那谁装饰了我的梦？？")


class Node:
    """
    链表的每个节点
    """
    def __init__(self, val, pnext):
        self.value = val  # 值域
        self.pnext = pnext  # 指针域


class LinkedList:
    """一个链表"""
    def __init__(self):
        self.head = None  # 链表头
        self.tail = self.head  # 链表尾
        self.length = 0  # 链表元素个数

    def insert_value(self, val, loc=None):
        """向链表中插入值"""
        if self.list_empty():
            # 如果链表为空
            self.head = Node(val, None)  # 新建一个节点
            self.tail = self.head
            self.length = 1
        else:
            if (not loc) | (loc == self.length):
                # 如果插入位置在尾部或者未空，直接在尾部插入节点
                new_node = Node(val, None)  # 新节点
                self.tail.pnext = new_node
                self.tail = new_node  # 重新地位尾节点
                self.length += 1
            else:
                new_node = Node(val, None)  # 新节点
                last_node = self.head
                for index in range(self.length):
                    if index == (loc - 1) - 1:  # 找到插入的位置
                        break
                    else:
                        last_node = last_node.pnext
                """
                插到第3个位置：
                1->2->3->4->5
                1->2->new->3->4->5
                """
                next_node = last_node.pnext  # next = 3
                last_node.pnext = new_node  # 2的next = new
                new_node.pnext = next_node  # new的next = 3（next）
                self.length += 1

    def delete_value(self, loc=None):
        """删除链表中的某个值"""
        if not self.list_empty():
            if loc:  # 位置是存在的，不为None
                last_node = self.head
                for index in range(self.length):
                    if index == (loc - 1) - 1:  # 找到该位置了
                        break
                    else:
                        last_node = last_node.pnext
                """
                该节点的 上个节点 指向该节点的 下个节点 就删除它了
                2->3->4
                删除3
                2->4
                """
                next_node = last_node.pnext.pnext  # next = 4
                last_node.pnext = next_node  # 2.next = 4 就删除3了
            else:  # 位置不存在则删除最后一个元素
                now_node = self.head
                while now_node:
                    if now_node.pnext.pnext is None:
                        now_node.pnext = None
                        break
                    else:
                        now_node = now_node.pnext

    def list_empty(self):
        """判断链表是否为空"""
        if self.head is None:
            return True
        else:
            return False

    def list_traverse(self):
        """遍历链表"""
        if not self.list_empty():
            now_node = self.head
            print('-' * 15)
            while now_node:  # 逐个元素打印
                print("value->: ", now_node.value)
                now_node = now_node.pnext


def test():
    my_linkedlist = LinkedList()
    for i in range(5):
        my_linkedlist.insert_value(i)
    print("当前链表：")
    my_linkedlist.list_traverse()
    print("插入一个列表到在第3个节点：")
    my_linkedlist.insert_value(['this', 'is', 'a', 'list'], 3)
    my_linkedlist.list_traverse()
    print("删除第二个节点：")
    my_linkedlist.delete_value(2)
    my_linkedlist.list_traverse()


if __name__ == '__main__':
    while True:
        print("=" * 30)
        print("1. 遍历win系统安装的软件目录")
        print("2. 列表去重")
        print("3. 计算斐波那契数列F(n)前20个")
        print("4. 报时")
        print("5. 递归计算阶乘")
        print("6. lambda表达式")
        print("7. 面向\"对象\"编程")  # 使用转义符号 "\"
        print("8. 捕获异常")
        print("9. 迭代器、生成器、过滤器")
        print("0. 装饰器")
        print('a: 使用python实现一个链表')
        print("!!! 输入非上述指令退出...")
        print("=" * 30)
        user_order = input("请输入你的指令序号: ")
        # 将每个指令序号映射为函数名
        menu = {
            "1": one,
            "2": two,
            "3": three,
            "4": four,
            "5": five,
            "6": six,
            "7": seven,
            "8": eight,
            "9": nine,
            "0": ten,
            "a": test
        }
        if user_order not in menu.keys():  # 访问menu字典的键
            break
        else:
            menu[user_order]()  # 通过函数名调用函数
