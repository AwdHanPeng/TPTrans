These dirs save processed data including these files for each language:
- node_vocab.json (The vocab for node)
- source_vocab.json (The vocab for methods body)
- target_vocab.json (The vocab for methods name)
- train.txt
- test.txt
- valid.txt

And also a dict file picked from the github repository of [Code Transformer](https://github.com/danielzuegner/code-transformer):


- ct_vocab.json

For ct_vocab.json, we remove some not used special tokens presented in Code Transformer, 
and then add ours special tokens _STR_, _METHOD_ and _NUM_. We don't change other words in the vocab.
Keeping the same vocab is crucial for fair comparison of our models compared with baselines (please refer the _statistic.py_ in _parser_ dir for detailed reasons).
