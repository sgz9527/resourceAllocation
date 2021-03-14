from kind import *
# 寻找虚拟机
def get_vm(name, vm_kind_list):
    for vm in vm_kind_list:
        if name == vm.get_name().strip():
            return vm


# 判断服务器是否能够容纳虚拟机
def is_enough(server: ServerKind, vm: VmKind):
    """

    :param server: 服务器
    :param vm:     虚拟机
    :return:       是否足够分配
    """
    # 单节点
    if vm.get_node_kind() == "0":
        cpu, memory = server.get_anode_info()
        if cpu > vm.get_cpu() and memory > vm.get_memory():
            return True
        else:
            cpu, memory = server.get_bnode_info()
            if cpu > vm.get_cpu() and memory > vm.get_memory():
                return True
            else:
                return False
    # 双节点
    else:
        a_cpu, a_memory = server.get_anode_info()
        b_cpu, b_memory = server.get_bnode_info()
        # 有一组节点满足要求即可
        if (a_cpu >= vm.get_cpu() // 2 and a_memory >= vm.get_memory() // 2) and (
                b_cpu >= vm.get_cpu() // 2 and b_memory >= vm.get_memory() // 2):
            return True
        return False
