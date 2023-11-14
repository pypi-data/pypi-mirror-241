"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import viewership_metric as components_viewership_metric
from datetime import datetime
from enum import Enum
from typing import List, Optional, Union

class QueryParamTimeStep(str, Enum):
    r"""The time step to aggregate viewership metrics by"""
    HOUR = 'hour'
    DAY = 'day'
    WEEK = 'week'
    MONTH = 'month'
    YEAR = 'year'

class QueryParamBreakdownBy(str, Enum):
    DEVICE_TYPE = 'deviceType'
    DEVICE = 'device'
    CPU = 'cpu'
    OS = 'os'
    BROWSER = 'browser'
    BROWSER_ENGINE = 'browserEngine'
    CONTINENT = 'continent'
    COUNTRY = 'country'
    SUBDIVISION = 'subdivision'
    TIMEZONE = 'timezone'
    VIEWER_ID = 'viewerId'


@dataclasses.dataclass
class GetCreatorMetricsRequest:
    asset_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'assetId', 'style': 'form', 'explode': True }})
    r"""The asset ID to filter metrics for"""
    breakdown_by: Optional[List[QueryParamBreakdownBy]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'breakdownBy[]', 'style': 'form', 'explode': True }})
    r"""The list of fields to break down the query results. Specify this
    query-string multiple times to break down by multiple fields.
    """
    creator_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'creatorId', 'style': 'form', 'explode': True }})
    r"""The creator ID to filter the query results"""
    from_: Optional[Union[datetime, int]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'from', 'style': 'form', 'explode': True }})
    r"""Start timestamp for the query range (inclusive)"""
    stream_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'streamId', 'style': 'form', 'explode': True }})
    r"""The stream ID to filter metrics for"""
    time_step: Optional[QueryParamTimeStep] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'timeStep', 'style': 'form', 'explode': True }})
    r"""The time step to aggregate viewership metrics by"""
    to: Optional[Union[datetime, int]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'to', 'style': 'form', 'explode': True }})
    r"""End timestamp for the query range (exclusive)"""
    



@dataclasses.dataclass
class GetCreatorMetricsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    data: Optional[List[components_viewership_metric.ViewershipMetric]] = dataclasses.field(default=None)
    r"""A list of Metric objects"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

