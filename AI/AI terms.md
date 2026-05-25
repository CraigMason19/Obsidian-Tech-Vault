#AI 

**Byte-Pair Encoding**
- A tokenization algorithm that builds tokens from characters .a common method of tokenizing a corpus before an LLM can train on it.

**Corpus**
- The body it is trained on

**Tokenization**
- Splitting text into pieces (Tokens)

 **Token**
 - The pieces of a split string.
- Can be words or substrings.

**Vocabulary**
- All the tokens it can recognize

```python
# for example "unlockable" can have different tokekenizations
tokenizations = [
	["un", "lockable"],
	["unlock", "able"],
]
