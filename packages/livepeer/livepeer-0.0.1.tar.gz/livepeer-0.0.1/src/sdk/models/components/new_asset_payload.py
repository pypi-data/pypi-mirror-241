"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .creator_id import CreatorID
from .input_creator_id import InputCreatorID
from .playback_policy import PlaybackPolicy
from .spec import Spec
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional, Union


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class NewAssetPayload1:
    r"""Set to true to make default export to IPFS. To customize the
    pinned files, specify an object with a spec field. False or null
    means to unpin from IPFS, but it's unsupported right now.
    """
    spec: Optional[Spec] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('spec') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class NewAssetPayloadStorage:
    ipfs: Optional[Union[NewAssetPayload1, bool]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ipfs') }})
    r"""Set to true to make default export to IPFS. To customize the
    pinned files, specify an object with a spec field. False or null
    means to unpin from IPFS, but it's unsupported right now.
    """
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class NewAssetPayloadEncryption:
    encrypted_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('encryptedKey') }})
    r"""Encryption key used to encrypt the asset. Only writable in the upload asset endpoints and cannot be retrieved back."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class NewAssetPayload:
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Name of the asset. This is not necessarily the filename, can be a
    custom name or title
    """
    creator_id: Optional[Union[Union[CreatorID1], str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('creatorId'), 'exclude': lambda f: f is None }})
    encryption: Optional[NewAssetPayloadEncryption] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('encryption'), 'exclude': lambda f: f is None }})
    playback_policy: Optional[PlaybackPolicy] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('playbackPolicy'), 'exclude': lambda f: f is None }})
    r"""Whether the playback policy for a asset or stream is public or signed"""
    static_mp4: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('staticMp4'), 'exclude': lambda f: f is None }})
    r"""Whether to generate MP4s for the asset."""
    storage: Optional[NewAssetPayloadStorage] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('storage'), 'exclude': lambda f: f is None }})
    url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url'), 'exclude': lambda f: f is None }})
    r"""URL where the asset contents can be retrieved. Only allowed (and
    also required) in the upload asset via URL endpoint.
    """
    

