# Benchmark Suite & DSPy Prompt Optimization

## Goal

Optimize the `_PROMPT_FRAMING` text in `src/core/writer.py` so coding agents
consistently exhibit five target behaviors when the codebase map is in their
system prompt.

## Target Outcomes

1. **Trust** — agent navigates directly to file:line from the map, doesn't grep to verify
2. **Type consistency** — generated code uses correct types matching the symbol table
3. **Import correctness** — import paths resolve against the module structure in the map
4. **API contract adherence** — implementations include all required methods from hierarchies
5. **Pattern adherence** — new code follows naming, error handling, and structural conventions

## What Gets Optimized

The **prompt framing text only** — the markdown wrapper around the TOON block.
The TOON content itself (symbols, modules, hierarchies, deps) stays as-is.
DSPy iterates on the framing until the composite metric converges.

Current framing (~7 lines in `src/core/writer.py:27-37`):

```markdown
## Live Codebase Map

The following is a **real-time structural map** of this codebase. It was
regenerated moments ago and reflects the current state of all files on disk.

All file paths and line numbers are accurate right now. When you edit a file,
this map updates before your next turn.

Use this map to navigate directly to the right files and line numbers without
searching. Trust these locations — they are current.
```

---

## Architecture

```
tests/bench/
├── PLAN.md                 # this file
├── harness.py              # DSPy optimization loop (MIPROv2 + GEPA)
├── metrics.py              # composite metric + 5 sub-metrics
├── tasks.py                # 50 benchmark tasks with ground truth
├── judge.py                # LLM-as-judge DSPy signatures
├── repos.py                # clone/setup/teardown OSS repos
├── generate_fixtures.py    # run codebase-graph on repos, save .codebase.md
├── run_eval.py             # promptfoo regression runner
├── conftest.py             # shared pytest fixtures (optional)
├── prompts/
│   └── baseline.md         # current _PROMPT_FRAMING extracted
├── fixtures/               # pre-generated .codebase.md per repo
│   └── .gitkeep
├── results/                # optimization run outputs
│   └── .gitkeep
└── promptfoo.yaml          # regression test config (post-optimization)
```

---

## Phase 1: Benchmark Codebases

### Repos

| Repo | Language | Why |
|------|----------|-----|
| `tiangolo/fastapi` | Python | Type-heavy, clear modules, dataclass models |
| `expressjs/express` | JavaScript | Classic Node.js patterns, well-known structure |
| `solidjs/solid` | TypeScript | Complex type hierarchies, reactive patterns |
| `pallets/flask` | Python | Simpler structure, good contrast to FastAPI |

### repos.py

Handles clone → generate → cleanup:

```python
BENCHMARK_REPOS = [
    {"name": "fastapi", "url": "https://github.com/tiangolo/fastapi.git", "shallow": True},
    {"name": "express", "url": "https://github.com/expressjs/express.git", "shallow": True},
    {"name": "solid",   "url": "https://github.com/solidjs/solid.git",    "shallow": True},
    {"name": "flask",   "url": "https://github.com/pallets/flask.git",    "shallow": True},
]
```

- Shallow clone (`--depth 1`) to save time/space
- Run `codebase-graph` oneshot to generate `.codebase.md`
- Copy the generated file to `fixtures/{repo_name}.codebase.md`
- Delete the cloned repo

Pre-generated fixtures are committed to the repo so the bench runs fast
day-to-day. Re-generate with `python -m tests.bench.generate_fixtures`.

---

## Phase 2: Task Definitions (50 tasks)

### Data Model

```python
@dataclass
class GroundTruth:
    target_files: list[str]         # files the agent should reference
    target_symbols: list[str]       # symbol FQNs it should use
    required_types: list[str]       # types it must use correctly
    required_imports: list[str]     # import paths it must get right
    patterns: list[str]             # conventions it should follow
    anti_patterns: list[str]        # behaviors it should NOT exhibit

@dataclass
class BenchTask:
    id: str                         # e.g. "fastapi_trust_01"
    repo: str                       # benchmark codebase name
    category: str                   # trust|type|import|contract|pattern
    instruction: str                # what the "user" asks
    ground_truth: GroundTruth       # expected correct behavior
```

### Task Categories (10 per category)

**Trust (navigation) — 10 tasks**
Agent should go directly to file:line from the map, not search.

- "Where is the `Request` class defined?"
- "What methods does `APIRouter` have?"
- "Find the function that handles dependency injection"
- "What does the `Response` model look like?"
- etc.

Ground truth: specific file paths + line numbers from the .codebase.md.
Metric: deterministic (regex for file:line, anti-patterns for search language).

**Type consistency — 10 tasks**
Agent should use correct types from the symbol table.

- "Add a `deactivate` method to `User` that sets `is_active` to False"
- "Write a function that takes a `Request` and returns a `Response`"
- "Create a helper that validates an `OrderItem`'s price"
- etc.

