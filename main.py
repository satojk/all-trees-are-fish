import src.experiment_harness as harness

__EXPERIMENT = None

def main() -> None:
    harness.run_experiment(__EXPERIMENT)

if __name__ == '__main__':
    main()
