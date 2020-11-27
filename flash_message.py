from enum import Enum

from flask import flash, redirect, render_template


class FlashCategories(Enum):
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"


class FlashMessage:
    @staticmethod
    def show_with_render_template(message: str, category: FlashCategories,
                                  template_file: str, **context_dict: dict):
        flash(message, category.value)
        return render_template(template_file, **context_dict)

    @staticmethod
    def show_with_redirect(message: str, category: FlashCategories, url: str):
        flash(message, category.value)
        return redirect(url)
