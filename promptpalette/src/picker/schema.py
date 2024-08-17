from pydantic import BaseModel, Field
from typing import List, Dict, Union, Optional, Literal


class PickerOutput(BaseModel):
    use_case_analysis: str = Field(
        ...,
        description=
        "Analyze the use case based on the objective and the requirements.")
    relevant_prompting_strategies: str = Field(
        ...,
        description=
        "Write your thoughts about the relevant prompting strategies.")
    prompt_recommendations: List[Literal[
        'guided-tree-of-thought-prompting', 'program-of-thoughts-prompting',
        'llm-human-level-prompt-engineers',
        'art-automatic-multi-step-reasoning-prompting',
        'chain-of-knowledge-prompting', 'reasoning-via-abstraction-prompting',
        'tree-of-thought-problem-solving-prompting',
        'contrastive-chain-of-thought-prompting', 'chain-of-table-prompting',
        'self-consistency-cot-prompting', 'chain-of-verification-prompting',
        'chain-of-symbol-prompting', 'active-prompting-cot',
        'llm-emotional-stimuli-prompting', 'scratchpad-prompting',
        'structured-chain-of-thought-code-generation-prompting',
        'zero-shot-chain-of-thought-reasoning-prompting',
        'chain-of-note-prompting', 'chain-of-code-prompting',
        'language-model-few-shot-learners', 'react-prompting', 'cot-prompting',
        'rephrase-and-response-prompting']] = Field(
            ...,
            description=
            "Provide a list (array) of prompting strategies based on your relevance category above."
        )
