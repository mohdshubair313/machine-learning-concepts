# AI Engineering Roadmap 2026
### Bina deep ML ke — basics se advanced tak, brick by brick

> Research base: [roadmap.sh/ai-engineer](https://roadmap.sh/ai-engineer) (197 topic nodes ka poora tree padha), YouTube video "6-Month Roadmap to Become an AI Engineer", Chip Huyen ki *AI Engineering* (O'Reilly, 2025) — ye field ki most-cited framework hai — aur AI Engineer World's Fair 2026 ke trend reports.

---

## 🎯 Sabse pehle: tumhara instinct sahi hai

roadmap.sh khud apni official definition mein likhta hai:

> "An AI Engineer uses pre-trained models and existing AI tools to improve user experiences... without building models from scratch. This is different from AI Researchers and ML Engineers, who focus more on creating new models."

Chip Huyen (ye field ki sabse authoritative voice hai — unhone *Designing ML Systems* aur *AI Engineering* dono likhi hain) isko aur crisp karti hain: **ML Engineering** = tum khud model banate/train karte ho (data, features, training loop, tumhara). **AI Engineering** = koi aur (OpenAI/Anthropic/Google) ne model bana diya, tum usko product mein use karte ho — prompting, context, retrieval, evaluation ke through.

**Matlab:** AI Engineering ka 90%+ kaam pure **software engineering + API integration + system design** hai. Isliye tumhara plan — ML side by side karne ki jagah AI engineering ko apna base bana lo — sahi direction hai.

---

## 🔶 ML kahan-kahan zaroori padega (sirf 5 jagah, wo bhi halka)

Poore roadmap mein maine har jagah ML ki zaroorat check ki hai. Yahi wo 5 spots hain jaha thoda conceptual ML samajhna help karta hai — inko maine niche bhi 🔶 se mark kiya hai jaha wo aayenge:

| # | Kahan | Kitna deep chahiye | Kab zaroori |
|---|-------|---------------------|--------------|
| 1 | **LLMs kaise kaam karte hain** (transformer, next-token prediction) | Sirf conceptual — koi math/backprop implement nahi karna | Phase 1 mein, ek baar samajh lo, kaafi hai |
| 2 | **Embeddings & similarity** (cosine similarity ka intuition) | Bahut halka — "similar meaning = closer vectors" bas itna | RAG banate waqt (Phase 4) |
| 3 | **Evaluation metrics** (precision/recall, statistical significance) | Halka stats — school-level | Evals banate waqt (Phase 6) |
| 4 | **Fine-tuning** (LoRA/QLoRA, overfitting, loss curve padhna) | Medium — par optional | Sirf tab jab prompting + RAG dono fail ho jaye (rare, Phase 8) |
| 5 | **Classical ML side-tasks** (classifiers, recommendation systems, anomaly detection) | Full ML (scikit-learn level) | Sirf kuch specific AI-engineer roles mein aata hai — core nahi hai |

**Baaki sab kuch — prompting, context engineering, RAG, agents, MCP, evals, deployment — zero ML background maangta hai.** Jaha bhi 🔶 nahi likha, wahan ML ki zaroorat hi nahi hai.

---

## 🧱 Phase 0 — Prerequisites (Non-ML), ~1-2 hafte

Ye already tumhare paas ho sakta hai — ek baar check kar lo:

- [ ] **Python (intermediate)** — functions, classes, list/dict comprehensions, `async`/`await` (LLM API calls mostly async hote hain), virtual environments, pip
- [ ] **Async Python deep** — `asyncio`, `aiohttp`, concurrent API calls, `asyncio.gather()`, semaphores se rate-limiting. LLM API calls 2-30 seconds lete hain — agar synchronous karo toh app crawl karega. Ye AI engineering mein daily kaam aata hai.
- [ ] **REST APIs samajhna** — HTTP methods, JSON, headers, status codes, API keys ko env variables mein rakhna (`.env` files)
- [ ] **Secret management** — `.env` files + `python-dotenv`, `.gitignore` mein `.env` dalna (ek baar API key GitHub pe leak hui = bill thousands mein). Production mein: environment variables, secret managers (AWS Secrets Manager, HashiCorp Vault) ka awareness.
- [ ] **Git & GitHub** — commit, branch, PR (portfolio projects yahi dikhoge)
- [ ] **Command line basics** — cd, ls, running scripts
- [ ] *(Nice to have)* Docker basics — later deployment mein kaam aayega
- [ ] **Data cleaning & preprocessing basics** — missing values handle karna, text cleaning (deduplication, formatting normalization), CSV/JSON parse karna. ML aur RAG dono mein "garbage in = garbage out" rule lagta hai — data quality > model choice.

### 🔶 Math Foundations — Minimum Viable Math (ML seekh rahe ho toh zaroori)

Bina math ke ML concepts "magic" lagenge. Ye minimum hai jo samajhna chahiye:

- [ ] **Linear Algebra (halka)** — vectors, matrices, matrix multiplication, dot product. Intuition: data ko numbers ke arrays mein represent karna. *Resource: 3Blue1Brown — Essence of Linear Algebra (YouTube, free)*
- [ ] **Calculus (halka)** — derivatives, partial derivatives, gradients, chain rule. Intuition: gradient descent kaise "seekhta" hai — loss function ka minimum kaise dhundhta hai. *Resource: 3Blue1Brown — Essence of Calculus*
- [ ] **Probability & Statistics (halka)** — distributions (Normal/Gaussian, Bernoulli), Bayes theorem, conditional probability, mean/variance/standard deviation, correlation vs causation. *Resource: StatQuest with Josh Starmer (YouTube, free)*
- [ ] **Practical approach:** Pure math theory mein mat doobe — concept seekho, phir turant code mein dekho (e.g., "chain rule kaise backpropagation mein kaam karti hai?"). NumPy se implement karo.

---

## Phase 1 — LLM Fundamentals (~1 hafta)

**Kya seekhna hai:**
- [ ] LLM kya hota hai — training data se next-token prediction tak 🔶 *(conceptual only)*
- [ ] Tokens & tokenization — LLM text ko kaise "dekhta" hai
- [ ] Context window — kitna text ek baar mein model ko de sakte ho
- [ ] Base models vs Instruct/Chat models
- [ ] Open-source vs closed-source models (trade-offs: cost, control, quality)
- [ ] Sampling parameters: temperature, top-p, top-k, repetition penalty — output ko control karna
- [ ] Sahi model kaise choose kare (task, cost, latency, context length ke basis pe)

**Model providers jo try karne hain:**
- [ ] OpenAI (GPT series) — API + Playground
- [ ] Anthropic Claude — API + Console
- [ ] Google Gemini
- [ ] Open-source route: Hugging Face, Ollama (local models chalana), LM Studio
- [ ] Ek baar OpenRouter dekh lo — ek hi API se multiple providers try kar sakte ho

**Mini project:** Ek CLI script banao jo 3 alag providers (OpenAI/Claude/Gemini) se same prompt ka response le aur compare kare.

---

## Phase 2 — Prompt Engineering (~1-2 hafte)

Ye tumhara sabse practical, roz-kaam-aane-wala skill hai.

**Kya seekhna hai:**
- [ ] System prompts, role & behavior design
- [ ] Zero-shot vs Few-shot prompting
- [ ] Chain-of-Thought (CoT) — model ko "step by step socho" bolna
- [ ] ReAct prompting (Reason + Act pattern — agents ki base hai, Phase 5 mein wapas aayega)
- [ ] Structured output — model se JSON/schema-locked output nikalwana
- [ ] **JSON mode vs Tool use vs Structured output — ye 3 alag cheezein hain** — beginners confuse karte hain. JSON mode ≠ function calling ≠ response_format. Provider-specific differences samajhna (OpenAI ka JSON mode ≠ Claude ka).
- [ ] **Structured output validation stack** — sirf prompt se structure enforce karna fragile hai. Production pattern:
  - Schema design (Pydantic models, enums for constrained values)
  - **Instructor library** / PydanticAI — auto-retry on validation failure ("fix-and-reask" loop)
  - **Outlines library** (awareness) — decode-time constraints, invalid tokens generate hi nahi ho sakte
  - "Validation Sandwich" pattern: schema → constrained generation → post-validation → retry
- [ ] Constraining inputs/outputs (guardrails ka basic form)
- [ ] Prompt injection — kya hota hai, kaise dhyan rakhna hai (security, Phase 9 mein detail)
- [ ] Prompt caching — repeated context ko cache karke cost/latency kam karna

**Mini project:** Ek "structured data extractor" banao — messy text (jaise resume ya email) do, clean JSON wapas nikalwao, Pydantic se schema validate karo, aur invalid output pe auto-retry implement karo (Instructor library try karo).

---

## Phase 3 — Context Engineering (~1 hafta) 🔥 *2026 ka sabse bada shift*

2025 tak baat "prompt engineering" ki thi. 2026 mein industry ka consensus hai: **context engineering** asli discipline ban gaya hai. Anthropic ka apna engineering blog isko define karta hai as — model ko sabse chhota, high-signal set of tokens dena jo best outcome de, na ki context window ko sab kuch bhar dena.

**Kya seekhna hai:**
- [ ] Prompt engineering vs Context engineering — farak samajhna
- [ ] Context window management — kya include kare, kya chhodo
- [ ] Context compaction/compression — lambi conversations ko summarize karna
- [ ] Context failure modes — "lost in the middle" problem (context jitna bada, model utna hi beech ka data miss karta hai)
- [ ] Memory systems — short-term (session) vs long-term (external/persistent) memory
- [ ] Multi-agent context sharing — jab multiple agents kaam kar rahe ho, context kaise share ho
- [ ] Context security & isolation — untrusted content agent ko confuse na kare

**Resource:** Anthropic ka article "Effective context engineering for AI agents" — ye is topic ka reference-standard hai.

---

## Phase 4 — RAG (Retrieval-Augmented Generation) (~2 hafte)

Ye wo skill hai jisse tum LLM ko **apna data** ya **latest data** ke saath jawab dilwate ho (jo training data mein nahi tha).

**Kya seekhna hai:**
- [ ] Embeddings kya hote hain 🔶 *(halka — "similar text = similar vector", cosine similarity ka intuition, math derive nahi karna)*
- [ ] **Chunking strategies — deep dive** — ye RAG quality ka #1 factor hai:
  - Fixed-size chunking vs Recursive character splitting vs Semantic chunking
  - **Overlap strategy** — chunks ke beech overlap rakhna (context continuity ke liye)
  - **Metadata preservation** — har chunk ke saath source doc, page number, section heading store karna (citations ke liye zaroori)
- [ ] Indexing & retrieval process
- [ ] Semantic search / similarity search
- [ ] **Hybrid search** — sirf vector/semantic search enough nahi hota. Keyword search (BM25) + Semantic search combine karna significantly better results deta hai. Most production RAG systems hybrid use karte hain.
- [ ] **Reranking** — retrieval ke baad results ko rerank karna. Initial retrieval recall optimize karta hai (zyada docs lao), reranking precision optimize karta hai (sabse relevant top pe). Tools: Cohere Rerank API, cross-encoder models (sentence-transformers). Ye ek line of code se RAG quality dramatically improve karta hai.
- [ ] Vector databases — Pinecone, Qdrant, Chroma, Weaviate, FAISS, LanceDB, MongoDB Atlas (kisi ek se shuru karo — Chroma sabse easy hai local ke liye)
- [ ] RAG vs Fine-tuning — kab kaunsa use kare (RAG = dynamic/fresh knowledge; fine-tuning = static behavior change)
- [ ] Frameworks: LangChain, LlamaIndex, Haystack (koi ek seekh lo, sab similar concepts hain)
- [ ] 🔥 *2026 trend:* **GraphRAG** — sirf vector search enterprise-grade knowledge assistants ke liye kaafi nahi hai; retrieval ab ek graph problem bhi maana ja raha hai. Basic RAG ke baad iska awareness rakhna.

**Mini project:** Apne college notes/PDFs pe ek "chat with your documents" app banao (RAG + citations dikhao ki answer kis page se aaya).

---

## Phase 5 — AI Agents & MCP (~2-3 hafte) 🔥 *sabse hot area abhi*

**Kya seekhna hai:**
- [ ] AI Agent kya hota hai — perceive → decide → act loop
- [ ] Function calling / tool use — LLM ko external tools (calculator, search, DB) use karna sikhana
- [ ] Multi-agent systems — multiple agents ek problem pe kaam karein
- [ ] Agent frameworks — koi ek try karo: OpenAI AgentKit/Agents SDK, Claude Agent SDK, Google ADK, ya LangChain/LangGraph agents
- [ ] **Model Context Protocol (MCP)** — ye 2026 ka standard ban chuka hai tools ko agents se connect karne ke liye
  - [ ] MCP client vs MCP server vs MCP host — samajhna
  - [ ] Ek chhota MCP server khud banake dekhna
  - [ ] Local vs remote server se connect karna
- [ ] 🔥 **Agent Skills** (Anthropic ne popularize kiya) — markdown files jo agent ko workflows/best-practices sikhate hain, bina orchestration code likhe. Industry isko "skills > tools" shift bol rahi hai abhi.
- [ ] **Agentic memory patterns** — agents bina memory ke har conversation fresh start karte hain. Samajhna:
  - **Short-term memory** — conversation buffer (current session ka context)
  - **Long-term memory** — vector DB based persistent memory (past sessions yaad rakhna)
  - **Working memory / Scratchpad** — multi-step reasoning ke liye temporary notes (agent apne intermediate results track kare)

**Mini project:** Ek agent banao jo web search + calculator + apna RAG tool — teeno use kar sake, aur ek MCP server bhi khud implement karo.

---

## Phase 6 — Evaluation & Observability (~1-2 hafte) — mostly log kiya jaata hai, mat karna

Beginners isko skip kar dete hain, lekin production mein yahi sabse zaroori hai — LLM outputs non-deterministic hote hain, isliye "vibes se check karna" kaam nahi karta.

**Kya seekhna hai:**
- [ ] Evaluation metrics — accuracy jaisa simple nahi hota generative output ke liye 🔶 *(precision/recall, statistical significance — halka stats)*
- [ ] Human evals vs Model-based evals (LLM-as-judge) vs Deterministic evals
- [ ] Regression testing — naya prompt/model version purane se better hai ya worse, kaise test kare
- [ ] Cost & latency monitoring
- [ ] **Hallucination detection & grounding** — ye 2026 ka #1 production problem hai. "Hallucination" ek single cheez nahi — 4 types samajhna:
  - **Factual hallucination** — real-world facts se contradict kare
  - **Grounding hallucination** — RAG context mein jo diya woh ignore karke kuch aur bole
  - **Citation hallucination** — fake sources/references generate kare
  - **Reasoning hallucination** — answer sahi dikhe but logic chain flawed ho
  - Detection techniques: NLI (Natural Language Inference) based checking, LLM-as-judge with consensus (ChainPoll), claim-level entailment scoring
- [ ] **Debugging LLM apps** — traditional debugging kaam nahi karta non-deterministic outputs pe. Trace-based debugging seekhna:
  - Input → reasoning → output chain ko trace karna (har step dekhna)
  - "Vibes" se "scientific debugging" — trace tools se root cause find karna
  - Observability tools (Langfuse, LangSmith) se traces dekhna aur failure patterns identify karna
- [ ] Tools: Ragas, DeepEval (eval frameworks), Langfuse, LangSmith, Helicone, Arize AI (observability/tracing)

**Mini project:** Apne Phase 4 ke RAG app ke liye ek eval suite banao — 20 test questions, expected answers, automatic scoring, **aur hallucination detection bhi add karo** (grounding check: answer RAG context se aaya ya model ne khud bana diya?).

---

## Phase 7 — Multimodal AI (~1 hafta)

- [ ] Image generation (DALL-E API, Gemini/Nano Banana image APIs)
- [ ] Image understanding / vision APIs (model ko image dikhana aur samjhwana)
- [ ] Audio: Speech-to-text (Whisper API), Text-to-speech
- [ ] Video understanding (basic awareness, less commonly needed)

**Mini project:** Ek voice-in, voice-out assistant — audio → Whisper → LLM → TTS pipeline.

---

## Phase 8 — Fine-tuning (~optional, tab karo jab zaroorat pade) 🔶 *sabse zyada ML yahan hai*

Ye AI engineering roadmap ka sabse "ML-heavy" hissa hai — par isko **sabse aakhri me, aur optional** rakha hai, kyunki zyadatar real-world problems prompt engineering + RAG se hi solve ho jaate hain.

**Kya seekhna hai (jab zaroorat pade tab):**
- [ ] Fine-tuning kya hota hai aur kab RAG se better hai (rare cases — jaise specific tone/format consistently chahiye)
- [ ] Parameter-efficient fine-tuning — LoRA/QLoRA (concept level: pura model retrain nahi, chhota adapter train hota hai)
- [ ] Overfitting, loss curve padhna — bas itna ki pata chale training sahi chal rahi hai ya nahi

**Note:** Managed fine-tuning services (OpenAI/Google ke fine-tuning APIs) use karte waqt bhi tumhe gradient descent implement nahi karna padta — bas data prepare karna aata hona chahiye. Deep dive tabhi karo jab koi real project isko demand kare.

---

## Phase 9 — Security, Safety & Guardrails (~1 hafta)

- [ ] Prompt injection attacks — attack patterns samajhna (Phase 2 mein basic cover ho chuka, ab depth)
- [ ] Adversarial testing / red-teaming apne app ka
- [ ] Content moderation APIs
- [ ] Bias & fairness, AI safety & ethics — awareness level
- [ ] Data classification & privacy (especially agar enterprise/healthcare/finance data touch kar rahe ho)

---

## Phase 10 — Production, Deployment & Dev Tools (~1-2 hafte)

- [ ] Apne AI app ko API ke peeche wrap karna (FastAPI jaisa kuch)
- [ ] Streaming responses (LLM output token-by-token frontend pe dikhana)
- [ ] Basic Docker deployment, ek cloud provider (AWS/GCP/Azure — koi ek basics)
- [ ] 🔥 **Coding agents** — Claude Code, Cursor, Codex, Gemini CLI, Windsurf — 2026 mein AI engineers khud in tools se apna dev workflow tez karte hain. In sabko try karo, apna workflow inke around banao.
- [ ] **Error handling, retries & fallbacks** — LLM API calls fail hote hain (rate limits, timeouts, model overload). Production must-haves:
  - Retry with exponential backoff (pehli baar fail → 1s wait → retry → 2s wait → retry...)
  - **Multi-provider fallback** — OpenAI down? Auto-switch to Claude/Gemini. Tools: LiteLLM, Portkey
  - Graceful degradation — agar sab fail ho jaye toh user ko friendly error dikhana, app crash nahi hona chahiye
- [ ] **Cost optimization & API economics** — production mein LLM costs bahut fast blow up hote hain:
  - Token-level cost tracking, per-request cost attribution
  - **Model routing/cascading** — simple queries → cheap/fast model (GPT-4o-mini, Flash), complex reasoning → frontier model. Ye alone 50-70% cost save karta hai
  - **Batch APIs** — non-realtime tasks (summarization, data extraction) pe 50%+ discount milta hai
  - **Prompt caching** — large system prompts cache karna (providers natively support karte hain, 90% input cost reduction)
  - **Semantic caching** — similar queries ka response cache karna (Redis + embeddings se)
- [ ] **Rate limiting your own API** — jab tum AI app deploy karo, users ke liye rate limiting lagani padegi. Token buckets, per-user quotas, abuse prevention.
- [ ] **AI Gateway (awareness)** — LiteLLM, Portkey jaisi tools ek centralized control plane deti hain: routing, caching, cost tracking, fallbacks — sab ek jagah. Production mein increasingly standard ban raha hai.

---

## 🔥 Phase 11 — 2026 ke Cutting-Edge Trends (jab base strong ho jaye)

Ye sab abhi industry mein active discussion hai (AI Engineer World's Fair 2026 se) — inko last mein, awareness ke liye:

- **Harness/Loop engineering** — agent "inner loop" mein kaam karta hai (execution), engineer "outer loop" mein rehta hai (direction, evaluation, decisions). Poori autonomy abhi unreliable maani ja rahi hai.
- **Skill engineering** — agents ke liye reusable "skills" (markdown-based workflows) design karna apne aap mein ek skill ban raha hai
- **Software factories** — companies multiple long-running agents ko parallel manage kar rahi hain, engineer "orchestrator" ban raha hai
- **Forward Deployed Engineer (FDE)** — naya role jaha AI engineers directly enterprise customers ke saath baithke unke system mein AI integrate karte hain
- **Verifiable rewards / RL for agents** — open-ended prompts se hatke, strict programmatic rubrics se agent reasoning train ho raha hai (ye deep ML/research side hai — sirf awareness ke liye, core skill nahi)

---

## 🔶 ML Learning Track — Parallel Path (ML seekh rahe ho toh ye follow karo)

Ye section specifically un logon ke liye hai jo **AI Engineering ke saath-saath ML bhi seekh rahe hain**. Ye main roadmap ka part nahi hai — ye ek parallel track hai jo tumhare ML concepts strong karega. Phase 0 mein math foundations already cover ho chuke hain, ye usse aage ka hai.

### ML Track 1 — Data Preprocessing & Feature Engineering 🔶
- [ ] **Data cleaning** — missing values handle karna (mean/median imputation, dropping rows), outlier detection & treatment, duplicate removal
- [ ] **Feature scaling** — Normalization (0-1 range) vs Standardization (mean=0, std=1) — kab kaunsa use kare
- [ ] **Encoding categorical variables** — One-hot encoding, Label encoding, Ordinal encoding — farak samajhna
- [ ] **Feature creation** — existing features combine karke naye informative features banana (e.g., age + income → spending_power)
- [ ] **Feature selection** — correlation analysis, feature importance (tree-based models se), dimensionality reduction (PCA awareness)
- [ ] **"ML mein 80% time data prep mein jaata hai"** — ye real hai. Model selection secondary hai, data quality primary.

### ML Track 2 — Core ML Concepts 🔶
- [ ] **Bias-Variance Tradeoff** — ML ka sabse fundamental concept:
  - Underfitting (high bias) — model too simple, patterns miss karta hai
  - Overfitting (high variance) — model training data memorize kar leta hai, new data pe fail
  - Diagnosis: training error vs validation error curves dekhna
  - Fix: more data, regularization, model complexity adjust karna
- [ ] **Cross-Validation** — single train/test split unreliable hota hai:
  - K-Fold cross validation (data ko K parts mein baanto, K baar train/test)
  - Stratified K-Fold (classification ke liye — har fold mein class ratio same rakho)
  - "My model has 95% accuracy" meaningless ho sakta hai bina proper cross-validation ke
- [ ] **Regularization** — overfitting rokne ka primary technique:
  - L1 (Lasso) — feature selection bhi karta hai (unnecessary features ki weight zero kar deta hai)
  - L2 (Ridge) — weights ko chhota rakhta hai (penalty deta hai bade weights ko)
  - Dropout (Deep Learning mein) — random neurons off karna training mein
  - Early Stopping — jab validation error badhne lage, training rok do

### ML Track 3 — Classical ML Algorithms 🔶
**Supervised Learning (labeled data se seekhna):**
- [ ] Linear Regression — continuous output predict karna (e.g., house price)
- [ ] Logistic Regression — binary classification (e.g., spam/not-spam)
- [ ] Decision Trees — if-else rules ka tree, interpretable
- [ ] Random Forest — multiple decision trees ka ensemble (bagging)
- [ ] Gradient Boosting — XGBoost / LightGBM — kaggle competitions ka king, tabular data pe best performer
- [ ] SVM (Support Vector Machines) — awareness level
- [ ] KNN (K-Nearest Neighbors) — simple, intuitive, baseline ke liye

**Unsupervised Learning (bina labels ke patterns dhundhna):**
- [ ] K-Means Clustering — data ko groups mein baantna
- [ ] PCA (Principal Component Analysis) — dimensions reduce karna (100 features → 10 important ones)
- [ ] DBSCAN — density-based clustering (awareness)

**Practical:**
- [ ] **scikit-learn** proficiency — ye ML ka "React" hai. Is ek library se 90% classical ML kaam ho jaata hai
- [ ] **When to use what** — problem type → algorithm selection (regression? classification? clustering?)

### ML Track 4 — Model Evaluation Metrics 🔶
**Classification metrics:**
- [ ] Confusion Matrix — TP, TN, FP, FN samajhna
- [ ] Precision — predicted positives mein se kitne sahi the
- [ ] Recall — actual positives mein se kitne pakde gaye
- [ ] F1-Score — precision aur recall ka harmonic mean (imbalanced data pe accuracy se better)
- [ ] ROC-AUC — model kitna achha positive/negative distinguish karta hai
- [ ] **"95% accuracy" trap** — agar 95% data ek class ka hai, toh model "sab same class" bol ke bhi 95% accuracy de dega. Isliye F1/AUC zaroori hai.

**Regression metrics:**
- [ ] MAE (Mean Absolute Error), MSE (Mean Squared Error), RMSE
- [ ] R² (R-squared) — model kitna variance explain karta hai

### ML Track 5 — Experiment Tracking & MLOps Basics 🔶
- [ ] **Experiment tracking** — hyperparameters, metrics, model versions track karna. Bina iske "which configuration was best?" ka answer kabhi nahi milega.
  - Tools: **MLflow** (open source, sabse popular), **Weights & Biases (W&B)** (best UI/UX)
- [ ] **Model versioning** — kaunsa model kab train hua, kis data pe, kya results the — sab log hona chahiye
- [ ] **MLOps awareness** — model drift kya hota hai (production mein model performance slowly degrade hona), data drift, concept drift — sirf awareness level

**Mini project (ML Track):** Kaggle pe ek tabular dataset lo (Titanic, House Prices), scikit-learn se 3-4 algorithms try karo, cross-validation karo, metrics compare karo, aur MLflow/W&B se experiments track karo.

---

## 📅 Suggested Timeline (~4-5 mahine, moderate pace)

| Hafte | Phase |
|-------|-------|
| 1 | Prerequisites check + Phase 1 (LLM Fundamentals) |
| 2-3 | Phase 2 (Prompt Engineering) |
| 4 | Phase 3 (Context Engineering) |
| 5-6 | Phase 4 (RAG) |
| 7-9 | Phase 5 (Agents & MCP) — sabse zyada time do isko |
| 10-11 | Phase 6 (Evaluation & Observability) |
| 12 | Phase 7 (Multimodal) |
| 13 | Phase 9 (Security) |
| 14-15 | Phase 10 (Production & Deployment) |
| 16+ | Phase 8 (Fine-tuning, agar zaroorat pade) + Phase 11 (trends) + portfolio polish |

---

## 🏗️ Portfolio Projects (in order of difficulty)

1. **Multi-provider prompt playground** — Phase 1-2
2. **Structured data extractor** — resume/invoice parser with JSON schema validation — Phase 2
3. **"Chat with your PDFs"** — full RAG app with citations — Phase 4
4. **Tool-using agent** — apna MCP server + agent jo web search, calculator, RAG sab use kare — Phase 5
5. **Eval-driven RAG/agent** — apne project #3 ya #4 ke upar ek proper eval suite + observability dashboard — Phase 6
6. **End-to-end deployed app** — koi bhi upar wala project, Dockerized, cloud pe live, streaming UI ke saath — Phase 10

Ye 6 projects hi tumhara solid GitHub portfolio ban jayega.

---

## 📚 Best Resources (curated)

**AI Engineering:**
- **[roadmap.sh/ai-engineer](https://roadmap.sh/ai-engineer)** — visual roadmap, isi se topic tree liya hai
- **Chip Huyen — *AI Engineering: Building Applications with Foundation Models*** (O'Reilly, 2025) — field ki most authoritative book. GitHub companion: [github.com/chiphuyen/aie-book](https://github.com/chiphuyen/aie-book) (free resources)
- **[modelcontextprotocol.io](https://modelcontextprotocol.io/)** — MCP official docs
- **Hugging Face MCP Course** (free) — huggingface.co/learn/mcp-course
- **Anthropic Engineering Blog** — "Effective context engineering for AI agents"
- **[Instructor library docs](https://python.useinstructor.com/)** — structured output validation ka industry standard
- Video jo tumne diya (KtHdbzChVWo) — practical 6-month structure ke liye achha hai, isi roadmap ke saath cross-check kiya hai

**ML & Math (ML Track ke liye):**
- **3Blue1Brown** (YouTube) — *Essence of Linear Algebra* aur *Essence of Calculus* — math ka visual intuition build karne ke liye best resource in the world
- **StatQuest with Josh Starmer** (YouTube) — ML concepts ko simple language mein todke samjhata hai — bias-variance, cross-validation, regularization sab yahan se seekho
- **[scikit-learn documentation](https://scikit-learn.org/)** — ML algorithms ka practical reference + excellent tutorials section
- **Andrew Ng — Machine Learning Specialization** (Coursera) — ML fundamentals ka gold standard course
- **Kaggle Learn** (free micro-courses) — Python, Pandas, ML intro, Feature Engineering — hands-on seekhne ke liye

---

## ✅ Bottom line

Tumhara plan sahi hai — AI Engineering ek pura career path hai jisme deep ML zaroori nahi. Jaha-jaha 🔶 hai, wahi discuss karne layak hai; baaki sab pure application-building skill hai jo tum abhi se, ML seekhe bina, shuru kar sakte ho.

Aur kyunki tum ML bhi seekh rahe ho — **ML Learning Track** (🔶 section) ko AI roadmap ke parallel follow karo. Ye dono paths ek dusre ko strengthen karte hain: ML concepts fine-tuning, evals, aur embeddings mein kaam aayenge, aur AI engineering ka practical exposure ML concepts ko "real" bana dega.
