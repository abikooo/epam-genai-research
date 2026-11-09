# Generative AI applications: research report

## 1. Code generation

Developers use generative models to write functions, fix bugs, explain unfamiliar code and draft tests. The clearest evidence for the business value is a set of three field experiments at Microsoft, Accenture and a Fortune 100 company, covering 4,867 developers. Those with an AI coding assistant completed 26.08% more tasks (standard error 10.3%) ([Cui et al., Management Science, 2025](https://papers.ssrn.com/abstract=4945566)). The tool tested was GitHub Copilot's code completion, and the figure counts completed tasks, not time saved.

The technical challenge is context. The code has to fit an existing codebase, including its architecture, dependencies and APIs across many files, without breaking what already works. The weak point is that developers understand AI-assisted code less well. In a controlled experiment with 69 participants, mostly students, those using AI were 12.5% worse at answering technical questions about the code they had written ([More Code, Less Understanding?, IEEE Transactions on Software Engineering, 2026](https://sscalabrino.github.io/files/2026/TSE2026MoreCodeLess.pdf)). The sample is small, so it works better as a warning than as a measurement.

Existing implementations:
- [Claude Code](https://claude.com/product/claude-code): Anthropic's coding agent that reads a codebase, edits files, runs commands and tests, and works from the terminal, an IDE or the web.
- [OpenAI Codex](https://openai.com/codex): OpenAI's coding agent that handles features, refactors and code review, and can run several tasks in parallel.
- [Cursor](https://cursor.com): a code editor with built-in AI that generates, edits and debugs code using context from the whole project.

## 2. Customer support chatbots

Support teams use generative models to suggest replies to agents and to answer customers directly. In a study of 5,172 support agents at a Fortune 500 software company, access to an AI assistant raised the number of issues resolved per hour by 15% on average ([Brynjolfsson, Li and Raymond, Quarterly Journal of Economics, 2025](https://arxiv.org/abs/2304.11771)). The assistant suggested replies to human agents and did not talk to customers itself, so the figure does not describe a fully autonomous chatbot.

The technical challenge is resolving multi-turn requests using company-specific knowledge, customer records and live business systems, while keeping the conversation context and handing off to a person at the right moment. The weak point is wrong answers about products or policies. A survey of 274 potential users by SINTEF researchers found that hallucinations can undermine trust, especially when the mistake has negative consequences for the customer ([SINTEF, 2025](https://www.sintef.no/en/publications/publication/10283331/)). It measures what users say they would feel, not what they do.

Existing implementations:
- [Fin](https://fin.ai): AI customer service agent, formerly Intercom's and now owned by Salesforce, that resolves support requests across chat, email and voice.
- [Ada](https://www.ada.cx): AI customer service platform that automates conversations and troubleshooting across channels and languages.
- [Zendesk AI agents](https://www.zendesk.com): AI agents built into Zendesk's support platform that resolve tickets and hand off to people.

## 3. Enterprise search and document question answering (RAG)

These systems retrieve passages from a company's documents and have a model write an answer with citations. The value is the time employees lose looking for information spread across wikis, drives and ticketing tools. No independent study isolating the productivity gain of RAG search was found, so this report gives no figure.

The technical challenge is retrieving the right and complete evidence from large, fragmented collections, with access permissions, ambiguous queries and content that keeps changing. An experience report on three RAG deployments (research, education and biomedical) lists seven failure points, among them missing content, relevant documents ranked too low, and answers that sit in the retrieved text but are not extracted. It concludes that a system can only be validated while it runs ([Barnett et al., 2024](https://arxiv.org/abs/2401.05856)). The weak point is that retrieval does not remove hallucination. A Stanford evaluation of RAG-based legal research tools from LexisNexis and Thomson Reuters found that each hallucinated between 17% and 33% of the time ([Magesh et al., Journal of Empirical Legal Studies, 2025](https://arxiv.org/abs/2405.20362)). That evidence comes from legal research, not from enterprise search in general.

Existing implementations:
- [Glean](https://www.glean.com): connects a company's apps and document stores so employees can search and get answers with citations and permission controls.
- [Coveo](https://www.coveo.com): relevance platform that retrieves enterprise content and generates answers with citations linking back to the source documents.
- [Agent Search](https://cloud.google.com/enterprise-search): Google Cloud's managed enterprise search, formerly Vertex AI Search, with built-in retrieval for grounded answers.

## 4. Marketing content generation

Marketing teams use generative models to draft copy, produce campaign variants and generate images and video. The business value is speed on routine writing. In a preregistered experiment with 453 college-educated professionals writing press releases and short reports, access to ChatGPT cut the average time taken by 40% and raised rated quality by 18% ([Noy and Zhang, Science, 2023](https://doi.org/10.1126/science.adh2586)). Image and video tools add faster asset production without waiting on a design queue.

The hard part is control. Output has to match a brand's voice, stay factually correct and avoid legal problems such as copyright and unapproved claims, so tools need brand guidelines, approval workflows and licensed training data. The weak points are sameness and accuracy. In a Science Advances experiment, stories written with AI ideas were rated as more creative individually but were more similar to each other than stories written without AI ([Doshi and Hauser, 2024](https://doi.org/10.1126/sciadv.adn5290)). The Noy and Zhang experiment did not fact-check the writing, so its speed gains say nothing about error rates.

Existing implementations:
- [Jasper](https://www.jasper.ai): marketing platform with brand voice controls and AI agents for campaign content.
- [Adobe Firefly](https://www.adobe.com/products/firefly.html): image, video and audio generation trained on licensed and public domain content, built into Adobe's creative apps.
- [Canva AI](https://www.canva.com/canva-ai): Canva's AI design and writing assistant, relaunched in 2026 as Canva AI 2.0.

## 5. Text-to-SQL and data analysis

Text-to-SQL tools let business users ask questions about company data in plain language and get back a query, a result and often a chart. The business value is fewer requests to the data team and faster answers. No independent study measuring that productivity gain was found, so this report gives no figure.

The technical challenge is scale and context. Spider 2.0 uses real enterprise databases with over 1,000 columns, several SQL dialects and documentation to consult. An agent built on o1-preview solved 21.3% of its tasks, against 91.2% on the older Spider 1.0 benchmark and 73.0% on BIRD ([Lei et al., ICLR 2025](https://arxiv.org/abs/2411.07763)). Those results come from 2024 models, so the current leaderboard should be checked. The weak point follows from this: a wrong query can look plausible and return a clean-looking wrong number. The products below reduce the risk by asking data teams to define a semantic model or curated space first, which moves the effort rather than removing it.

Existing implementations:
- [Snowflake Cortex Analyst](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst): natural language to SQL over Snowflake data, guided by a semantic model and verified queries.
- [Databricks Genie](https://docs.databricks.com/en/genie/index.html): conversational analytics on governed Databricks data through Genie Spaces and dashboards.
- [ThoughtSpot Spotter](https://www.thoughtspot.com): AI analyst that answers questions against cloud data warehouses and builds semantic models from prompts.

## 6. Automated test generation

Writing tests by hand is slow, and models can draft unit and end-to-end tests quickly. The best evidence comes from Meta's TestGen-LLM. In an evaluation on Instagram Reels and Stories, 75% of generated test cases built correctly, 57% passed reliably and 25% increased coverage. In Meta's test-a-thons, engineers accepted 73% of its recommendations for production ([Alshahwan et al., FSE 2024](https://arxiv.org/abs/2402.09171)). It is Meta's own tool and report, not an independent study.

The core technical challenge is the test oracle problem. A test is only useful if its expected values are right, and a model reading the code tends to assert what the code currently does. Meta handled this by filtering out tests that fail to build, pass unreliably or add no coverage. The weak point is that bugs can get locked in. A study on 24 open-source Java repositories found that LLMs have trouble telling actual from expected behavior when the code under test is buggy ([arXiv 2410.21136](https://arxiv.org/abs/2410.21136)), so human review stays necessary.

Existing implementations:
- [Diffblue Cover](https://diffblue.com/cover): generates and maintains Java unit tests using reinforcement learning rather than a prompt-driven LLM.
- [Qodo](https://www.qodo.ai): code review and test generation platform, formerly CodiumAI.
- [mabl](https://www.mabl.com): AI-native test automation for web, mobile and API tests, with generative test creation and self-healing.

## 7. Translation and localization

Language barriers limit sales, and automated translation lowers them. When eBay introduced machine translation, US exports to Spanish-speaking Latin American countries on the platform rose by 17.5% ([Brynjolfsson, Hui and Liu, Management Science, 2019](https://www.nber.org/papers/w24917)). That study covers neural machine translation from before large language models, but it shows the business value. Generative models add context-aware translation, tone control and glossary use.

The technical challenge is consistency. Terminology, tone and formatting have to hold across large volumes of content and fit into review workflows with translation memory and glossaries. The weak point is reliability outside major languages. A study of over 100 language pairs found hallucinated translations mainly in low-resource directions and when translating out of English ([Guerreiro et al., TACL, 2023](https://doi.org/10.1162/tacl_a_00615)). High-stakes content still needs a human reviewer.

Existing implementations:
- [DeepL](https://www.deepl.com): translation and writing platform built on its own language model, with voice translation and enterprise features.
- [Smartling](https://www.smartling.com): enterprise AI translation and localization platform, majority-owned by Vitruvian Partners since September 2026.
- [Lokalise](https://lokalise.com): localization platform for product teams that routes strings between AI models and scores translation quality automatically.

## 8. Workflow automation with AI agents

Agents take a goal and carry out steps across business apps, such as updating a CRM record, triaging email or filing a ticket. The business value is removing repetitive coordination work. No independent study quantifying that effect was found, so this report gives no figure.

The technical challenge is long multi-step work across many tools with the right permissions. TheAgentCompany benchmark has 175 tasks in a simulated software company. The best agent, built on Gemini 2.5 Pro, completed 30.3% of them autonomously. Simpler tasks were solved, while long ones were out of reach, and the models tested date from 2025 ([Xu et al., NeurIPS 2025](https://arxiv.org/abs/2412.14161)). The weak point is that agents act on real systems, so a wrong step has side effects. Platforms respond with human approval steps and run histories.

Existing implementations:
- [n8n](https://n8n.io): workflow automation platform with AI agent nodes, self-hosted or in the cloud.
- [Zapier](https://zapier.com): automation across thousands of apps, with AI steps inside Zaps since the standalone Agents product was folded into them in 2026.
- [Microsoft Copilot Studio](https://www.microsoft.com/en-us/microsoft-copilot/microsoft-copilot-studio): platform for building conversational and autonomous agents connected to business data and tools.