Ground truth: type names + field names from symbol table.
Metric: check that generated code references types that exist in the map.

**Import correctness — 10 tasks**
Agent should import from the right modules.

- "Create a new endpoint file that uses `User` from the auth module"
- "Add a utility function that uses `Order` — show the import"
- "Import the `validate` function in a new file"
- etc.

Ground truth: correct import paths derived from module table.
Metric: parse imports from generated code, check against module paths.

**API contract adherence — 10 tasks**
Agent should implement required methods from interfaces/base classes.

- "Create a new class that extends `BaseModel`"
- "Implement the `Serializable` interface in a new class"
- "Add a new service that follows the `AuthService` pattern"
- etc.

Ground truth: required methods/fields from hierarchy table.
Metric: LLM-as-judge (does the implementation satisfy the contract?).

**Pattern adherence — 10 tasks**
Agent should follow existing conventions visible in the map.

- "Add a new route handler following the existing pattern"
- "Create a new data model following the project's conventions"
- "Write error handling for this endpoint"
- etc.

Ground truth: pattern descriptions extracted from codebase conventions.
Metric: LLM-as-judge (does the code match existing patterns?).

### Train/Dev Split

- **Train set:** 35 tasks (7 per category) — used by DSPy optimizer
- **Dev set:** 15 tasks (3 per category) — used for evaluation only

---

## Phase 3: Metrics

### Composite Metric

```python
def composite_metric(example, pred, trace=None):
    scores = {
        "trust":    trust_metric(example, pred),
        "type":     type_consistency_metric(example, pred),
        "import":   import_correctness_metric(example, pred),
        "contract": contract_adherence_metric(example, pred),
        "pattern":  pattern_adherence_metric(example, pred),
    }
    weights = {
        "trust": 0.30,       # foundational — everything depends on this
        "type": 0.20,
        "import": 0.20,
        "contract": 0.15,
        "pattern": 0.15,
    }
    return sum(scores[k] * weights[k] for k in scores)
```

### Sub-Metrics

**trust_metric (deterministic)**
```
+ 0.4  if response contains file path from ground_truth.target_files
+ 0.3  if response contains line number near ground_truth target
+ 0.3  if response does NOT contain anti_patterns:
       "let me search", "let me verify", "grep", "find", "I'll look for",
       "searching for", "scanning", "let me check"
```

**type_consistency_metric (deterministic + LLM-judge)**
```
+ 0.5  deterministic: do type names in generated code exist in symbol table?
+ 0.5  LLM-judge: "Does the generated code use the correct field names and
       types for the symbols referenced, according to the codebase map?"
```

**import_correctness_metric (deterministic)**
```
+ 0.5  import paths reference modules that exist in the module table
+ 0.3  imported symbols exist in the target module
+ 0.2  no circular dependency introduced
```

**contract_adherence_metric (LLM-judge)**
```
LLM-judge: "Given that {symbol} implements/extends {target} which requires
{methods}, does the generated code implement all required methods with
correct signatures?"
Score: 0.0 to 1.0
```

**pattern_adherence_metric (LLM-judge)**
```
LLM-judge: "Given the existing codebase patterns shown in the map
(naming conventions, error handling, return types, class structure),
does the generated code follow these conventions?"
Score: 0.0 to 1.0
```

### LLM-as-Judge (judge.py)

```python
class AssessTypeConsistency(dspy.Signature):
    """Assess whether generated code uses types consistent with the codebase map."""
    codebase_map: str = dspy.InputField()
    generated_code: str = dspy.InputField()
    ground_truth_types: str = dspy.InputField()
    score: float = dspy.OutputField(desc="0.0 to 1.0")
    reasoning: str = dspy.OutputField()

class AssessContractAdherence(dspy.Signature):
    """Assess whether generated code satisfies the interface/base class contract."""
    codebase_map: str = dspy.InputField()
    generated_code: str = dspy.InputField()
    contract_requirements: str = dspy.InputField()
    score: float = dspy.OutputField(desc="0.0 to 1.0")
    reasoning: str = dspy.OutputField()

class AssessPatternAdherence(dspy.Signature):
    """Assess whether generated code follows conventions from the codebase."""
    codebase_map: str = dspy.InputField()
    generated_code: str = dspy.InputField()
    pattern_description: str = dspy.InputField()
    score: float = dspy.OutputField(desc="0.0 to 1.0")
    reasoning: str = dspy.OutputField()
```

---

## Phase 4: DSPy Harness

### Program

```python
class CodebaseMapFraming(dspy.Signature):
    """Given a codebase structural map and a coding task, produce a response
    that navigates directly using the map data, maintains type consistency,
    uses correct imports, adheres to API contracts, and follows patterns."""

    codebase_map: str = dspy.InputField(desc="TOON-format codebase map with prompt framing")
    task: str = dspy.InputField(desc="coding task for the agent")
    response: str = dspy.OutputField(desc="agent response with code")
```

