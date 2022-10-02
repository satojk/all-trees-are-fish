import os
import csv
import json

def get_score_vector(results_path: str) -> list:
    with open(results_path, 'r') as f:
        results = json.load(f)
    score_vector = []
    for ix, output in enumerate(results['outputs']):
        if output == results['answers'][ix]:
            score_vector.append(1)
        else:
            score_vector.append(0)
    return score_vector

def get_results_matrix(results_dir_path: str) -> list:
    results_matrix = []
    results_paths = [f for f in os.listdir(results_dir_path) if '.json' in f]
    for results_path in results_paths:
        with open(os.path.join(results_dir_path, results_path), 'r') as f:
            results = json.load(f)
        # Standardize outputs (e.g. replace "valid"s with "good"s)
        std_f = lambda out: 'good' if out == 'valid' else ('poor' if out == 'invalid' else out)
        standardized_outputs = [std_f(out) for out in results['outputs']]
        results_matrix.append([results_path] + standardized_outputs)

    with open(os.path.join(results_dir_path, 'results_matrix.csv'), 'w') as f:
        writer = csv.writer(f)
        writer.writerows(results_matrix)

    return results_matrix

