from utils import *
import random

train_path = "../test.txt"
running_server = []


def main():
    f = open(train_path, "r")
    # 服务器数量
    server_num = int(f.readline().strip())
    server_list = []
    # 存储服务器类型
    for _ in range(server_num):
        name, cpu, memory, hardware_cost, electroic_cost = f.readline().strip().strip("(").strip(")").split(",")
        server_list.append(ServerKind(name, int(cpu), int(memory), int(hardware_cost), int(electroic_cost)))
    # 虚拟机类型
    vm_num = int(f.readline().strip())
    vm_list = []
    for _ in range(vm_num):
        name, cpu, memory, node_kind = f.readline().strip().strip("(").strip(")").split(",")
        vm_list.append(VmKind(name, int(cpu), int(memory), node_kind))
    # 总共请求天数
    day_num = int(f.readline().strip())
    # 第一天请求
    request_num = int(f.readline().strip())
    list_request = []
    for _ in range(request_num):
        list_request.append(f.readline().strip())
    # 处理第一天请求
    MCMC(list_request, server_list, vm_list, running_server)
    print(running_server)

    # 之后的请求
    for _ in range(day_num - 1):
        pass


# 第一天请求策略
def MCMC(request_lst, server_lst, vm_list, running_server=None):
    """

    :param running_server:
    :param request_lst: 请求列表
    :param server_lst:  可用服务器列表
    :param vm_list:     可用虚拟机列表
    :return:
    """
    all_prices = 9999999
    temp_server = []
    count = 0
    while count < 1000:
        lst = request_lst
        temp_prices = 0
        # 初始化服务器
        server = server_lst[random.randint(0, len(server_lst) - 1)]
        # 增加成本
        temp_prices += cost(server, need_hardware=True, need_electroic=True, money=temp_prices)
        temp_server.append(server)
        while len(lst) > 0:
            request = lst.pop()
            # 资源不够
            op, vm_name, _id = request.strip("(").strip(")").split(",")
            vm = get_vm(vm_name.strip(), vm_list)
            changed = False
            while not is_full(server, vm):
                # 申请服务器
                server = server_lst[random.randint(0, len(server_lst) - 1)]
                changed = True
            # 增加成本
            if changed:
                temp_prices += cost(server, need_hardware=True, need_electroic=True, money=temp_prices)
                temp_server.append(server)

            server.distribute_resource(vm.get_cpu(), vm.get_memory(), vm.get_node_kind())
        if temp_prices < all_prices:
            all_prices = temp_prices
        count += 1
    running_server += temp_server
    # running_server
    print(all_prices)

    return all_prices


def request_policy(running_server, server_list1, server_list2, vm_lst, request_lst, ):
    """
    请求处理策略
    init 获取两种排序之后的服务器列表
    1.判断现有服务中是否有空余位置给虚拟机
    2.判断虚拟机类型(cpu > memory or memory > cpu)
    3.从两个服务器列表中 选择服务器类型与虚拟机一样的最大的型号
    4.填入服务器
    所有请求全部完成后,判断所有有空闲容量的服务器，判断更小的服务器能否替代
    :param server_list1:    cpu > memory 的服务器列表
    :param server_list2:    memory > cpu 的服务器列表
    :param running_server:  正在运行的服务器
    :param vm_lst:          虚拟机信息
    :param request_lst:     请求列表
    :return:
    """

    pass


def sort_server(server_lst):
    """
    服务器排序 分为两种 CPU > 内存 or 内存 > CPU
    :param server_lst: 服务器列表
    :return:
    """
    server_list1 = []
    server_list2 = []
    for server in server_lst:
        a_cpu, a_memory = server.get_anode_info()
        if a_cpu >= a_memory:
            server_list1.append(server)
        else:
            server_list2.append(server)
    server_list1 = sorted(server_list1,key=get_key_value)
    server_list2 = sorted(server_list2,key=get_key_value)
    return server_list1,server_list2


def get_key_value(server):
    return server.get_beishu()


# 扩容策略
def expansion():
    pass


# 迁移策略
def transfer():
    pass


if __name__ == "__main__":
    main()
