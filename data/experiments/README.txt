Here are brief descriptions of each experiment.

test: a small experiment with three different prompts meant to simply 
validate that the experiment pipeline is working correctly.

ns_orig_zeroshot_v1: the 30 candidate syllogisms from the original Nonsense 
Syllogisms test, where each prompt contains only the candidate syllogism in 
question, to be judged as good or poor reasoning.

ns_orig_fewshot_v1: the 30 candidate syllogisms from the original Nonsense 
Syllogisms test, where each prompt contains the first two solved examples from 
the original test instructions, followed by the candidate syllogism in 
question, to be judged as good or poor reasoning.

ns_orig_manyshot_v1: the 30 candidate syllogisms from the original Nonsense 
Syllogisms test, where each prompt contains all seven solved examples from 
the original test instructions, followed by the candidate syllogism in 
question, to be judged as good or poor reasoning.

ns_orig_manyshot_v2: Same as v1 above, but the prompt prefix is slightly longer 
and explicitly declares the statements are all nonsense.
