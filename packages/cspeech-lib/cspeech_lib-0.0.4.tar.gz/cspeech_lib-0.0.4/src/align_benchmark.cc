#include <benchmark/benchmark.h>
#include "align.h"


using namespace cspeech;

static void BM_AlignAudioSeconds(benchmark::State& state) {
  for (auto _ : state) {
    state.PauseTiming();
    int time_steps = state.range(0)*50; // 50hz audio
    int num_nodes = state.range(0)*30; // 30hz phonemes
    int num_classes = 30; // about 30 phonemes
    std::vector<float> logits;
    logits.reserve(num_classes*time_steps);
    for (int i=0; i < num_classes*time_steps; i++) {
      logits.push_back(static_cast<float>(std::rand() % 10000) / 10000);
    }
    std::vector<Node> nodes;
    for (int i=0; i < num_nodes; i++) {
      nodes.push_back(Node{.edges={Edge{.class_id=rand() % num_classes, .target=i+1}}});
    }
    nodes.push_back(Node{});

    state.ResumeTiming();
    align(nodes, logits.data(), num_classes, time_steps);
  }
}

// V1
//-------------------------------------------------------------------
//Benchmark                         Time             CPU   Iterations
//-------------------------------------------------------------------
//BM_AlignAudioSeconds/10        1.88 ms         1.88 ms          356
//BM_AlignAudioSeconds/100        237 ms          237 ms            3
//BM_AlignAudioSeconds/200        981 ms          980 ms            1

// Register the function as a benchmark
BENCHMARK(BM_AlignAudioSeconds)->Unit(benchmark::kMillisecond)->Arg(10)->Arg(100)->Arg(200);
// Run the benchmark
BENCHMARK_MAIN();


