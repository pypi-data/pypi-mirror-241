"""
Dataitem metadata module.
"""
from __future__ import annotations

from digitalhub_core.entities._base.metadata import Metadata


class DataitemMetadata(Metadata):
    """
    A class representing Dataitem metadata.
    """

    def __init__(
        self,
        project: str,
        created: str | None = None,
        updated: str | None = None,
        name: str | None = None,
        version: str | None = None,
        description: str | None = None,
        embedded: bool = False,
    ) -> None:
        """
        Constructor.

        Parameters
        ----------
        name : str
            Name of the object.
        version : str
            Version of the object.
        description : str
            Description of the entity.
        embedded : bool
            If True, embed object in backend.

        See Also
        --------
        Metadata.__init__
        """
        super().__init__(project, created, updated)
        self.name = name
        self.version = version
        self.description = description
        self.embedded = embedded
