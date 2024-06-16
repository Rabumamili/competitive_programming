class Node:
    def __init__(self, k, v, p, n):
        self.frq = 0
        self.k = k
        self.v = v
        self.prev = p
        self.next = n
        
class LFUCache:

    def __init__(self, cap: int):
        self.cap = cap
        self.most_f = Node(None, None, None, None)
        self.least_f = Node(None, None, self.most_f, None)
        self.most_f.next = self.least_f
        self.k_map = {}
        self.f_map = {}
        
    def pop(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        return node

    def push_front(self, node):
        self.most_f.next.prev = node
        node.next = self.most_f.next
        self.most_f.next = node
        node.prev = self.most_f
        return node
        
    def get(self, k: int) -> int:
        if k not in self.k_map:
            return -1
        node = self.k_map[k]
        self.f_map[node.frq].remove(k)
        if not self.f_map[node.frq]:
            del self.f_map[node.frq]
        node.frq += 1
        if node.frq in self.f_map:
            self.f_map[node.frq].append(k)
        else:
            self.f_map[node.frq] = [k]
        return node.v

    def put(self, k: int, v: int) -> None:
        if self.cap == 0:
            return
        if k not in self.k_map:
            if len(self.k_map) == self.cap:
                self.remove()
            node = Node(k, v, None, None)
            self.k_map[k] = self.push_front(node)
            node.frq += 1
            if node.frq in self.f_map:
                self.f_map[node.frq].append(k)
            else:
                self.f_map[node.frq] = [k]
        else:
            node = self.k_map[k]
            node.v = v
            self.f_map[node.frq].remove(k)
            if not self.f_map[node.frq]:
                del self.f_map[node.frq]
            node.frq += 1
            if node.frq in self.f_map:
                self.f_map[node.frq].append(k)
            else:
                self.f_map[node.frq] = [k]
                
    def remove(self):
        least_f = min(self.f_map.keys())
        k = self.f_map[least_f].pop(0)
        node = self.pop(self.k_map[k])
        del self.k_map[k]
        if not self.f_map[node.frq]:
            del self.f_map[node.frq]

# Example of usage:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key, value)
