"""One structured-output call to Claude, shared by the listing and video stages."""

from typing import TypeVar

import anthropic
from pydantic import BaseModel

from . import config

T = TypeVar("T", bound=BaseModel)

_client: anthropic.Anthropic | None = None


class RefusedError(RuntimeError):
    pass


def client() -> anthropic.Anthropic:
    global _client
    if _client is None:
        _client = anthropic.Anthropic()
    return _client


def generate(system: str, prompt: str, schema: type[T], effort: str = "high") -> T:
    """Ask Claude for JSON matching ``schema``; returns the validated model."""
    response = client().beta.messages.parse(
        model=config.MODEL,
        max_tokens=16000,
        system=system,
        messages=[{"role": "user", "content": prompt}],
        output_format=schema,
        thinking={"type": "adaptive"},
        output_config={"effort": effort},
        # On a safety decline, the API retries on a fallback model it picks by refusal category.
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",
    )
    if response.stop_reason == "refusal":
        raise RefusedError(f"Claude declined: {response.stop_details}")
    if response.stop_reason == "max_tokens" or response.parsed_output is None:
        raise RuntimeError(f"No complete output (stop_reason={response.stop_reason})")
    return response.parsed_output
