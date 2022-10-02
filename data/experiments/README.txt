Here are brief descriptions of each experiment.

test: a small experiment with three different prompts meant to simply 
validate that the experiment pipeline is working correctly.

All other experiments start with "ns", standing for "Nonsense Syllogisms".

Then they are either orig ("original"), or nonsense, or halfsense. These mean, 
respectively, that the syllogisms are exactly as in the original test, or 
substituted for nonsense words preserving the logical structures. or keep the 
prompted syllogism as in the original, while making the training syllogisms 
nonsensical as in the nonsense examples.

Then they are either zeroshot, fewshot, sixshot, or manyshot. These mean, 
respectively, that with each prompt we provide zero, two, six, or seven 
training syllogisms.

Then they are either v1, v2, or v3. These mean, respectively, that with each 
prompt we make no reference to "nonsense" or "syllogisms", or that we make 
reference to "nonsense" but not "syllogisms", or that we make reference to 
"syllogisms" but not "nonsense".
