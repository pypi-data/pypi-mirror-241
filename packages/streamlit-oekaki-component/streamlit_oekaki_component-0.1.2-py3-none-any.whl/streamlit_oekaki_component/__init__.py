from __future__ import annotations
import base64
from pathlib import Path
import streamlit.components.v1 as components
from dataclasses import dataclass
from typing import Optional


@dataclass
class OekakiResponse:
    is_submitted: bool
    image_bytes: Optional[bytes] = None
    image_base64: Optional[str] = None


# Declare a Streamlit component
_frontend_dir = (Path(__file__).parent / "frontend").absolute()
_declare_component = components.declare_component("oekaki", path=str(_frontend_dir))


def _data_url_to_bytes(data_url: str) -> bytes:
    _, encoded = data_url.split(";base64,")
    return base64.b64decode(encoded)


def oekaki(
    stroke_width: int = 30,
    stroke_color: str = "#FFFFFF",
    background_color: str = "#000000",
    width: int = 300,
    height: int = 300,
    button_height: int = 30,
    submit_button_label: str = "Submit",
    submit_background_color: str = "#FAFAFA",
    clear_button_label: str = "Clear",
    clear_background_color: str = "#FAFAFA",
    key=None,
) -> OekakiResponse:
    component_value = _declare_component(
        strokeWidth=stroke_width,
        strokeColor=stroke_color,
        backgroundColor=background_color,
        canvasWidth=width,
        canvasHeight=height,
        buttonHeight=button_height,
        submitButtonLabel=submit_button_label,
        submitBackgroundColor=submit_background_color,
        clearButtonLabel=clear_button_label,
        clearBackgroundColor=clear_background_color,
        key=key,
        default=None,
    )

    is_submitted = (
        component_value.get("is_submitted", False) if component_value else False
    )
    image_base64 = component_value.get("image_data") if component_value else None
    image_bytes = _data_url_to_bytes(image_base64) if image_base64 else None

    return OekakiResponse(
        is_submitted=is_submitted, image_bytes=image_bytes, image_base64=image_base64
    )
