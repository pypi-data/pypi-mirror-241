from logging import getLogger
from pathlib import Path
from typing import TypeAlias

import jinja2
from tipsql.core.exception import (
    TipsqlJinjaRenderError,
    TipsqlJinjaTemplateRuntimeError,
    TipsqlJinjaTemplateSyntaxError,
)

logger = getLogger(__name__)

PythonCode: TypeAlias = str
GeneratedPythonCode: TypeAlias = str


def render_template(template_path: Path, **kwargs) -> "GeneratedPythonCode":
    if template_path is None:
        raise ValueError("template_path must be specified.")

    elif not template_path.exists():
        raise FileNotFoundError(template_path)

    with open(template_path, "r") as f:
        try:
            environment = jinja2.Environment(
                loader=jinja2.BaseLoader(),
                undefined=jinja2.StrictUndefined,
                trim_blocks=True,
            )

            return (
                environment.from_string(f.read()).render(
                    **kwargs,
                )
            ).strip() + "\n"

        except jinja2.TemplateSyntaxError as error:
            raise TipsqlJinjaTemplateSyntaxError(template_path, error)

        except jinja2.TemplateRuntimeError as error:
            raise TipsqlJinjaTemplateRuntimeError(template_path, error)

        except Exception as error:
            raise TipsqlJinjaRenderError(template_path, error)
