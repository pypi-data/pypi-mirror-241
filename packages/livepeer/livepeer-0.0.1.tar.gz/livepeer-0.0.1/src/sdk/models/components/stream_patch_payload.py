"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .creator_id import CreatorID
from .input_creator_id import InputCreatorID
from .multistream import Multistream
from .playback_policy import PlaybackPolicy
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional, Union


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class StreamPatchPayload:
    creator_id: Optional[Union[Union[CreatorID1], str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('creatorId'), 'exclude': lambda f: f is None }})
    multistream: Optional[Multistream] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('multistream'), 'exclude': lambda f: f is None }})
    playback_policy: Optional[PlaybackPolicy] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('playbackPolicy'), 'exclude': lambda f: f is None }})
    r"""Whether the playback policy for a asset or stream is public or signed"""
    record: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('record'), 'exclude': lambda f: f is None }})
    r"""Should this stream be recorded? Uses default settings. For more
    customization, create and configure an object store.
    """
    suspended: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('suspended'), 'exclude': lambda f: f is None }})
    r"""If currently suspended"""
    

