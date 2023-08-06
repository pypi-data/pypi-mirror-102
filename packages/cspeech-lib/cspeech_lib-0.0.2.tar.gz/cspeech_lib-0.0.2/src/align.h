#ifndef CSPEECH_SRC_ALIGN_H_
#define CSPEECH_SRC_ALIGN_H_

#include <vector>
#include <iostream>
#include <absl/strings/str_format.h>

namespace cspeech {

struct Edge;

struct BestInfo {
  float logit = std::numeric_limits<float>::infinity();
  int via_time;
};

struct Node {
  std::vector<Edge> edges = {};

  // Populated by graph prep.
  std::vector<Edge*> in_edges = {};
  // Populated by align.
  float best = std::numeric_limits<float>::infinity();
  Edge* best_edge;
  std::vector<std::pair<int, std::pair<int, Edge*>>> best_edge_history;

};

struct Edge {
  // Id of the logit class, set to -1 for the skip-type edge.
  int class_id;
  // Optional penalty for choosing this edge.
  float logit_penalty = 0.0f;
  // Optional penalty for the duration of this edge.
  float length_logit_penalty = 0.0f;
  // Target node.
  int target;

  // Populated by graph prep.
  int source;
  // Populated by align
  BestInfo best;
//  std::vector<BestInfo> best_history = {};
};

float add(float a, float b) {
  return a + b;
}

void validate_nodes(const std::vector<Node>& nodes, int num_classes) {
  int i = 0;
  for (const Node& node : nodes) {
    if (i == 0) {
      // first node
      if (node.edges.empty() || !node.in_edges.empty()) {
        throw std::invalid_argument("first node cannot must have outgoing edges and no incoming edges.");
      }
    } else if ((i + 1) == nodes.size()) {
      // last node
      if (!node.edges.empty() || node.in_edges.empty()) {
        throw std::invalid_argument("last node must have incoming edges and no outgoing edges");
      }
    } else {
      // middle node
      if (node.edges.empty() || node.in_edges.empty()) {
        throw std::invalid_argument("middle node must have both: incoming edges and outgoing edges");
      }
    }
    // Check no cyclic dependencies & validate classes
    for (const Edge* in_edge : node.in_edges) {
      if (in_edge->source >= i) {
        throw std::invalid_argument(absl::StrFormat(
            "a node can only point to a later node, but found edge from %d to %d",
            in_edge->source,
            i));
      }
      if (in_edge->class_id >= num_classes) {
        throw std::invalid_argument("class_id must be smaller than num_classes");
      }
    }
    i++;
  }

}

void graph_prep(std::vector<Node>& nodes, int num_classes) {
  int i = 0;
  for (Node& node : nodes) {
    for (Edge& edge : node.edges) {
      edge.source = i;
      if (edge.target >= nodes.size() || edge.target < 0) {
        throw std::invalid_argument(absl::StrFormat("invalid target for node %d: %d", i, edge.target));
      }
      nodes[edge.target].in_edges.push_back(&edge);
    }
    i++;
  }
  validate_nodes(nodes, num_classes);
}

std::vector<const Edge*> get_path(const std::vector<Node>& nodes, int num_steps) {
  int t = num_steps - 1;
  std::vector<const Edge*> path;
  path.reserve(num_steps);
  int current_node = nodes.size() - 1;
  size_t num_iterations = 0;
  while (t >= 0) {
    const Node& node = nodes.at(current_node);
//    std::cout << absl::StrFormat("At node: %d (history has %d elements)", current_node, node.best_edge_history.size()) << std::endl;
    int history_index = node.best_edge_history.size();
    while (--history_index >= 0) {
      if (node.best_edge_history.at(history_index).first <= t) {
        break;
      }
    }
    if (history_index < 0) {
      // This cannot happen unless there is a bug in the alignment.
      throw std::logic_error("invalid history");
    }
    int entered_at;
    Edge* edge;
    std::tie(entered_at, edge) = node.best_edge_history.at(history_index).second;

    //    std::cout << absl::StrFormat("  Reached source node: %d -> %d, transition was at %d, via %d", current_node, edge->source, entered_at, edge->class_id) << std::endl;
    current_node = edge->source;
    if (edge->class_id < 0) {
      continue;
    }
    while (t >= entered_at) {
      path.push_back(edge);
      t--;
    }
    num_iterations++;
    if (num_iterations > 10000000) {
      throw std::logic_error("Something is wrong or input too large, should have finished already.");
    }
  }
  if (current_node != 0) {
    throw std::logic_error("did not end up at the root node");
  }
  if (path.size() != num_steps) {
    throw std::logic_error("computed path of invalid length");

  }
  std::reverse(path.begin(), path.end());
//  for (const Edge* edge : path) {
//    std::cout << absl::StrFormat("Path: %d -> %d (via %d)", edge->source, edge->target, edge->class_id) << std::endl;
//  }
  return path;
}

// Complexity edges * num_time_steps :/ Anyway for 50hz audio logits we can process say 3k steps -> 1 minute in ~1ms.
std::vector<const Edge*> align(std::vector<Node>& nodes,
                               const float* logits,
                               int num_classes,
                               int num_time_steps,
                               int blank_class = 0,
                               bool allow_class_repeats = true) {
  if (nodes.size() <= 1) {
    return {};
  }
  if (nodes.at(1).in_edges.empty()) {
    graph_prep(nodes, num_classes);
  }
//  std::vector<Edge*> edges;
//  for (Node& node : nodes) {
//    for (Edge& edge : node.edges) {
//      edges.push_back(&edge);
//    }
//  }

  Node& start_node = nodes.front();
  start_node.best = 0.0f;
  for (int t = 0; t < num_time_steps; t++) {
//    std::cout << "T: " << t << std::endl;
    // We could in theory parallelize over edges, but IMO better to do a coarse alignment first to split the problem
    //  into small chunks (say 500 nodes long).
    int i = 0;
    for (Node& node : nodes) {
      const float source_logit = node.best;
      // All incoming edges to this node have been already processed. Find next best.
      float next_best_logit = std::numeric_limits<float>::infinity();
      Edge* next_best_edge = nullptr;
      for (Edge* in_edge : node.in_edges) {
        float cand_logit = in_edge->best.logit;
        if (cand_logit < next_best_logit) {
          next_best_logit = cand_logit;
          next_best_edge = in_edge;
        }
      }
//      std::cout << absl::StrFormat("  Node %d. Best %.2f -> %.2f", i, source_logit, next_best_logit) << std::endl;
      for (Edge& edge : node.edges) {
        if (edge.class_id < 0) {
          // Skip-type edge. Simply copy the source next best logit. No history needed for this edge.
          edge.best.logit = next_best_logit;

        } else {
          // 2 options for the edge, either start a new one or continue.
          const float continue_logit = edge.best.logit + logits[edge.class_id] + edge.length_logit_penalty;
          const float new_logit = source_logit + edge.logit_penalty + logits[edge.class_id] + edge.length_logit_penalty;
          if (new_logit < continue_logit || (!allow_class_repeats && edge.class_id != blank_class)) {
            edge.best.logit = new_logit;
            edge.best.via_time = t;
//            edge.best_history.push_back(edge.best);
          } else {
            // Continue.
            edge.best.logit = continue_logit;
          }
        }
//        std::cout << absl::StrFormat("    Edge %d->%d via %d. Cost: %.2f", i, edge.target, edge.class_id, edge.best.logit) << std::endl;

      }
      node.best = next_best_logit;
      if (next_best_edge) {
        node.best_edge = next_best_edge;
//        if (node.best_edge_history)
        bool should_save;
        if (node.best_edge_history.empty()) {
          should_save = true;
        } else {
          int saved_via_time;
          Edge* saved_edge;
          std::tie(saved_via_time, saved_edge) = node.best_edge_history.back().second;
          should_save = next_best_edge != saved_edge || saved_via_time != next_best_edge->best.via_time;
        }
        if (should_save) {
          node.best_edge_history.push_back({t, {next_best_edge->best.via_time, next_best_edge}});
//          std::cout << "Saving...\n";
        } else {
//          std::cout << "Not saving...\n";
        }
      }
      i++;
    }
    logits += num_classes;
  }
//  return {};
  if (nodes.back().best_edge_history.empty()) {
    throw std::invalid_argument(
        "Did not manage to reach the end node, maybe the number of nodes is too large for the time length?");
  }
  return get_path(nodes, num_time_steps);
}

}  // namespace cspeech



#endif //CSPEECH_SRC_ALIGN_H_
