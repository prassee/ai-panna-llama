# AI PANNA LLAMA - Lets Do AI with LLAMA

## Tech Stack

- LLAMA 2
- llama-cpp-python

## Stage

- Tested to generate column descriptions for the files listed on tablelist.txt
- Usage Example

```
cat tablelist.txt | xargs -0 python main.py "The following input lists tables and their respective columns starting from - char. Provide a relationship between these tables"  
```
