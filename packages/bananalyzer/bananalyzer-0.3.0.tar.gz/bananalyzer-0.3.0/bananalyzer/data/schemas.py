import json
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Literal, Optional, Union

import pytest
from deepdiff import DeepDiff
from pydantic import BaseModel, Field, model_validator

from bananalyzer.data.fetch_schemas import fetch_schemas

GoalType = Literal[
    "fetch",  # Scrape specific JSON information from a single page. Does not require navigation
    "links",  # Scrape all detail page links from a single page
    "click",  # Make a single click on a page
    "navigate",  # Travel to a new page
    "search",  # Search for the answer to a specific query
    "multiple",  # Perform multiple intents
]


class Eval(BaseModel, ABC):
    """
    Base class for all evals. Evals are used to determine if an action or result is correct
    """

    @abstractmethod
    def eval_action(self, action: str) -> bool:
        raise NotImplementedError("eval_action not implemented")

    @abstractmethod
    def eval_result(self, result: str) -> bool:
        raise NotImplementedError("eval_result not implemented")


class JSONEval(BaseModel):
    type: Literal["json_match"] = Field(default="json_match")
    expected: Union[Dict[str, Any], List[str]]

    def eval_action(self, _: str) -> bool:
        # We don't care about action level evaluations
        return True

    def eval_results(self, result: Dict[str, Any]) -> None:
        diff = DeepDiff(
            self.expected, result, ignore_order=True, report_repetition=True
        )
        if diff:
            # Pretty print both expected and actual results
            pretty_expected = json.dumps(self.expected, indent=4)
            pretty_actual = json.dumps(result, indent=4)

            diff_msg = f"Actual: {pretty_actual}\nExpected: {pretty_expected}"
            pytest.fail(f"JSONEval mismatch!\n{diff_msg}")


class ActionEval(BaseModel):
    actions: Dict[str, str]


class Example(BaseModel):
    id: str
    url: str
    source: Literal["mhtml", "hosted"] = Field(description="Source of the website")
    domain: str = Field(description="Domain of the website")
    subdomain: str = Field(description="Subdomain of the website")
    type: GoalType = Field(
        description="The high level goal intent the agent is aiming to do"
    )
    goal: Union[str, Dict[str, Any]] = Field(
        description="The goal of the agent for this specific example"
    )
    fetch_id: Optional[
        Literal["job_posting", "manufacturing_commerce", "contact"]
    ] = Field(
        default=None,
        description="If it is a fetch type, we can infer the goal based on this id to avoid large schemas in json",
    )
    evals: List[Union[JSONEval]] = Field(
        description="Various evaluations to test for within the example"
    )

    def get_static_url(self) -> str:
        from bananalyzer.runner.website_responder import get_website_responder

        return get_website_responder(self).get_url(self)

    @model_validator(mode="before")
    def set_goal_if_fetch_id_provided(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        goal_type = values.get("type")
        if goal_type != "fetch":
            return values

        fetch_id = values.get("fetch_id")
        if fetch_id is None:
            raise ValueError("fetch_id must be provided for fetch goal types")

        goal = values.get("goal")
        if goal is not None:
            raise ValueError("goal must not be provided if fetch_id is provided")

        values["goal"] = fetch_schemas[fetch_id]
        return values
