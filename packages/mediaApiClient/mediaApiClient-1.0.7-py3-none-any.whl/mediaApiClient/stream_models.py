from typing import List, Optional, Dict
from pydantic import BaseModel


class FFmpegStreamWrapper(BaseModel):
    index: Optional[int] = None
    codec_name: Optional[str] = None
    codec_long_name: Optional[str] = None
    profile: Optional[str] = None
    codec_type: Optional[str] = None
    codec_time_base: Optional[str] = None
    codec_tag_string: Optional[str] = None
    codec_tag: Optional[str] = None
    width: Optional[int] = None
    height: Optional[int] = None
    has_b_frames: Optional[int] = None
    sample_aspect_ratio: Optional[str] = None
    display_aspect_ratio: Optional[str] = None
    pix_fmt: Optional[str] = None
    level: Optional[int] = None
    chroma_location: Optional[str] = None
    refs: Optional[int] = None
    is_avc: Optional[str] = None
    nal_length_size: Optional[str] = None
    r_frame_rate: Optional[str] = None
    avg_frame_rate: Optional[str] = None
    time_base: Optional[str] = None
    start_pts: Optional[int] = None
    start_time: Optional[float] = None
    duration_ts: Optional[int] = None
    duration: Optional[float] = None
    bit_rate: Optional[int] = None
    max_bit_rate: Optional[int] = None
    bits_per_raw_sample: Optional[int] = None
    bits_per_sample: Optional[int] = None
    nb_frames: Optional[int] = None
    sample_fmt: Optional[str] = None
    sample_rate: Optional[int] = None
    channels: Optional[int] = None
    channel_layout: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class Stream(BaseModel):
    type: Optional[str] = None
    streamUrl: Optional[str] = None
    streamInfo: Optional[List[FFmpegStreamWrapper]] = None


class Language(BaseModel):
    label: Optional[str] = None
    value: Optional[str] = None


class Item(BaseModel):
    quality: Optional[str] = None
    streams: Optional[List[Stream]] = None


class ClientStreamResponseV2(BaseModel):
    thumbUrl: Optional[str] = None
    items: Optional[List[Item]] = None
