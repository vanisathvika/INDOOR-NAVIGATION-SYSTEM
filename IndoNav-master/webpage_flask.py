from flask import Flask, render_template, request, jsonify
import heapq

app = Flask(__name__)

# Load edges data from JSON file or define it directly in the code
edges_dict = {'room201': {'201nav252': 1.5},
              'room252': {'201nav252': 1.5},
              'room202': {'202nav251': 1.5},
              'room251': {'202nav251': 1.5},
              'room203': {'203nav': 1.5},
              'room204': {'204nav250': 1.5},
              'room250': {'204nav250': 1.5},
              'room205': {'205nav': 1.5},
              'room249': {'249nav': 1.5},
              'room206': {'206nav': 1.5},
              'room248': {'248nav': 1.5},
              'room207': {'207nav': 1.5},
              'room208': {'208nav': 1.5},
              'room209': {'209nav': 1.5},
              'room210': {'210nav': 1.5},
              'room211': {'211nav247': 1.5},
              'room247': {'211nav247': 1.5},
              'room212': {'212nav246': 1.5},
              'room246': {'212nav246': 1.5},
              'room213': {'213nav245': 1.5},
              'room245': {'213nav245': 1.5},
              'room214': {'214nav233': 1.5},
              'room233': {'214nav233': 1.5},
              'room215': {'215nav232': 1.5},
              'room232': {'215nav232': 1.5},
              'room216': {'216nav231': 1.5},
              'room231': {'216nav231': 1.5},
              'room217': {'217nav': 1.5},
              'room218': {'218nav': 1.5},
              'room219': {'219nav': 1.5},
              'room220': {'220nav': 1.5},
              'room221': {'221nav230': 1.5},
              'room230': {'221nav230': 1.5},
              'room222': {'222nav': 1.5},
              'room223': {'223nav229': 1.5},
              'room229': {'223nav229': 1.5},
              'room224': {'224nav': 1.5},
              'room225': {'225nav228': 1.5},
              'room228': {'225nav228': 1.5},
              'room226': {'226nav227': 1.5},
              'room227': {'226nav227': 1.5},
              'room244': {'244nav': 1},
              'room243': {'243nav': 1},
              'room242': {'242nav': 1.5},
              'room241': {'241nav': 1.5},
              'room240': {'navcs': 1.5},
              'room239': {'239nav': 1.5},
              'room238': {'238nav': 1.5},
              'room237': {'237nav': 1},
              'room236': {'236nav': 1},
              'room235': {'235nav': 1, 'room234': 4},
              'room234': {'room235': 4},

              '201nav252': {'202nav251': 4, 'room201': 1.5, 'room252': 1.5},
              '202nav251': {'201nav252': 4, 'room202': 1.5, 'room251': 1.5, '203nav': 7},
              '203nav': {'202nav251': 7, '204nav250': 7, 'navcw': 22},
              '204nav250': {'203nav': 7, 'room204': 1.5, 'room250': 1.5, '205nav': 2},
              '205nav': {'204nav250': 2, 'room205': 1.5, '249nav': 3},
              '249nav': {'room249': 1.5, '205nav': 3, '206nav': 2},
              '206nav': {'room206': 1.5, '249nav': 2, '248nav': 2},
              '248nav': {'room248': 1.5, '206nav': 2, '207nav': 5},
              '207nav': {'room207': 1.5, '248nav': 5, '208nav': 3},
              '208nav': {'room208': 1.5, '207nav': 3, '209nav': 7},
              '209nav': {'room209': 1.5, '208nav': 7, '210nav': 7},
              '210nav': {'room210': 1.5, '211nav247': 7, '209nav': 7},
              '211nav247': {'210nav': 7, 'room211': 1.5, 'room247': 1.5, '212nav246': 7},
              '212nav246': {'211nav247': 7, '213nav245': 7, 'room212': 1.5, 'room246': 1.5},
              '213nav245': {'212nav246': 7, 'room212': 1.5, 'room246': 1.5, 'lounge': 5},
              'lounge': {'loungelane': 22, '213nav245': 5, '214nav233': 10},
              '214nav233': {'lounge': 10, '215nav232': 7, 'room214': 1.5, 'room233': 1.5},
              '215nav232': {'214nav233': 7, '216nav231': 7, 'room215': 1.5, 'room232': 1.5},
              '216nav231': {'215nav232': 7, '217nav': 1.5, 'room216': 1.5, 'room231': 1.5},
              '217nav': {'room217': 1.5, '216nav231': 1.5, '218nav': 6},
              '218nav': {'room218': 1.5, '217nav': 6, '219nav': 7},
              '219nav': {'room219': 1.5, '218nav': 7, '220nav': 3},
              '220nav': {'room220': 1.5, '219nav': 3, '221nav230': 9},
              '221nav230': {'220nav': 9, '222nav': 7, 'room221': 1.5, 'room230': 1.5},
              '222nav': {'room222': 1.5, '221nav230': 7, '223nav229': 8},
              '223nav229': {'222nav': 8, '224nav': 3, 'room223': 1.5, 'room229': 1.5},
              '224nav': {'223nav229': 3, '225nav228': 7, 'room224': 1.5, 'navce': 22},
              '225nav228': {'224nav': 7, '226nav227': 4, 'room225': 1.5, 'room228': 1.5},
              '226nav227': {'225nav228': 4, 'room226': 1.5, 'room227': 1.5},
              'loungelane': {'lounge': 22, '244nav': 6, '234nav': 6},
              '244nav': {'loungelane': 6, 'room244': 1, '243nav': 8},
              '243nav': {'244nav': 8, 'room243': 1, '242nav': 8},
              '242nav': {'room242': 1, 'navcw': 2, 'navcn': 5, '243nav': 8},
              'navcw': {'203nav': 22, 'navcs': 5, '241nav': 3, '242nav': 2},
              '241nav': {'room241': 1, 'navcw': 3, 'navcs': 3},
              'navcs': {'241nav': 3, 'navcw': 5, 'room240': 2, '239nav': 3, 'navce': 5},
              '239nav': {'room239': 2, 'navcs': 3, 'navce': 3},
              'navce': {'224nav': 22, 'navcs': 5, 'navcn': 5, '239nav': 3, '238nav': 2},
              'navcn': {'navcw': 5, 'navce': 5, '242nav': 4, '238nav': 5, '237nav': 4},
              '238nav': {'navce': 2, 'navcn': 5, '237nav': 4, 'room238': 1},
              '237nav': {'navcn': 4, '238nav': 4, '236nav': 4, 'room237': 1},
              '236nav': {'237nav': 4, '235nav': 4, 'room236': 1},
              '235nav': {'236nav': 4, 'room235': 1, 'room234': 4},
              '234nav': {'loungelane': 6, '235nav': 4}}


# Dijkstra's algorithm implementation
def dijkstra(graph, start, end):
    queue = [(0, start, [])]
    visited = set()
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            path = path + [node]
            if node == end:
                return cost, path

            for neighbor, weight in graph.get(node, {}).items():
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + weight, neighbor, path))
    return float("inf"), []


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get_path", methods=["POST"])
def get_path():
    data = request.get_json()
    source = data['source']
    destination = data['destination']

    distance, path = dijkstra(edges_dict, source, destination)

    if path:
        return jsonify({"path": path, "distance": distance}), 200
    else:
        return jsonify({"error": "No path found for the given source and destination."}), 404


if __name__ == "__main__":
    app.run(debug=True)
