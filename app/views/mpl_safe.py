"""Ajustes de matplotlib comunes a todos los gráficos (capturas, resultado, señales).

Problema que evita: matplotlib interpreta como *mathtext* cualquier texto con dos o más ``$`` sin
escapar. Los gráficos escriben importes en dólares (``+$572 (+0.68%)``, ``-2.42 $``) y textos que
llegan de fuera (comentarios/motivos de cierre de MT5, notas, callouts de la señal). El texto entre
``$…$`` se manda al parser de mathtext, que:

* lanza ``ValueError`` (ParseException) con importes como ``+$572 (+0.68%) · -$300``, o
* lanza ``RecursionError: maximum recursion depth exceeded`` con llaves/raíces/exponentes anidados
  (``$ {{{{…`` o ``$\\sqrt{\\sqrt{…``), y el gráfico no se genera.

Ningún gráfico del proyecto usa mathtext a propósito, así que se desactiva globalmente.
"""
from __future__ import annotations

import re
from typing import Any

MAX_TEXT_LEN = 300
_CONTROL_RE = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")


def disable_mathtext() -> None:
    """``text.parse_math = False``: ``$`` es un carácter normal. Idempotente."""
    import matplotlib

    try:
        matplotlib.rcParams["text.parse_math"] = False
    except KeyError:  # matplotlib < 3.6 (instalaciones antiguas, p. ej. apt en Android): el rcParam no existe
        pass


def safe_text(value: Any, *, max_len: int = MAX_TEXT_LEN) -> str:
    """Texto externo (comentario MT5, etiqueta…) acotado y sin caracteres de control, para dibujarlo."""
    text = _CONTROL_RE.sub("", "" if value is None else str(value))
    return text if len(text) <= max_len else text[: max_len - 1] + "…"


def print_compact_traceback(exc: BaseException, file=None, *, head: int = 12, tail: int = 8) -> None:
    """Traceback acotado a stderr (el servidor lo registra). Nunca lanza.

    Un ``RecursionError`` trae ~1000 frames casi iguales: se imprimen los primeros ``head`` (dónde empieza
    el ciclo: es lo que sirve para diagnosticarlo) y no el volcado completo. El resto: los últimos ``tail``.
    """
    import sys
    import traceback

    out = file or sys.stderr
    try:
        frames = traceback.extract_tb(exc.__traceback__)
        if isinstance(exc, RecursionError):
            shown, note = frames[:head], f"  … {max(len(frames) - head, 0)} frames más (recursión)\n"
        else:
            shown, note = frames[-tail:], ""
        out.write("Traceback (resumido):\n")
        out.write("".join(traceback.format_list(shown)))
        out.write(note)
        out.write("".join(traceback.format_exception_only(type(exc), exc)))
        out.flush()
    except Exception:  # noqa: BLE001 — el traceback es solo diagnóstico
        pass


def use_agg_without_mathtext() -> None:
    """Backend Agg (sin ventana; Android/servidor) + sin mathtext."""
    import matplotlib

    matplotlib.use("Agg")
    disable_mathtext()
