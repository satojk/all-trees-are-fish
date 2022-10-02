import os
import src.experiment_harness as harness
import src.results_analysis as analysis

__EXPERIMENTS_PATH = 'data/experiments/'
__API_KEY_PATH = 'data/api_key.txt'

def main() -> None:
    experiments = [f for f in os.listdir(__EXPERIMENTS_PATH) if '.json' in f]
    for experiment in experiments:
            harness.run_experiment(os.path.join(__EXPERIMENTS_PATH, experiment),
                                   __API_KEY_PATH)
    analysis.get_results_matrix('data/results/')

if __name__ == '__main__':
    main()
