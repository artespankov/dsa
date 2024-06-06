from collections import deque


def is_mango_seller(name):
    return name in ('thom', 'jonny', 'alice')


# 1 Model relations as a graph
def build_graph():
    graph = dict()
    graph['you'] = ['alice', 'bob', 'claire']
    graph['bob'] = ['janusz', 'peggy']
    graph['alice'] = ['peggy']
    graph['claire'] = ['thom', 'jonny']
    graph['janusz'] = []
    graph['peggy'] = []
    graph['thom'] = []
    graph['jonny'] = []
    return graph


# 2 Search for shortest path to the seller
def search_mango_seller():
    search_queue = deque()
    graph = build_graph()
    search_queue += graph["you"]
    checked = []
    while search_queue:
        person = search_queue.popleft()
        if person not in checked:
            if is_mango_seller(person):
                print(f'{person} is a mango seller!')
                return True
            else:
                search_queue += graph[person]
                checked.append(person)
    return False


search_mango_seller()