The docstring of this Signature IS the instruction that DSPy optimizes.

### Optimizers (run both, compare)

**MIPROv2** (battle-tested, 0-shot instruction optimization):
```python
mipro = dspy.MIPROv2(metric=composite_metric, auto="medium", num_threads=4)
optimized_mipro = mipro.compile(
    dspy.Predict(CodebaseMapFraming),
    trainset=train_tasks,
    max_bootstrapped_demos=0,
    max_labeled_demos=0,
)
```

**GEPA** (newer, reflective evolution, accepts textual feedback):
```python
gepa = dspy.GEPA(
    metric=composite_metric_with_feedback,
    auto="medium",
    reflection_lm=dspy.LM("openrouter/anthropic/claude-sonnet-4-20250514"),
)
optimized_gepa = gepa.compile(dspy.Predict(CodebaseMapFraming), trainset=train_tasks)
```

### LLM Configuration (via OpenRouter)

```python
# Target model — the one being tested
target_lm = dspy.LM("openrouter/anthropic/claude-sonnet-4-20250514")

# Judge model — for LLM-as-judge metrics
judge_lm = dspy.LM("openrouter/openai/gpt-4.1")

# Reflection model — for GEPA optimizer
reflection_lm = dspy.LM("openrouter/anthropic/claude-sonnet-4-20250514", temperature=1.0)
```

### Output

DSPy saves the optimized program to `results/optimized_{optimizer}_{timestamp}.json`.
The optimized instruction text is extracted and saved to `prompts/optimized.md`.

---

## Phase 5: Promptfoo Regression Suite

After DSPy finds a winning prompt, lock it in with deterministic + LLM-rubric
assertions across multiple models.

```yaml
# promptfoo.yaml
prompts:
  - file://prompts/baseline.md
  - file://prompts/optimized.md

providers:
  - openrouter:anthropic/claude-sonnet-4-20250514
  - openrouter:openai/gpt-4.1
  - openrouter:google/gemini-2.5-pro

defaultTest:
  assert:
    - type: not-icontains
      value: "let me search"
    - type: not-icontains
      value: "let me verify"

tests:
  # Trust tasks
  - vars:
      codebase_map: file://fixtures/fastapi.codebase.md
      task: "Where is the Request class defined?"
    assert:
      - type: icontains
        value: "request"
      - type: javascript
        value: |
          const hasLine = /line\s*\d+|:\d+/.test(output);
          return { pass: hasLine, score: hasLine ? 1 : 0 };

  # Type consistency tasks
  - vars:
      codebase_map: file://fixtures/fastapi.codebase.md
      task: "Add a validate method to the User model"
    assert:
      - type: llm-rubric
        value: "Does the code use the correct User type fields as shown in the codebase map?"

  # ... 48 more tasks
```

Run with: `npx promptfoo eval && npx promptfoo view`

---

## Phase 6: Ship the Winner

1. Extract the optimized framing text from DSPy results
2. Replace `_PROMPT_FRAMING` in `src/core/writer.py`
3. Run existing 304 tests — verify nothing breaks
4. Regenerate `.codebase.md` for codebase-graph itself
5. Bump version to 0.2.0
6. `python -m build && twine upload dist/*`
7. Commit + push

---

## Dependencies

```toml
# pyproject.toml — new optional group
[project.optional-dependencies]
bench = [
    "dspy>=3.1.0",
]
```

Plus: `npm install -g promptfoo` (for regression suite).

OpenRouter API key required: `OPENROUTER_API_KEY` env var.

---

## Estimated Cost

| Phase | Calls | Cost (OpenRouter) |
|-------|-------|-------------------|
| DSPy MIPROv2 medium | ~1500 | $5-15 |
| DSPy GEPA medium | ~1500 | $5-15 |
| Promptfoo regression (50 tasks × 3 models × 2 prompts) | ~300 | $1-3 |
| **Total** | **~3300** | **$11-33** |

---

## How to Run

```bash
# Install bench dependencies
pip install -e ".[bench]"
npm install -g promptfoo

# Generate fixtures (clones repos, runs codebase-graph, cleans up)
python -m tests.bench.generate_fixtures

# Run DSPy optimization
OPENROUTER_API_KEY=... python -m tests.bench.harness

# Run promptfoo regression
cd tests/bench && npx promptfoo eval && npx promptfoo view
```

---

## Open Questions

- Should we also test injecting the map as the last user message instead of
  system prompt? (deferred — not in v1 of the harness)
- Should the TOON schema itself be optimized (adding/removing fields), or
  just the framing? (just framing for now — schema changes are a separate effort)
- Should we cross-validate across models? (yes — promptfoo handles this)
