"""LLM-as-judge DSPy Signatures for benchmark evaluation.

Three judge signatures used by the harder metrics (type consistency,
contract adherence, pattern adherence). The deterministic metrics
(trust, import) don't need LLM judges.
"""

from __future__ import annotations

import dspy


class AssessTypeConsistency(dspy.Signature):
    """Assess whether generated code uses types consistent with the codebase map.

    Score 1.0 if all referenced types match the map and field access is correct.
    Score 0.5 if some types match but others are invented or used incorrectly.
    Score 0.0 if types are entirely invented or wrong."""

    codebase_map: str = dspy.InputField(
        desc="TOON-format structural map of the codebase"
    )
    generated_code: str = dspy.InputField(
        desc="code produced by the agent being evaluated"
    )
    expected_types: str = dspy.InputField(
        desc="comma-separated type names the code should use correctly"
    )
    score: float = dspy.OutputField(desc="0.0 to 1.0")
    reasoning: str = dspy.OutputField(
        desc="brief explanation of what was correct or wrong"
    )


class AssessContractAdherence(dspy.Signature):
    """Assess whether generated code implements all required methods and fields
    from the interface or base class contract shown in the codebase map.

    Score 1.0 if all required members are present with correct signatures.
    Score 0.5 if some required members are present. Score 0.0 if the
    contract is ignored."""

    codebase_map: str = dspy.InputField(
        desc="TOON-format structural map of the codebase"
    )
    generated_code: str = dspy.InputField(
        desc="code produced by the agent being evaluated"
    )
    contract_requirements: str = dspy.InputField(
        desc="required methods/fields the code must implement, as comma-separated list"
    )
    score: float = dspy.OutputField(desc="0.0 to 1.0")
    reasoning: str = dspy.OutputField(
        desc="brief explanation of what was implemented correctly or missing"
    )


class AssessPatternAdherence(dspy.Signature):
    """Assess whether generated code follows the naming conventions, error
    handling patterns, structural patterns, and idioms visible in the codebase map.

    Score 1.0 if the code looks like it belongs in the project.
    Score 0.5 if partially consistent. Score 0.0 if it ignores conventions."""

    codebase_map: str = dspy.InputField(
        desc="TOON-format structural map of the codebase"
    )
    generated_code: str = dspy.InputField(
        desc="code produced by the agent being evaluated"
    )
    pattern_description: str = dspy.InputField(
        desc="comma-separated patterns/conventions the code should follow"
    )
    score: float = dspy.OutputField(desc="0.0 to 1.0")
    reasoning: str = dspy.OutputField(
        desc="brief explanation of how well patterns were followed"
    )
