from collections import defaultdict

class PassagePathing:
    def __init__(self,graph):
        self.graph = graph
        self.part1_count = 0
        self.part2_count = 0
        
    def part1(self):
        self.part1_count = 0
        visited = {}
        self.tally_part1_paths(self.graph['start'],visited,"start",["start"])
        return self.part1_count
        
    def tally_part1_paths(self,nodes,visited,prev_node,order):
        visited_copied = visited.copy()

        for node in nodes:
            visited_copied = visited.copy()
            order_copy = order.copy()
            visited_copied.setdefault(node,False)
            
            if node == 'start':
                continue
            elif node == 'end':
                order_copy.append("end")
                self.part1_count +=1
                # print(order_copy)
            elif visited_copied[node] and node.lower() == node:
                continue
            elif visited_copied[node] and node.upper() == node:
                order_copy.append(node)
                self.tally_part1_paths(graph[node],visited_copied,node,order_copy)
            elif not visited_copied[node]:
                order_copy.append(node)
                visited_copied[node] = True
                
                self.tally_part1_paths(graph[node],visited_copied,node,order_copy)

    def part2(self):
        self.part2_count = 0
        visits = {}
        self.tally_part2_paths(self.graph['start'],visits,"start",["start"],False)
        return self.part2_count
        
    def tally_part2_paths(self,nodes,visits,prev_node,order,small_cave_visit_twice):
        visits_copied = visits.copy()

        for node in nodes:
            visits_copied = visits.copy()
            order_copy = order.copy()
            visits_copied.setdefault(node,0)
            small_cave_visit_twice_copied = small_cave_visit_twice
            
            if node == 'start':
                continue
            elif node == 'end':
                order_copy.append("end")
                self.part2_count +=1
                # print(order_copy)
            elif small_cave_visit_twice_copied and visits_copied[node] and node.lower() == node:
                continue
        
            elif visits_copied[node] and node.upper() == node:
                order_copy.append(node)
                self.tally_part2_paths(graph[node],visits_copied,node,order_copy,small_cave_visit_twice_copied)
            elif not visits_copied[node] or (visits_copied[node] <2 and node.lower() == node):
                visits_copied[node]+=1
                if visits_copied[node] == 2:
                    small_cave_visit_twice_copied = True
                    
                order_copy.append(node)
                
                self.tally_part2_paths(graph[node],visits_copied,node,order_copy,small_cave_visit_twice_copied)
            
if __name__ == '__main__':
    graph = defaultdict(list)

    with open("solutions/day_12_input.txt") as f:
        for line in f:
            path1,path2=line.strip().split('-')
            graph[path1].append(path2)
            graph[path2].append(path1)

    p = PassagePathing(graph)
    # part 1
    print(p.part1())

    # part 2
    print(p.part2())

        
        