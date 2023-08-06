#include <stdio.h>
#include <filesystem>

#include "align.h"
#include "gtest/gtest.h"
#include "gmock/gmock.h"

namespace cspeech {
namespace {

//using ::testing::UnorderedElementsAre;
using ::testing::ElementsAre;
//using ::testing::ElementsAreArray;
//using ::testing::Pair;


TEST(Alignment, SimpleOneClass) {
  std::vector<Node> nodes;
  nodes.push_back(
      Node{.edges={Edge{.class_id=0, .logit_penalty=0.1, .target=1}}}
  );
  nodes.push_back(
      Node{.edges={Edge{.class_id=0, .logit_penalty=0.2, .target=2}}}
  );
  nodes.push_back(Node{});
  std::vector<float> logits = {
      0.0, 0.0, 0.0, 0.0
  };

  auto path = align(nodes, logits.data(), 1, 4);
  std::vector<int> class_ids;
  std::vector<int> targets;
  for (const Edge* edge : path) {
    class_ids.push_back(edge->class_id);
    targets.push_back(edge->target);
  }

  EXPECT_EQ(nodes.back().best, 0.3f);
  EXPECT_THAT(class_ids, ElementsAre(0, 0, 0, 0));
  // Should be deterministic, even though multiple solutions exist.
  EXPECT_THAT(targets, ElementsAre(1, 2, 2, 2));
}

TEST(Alignment, SimpleTwoClasses) {
  std::vector<Node> nodes;
  nodes.reserve(2);
  nodes.push_back(
      Node{.edges={Edge{.class_id=0, .target=1}, Edge{.class_id=1, .target=1}}}
  );

  nodes.push_back(Node{});
  std::vector<float> logits = {
      1.0, 0.0,
      1.0, 0.0,
      1.0, 0.0,
      0.0, 0.0,
  };

  auto path = align(nodes, logits.data(), 2, 4);
  std::vector<int> class_ids;
  std::vector<int> targets;
  for (const Edge* edge : path) {
    class_ids.push_back(edge->class_id);
    targets.push_back(edge->target);
  }

  EXPECT_EQ(nodes.back().best, 0.0f);
  EXPECT_THAT(class_ids, ElementsAre(1, 1, 1, 1));
  // Should be deterministic, even though multiple solutions exist.
  EXPECT_THAT(targets, ElementsAre(1, 1, 1, 1));
}


TEST(Alignment, SimpleTwoClassesNoRepeats) {
  std::vector<Node> nodes;
  nodes.reserve(2);
  nodes.push_back(
      Node{.edges={Edge{.class_id=0, .target=1}, Edge{.class_id=1, .target=1}}}
  );

  nodes.push_back(Node{});
  std::vector<float> logits = {
      1.0, 0.0,
      1.0, 0.0,
      1.0, 0.0,
      0.0, 0.0,
  };

  auto path = align(nodes, logits.data(), 2, 4, 0, false);
  std::vector<int> class_ids;
  std::vector<int> targets;
  for (const Edge* edge : path) {
    class_ids.push_back(edge->class_id);
    targets.push_back(edge->target);
  }

  EXPECT_EQ(nodes.back().best, 3.0f);
  EXPECT_THAT(class_ids, ElementsAre(0, 0, 0, 0));
  // Should be deterministic, even though multiple solutions exist.
  EXPECT_THAT(targets, ElementsAre(1, 1, 1, 1));
}

TEST(Alignment, SimpleTwoClassesNoRepeatsCustomBlank) {
  std::vector<Node> nodes;
  nodes.reserve(2);
  nodes.push_back(
      Node{.edges={Edge{.class_id=0, .target=1}, Edge{.class_id=1, .target=1}}}
  );

  nodes.push_back(Node{});
  std::vector<float> logits = {
      1.0, 0.0,
      1.0, 0.0,
      1.0, 0.0,
      0.0, 0.0,
  };

  auto path = align(nodes, logits.data(), 2, 4, 1, false);
  std::vector<int> class_ids;
  std::vector<int> targets;
  for (const Edge* edge : path) {
    class_ids.push_back(edge->class_id);
    targets.push_back(edge->target);
  }

  EXPECT_EQ(nodes.back().best, 0.0f);
  EXPECT_THAT(class_ids, ElementsAre(1, 1, 1, 1));
  // Should be deterministic, even though multiple solutions exist.
  EXPECT_THAT(targets, ElementsAre(1, 1, 1, 1));
}

TEST(Alignment, SimpleTwoClassesAmbiguous) {
  std::vector<Node> nodes;
  nodes.reserve(2);
  nodes.push_back(
      Node{.edges={Edge{.class_id=0, .target=1}, Edge{.class_id=1, .target=1}}}
  );
  nodes.push_back(
      Node{.edges={Edge{.class_id=0, .target=2}, Edge{.class_id=1, .target=2}}}
  );

  nodes.push_back(Node{});
  std::vector<float> logits = {
      0.0, 0.0,
      0.0, 0.0,
      0.0, 0.0,
      0.0, 0.0,
  };

  auto path = align(nodes, logits.data(), 2, 4, 0, false);
  std::vector<int> class_ids;
  std::vector<int> targets;
  for (const Edge* edge : path) {
    class_ids.push_back(edge->class_id);
    targets.push_back(edge->target);
  }

  EXPECT_EQ(nodes.back().best, 0.0f);
  EXPECT_THAT(class_ids, ElementsAre(0, 0, 0, 0));
  // Should be deterministic, even though multiple solutions exist.
  EXPECT_THAT(targets, ElementsAre(1, 2, 2, 2));
}

TEST(Alignment, TwoClassesLengthPenalty) {
  std::vector<Node> nodes;
  nodes.push_back(
      Node{.edges={Edge{.class_id=0, .target=1}}}
  );
  nodes.push_back(
      Node{.edges={Edge{.class_id=1, .target=2}}}
  );
  nodes.push_back(
      Node{.edges={Edge{.class_id=0, .length_logit_penalty=0.11, .target=3}, Edge{.class_id=-1, .target=3}}}
  );
  nodes.push_back(
      Node{.edges={Edge{.class_id=1, .target=4}}}
  );
  nodes.push_back(
      Node{.edges={Edge{.class_id=0, .target=5}}}
  );

  nodes.push_back(Node{});
  std::vector<float> logits = {
      0.0, 1.0,
      0.0, 1.0,
      0.0, 1.0,
      0.0, 0.0,
      0.0, 0.5,
      0.0, 1.0,
      0.0, 1.0,
      0.0, 1.0,
      0.0, 1.0,
      0.0, 0.0,
      0.0, 1.0,
  };

  auto path = align(nodes, logits.data(), 2, 11, 0, false);
  std::vector<int> class_ids;
  std::vector<int> targets;
  for (const Edge* edge : path) {
    class_ids.push_back(edge->class_id);
    targets.push_back(edge->target);
  }

  EXPECT_EQ(nodes.back().best, 0.5f);
  EXPECT_THAT(class_ids, ElementsAre(0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0 ));
  EXPECT_THAT(targets, ElementsAre(1, 1, 1, 2, 4, 5, 5, 5, 5, 5, 5 ));
}

TEST(Alignment, TwoClassesLengthPenaltyButStillWorthIt) {
  std::vector<Node> nodes;
  nodes.push_back(
      Node{.edges={Edge{.class_id=0, .target=1}}}
  );
  nodes.push_back(
      Node{.edges={Edge{.class_id=1, .target=2}}}
  );
  nodes.push_back(
      Node{.edges={Edge{.class_id=0, .length_logit_penalty=0.09, .target=3}, Edge{.class_id=-1, .target=3}}}
  );
  nodes.push_back(
      Node{.edges={Edge{.class_id=1, .target=4}}}
  );
  nodes.push_back(
      Node{.edges={Edge{.class_id=0, .target=5}}}
  );

  nodes.push_back(Node{});
  std::vector<float> logits = {
      0.0, 1.0,
      0.0, 1.0,
      0.0, 1.0,
      0.0, 0.0,
      0.0, 0.5,
      0.0, 1.0,
      0.0, 1.0,
      0.0, 1.0,
      0.0, 1.0,
      0.0, 0.0,
      0.0, 1.0,
  };

  auto path = align(nodes, logits.data(), 2, 11, 0, false);
  std::vector<int> class_ids;
  std::vector<int> targets;
  for (const Edge* edge : path) {
    class_ids.push_back(edge->class_id);
    targets.push_back(edge->target);
  }

  EXPECT_THAT(nodes.back().best, testing::FloatNear(0.45f, 1e-5));
  EXPECT_THAT(class_ids, ElementsAre(0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0));
  EXPECT_THAT(targets, ElementsAre(1, 1, 1, 2, 3, 3, 3, 3, 3, 4, 5  ));
}

TEST(Alignment, TwoClassesLogitPenalty) {
  std::vector<Node> nodes;
  nodes.push_back(
      Node{.edges={Edge{.class_id=0, .target=1}}}
  );
  nodes.push_back(
      Node{.edges={Edge{.class_id=1, .target=2}}}
  );
  nodes.push_back(
      Node{.edges={Edge{.class_id=0, .logit_penalty=0.55, .target=3}, Edge{.class_id=-1, .target=3}}}
  );
  nodes.push_back(
      Node{.edges={Edge{.class_id=1, .target=4}}}
  );
  nodes.push_back(
      Node{.edges={Edge{.class_id=0, .target=5}}}
  );

  nodes.push_back(Node{});
  std::vector<float> logits = {
      0.0, 1.0,
      0.0, 1.0,
      0.0, 1.0,
      0.0, 0.0,
      0.0, 0.5,
      0.0, 1.0,
      0.0, 1.0,
      0.0, 1.0,
      0.0, 1.0,
      0.0, 0.0,
      0.0, 1.0,
  };

  auto path = align(nodes, logits.data(), 2, 11, 0, false);
  std::vector<int> class_ids;
  std::vector<int> targets;
  for (const Edge* edge : path) {
    class_ids.push_back(edge->class_id);
    targets.push_back(edge->target);
  }

  EXPECT_EQ(nodes.back().best, 0.5f);
  EXPECT_THAT(class_ids, ElementsAre(0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0 ));
  EXPECT_THAT(targets, ElementsAre(1, 1, 1, 2, 4, 5, 5, 5, 5, 5, 5 ));
}


TEST(Alignment, TwoClassesLogitPenaltyButStillWorthIt) {
  std::vector<Node> nodes;
  nodes.push_back(
      Node{.edges={Edge{.class_id=0, .target=1}}}
  );
  nodes.push_back(
      Node{.edges={Edge{.class_id=1, .target=2}}}
  );
  nodes.push_back(
      Node{.edges={Edge{.class_id=0, .logit_penalty=0.19, .target=3}, Edge{.class_id=-1, .target=3}}}
  );
  nodes.push_back(
      Node{.edges={Edge{.class_id=1, .target=4}}}
  );
  nodes.push_back(
      Node{.edges={Edge{.class_id=0, .target=5}}}
  );

  nodes.push_back(Node{});
  std::vector<float> logits = {
      0.0, 1.0,
      0.0, 1.0,
      0.0, 1.0,
      0.0, 0.0,
      0.0, 0.5,
      0.0, 1.0,
      0.0, 1.0,
      0.0, 1.0,
      0.0, 1.0,
      0.0, 0.0,
      0.0, 1.0,
  };

  auto path = align(nodes, logits.data(), 2, 11, 0, false);
  std::vector<int> class_ids;
  std::vector<int> targets;
  for (const Edge* edge : path) {
    class_ids.push_back(edge->class_id);
    targets.push_back(edge->target);
  }

  EXPECT_THAT(nodes.back().best, testing::FloatNear(0.19f, 1e-5));
  EXPECT_THAT(class_ids, ElementsAre(0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0));
  EXPECT_THAT(targets, ElementsAre(1, 1, 1, 2, 3, 3, 3, 3, 3, 4, 5  ));
}

TEST(Alignment, SimpleTwoClassesLogitPenalty) {
  std::vector<Node> nodes;
  nodes.reserve(2);
  nodes.push_back(
      Node{.edges={Edge{.class_id=0, .logit_penalty=0.01, .target=1}, Edge{.class_id=1, .target=1}}}
  );
  nodes.push_back(
      Node{.edges={Edge{.class_id=0, .target=2}, Edge{.class_id=1, .target=2}}}
  );

  nodes.push_back(Node{});
  std::vector<float> logits = {
      0.0, 0.0,
      0.0, 0.0,
      0.0, 0.0,
      0.0, 0.0,
  };

  auto path = align(nodes, logits.data(), 2, 4, 0, false);
  std::vector<int> class_ids;
  std::vector<int> targets;
  for (const Edge* edge : path) {
    class_ids.push_back(edge->class_id);
    targets.push_back(edge->target);
  }

  EXPECT_EQ(nodes.back().best, 0.0f);
  EXPECT_THAT(class_ids, ElementsAre(1, 0, 0, 0));
  // Should be deterministic, even though multiple solutions exist.
  EXPECT_THAT(targets, ElementsAre(1, 2, 2, 2));
}

TEST(Alignment, TwoClassesWithLogitPenalty) {
  std::vector<Node> nodes;
  nodes.reserve(4);
  nodes.push_back(
      Node{.edges={Edge{.class_id=0, .target=1}, Edge{.class_id=1, .logit_penalty=0.1, .target=1}}}
  );
  nodes.push_back(
      Node{.edges={Edge{.class_id=0, .target=2}, Edge{.class_id=1, .logit_penalty=2.5, .target=2}}}
  );
  nodes.push_back(
      Node{.edges={Edge{.class_id=0, .target=3}, Edge{.class_id=1, .logit_penalty=1.1, .target=3}}}
  );

  nodes.push_back(Node{});
  std::vector<float> logits = {
      0.0, 1.0,
      1.0, 0.0,
      1.0, 0.0,
      1.0, 0.0,
      1.0, 0.0,
      1.0, 0.0,
      0.0, 1.0,
  };

  auto path = align(nodes, logits.data(), 2, 7);
  std::vector<int> class_ids;
  std::vector<int> targets;
  for (const Edge* edge : path) {
    class_ids.push_back(edge->class_id);
    targets.push_back(edge->target);
  }

  EXPECT_EQ(nodes.back().best, 2.1f);
  EXPECT_THAT(class_ids, ElementsAre(1, 1, 1, 1, 1, 0, 0));
  EXPECT_THAT(targets, ElementsAre(1, 1, 1, 1, 1, 2, 3));
}

TEST(Alignment, TwoClassesWithSkips) {
  std::vector<Node> nodes;
  nodes.reserve(4);
  nodes.push_back(
      Node{.edges={Edge{.class_id=0, .target=1}, Edge{.class_id=1, .logit_penalty=0.1, .target=1}}}
  );
  nodes.push_back(
      Node{.edges={Edge{.class_id=0, .target=2}, Edge{.class_id=1, .logit_penalty=2.5, .target=2},
                   Edge{.class_id=-1, .target=2}}}
  );
  nodes.push_back(
      Node{.edges={Edge{.class_id=0, .target=3}, Edge{.class_id=1, .logit_penalty=1.1, .target=3}}}
  );

  nodes.push_back(Node{});
  std::vector<float> logits = {
      0.0, 1.0,
      1.0, 0.0,
      1.0, 0.0,
      1.0, 0.0,
      1.0, 0.0,
      1.0, 0.0,
      0.0, 1.0,
  };

  auto path = align(nodes, logits.data(), 2, 7);
  std::vector<int> class_ids;
  std::vector<int> targets;
  for (const Edge* edge : path) {
    class_ids.push_back(edge->class_id);
    targets.push_back(edge->target);
  }

  EXPECT_EQ(nodes.back().best, 1.1f);
  EXPECT_THAT(class_ids, ElementsAre(1, 1, 1, 1, 1, 1, 0));
  EXPECT_THAT(targets, ElementsAre(1, 1, 1, 1, 1, 1, 3));
}



}  // namespace
}  // namespace cspeech