## Office GPT

This is Language Model which generates Dialogues in style of the TV-show "*The Office*". Data set used for training can be found from https://www.kaggle.com/datasets/nasirkhalid24/the-office-us-complete-dialoguetranscript/data. Only the first four seasons were used for training. I got the idea for this from https://cs224d.stanford.edu/reports/oguz.pdf and Andrej Karpathy's intro to Language Models.

The model can be trained by running:

`python3 scripts/train.py`

After this, inference can be ran by:

`python3 scripts/inference.py ${start_text} ${max_tokens}`

The output is pure gibberish, but this is what you achieve with **10 805 078 parameters** and lazy hyperparameter tuning.

### Example output:

```
Michael:
Good morning Jim!

Jim:
I am gonna call you down in the back, you can get your party.

Michael:
Yes, it is everyone with your stripper and it co-rabbed, happy. And for smaking sprays in deposition.  Thank you.

Jan:
Michael?

Michael:
They have no idea.

Jan:
No, I didn't give a cats, I think it is in my own caskward.

Michael:
What did I die to do?

Jan:
I like the party, so...

Michael:
It was just fine for me. 
```

### Technical details
- **Multi-Head Attention**: Enhances the model's ability to process different parts of the input sequence in parallel.

- **Layer Normalization**: Applied both before the multi-head attention mechanism and before the feed-forward network in each transformer block.

- **Residual Connections**: Used in each transformer block to facilitate the flow of information and gradients through the network.

- **Embedding Layers**: The model utilizes separate embedding layers for tokens and positional encodings.

- **Character-Level Encoding**: Each character is treated as a distinct entity, allowing the model to learn and generate text at the granular level of individual characters.
