# 服务器类型
class ServerKind:

    def __init__(self, name, cpu, memory, hardware_cost, electroic_cost):
        # 服务器名字
        self.name = name

        # 服务器硬件成本
        self.hardware_cost = hardware_cost

        # 服务器电费
        self.electroic_cost = electroic_cost

        # 服务器资源
        self.a_cpu = cpu // 2
        self.a_memory = memory // 2

        self.b_cpu = cpu // 2
        self.b_memory = memory // 2

    # 获取服务器名字
    def get_server_name(self):
        return self.name.strip()

    # 获取 A节点剩余信息
    def get_anode_info(self):
        return self.a_cpu, self.a_memory

    # 获取B节点剩余信息
    def get_bnode_info(self):
        return self.b_cpu, self.b_memory

    # 资源分配
    def distribute_resource(self, cpu, memory, kind):
        if kind == "0":
            return self.S_distribute_resource(cpu, memory)
        else:
            return self.D_distribute_resource(cpu, memory)

    # 单节点资源分配
    def S_distribute_resource(self, cpu: int, memory: int):
        a_cpu, a_memory = self.get_anode_info()
        b_cpu, b_memory = self.get_bnode_info()
        if (a_cpu >= cpu and a_memory >= memory) and (b_cpu >= cpu and b_memory >= memory):
            if a_cpu + a_memory >= b_cpu + b_memory:
                self.a_cpu -= cpu
                self.a_memory -= memory
            else:
                self.b_cpu -= cpu
                self.b_memory -= memory
        elif b_cpu >= cpu and b_memory >= memory:
            self.b_cpu -= cpu
            self.b_memory -= memory
        elif a_cpu >= cpu and a_memory >= memory:
            self.a_cpu -= cpu
            self.a_memory -= memory
        else:
            print("资源不足分配")

    # 双节点资源分配
    def D_distribute_resource(self, cpu: int, memory: int):
        if (self.a_cpu >= cpu // 2 and self.b_cpu >= cpu // 2) and (self.a_memory >= memory // 2 and self.b_memory >= memory // 2):
            self.a_cpu -= cpu // 2
            self.a_memory -= memory // 2
            self.b_cpu -= cpu // 2
            self.b_memory -= memory // 2
        else:
            print("资源不足分配")


# 虚拟机类型
class VmKind:
    def __init__(self, name, cpu: int, memory: int, node_kind):
        self.name = name
        self.cpu = cpu
        self.memory = memory
        # 0 单节点 1 双节点
        self.node_kind = node_kind

    def get_memory(self):
        return self.memory

    def get_cpu(self):
        return self.cpu

    def get_node_kind(self):
        return self.node_kind.strip()

    def get_name(self):
        return self.name.strip()
