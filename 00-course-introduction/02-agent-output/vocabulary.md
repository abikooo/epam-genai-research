# GenAI vocabulary (20 terms for SMEs)

1. **Large Language Model (LLM)** — A neural network trained on large text corpora to predict and generate language. LLMs can be adapted to tasks like Q&A, summarization, and drafting.

2. **Prompt** — The input text (instructions + context) given to a model. Prompt wording and structure strongly influence output quality and safety.

3. **System prompt** — A high-priority instruction that sets the assistant’s role, rules, and boundaries. It is typically used to enforce policy, tone, and safety constraints.

4. **Context window** — The maximum amount of text (tokens) the model can consider at once. Longer conversations or documents may require summarization or chunking to fit.

5. **Token** — A unit of text used by models (often parts of words). Cost, latency, and context limits are usually measured in tokens.

6. **Temperature** — A decoding parameter that controls randomness in generation. Lower temperature is more deterministic; higher temperature yields more varied outputs.

7. **Top-p (nucleus sampling)** — A decoding method that samples from the smallest set of tokens whose probabilities sum to p. It’s another way to control creativity versus determinism.

8. **Hallucination** — When a model outputs confident but incorrect or unsupported information. Hallucinations are especially risky in high-stakes or regulated workflows.

9. **Retrieval-Augmented Generation (RAG)** — A pattern where the model retrieves relevant documents and uses them as grounded context for answering. RAG improves factuality and enables citation of sources.

10. **Embedding** — A numeric vector representation of text (or other data) capturing semantic similarity. Embeddings are commonly used for search, clustering, and retrieval.

11. **Vector database** — A datastore optimized for similarity search over embeddings. It supports fast retrieval of the most semantically similar chunks.

12. **Chunking** — Splitting long documents into smaller segments for indexing and retrieval. Good chunking improves recall and reduces irrelevant context.

13. **Fine-tuning** — Additional training on task- or domain-specific examples to adapt model behavior. It can improve style and task performance but requires careful data governance.

14. **Instruction tuning** — Training a model to follow human instructions more reliably. Many chat models are instruction-tuned for better task adherence.

15. **Reinforcement Learning from Human Feedback (RLHF)** — A technique where humans rank outputs and the model is optimized toward preferred responses. RLHF is often used to improve helpfulness and reduce unsafe behavior.

16. **Tool calling / function calling** — A capability where the model requests structured actions (e.g., call an API) instead of only generating text. This enables automation and access to real-time data.

17. **Agent** — A system that uses an LLM to plan and execute multi-step tasks, often via tools and memory. Agents can iterate, check results, and escalate when needed.

18. **Guardrails** — Controls that constrain model behavior (policy checks, allowed tools, content filters, validation rules). Guardrails help reduce safety, compliance, and quality risks.

19. **Prompt injection** — An attack where malicious content in user input or retrieved documents tries to override instructions or exfiltrate data. Defenses include strict tool permissions and content separation.

20. **Evaluation (evals)** — A repeatable method to measure model quality, safety, and latency using test sets and metrics. Evals help detect regressions and compare prompts/models objectively.
