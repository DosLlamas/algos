#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>

using namespace std;

// Helper function to perform depth-first search to detect cycles
bool hasCycle(map<string, vector<string>>& graph, set<string>& visited, set<string>& recStack, const string& node) {
    if (!visited.count(node)) {
        visited.insert(node);
        recStack.insert(node);

        for (const string& neighbor : graph[node]) {
            if (!visited.count(neighbor) && hasCycle(graph, visited, recStack, neighbor)) {
                return true;
            }
            if (recStack.count(neighbor)) {
                return true;
            }
        }
    }
    recStack.erase(node);
    return false;
}

bool isPossible(int n, vector<string>& statements) {
    map<string, vector<string>> graph;

    // Parse the statements and build the directed graph
    for (const string& statement : statements) {
        string name1, name2, relation;
        size_t pos1 = statement.find(' ');
        name1 = statement.substr(0, pos1);
        size_t pos2 = statement.find(' ', pos1 + 1);
        relation = statement.substr(pos1 + 1, pos2 - pos1 - 1);
        name2 = statement.substr(pos2 + 1);

        if (relation == ">") {
            graph[name1].push_back(name2);
        } else if (relation == "<") {
            graph[name2].push_back(name1);
        }
    }

    // Check for cycles in the graph
    set<string> visited;
    set<string> recStack;
    for (const auto& node : graph) {
        if (!visited.count(node.first)) {
            if (hasCycle(graph, visited, recStack, node.first)) {
                return false;
            }
        }
    }

    return true;
}

int main() {
    int n;
    cin >> n;
    cin.ignore();
    vector<string> statements(n);
    for (int i = 0; i < n; ++i) {
        getline(cin, statements[i]);
    }

    if (isPossible(n, statements)) {
        cout << "possible" << endl;
    } else {
        cout << "impossible" << endl;
    }

    return 0;
}