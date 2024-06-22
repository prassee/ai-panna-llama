from llama_cpp import Llama
import sys

llm = Llama(
    model_path="/data/llmworkspace/llama-2-7b-chat.Q4_K_M.gguf",
    n_ctx=2048,
    n_threads=4,
    n_threads_batch=4,
    n_gpu_layers=0,
)
context = sys.argv[1]
question = sys.argv[2]
output = llm(
    f"Q: {context} ... {question}  A:",
    max_tokens=4096,
    temperature=0.8,
    # stop=["Q:", "\n"],
    # echo=True,
)

# output = llm.create_chat_completion(
#     messages=[
#         {
#             "role": "system",
#             "content": "You are a Data Modelling Specialist. Given a list of columns from a table. Provide descrtion for each column. The columns are separated by line breaks",
#         },
#         {"role": "user", "content": f"{question}"},
#     ],
#     response_format={"type": "json_object"},
#     temperature=0.3,
# )

print(output)
