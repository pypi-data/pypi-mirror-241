"""
Task specification module.
"""
from __future__ import annotations

from pydantic import BaseModel

from digitalhub_core.entities._base.spec import Spec


class TaskSpec(Spec):
    """Task specification."""

    def __init__(self, function: str | None = None, **kwargs) -> None:
        """
        Constructor.

        Parameters
        ----------
        function : str
            Function string.
        **kwargs
            Keyword arguments.
        """
        self.function = function

        self._any_setter(**kwargs)


class TaskParams(BaseModel):
    """
    Base task model.
    """

    function: str = None
    """Task function."""
