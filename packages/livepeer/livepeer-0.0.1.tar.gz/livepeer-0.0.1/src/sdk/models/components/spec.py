"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils
from typing import Optional

class SpecNftMetadataTemplate(str, Enum):
    r"""Name of the NFT metadata template to export. 'player'
    will embed the Livepeer Player on the NFT while 'file'
    will reference only the immutable MP4 files.
    """
    FILE = 'file'
    PLAYER = 'player'


@dataclasses.dataclass
class SpecNftMetadata:
    r"""Additional data to add to the NFT metadata exported to
    IPFS. Will be deep merged with the default metadata
    exported.
    """
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Spec:
    nft_metadata: Optional[SpecNftMetadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nftMetadata'), 'exclude': lambda f: f is None }})
    r"""Additional data to add to the NFT metadata exported to
    IPFS. Will be deep merged with the default metadata
    exported.
    """
    nft_metadata_template: Optional[SpecNftMetadataTemplate] = dataclasses.field(default=SpecNftMetadataTemplate.FILE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nftMetadataTemplate'), 'exclude': lambda f: f is None }})
    r"""Name of the NFT metadata template to export. 'player'
    will embed the Livepeer Player on the NFT while 'file'
    will reference only the immutable MP4 files.
    """
    

