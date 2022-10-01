import src.experiment_harness as harness

__EXPERIMENT_PATH = 'test.json'
__API_KEY_PATH = 'data/api_key.txt'

def main() -> None:
    harness.run_experiment(__EXPERIMENT_PATH, __API_KEY_PATH)

if __name__ == '__main__':
    main()
