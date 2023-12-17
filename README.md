## Office GPT

This is Language Model which generates Dialogues in style of the TV-show "*The Office*". Data set used for training can be found from https://www.kaggle.com/datasets/nasirkhalid24/the-office-us-complete-dialoguetranscript/data. Only the first four seasons were used for training.

The model can be trained by running:

`python3 scripts/train.py`

After this, inference can be ran by:

`python3 scripts/inference.py ${start_text} ${max_tokens}`

The output is pure gibberish, but this is what you achieve with **10 805 078 parameters**.

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
