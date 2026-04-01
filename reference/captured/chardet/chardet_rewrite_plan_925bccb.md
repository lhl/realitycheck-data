# Chardet Rewrite Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a ground-up, MIT-licensed, API-compatible replacement for chardet 6.x with high accuracy and performance.

**Architecture:** Layered detection pipeline — Stage 0 (binary detection) → Stage 1 (deterministic: BOM, ASCII, UTF-8, markup) → Stage 2a (byte validity filtering) → Stage 2b (multi-byte structural probing) → Stage 3 (parallel statistical bigram scoring). Each stage either returns a confident result or passes remaining candidates to the next stage.

**Tech Stack:** Python 3.10+, uv, ruff, pytest, pre-commit. Zero runtime dependencies. Hugging Face `datasets` for training only.

**Design doc:** `docs/plans/2026-02-25-chardet-rewrite-design.md`

---

### Task 1: Project Scaffolding

**Files:**
- Create: `pyproject.toml`
- Create: `.gitignore`
- Create: `.pre-commit-config.yaml`
- Create: `src/chardet/__init__.py`
- Create: `src/chardet/py.typed`
- Create: `tests/__init__.py`

**Step 1: Initialize the uv package project**

```bash
uv init --package --name chardet --python ">=3.10" .
```

This creates a basic `pyproject.toml` and `src/chardet/__init__.py`. If uv
creates files we don't want (like `README.md`), that's fine — we'll configure
them later.

**Step 2: Configure pyproject.toml**

Replace the generated `pyproject.toml` with:

```toml
[project]
name = "chardet"
version = "6.1.0"
description = "Universal character encoding detector"
license = "MIT"
requires-python = ">=3.10"
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Text Processing :: Linguistic",
]

[project.scripts]
chardetect = "chardet.cli:main"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src/chardet"]

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_functions = ["test_*"]
addopts = [
    "--strict-markers",
    "--strict-config",
]
markers = [
    "benchmark: marks tests as benchmarks (deselect with '-m \"not benchmark\"')",
]

[tool.ruff]
line-length = 88
target-version = "py310"

[tool.ruff.lint]
select = [
    "E",
    "F",
    "I",
    "B",
    "C4",
    "UP",
]
ignore = [
    "E501",
]

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
```

**Step 3: Create .gitignore**

```
__pycache__/
*.py[cod]
*$py.class
*.egg-info/
dist/
build/
.eggs/
*.egg
.venv/
.env
.ruff_cache/
.pytest_cache/
.coverage
htmlcov/
data/
tests/data/
uv.lock
```

**Step 4: Create .pre-commit-config.yaml**

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.9.7
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v5.0.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-toml
      - id: check-added-large-files
```

**Step 5: Create src/chardet/__init__.py stub**

```python
"""Universal character encoding detector — MIT-licensed rewrite."""

__version__ = "6.1.0"
```

**Step 6: Create src/chardet/py.typed (empty marker file for PEP 561)**

Empty file.

**Step 7: Create tests/__init__.py (empty)**

Empty file.

**Step 8: Add dev dependencies**

```bash
uv add --dev pytest pytest-cov ruff pre-commit
```

**Step 9: Install pre-commit hooks**

```bash
uvx pre-commit install
```

**Step 10: Verify setup**

```bash
uv run pytest
uv run ruff check .
uv run ruff format --check .
```

All should pass (no tests yet, but no errors).

**Step 11: Commit**

```bash
git add pyproject.toml .gitignore .pre-commit-config.yaml src/ tests/__init__.py
git commit -m "chore: scaffold project with uv, ruff, pytest, pre-commit"
```

---

### Task 2: EncodingEra Enum

**Files:**
- Create: `src/chardet/enums.py`
- Create: `tests/test_enums.py`

**Step 1: Write the failing tests**

```python
# tests/test_enums.py
import enum

from chardet.enums import EncodingEra


def test_encoding_era_is_int_flag():
    assert issubclass(EncodingEra, enum.IntFlag)


def test_encoding_era_members_exist():
    expected = {
        "MODERN_WEB",
        "LEGACY_ISO",
        "LEGACY_MAC",
        "LEGACY_REGIONAL",
        "DOS",
        "MAINFRAME",
        "ALL",
    }
    assert set(EncodingEra.__members__.keys()) == expected


def test_encoding_era_bitwise_or():
    combined = EncodingEra.MODERN_WEB | EncodingEra.LEGACY_ISO
    assert EncodingEra.MODERN_WEB in combined
    assert EncodingEra.LEGACY_ISO in combined
    assert EncodingEra.DOS not in combined


def test_encoding_era_all_contains_every_member():
    for member in EncodingEra:
        if member is not EncodingEra.ALL:
            assert member in EncodingEra.ALL


def test_encoding_era_values_are_powers_of_two():
    for member in EncodingEra:
        if member is not EncodingEra.ALL:
            assert member.value & (member.value - 1) == 0, (
                f"{member.name} is not a power of two"
            )
```

**Step 2: Run tests to verify they fail**

```bash
uv run pytest tests/test_enums.py -v
```

Expected: ImportError — `chardet.enums` doesn't exist yet.

**Step 3: Write the implementation**

```python
# src/chardet/enums.py
"""Enumerations for chardet."""

import enum


class EncodingEra(enum.IntFlag):
    """Bit flags representing encoding eras for filtering detection candidates."""

    MODERN_WEB = 1
    LEGACY_ISO = 2
    LEGACY_MAC = 4
    LEGACY_REGIONAL = 8
    DOS = 16
    MAINFRAME = 32
    ALL = MODERN_WEB | LEGACY_ISO | LEGACY_MAC | LEGACY_REGIONAL | DOS | MAINFRAME
```

**Step 4: Run tests to verify they pass**

```bash
uv run pytest tests/test_enums.py -v
```

Expected: All PASS.

**Step 5: Lint and format**

```bash
uv run ruff check src/chardet/enums.py tests/test_enums.py
uv run ruff format src/chardet/enums.py tests/test_enums.py
```

**Step 6: Commit**

```bash
git add src/chardet/enums.py tests/test_enums.py
git commit -m "feat: add EncodingEra IntFlag enum"
```

---

### Task 3: Encoding Registry

**Files:**
- Create: `src/chardet/registry.py`
- Create: `tests/test_registry.py`

**Context:** The registry maps every supported encoding to its metadata.
Era assignments MUST match chardet 6.0.0's `chardet/metadata/charsets.py` at
https://raw.githubusercontent.com/chardet/chardet/f0676c0d6a4263827924b78a62957547fca40052/chardet/metadata/charsets.py

Fetch that file and use it as the authoritative reference for which encodings
belong to which era. Do not invent era assignments.

**Step 1: Write the failing tests**

```python
# tests/test_registry.py
from chardet.enums import EncodingEra
from chardet.registry import REGISTRY, EncodingInfo, get_candidates


def test_encoding_info_is_frozen():
    info = REGISTRY[0]
    assert isinstance(info, EncodingInfo)
    try:
        info.name = "something"  # type: ignore[misc]
        raise AssertionError("Should not be able to mutate frozen dataclass")
    except AttributeError:
        pass


def test_registry_is_tuple():
    assert isinstance(REGISTRY, tuple)


def test_registry_has_entries():
    assert len(REGISTRY) > 50


def test_registry_utf8_is_modern_web():
    utf8 = next(e for e in REGISTRY if e.name == "utf-8")
    assert EncodingEra.MODERN_WEB in utf8.era


def test_registry_iso_8859_1_is_legacy_iso():
    iso = next(e for e in REGISTRY if e.name == "iso-8859-1")
    assert EncodingEra.LEGACY_ISO in iso.era


def test_registry_cp037_is_mainframe():
    cp037 = next(e for e in REGISTRY if e.name == "cp037")
    assert EncodingEra.MAINFRAME in cp037.era


def test_registry_macroman_is_legacy_mac():
    mac = next(e for e in REGISTRY if e.name == "mac-roman")
    assert EncodingEra.LEGACY_MAC in mac.era


def test_registry_cp437_is_dos():
    cp437 = next(e for e in REGISTRY if e.name == "cp437")
    assert EncodingEra.DOS in cp437.era


def test_registry_kz1048_is_legacy_regional():
    kz = next(e for e in REGISTRY if e.name == "kz-1048")
    assert EncodingEra.LEGACY_REGIONAL in kz.era


def test_get_candidates_filters_by_era():
    modern = get_candidates(EncodingEra.MODERN_WEB)
    for enc in modern:
        assert EncodingEra.MODERN_WEB in enc.era


def test_get_candidates_all_returns_everything():
    all_candidates = get_candidates(EncodingEra.ALL)
    assert len(all_candidates) == len(REGISTRY)


def test_get_candidates_combined_eras():
    combined = get_candidates(EncodingEra.MODERN_WEB | EncodingEra.LEGACY_ISO)
    names = {e.name for e in combined}
    assert "utf-8" in names
    assert "iso-8859-1" in names


def test_multibyte_encodings_flagged():
    shift_jis = next(e for e in REGISTRY if e.name == "shift_jis")
    assert shift_jis.is_multibyte is True

    iso_8859_1 = next(e for e in REGISTRY if e.name == "iso-8859-1")
    assert iso_8859_1.is_multibyte is False


def test_python_codec_is_valid():
    import codecs

    for enc in REGISTRY:
        codec_info = codecs.lookup(enc.python_codec)
        assert codec_info is not None, f"Invalid codec: {enc.python_codec}"
```

**Step 2: Run tests to verify they fail**

```bash
uv run pytest tests/test_registry.py -v
```

Expected: ImportError.

**Step 3: Write the implementation**

Create `src/chardet/registry.py` with:

1. An `EncodingInfo` frozen dataclass with fields: `name`, `aliases`, `era`,
   `is_multibyte`, `python_codec`
2. A `REGISTRY` tuple containing an `EncodingInfo` for every encoding supported
   by chardet 6.0.0
3. A `get_candidates(era: EncodingEra) -> tuple[EncodingInfo, ...]` function

Reference the chardet 6.0.0 charsets.py file linked above for the complete list
of encodings and their era assignments. For `is_multibyte`, flag these encodings
as True: Big5, CP932, CP949, EUC-JP, EUC-KR, GB18030, HZ-GB-2312, ISO-2022-JP,
ISO-2022-KR, Johab, Shift_JIS. For `python_codec`, use the name that
`codecs.lookup()` accepts (test each one).

**Step 4: Run tests to verify they pass**

```bash
uv run pytest tests/test_registry.py -v
```

**Step 5: Lint, format, commit**

```bash
uv run ruff check . && uv run ruff format .
git add src/chardet/registry.py tests/test_registry.py
git commit -m "feat: add encoding registry with era classifications"
```

---

### Task 4: Pipeline Result Type and Stage Interface

**Files:**
- Create: `src/chardet/pipeline/__init__.py`
- Create: `tests/test_pipeline_types.py`

**Step 1: Write the failing tests**

```python
# tests/test_pipeline_types.py
from chardet.pipeline import DetectionResult


def test_detection_result_fields():
    r = DetectionResult(encoding="utf-8", confidence=0.99, language="English")
    assert r.encoding == "utf-8"
    assert r.confidence == 0.99
    assert r.language == "English"


def test_detection_result_to_dict():
    r = DetectionResult(encoding="utf-8", confidence=0.99, language=None)
    d = r.to_dict()
    assert d == {"encoding": "utf-8", "confidence": 0.99, "language": None}


def test_detection_result_none():
    r = DetectionResult(encoding=None, confidence=0.0, language=None)
    assert r.to_dict() == {"encoding": None, "confidence": 0.0, "language": None}
```

**Step 2: Run tests to verify they fail**

```bash
uv run pytest tests/test_pipeline_types.py -v
```

**Step 3: Write the implementation**

```python
# src/chardet/pipeline/__init__.py
"""Detection pipeline stages and shared types."""

from __future__ import annotations

import dataclasses


@dataclasses.dataclass(frozen=True, slots=True)
class DetectionResult:
    encoding: str | None
    confidence: float
    language: str | None

    def to_dict(self) -> dict[str, str | float | None]:
        return {
            "encoding": self.encoding,
            "confidence": self.confidence,
            "language": self.language,
        }
```

**Step 4: Run tests to verify they pass**

```bash
uv run pytest tests/test_pipeline_types.py -v
```

**Step 5: Commit**

```bash
git add src/chardet/pipeline/__init__.py tests/test_pipeline_types.py
git commit -m "feat: add DetectionResult type for pipeline stages"
```

---

### Task 5: Stage 0 — Binary Detection

**Files:**
- Create: `src/chardet/pipeline/binary.py`
- Create: `tests/test_binary.py`

**Step 1: Write the failing tests**

```python
# tests/test_binary.py
from chardet.pipeline.binary import is_binary


def test_empty_input_is_not_binary():
    assert is_binary(b"") is False


def test_plain_ascii_is_not_binary():
    assert is_binary(b"Hello, world!") is False


def test_text_with_newlines_tabs_is_not_binary():
    assert is_binary(b"Hello\n\tworld\r\n") is False


def test_all_null_bytes_is_binary():
    assert is_binary(b"\x00" * 100) is True


def test_high_null_concentration_is_binary():
    # >1% null bytes
    data = b"Hello" + b"\x00" * 10 + b"world" * 10
    assert is_binary(data) is True


def test_single_null_in_large_text_is_not_binary():
    # <1% null bytes
    data = b"a" * 500 + b"\x00" + b"b" * 500
    assert is_binary(data) is False


def test_control_characters_indicate_binary():
    # Bytes 0x01-0x08, 0x0E-0x1F (excluding \t=0x09, \n=0x0A, \r=0x0D)
    data = b"\x01\x02\x03\x04\x05\x06\x07\x08" * 20
    assert is_binary(data) is True


def test_few_control_chars_in_large_text_is_not_binary():
    data = b"Normal text " * 100 + b"\x01"
    assert is_binary(data) is False


def test_jpeg_header_is_binary():
    jpeg = b"\xff\xd8\xff\xe0" + b"\x00" * 50 + bytes(range(256))
    assert is_binary(jpeg) is True


def test_utf8_text_is_not_binary():
    assert is_binary("Héllo wörld".encode("utf-8")) is False


def test_max_bytes_respected():
    # Binary content after max_bytes should be ignored
    text = b"clean text " * 100
    binary_tail = b"\x00" * 1000
    assert is_binary(text + binary_tail, max_bytes=len(text)) is False
```

**Step 2: Run tests to verify they fail**

```bash
uv run pytest tests/test_binary.py -v
```

**Step 3: Write the implementation**

```python
# src/chardet/pipeline/binary.py
"""Stage 0: Binary content detection."""

from __future__ import annotations

# Control chars that indicate binary (excluding tab, newline, carriage return)
_BINARY_CONTROL_BYTES = frozenset(range(0x00, 0x09)) | frozenset(range(0x0E, 0x20))

# Threshold: if more than this fraction of bytes are binary indicators, it's binary
_BINARY_THRESHOLD = 0.01


def is_binary(data: bytes, max_bytes: int = 200_000) -> bool:
    """Return True if data appears to be binary (not text) content."""
    data = data[:max_bytes]
    if not data:
        return False

    binary_count = sum(1 for b in data if b in _BINARY_CONTROL_BYTES)
    return binary_count / len(data) > _BINARY_THRESHOLD
```

**Step 4: Run tests to verify they pass**

```bash
uv run pytest tests/test_binary.py -v
```

If any tests fail, adjust the threshold or implementation logic to match the
test expectations. The threshold and set of binary indicator bytes may need
tuning.

**Step 5: Lint, format, commit**

```bash
uv run ruff check . && uv run ruff format .
git add src/chardet/pipeline/binary.py tests/test_binary.py
git commit -m "feat: add Stage 0 binary content detection"
```

---

### Task 6: Stage 1a — BOM Detection

**Files:**
- Create: `src/chardet/pipeline/bom.py`
- Create: `tests/test_bom.py`

**Step 1: Write the failing tests**

```python
# tests/test_bom.py
from chardet.pipeline import DetectionResult
from chardet.pipeline.bom import detect_bom


def test_utf8_bom():
    data = b"\xef\xbb\xbfHello"
    result = detect_bom(data)
    assert result == DetectionResult("utf-8-sig", 1.0, None)


def test_utf16_le_bom():
    data = b"\xff\xfeH\x00e\x00l\x00l\x00o\x00"
    result = detect_bom(data)
    assert result == DetectionResult("utf-16-le", 1.0, None)


def test_utf16_be_bom():
    data = b"\xfe\xff\x00H\x00e\x00l\x00l\x00o"
    result = detect_bom(data)
    assert result == DetectionResult("utf-16-be", 1.0, None)


def test_utf32_le_bom():
    data = b"\xff\xfe\x00\x00" + b"\x48\x00\x00\x00"
    result = detect_bom(data)
    assert result == DetectionResult("utf-32-le", 1.0, None)


def test_utf32_be_bom():
    data = b"\x00\x00\xfe\xff" + b"\x00\x00\x00\x48"
    result = detect_bom(data)
    assert result == DetectionResult("utf-32-be", 1.0, None)


def test_no_bom():
    data = b"Hello, world!"
    result = detect_bom(data)
    assert result is None


def test_empty_input():
    assert detect_bom(b"") is None


def test_too_short_for_bom():
    assert detect_bom(b"\xef") is None
    assert detect_bom(b"\xef\xbb") is None


def test_utf32_le_checked_before_utf16_le():
    # UTF-32-LE BOM starts with \xff\xfe (same as UTF-16-LE) but has \x00\x00 after
    data = b"\xff\xfe\x00\x00" + b"\x48\x00\x00\x00"
    result = detect_bom(data)
    assert result is not None
    assert result.encoding == "utf-32-le"
```

**Step 2: Run tests to verify they fail**

```bash
uv run pytest tests/test_bom.py -v
```

**Step 3: Write the implementation**

```python
# src/chardet/pipeline/bom.py
"""Stage 1: BOM (Byte Order Mark) detection."""

from __future__ import annotations

from chardet.pipeline import DetectionResult

# Ordered longest-first so UTF-32 is checked before UTF-16
# (UTF-32-LE BOM starts with the same bytes as UTF-16-LE BOM)
_BOMS: tuple[tuple[bytes, str], ...] = (
    (b"\x00\x00\xfe\xff", "utf-32-be"),
    (b"\xff\xfe\x00\x00", "utf-32-le"),
    (b"\xef\xbb\xbf", "utf-8-sig"),
    (b"\xfe\xff", "utf-16-be"),
    (b"\xff\xfe", "utf-16-le"),
)


def detect_bom(data: bytes) -> DetectionResult | None:
    """Check for a BOM at the start of data. Returns result or None."""
    for bom_bytes, encoding in _BOMS:
        if data.startswith(bom_bytes):
            return DetectionResult(encoding=encoding, confidence=1.0, language=None)
    return None
```

**Step 4: Run tests to verify they pass**

```bash
uv run pytest tests/test_bom.py -v
```

**Step 5: Commit**

```bash
uv run ruff check . && uv run ruff format .
git add src/chardet/pipeline/bom.py tests/test_bom.py
git commit -m "feat: add Stage 1a BOM detection"
```

---

### Task 7: Stage 1b — ASCII Check

**Files:**
- Create: `src/chardet/pipeline/ascii.py`
- Create: `tests/test_ascii.py`

**Step 1: Write the failing tests**

```python
# tests/test_ascii.py
from chardet.pipeline import DetectionResult
from chardet.pipeline.ascii import detect_ascii


def test_pure_ascii():
    result = detect_ascii(b"Hello, world! 123")
    assert result == DetectionResult("ascii", 1.0, None)


def test_ascii_with_common_whitespace():
    result = detect_ascii(b"Hello\n\tworld\r\n")
    assert result == DetectionResult("ascii", 1.0, None)


def test_high_byte_not_ascii():
    result = detect_ascii(b"Hello \x80 world")
    assert result is None


def test_utf8_multibyte_not_ascii():
    result = detect_ascii("Héllo".encode("utf-8"))
    assert result is None


def test_empty_input():
    result = detect_ascii(b"")
    assert result is None


def test_single_ascii_byte():
    result = detect_ascii(b"A")
    assert result == DetectionResult("ascii", 1.0, None)


def test_all_printable_ascii():
    data = bytes(range(0x20, 0x7F))
    result = detect_ascii(data)
    assert result == DetectionResult("ascii", 1.0, None)


def test_null_byte_not_ascii():
    # Null bytes should have been caught by binary detection (Stage 0),
    # but ASCII check should still reject them
    result = detect_ascii(b"Hello\x00world")
    assert result is None
```

**Step 2: Run tests to verify they fail**

```bash
uv run pytest tests/test_ascii.py -v
```

**Step 3: Write the implementation**

```python
# src/chardet/pipeline/ascii.py
"""Stage 1: Pure ASCII detection."""

from __future__ import annotations

from chardet.pipeline import DetectionResult


def detect_ascii(data: bytes) -> DetectionResult | None:
    """Return ASCII result if all bytes are printable ASCII + common whitespace."""
    if not data:
        return None
    # Check that every byte is in the range 0x09-0x0D (whitespace) or 0x20-0x7E
    for byte in data:
        if byte > 0x7E or (byte < 0x20 and byte not in (0x09, 0x0A, 0x0D)):
            return None
    return DetectionResult(encoding="ascii", confidence=1.0, language=None)
```

**Step 4: Run tests to verify they pass**

```bash
uv run pytest tests/test_ascii.py -v
```

**Step 5: Commit**

```bash
uv run ruff check . && uv run ruff format .
git add src/chardet/pipeline/ascii.py tests/test_ascii.py
git commit -m "feat: add Stage 1b ASCII detection"
```

---

### Task 8: Stage 1c — UTF-8 Structural Validation

**Files:**
- Create: `src/chardet/pipeline/utf8.py`
- Create: `tests/test_utf8.py`

**Step 1: Write the failing tests**

```python
# tests/test_utf8.py
from chardet.pipeline import DetectionResult
from chardet.pipeline.utf8 import detect_utf8


def test_valid_utf8_with_multibyte():
    data = "Héllo wörld café".encode("utf-8")
    result = detect_utf8(data)
    assert result is not None
    assert result.encoding == "utf-8"
    assert result.confidence >= 0.9


def test_valid_utf8_chinese():
    data = "你好世界".encode("utf-8")
    result = detect_utf8(data)
    assert result is not None
    assert result.encoding == "utf-8"


def test_valid_utf8_emoji():
    data = "Hello 🌍🌎🌏".encode("utf-8")
    result = detect_utf8(data)
    assert result is not None
    assert result.encoding == "utf-8"


def test_pure_ascii_returns_none():
    # Pure ASCII is valid UTF-8 but should be handled by ASCII detector
    result = detect_utf8(b"Hello world")
    assert result is None


def test_invalid_utf8():
    # Invalid continuation byte
    result = detect_utf8(b"\xc3\x00")
    assert result is None


def test_overlong_encoding():
    # Overlong encoding of '/' (should be 0x2F, not 0xC0 0xAF)
    result = detect_utf8(b"\xc0\xaf")
    assert result is None


def test_invalid_start_byte():
    result = detect_utf8(b"\xff\xfe")
    assert result is None


def test_truncated_multibyte():
    # Start of 2-byte sequence but data ends
    result = detect_utf8(b"Hello \xc3")
    assert result is None


def test_empty_input():
    result = detect_utf8(b"")
    assert result is None


def test_latin1_is_not_valid_utf8():
    data = "Héllo".encode("latin-1")  # \xe9 is not a valid UTF-8 start byte
    result = detect_utf8(data)
    assert result is None
```

**Step 2: Run tests to verify they fail**

```bash
uv run pytest tests/test_utf8.py -v
```

**Step 3: Write the implementation**

Validate UTF-8 byte structure manually (do NOT use `data.decode('utf-8')` — we
want to check structural validity including rejecting overlong sequences). Track
whether any multi-byte sequences are found. If all bytes are valid UTF-8 AND at
least one multi-byte sequence exists, return `DetectionResult("utf-8", ...)`. If
all bytes are <0x80 (pure ASCII), return `None` to let the ASCII detector handle
it.

The confidence should scale with the amount of valid multi-byte data — more
multi-byte sequences = higher confidence.

```python
# src/chardet/pipeline/utf8.py
"""Stage 1: UTF-8 structural validation."""

from __future__ import annotations

from chardet.pipeline import DetectionResult


def detect_utf8(data: bytes) -> DetectionResult | None:
    """Validate UTF-8 byte structure. Returns result only if multi-byte sequences found."""
    if not data:
        return None

    i = 0
    length = len(data)
    multibyte_count = 0
    total_bytes = 0

    while i < length:
        byte = data[i]
        total_bytes += 1

        if byte < 0x80:
            # ASCII byte
            i += 1
            continue

        # Determine expected sequence length
        if 0xC2 <= byte <= 0xDF:
            seq_len = 2
        elif 0xE0 <= byte <= 0xEF:
            seq_len = 3
        elif 0xF0 <= byte <= 0xF4:
            seq_len = 4
        else:
            # Invalid start byte (includes 0x80-0xBF, 0xC0-0xC1, 0xF5+)
            return None

        # Check we have enough bytes
        if i + seq_len > length:
            return None

        # Validate continuation bytes
        for j in range(1, seq_len):
            if not (0x80 <= data[i + j] <= 0xBF):
                return None

        # Reject overlong sequences and invalid ranges
        if seq_len == 2 and byte < 0xC2:
            return None
        elif seq_len == 3:
            if byte == 0xE0 and data[i + 1] < 0xA0:
                return None
            if byte == 0xED and data[i + 1] > 0x9F:
                return None  # Surrogate halves
        elif seq_len == 4:
            if byte == 0xF0 and data[i + 1] < 0x90:
                return None
            if byte == 0xF4 and data[i + 1] > 0x8F:
                return None

        multibyte_count += 1
        i += seq_len

    if multibyte_count == 0:
        return None  # Pure ASCII — let ASCII detector handle it

    # Confidence scales with multibyte density
    confidence = min(0.99, 0.8 + 0.19 * (multibyte_count / max(total_bytes, 1)))
    return DetectionResult(encoding="utf-8", confidence=confidence, language=None)
```

**Step 4: Run tests to verify they pass**

```bash
uv run pytest tests/test_utf8.py -v
```

**Step 5: Commit**

```bash
uv run ruff check . && uv run ruff format .
git add src/chardet/pipeline/utf8.py tests/test_utf8.py
git commit -m "feat: add Stage 1c UTF-8 structural validation"
```

---

### Task 9: Stage 1d — Markup Charset Extraction

**Files:**
- Create: `src/chardet/pipeline/markup.py`
- Create: `tests/test_markup.py`

**Step 1: Write the failing tests**

```python
# tests/test_markup.py
from chardet.pipeline import DetectionResult
from chardet.pipeline.markup import detect_markup_charset


def test_xml_encoding_declaration():
    data = b'<?xml version="1.0" encoding="iso-8859-1"?><root/>'
    result = detect_markup_charset(data)
    assert result is not None
    assert result.encoding == "iso-8859-1"
    assert result.confidence < 1.0  # Declarations can lie


def test_html5_meta_charset():
    data = b'<html><head><meta charset="utf-8"></head></html>'
    result = detect_markup_charset(data)
    assert result is not None
    assert result.encoding == "utf-8"


def test_html4_content_type():
    data = (
        b"<html><head>"
        b'<meta http-equiv="Content-Type" content="text/html; charset=windows-1252">'
        b"</head></html>"
    )
    result = detect_markup_charset(data)
    assert result is not None
    assert result.encoding == "windows-1252"


def test_no_markup():
    result = detect_markup_charset(b"Just plain text with no HTML or XML")
    assert result is None


def test_empty_input():
    result = detect_markup_charset(b"")
    assert result is None


def test_xml_single_quotes():
    data = b"<?xml version='1.0' encoding='shift_jis'?><root/>"
    result = detect_markup_charset(data)
    assert result is not None
    assert result.encoding == "shift_jis"


def test_case_insensitive_meta():
    data = b'<META CHARSET="UTF-8">'
    result = detect_markup_charset(data)
    assert result is not None
    assert result.encoding == "utf-8"


def test_charset_with_whitespace():
    data = b'<meta charset = "utf-8" >'
    result = detect_markup_charset(data)
    assert result is not None
    assert result.encoding == "utf-8"


def test_unknown_encoding_returns_none():
    data = b'<meta charset="not-a-real-encoding">'
    result = detect_markup_charset(data)
    assert result is None


def test_only_scans_first_bytes():
    # Charset deep in the document should still be found if within scan limit
    padding = b"<!-- " + b"x" * 2000 + b" -->"
    data = padding + b'<meta charset="utf-8">'
    result = detect_markup_charset(data)
    assert result is not None
```

**Step 2: Run tests to verify they fail**

```bash
uv run pytest tests/test_markup.py -v
```

**Step 3: Write the implementation**

Use `re` module to scan the first ~4KB of input for:
1. `<?xml ... encoding="..."?>`
2. `<meta charset="...">`
3. `<meta http-equiv="Content-Type" content="...; charset=...">`

Validate that the extracted encoding name is recognized by `codecs.lookup()`.
Return `DetectionResult` with confidence ~0.95 (high but not 1.0 — markup can
lie). Return `None` if no declaration found or encoding name is invalid.

```python
# src/chardet/pipeline/markup.py
"""Stage 1: HTML/XML charset declaration extraction."""

from __future__ import annotations

import codecs
import re

from chardet.pipeline import DetectionResult

_SCAN_LIMIT = 4096
_MARKUP_CONFIDENCE = 0.95

_XML_ENCODING_RE = re.compile(
    rb"""<\?xml[^>]+encoding\s*=\s*['"]([^'"]+)['"]""", re.IGNORECASE
)
_HTML5_CHARSET_RE = re.compile(
    rb"""<meta[^>]+charset\s*=\s*['"]?\s*([^\s'">;]+)""", re.IGNORECASE
)
_HTML4_CONTENT_TYPE_RE = re.compile(
    rb"""<meta[^>]+content\s*=\s*['"][^'"]*charset=([^\s'">;]+)""", re.IGNORECASE
)


def _normalize_encoding(name: bytes) -> str | None:
    """Validate and normalize an encoding name via codecs.lookup()."""
    try:
        codec_info = codecs.lookup(name.decode("ascii"))
        return codec_info.name
    except (LookupError, UnicodeDecodeError, ValueError):
        return None


def detect_markup_charset(data: bytes) -> DetectionResult | None:
    """Extract charset from HTML/XML declarations. Returns result or None."""
    if not data:
        return None

    head = data[:_SCAN_LIMIT]

    for pattern in (_XML_ENCODING_RE, _HTML5_CHARSET_RE, _HTML4_CONTENT_TYPE_RE):
        match = pattern.search(head)
        if match:
            encoding = _normalize_encoding(match.group(1))
            if encoding is not None:
                return DetectionResult(
                    encoding=encoding,
                    confidence=_MARKUP_CONFIDENCE,
                    language=None,
                )

    return None
```

**Step 4: Run tests to verify they pass**

```bash
uv run pytest tests/test_markup.py -v
```

**Step 5: Commit**

```bash
uv run ruff check . && uv run ruff format .
git add src/chardet/pipeline/markup.py tests/test_markup.py
git commit -m "feat: add Stage 1d markup charset extraction"
```

---

### Task 10: Stage 2a — Byte Validity Filtering

**Files:**
- Create: `src/chardet/pipeline/validity.py`
- Create: `tests/test_validity.py`

**Step 1: Write the failing tests**

```python
# tests/test_validity.py
from chardet.enums import EncodingEra
from chardet.pipeline.validity import filter_by_validity
from chardet.registry import REGISTRY, get_candidates


def test_utf8_text_valid_under_utf8():
    data = "Héllo wörld".encode("utf-8")
    candidates = get_candidates(EncodingEra.ALL)
    valid = filter_by_validity(data, candidates)
    valid_names = {e.name for e in valid}
    assert "utf-8" in valid_names


def test_latin1_text_invalid_under_strict_multibyte():
    data = "Héllo".encode("latin-1")  # \xe9 — not valid Shift-JIS
    candidates = get_candidates(EncodingEra.ALL)
    valid = filter_by_validity(data, candidates)
    valid_names = {e.name for e in valid}
    # latin-1 should survive (it accepts any byte)
    assert "iso-8859-1" in valid_names


def test_shift_jis_text_valid_under_shift_jis():
    data = "こんにちは".encode("shift_jis")
    candidates = get_candidates(EncodingEra.ALL)
    valid = filter_by_validity(data, candidates)
    valid_names = {e.name for e in valid}
    assert "shift_jis" in valid_names


def test_eliminates_impossible_encodings():
    data = "Привет".encode("windows-1251")  # Cyrillic
    candidates = get_candidates(EncodingEra.ALL)
    valid = filter_by_validity(data, candidates)
    # Should have fewer candidates than we started with
    assert len(valid) < len(candidates)


def test_empty_input_returns_all():
    candidates = get_candidates(EncodingEra.MODERN_WEB)
    valid = filter_by_validity(b"", candidates)
    assert len(valid) == len(candidates)


def test_returns_tuple():
    candidates = get_candidates(EncodingEra.MODERN_WEB)
    valid = filter_by_validity(b"Hello", candidates)
    assert isinstance(valid, tuple)
```

**Step 2: Run tests to verify they fail**

```bash
uv run pytest tests/test_validity.py -v
```

**Step 3: Write the implementation**

```python
# src/chardet/pipeline/validity.py
"""Stage 2a: Byte sequence validity filtering."""

from __future__ import annotations

from chardet.registry import EncodingInfo


def filter_by_validity(
    data: bytes, candidates: tuple[EncodingInfo, ...]
) -> tuple[EncodingInfo, ...]:
    """Filter candidates to only those where data decodes without errors."""
    if not data:
        return candidates

    valid = []
    for enc in candidates:
        try:
            data.decode(enc.python_codec, errors="strict")
            valid.append(enc)
        except (UnicodeDecodeError, LookupError):
            continue
    return tuple(valid)
```

**Step 4: Run tests to verify they pass**

```bash
uv run pytest tests/test_validity.py -v
```

**Step 5: Commit**

```bash
uv run ruff check . && uv run ruff format .
git add src/chardet/pipeline/validity.py tests/test_validity.py
git commit -m "feat: add Stage 2a byte validity filtering"
```

---

### Task 11: Stage 2b — Multi-Byte Structural Probing

**Files:**
- Create: `src/chardet/pipeline/structural.py`
- Create: `tests/test_structural.py`

**Step 1: Write the failing tests**

```python
# tests/test_structural.py
from chardet.pipeline.structural import compute_structural_score
from chardet.registry import REGISTRY


def _get_encoding(name: str):
    return next(e for e in REGISTRY if e.name == name)


def test_shift_jis_scores_high_on_shift_jis_data():
    data = "こんにちは世界".encode("shift_jis")
    score = compute_structural_score(data, _get_encoding("shift_jis"))
    assert score > 0.7


def test_euc_jp_scores_high_on_euc_jp_data():
    data = "こんにちは世界".encode("euc-jp")
    score = compute_structural_score(data, _get_encoding("euc-jp"))
    assert score > 0.7


def test_shift_jis_scores_low_on_euc_jp_data():
    data = "こんにちは世界".encode("euc-jp")
    euc_score = compute_structural_score(data, _get_encoding("euc-jp"))
    sjis_score = compute_structural_score(data, _get_encoding("shift_jis"))
    assert euc_score > sjis_score


def test_euc_kr_scores_high_on_korean_data():
    data = "안녕하세요".encode("euc-kr")
    score = compute_structural_score(data, _get_encoding("euc-kr"))
    assert score > 0.7


def test_gb18030_scores_high_on_chinese_data():
    data = "你好世界".encode("gb18030")
    score = compute_structural_score(data, _get_encoding("gb18030"))
    assert score > 0.7


def test_big5_scores_high_on_big5_data():
    data = "你好世界".encode("big5")
    score = compute_structural_score(data, _get_encoding("big5"))
    assert score > 0.7


def test_single_byte_encoding_returns_zero():
    data = b"Hello world"
    enc = _get_encoding("iso-8859-1")
    score = compute_structural_score(data, enc)
    assert score == 0.0


def test_empty_data_returns_zero():
    score = compute_structural_score(b"", _get_encoding("shift_jis"))
    assert score == 0.0
```

**Step 2: Run tests to verify they fail**

```bash
uv run pytest tests/test_structural.py -v
```

**Step 3: Write the implementation**

Implement `compute_structural_score(data, encoding_info) -> float` that returns
0.0-1.0 based on how well the byte patterns match the encoding's expected
multi-byte structure. For single-byte encodings, always return 0.0.

For each multi-byte encoding, define the expected lead byte ranges and trail
byte ranges. Score = (valid multi-byte pairs) / (total bytes that could be
lead bytes). Specific byte range specs per encoding:

- **Shift_JIS / CP932:** Lead 0x81-0x9F,0xE0-0xEF; Trail 0x40-0x7E,0x80-0xFC
- **EUC-JP:** Lead 0xA1-0xFE; Trail 0xA1-0xFE (also SS2: 0x8E + 0xA1-0xDF)
- **EUC-KR / CP949:** Lead 0xA1-0xFE; Trail 0xA1-0xFE
- **GB18030 / GB2312:** Lead 0xA1-0xF7; Trail 0xA1-0xFE (2-byte); also 4-byte
- **Big5:** Lead 0xA1-0xF9; Trail 0x40-0x7E,0xA1-0xFE
- **ISO-2022-JP/KR:** Escape-sequence based — check for ESC sequences
- **HZ-GB-2312:** Tilde-escape based — check for ~{ and ~} markers
- **Johab:** Lead 0x84-0xD3,0xD8-0xDE,0xE0-0xF9; Trail 0x31-0x7E,0x91-0xFE

The function should iterate through bytes, identify sequences that match the
structural pattern, and compute the ratio of well-formed sequences.

**Step 4: Run tests to verify they pass**

```bash
uv run pytest tests/test_structural.py -v
```

**Step 5: Commit**

```bash
uv run ruff check . && uv run ruff format .
git add src/chardet/pipeline/structural.py tests/test_structural.py
git commit -m "feat: add Stage 2b multi-byte structural probing"
```

---

### Task 12: Model Format, Loading, and Training Script

**Files:**
- Create: `src/chardet/models/__init__.py`
- Create: `tests/test_models.py`
- Create: `scripts/train.py`

This task has two parts: (A) the model loading code used at runtime, and (B) the
training script that produces the model file.

**Part A: Model loading**

**Step 1: Write the failing tests for model loading**

```python
# tests/test_models.py
from chardet.models import load_models, score_bigrams


def test_load_models_returns_dict():
    models = load_models()
    assert isinstance(models, dict)


def test_load_models_has_entries():
    models = load_models()
    assert len(models) > 0


def test_model_keys_are_strings():
    models = load_models()
    for key in models:
        assert isinstance(key, str)


def test_score_bigrams_returns_float():
    models = load_models()
    # Pick any encoding that has a model
    encoding = next(iter(models))
    score = score_bigrams(b"Hello world this is a test", encoding, models)
    assert isinstance(score, float)
    assert 0.0 <= score <= 1.0


def test_score_bigrams_unknown_encoding():
    models = load_models()
    score = score_bigrams(b"Hello", "not-a-real-encoding", models)
    assert score == 0.0


def test_score_bigrams_empty_data():
    models = load_models()
    encoding = next(iter(models))
    score = score_bigrams(b"", encoding, models)
    assert score == 0.0
```

**Step 2: Run tests to verify they fail**

```bash
uv run pytest tests/test_models.py -v
```

**Step 3: Write the model loading implementation**

```python
# src/chardet/models/__init__.py
"""Model loading and bigram scoring utilities."""

from __future__ import annotations

import importlib.resources
import struct

_MODEL_CACHE: dict[str, dict[tuple[int, int], int]] | None = None

# Header format for models.bin:
# - 4 bytes: uint32 number of encodings
# For each encoding:
# - 4 bytes: uint32 encoding name length
# - N bytes: encoding name (utf-8)
# - 4 bytes: uint32 number of bigram entries
# For each bigram entry:
# - 3 bytes: byte1 (uint8), byte2 (uint8), weight (uint8)


def load_models() -> dict[str, dict[tuple[int, int], int]]:
    """Load all bigram models from the bundled models.bin file."""
    global _MODEL_CACHE
    if _MODEL_CACHE is not None:
        return _MODEL_CACHE

    models: dict[str, dict[tuple[int, int], int]] = {}

    ref = importlib.resources.files("chardet.models").joinpath("models.bin")
    data = ref.read_bytes()

    if not data:
        _MODEL_CACHE = models
        return models

    offset = 0
    (num_encodings,) = struct.unpack_from("!I", data, offset)
    offset += 4

    for _ in range(num_encodings):
        (name_len,) = struct.unpack_from("!I", data, offset)
        offset += 4
        name = data[offset : offset + name_len].decode("utf-8")
        offset += name_len
        (num_entries,) = struct.unpack_from("!I", data, offset)
        offset += 4

        bigrams: dict[tuple[int, int], int] = {}
        for _ in range(num_entries):
            b1, b2, weight = struct.unpack_from("!BBB", data, offset)
            offset += 3
            bigrams[(b1, b2)] = weight

        models[name] = bigrams

    _MODEL_CACHE = models
    return models


def score_bigrams(
    data: bytes,
    encoding: str,
    models: dict[str, dict[tuple[int, int], int]],
) -> float:
    """Score data against a specific encoding's bigram model. Returns 0.0-1.0."""
    if not data or encoding not in models:
        return 0.0

    model = models[encoding]
    if not model:
        return 0.0

    # Compute bigram hits
    total_bigrams = len(data) - 1
    if total_bigrams <= 0:
        return 0.0

    score = 0
    max_possible = 0
    for i in range(total_bigrams):
        pair = (data[i], data[i + 1])
        if pair in model:
            score += model[pair]
        max_possible += 255  # Maximum possible weight

    if max_possible == 0:
        return 0.0

    return score / max_possible
```

**Step 4: Create an empty models.bin placeholder**

Create `src/chardet/models/models.bin` as an empty file initially. The training
script will populate it.

For tests to pass before training, create a minimal models.bin with at least one
encoding. Write a small helper script or add a test fixture that creates a
minimal binary model file.

**Step 5: Run tests to verify they pass**

```bash
uv run pytest tests/test_models.py -v
```

**Step 6: Commit model loading code**

```bash
uv run ruff check . && uv run ruff format .
git add src/chardet/models/__init__.py src/chardet/models/models.bin tests/test_models.py
git commit -m "feat: add model loading and bigram scoring"
```

**Part B: Training script**

**Step 7: Add training dev dependencies**

```bash
uv add --dev datasets
```

**Step 8: Write the training script**

Create `scripts/train.py` that:

1. Uses `datasets` library to load Wikipedia articles for each target language
2. Also loads HTML/web content (e.g., from `oscar-corpus/OSCAR-2301` or similar
   web crawl dataset on Hugging Face that includes markup)
3. For each target encoding:
   a. Takes the UTF-8 source text and encodes it into the target encoding
      (using `text.encode(encoding, errors='ignore')` — skip chars that can't
      be encoded)
   b. Computes byte bigram frequency counts
4. Normalizes frequencies to uint8 (0-255) weights
5. Prunes bigrams below a threshold to keep models sparse
6. Serializes to `src/chardet/models/models.bin` using the binary format
   described above
7. Caches downloaded data in `data/` directory (gitignored)
8. Prints stats: number of encodings, total model size, per-encoding entry counts

The script should accept CLI args:
- `--output`: output path (default: `src/chardet/models/models.bin`)
- `--cache-dir`: data cache directory (default: `data/`)
- `--min-weight`: minimum bigram weight to keep (default: 1)
- `--max-samples`: max text samples per language (default: 1000)

Map each target encoding to appropriate Wikipedia language codes. For example:
- `shift_jis` → Japanese (`ja`)
- `euc-kr` → Korean (`ko`)
- `gb18030` → Chinese (`zh`)
- `iso-8859-1` → English, French, German, Spanish, etc.
- `windows-1251` → Russian (`ru`)
- `iso-8859-7` → Greek (`el`)
- etc.

**Step 9: Run the training script**

```bash
uv run python scripts/train.py --max-samples 100
```

This should produce `src/chardet/models/models.bin`. Verify it's non-empty.

**Step 10: Re-run model loading tests with real models**

```bash
uv run pytest tests/test_models.py -v
```

**Step 11: Commit training script and generated models**

```bash
uv run ruff check . && uv run ruff format .
git add scripts/train.py src/chardet/models/models.bin
git commit -m "feat: add training script and initial bigram models"
```

---

### Task 13: Stage 3 — Statistical Scoring with Parallelism

**Files:**
- Create: `src/chardet/pipeline/statistical.py`
- Create: `tests/test_statistical.py`

**Step 1: Write the failing tests**

```python
# tests/test_statistical.py
from chardet.pipeline.statistical import score_candidates
from chardet.registry import REGISTRY, get_candidates
from chardet.enums import EncodingEra


def _get_encoding(name: str):
    return next(e for e in REGISTRY if e.name == name)


def test_score_candidates_returns_sorted_results():
    data = "Héllo wörld".encode("windows-1252")
    candidates = get_candidates(EncodingEra.MODERN_WEB)
    results = score_candidates(data, candidates)
    # Results should be sorted by confidence descending
    confidences = [r.confidence for r in results]
    assert confidences == sorted(confidences, reverse=True)


def test_score_candidates_returns_detection_results():
    from chardet.pipeline import DetectionResult

    data = "Hello world".encode("utf-8")
    candidates = get_candidates(EncodingEra.MODERN_WEB)
    results = score_candidates(data, candidates)
    for r in results:
        assert isinstance(r, DetectionResult)


def test_score_candidates_empty_data():
    candidates = get_candidates(EncodingEra.MODERN_WEB)
    results = score_candidates(b"", candidates)
    assert len(results) == 0


def test_score_candidates_empty_candidates():
    results = score_candidates(b"Hello", ())
    assert len(results) == 0


def test_score_candidates_small_set_no_pool():
    # With very few candidates, should work without process pool
    candidates = tuple(
        e for e in get_candidates(EncodingEra.MODERN_WEB) if e.name == "utf-8"
    )
    results = score_candidates(b"Hello", candidates)
    assert len(results) <= len(candidates)


def test_correct_encoding_scores_highest():
    text = "Привет мир, как дела?".encode("windows-1251")
    candidates = (
        _get_encoding("windows-1251"),
        _get_encoding("iso-8859-1"),
    )
    results = score_candidates(text, candidates)
    assert len(results) > 0
    assert results[0].encoding == "windows-1251"
```

**Step 2: Run tests to verify they fail**

```bash
uv run pytest tests/test_statistical.py -v
```

**Step 3: Write the implementation**

```python
# src/chardet/pipeline/statistical.py
"""Stage 3: Statistical bigram scoring with optional parallelism."""

from __future__ import annotations

import concurrent.futures
import os

from chardet.models import load_models, score_bigrams
from chardet.pipeline import DetectionResult
from chardet.registry import EncodingInfo

_PARALLEL_THRESHOLD = 6  # Use pool only if more candidates than this

_pool: concurrent.futures.ProcessPoolExecutor | None = None


def _get_pool() -> concurrent.futures.ProcessPoolExecutor:
    global _pool
    if _pool is None:
        workers = int(os.environ.get("CHARDET_WORKERS", 0)) or os.cpu_count() or 1
        if workers <= 1:
            raise RuntimeError("Parallelism disabled")
        _pool = concurrent.futures.ProcessPoolExecutor(max_workers=workers)
    return _pool


def _score_one(data: bytes, encoding_name: str) -> tuple[str, float]:
    """Score a single encoding — callable by pool workers."""
    models = load_models()
    return (encoding_name, score_bigrams(data, encoding_name, models))


def score_candidates(
    data: bytes, candidates: tuple[EncodingInfo, ...]
) -> list[DetectionResult]:
    """Score all candidates and return results sorted by confidence descending."""
    if not data or not candidates:
        return []

    models = load_models()
    scores: list[tuple[str, float]] = []

    use_parallel = (
        len(candidates) > _PARALLEL_THRESHOLD
        and os.environ.get("CHARDET_WORKERS") != "1"
    )

    if use_parallel:
        try:
            pool = _get_pool()
            futures = {
                pool.submit(_score_one, data, enc.name): enc for enc in candidates
            }
            for future in concurrent.futures.as_completed(futures):
                try:
                    scores.append(future.result())
                except Exception:
                    enc = futures[future]
                    scores.append((enc.name, 0.0))
        except (RuntimeError, OSError):
            # Pool failed — fall back to sequential
            use_parallel = False

    if not use_parallel:
        for enc in candidates:
            s = score_bigrams(data, enc.name, models)
            scores.append((enc.name, s))

    # Sort by score descending
    scores.sort(key=lambda x: x[1], reverse=True)

    # Normalize scores to confidence values
    max_score = scores[0][1] if scores else 0.0
    results = []
    for name, s in scores:
        if s <= 0.0:
            continue
        confidence = s / max_score if max_score > 0 else 0.0
        results.append(
            DetectionResult(encoding=name, confidence=confidence, language=None)
        )

    return results
```

**Step 4: Run tests to verify they pass**

```bash
uv run pytest tests/test_statistical.py -v
```

Note: the `test_correct_encoding_scores_highest` test depends on having
reasonable trained models. If it fails, retrain with more data and re-run.

**Step 5: Commit**

```bash
uv run ruff check . && uv run ruff format .
git add src/chardet/pipeline/statistical.py tests/test_statistical.py
git commit -m "feat: add Stage 3 statistical scoring with parallel support"
```

---

### Task 14: Pipeline Orchestrator

**Files:**
- Create: `src/chardet/pipeline/orchestrator.py`
- Create: `tests/test_orchestrator.py`

**Step 1: Write the failing tests**

```python
# tests/test_orchestrator.py
from chardet.enums import EncodingEra
from chardet.pipeline import DetectionResult
from chardet.pipeline.orchestrator import run_pipeline


def test_empty_input():
    result = run_pipeline(b"", EncodingEra.MODERN_WEB)
    assert result == [DetectionResult(None, 0.0, None)]


def test_bom_detected():
    data = b"\xef\xbb\xbfHello"
    result = run_pipeline(data, EncodingEra.ALL)
    assert result[0].encoding == "utf-8-sig"
    assert result[0].confidence == 1.0


def test_pure_ascii():
    result = run_pipeline(b"Hello world 123", EncodingEra.ALL)
    assert result[0].encoding == "ascii"
    assert result[0].confidence == 1.0


def test_utf8_multibyte():
    data = "Héllo wörld café".encode("utf-8")
    result = run_pipeline(data, EncodingEra.ALL)
    assert result[0].encoding == "utf-8"
    assert result[0].confidence >= 0.9


def test_binary_content():
    data = b"\x00\x01\x02\x03\x04\x05" * 100
    result = run_pipeline(data, EncodingEra.ALL)
    assert result[0].encoding is None


def test_xml_charset_declaration():
    data = b'<?xml version="1.0" encoding="iso-8859-1"?><root>Hello</root>'
    result = run_pipeline(data, EncodingEra.ALL)
    assert result[0].encoding == "iso-8859-1"


def test_max_bytes_truncation():
    data = b"Hello" * 100_000
    result = run_pipeline(data, EncodingEra.ALL, max_bytes=100)
    assert result[0] is not None


def test_returns_list():
    result = run_pipeline(b"Hello", EncodingEra.ALL)
    assert isinstance(result, list)
    assert all(isinstance(r, DetectionResult) for r in result)


def test_encoding_era_filtering():
    # Should work with any era filter
    data = "Hello world".encode("ascii")
    for era in EncodingEra:
        result = run_pipeline(data, era)
        assert len(result) >= 1
```

**Step 2: Run tests to verify they fail**

```bash
uv run pytest tests/test_orchestrator.py -v
```

**Step 3: Write the implementation**

```python
# src/chardet/pipeline/orchestrator.py
"""Pipeline orchestrator — runs all detection stages in sequence."""

from __future__ import annotations

from chardet.enums import EncodingEra
from chardet.pipeline import DetectionResult
from chardet.pipeline.ascii import detect_ascii
from chardet.pipeline.binary import is_binary
from chardet.pipeline.bom import detect_bom
from chardet.pipeline.markup import detect_markup_charset
from chardet.pipeline.statistical import score_candidates
from chardet.pipeline.structural import compute_structural_score
from chardet.pipeline.utf8 import detect_utf8
from chardet.pipeline.validity import filter_by_validity
from chardet.registry import get_candidates

_NONE_RESULT = DetectionResult(encoding=None, confidence=0.0, language=None)
_STRUCTURAL_CONFIDENCE_THRESHOLD = 0.85


def run_pipeline(
    data: bytes,
    encoding_era: EncodingEra,
    max_bytes: int = 200_000,
) -> list[DetectionResult]:
    """Run the full detection pipeline. Returns list of results sorted by confidence."""
    data = data[:max_bytes]

    if not data:
        return [_NONE_RESULT]

    # Stage 0: Binary detection
    if is_binary(data, max_bytes=max_bytes):
        return [_NONE_RESULT]

    # Stage 1: Deterministic checks
    # 1a: BOM
    bom_result = detect_bom(data)
    if bom_result is not None:
        return [bom_result]

    # 1b: ASCII
    ascii_result = detect_ascii(data)
    if ascii_result is not None:
        return [ascii_result]

    # 1c: UTF-8 structural validation
    utf8_result = detect_utf8(data)
    if utf8_result is not None:
        return [utf8_result]

    # 1d: Markup charset extraction
    markup_result = detect_markup_charset(data)
    if markup_result is not None:
        return [markup_result]

    # Stage 2a: Byte validity filtering
    candidates = get_candidates(encoding_era)
    valid_candidates = filter_by_validity(data, candidates)

    if not valid_candidates:
        return [_NONE_RESULT]

    # Stage 2b: Structural probing for multi-byte encodings
    structural_scores: list[tuple[str, float]] = []
    remaining_candidates = []
    for enc in valid_candidates:
        if enc.is_multibyte:
            score = compute_structural_score(data, enc)
            if score > 0.0:
                structural_scores.append((enc.name, score))
            if score < _STRUCTURAL_CONFIDENCE_THRESHOLD:
                remaining_candidates.append(enc)
        else:
            remaining_candidates.append(enc)

    # If a multi-byte encoding scored very high, return it directly
    if structural_scores:
        structural_scores.sort(key=lambda x: x[1], reverse=True)
        best_name, best_score = structural_scores[0]
        if best_score >= _STRUCTURAL_CONFIDENCE_THRESHOLD:
            results = [
                DetectionResult(encoding=name, confidence=score, language=None)
                for name, score in structural_scores
            ]
            # Also include statistical results for remaining candidates
            if remaining_candidates:
                stat_results = score_candidates(data, tuple(remaining_candidates))
                results.extend(stat_results)
            results.sort(key=lambda r: r.confidence, reverse=True)
            return results

    # Stage 3: Statistical scoring
    all_for_scoring = tuple(remaining_candidates)
    # Also include multibyte encodings that didn't score high enough structurally
    for enc in valid_candidates:
        if enc.is_multibyte and enc not in remaining_candidates:
            all_for_scoring = (*all_for_scoring, enc)

    results = score_candidates(data, all_for_scoring)

    if not results:
        return [_NONE_RESULT]

    return results
```

**Step 4: Run tests to verify they pass**

```bash
uv run pytest tests/test_orchestrator.py -v
```

**Step 5: Commit**

```bash
uv run ruff check . && uv run ruff format .
git add src/chardet/pipeline/orchestrator.py tests/test_orchestrator.py
git commit -m "feat: add pipeline orchestrator connecting all stages"
```

---

### Task 15: Public API — detect() and detect_all()

**Files:**
- Modify: `src/chardet/__init__.py`
- Create: `tests/test_api.py`

**Step 1: Write the failing tests**

```python
# tests/test_api.py
import chardet
from chardet.enums import EncodingEra


def test_detect_returns_dict():
    result = chardet.detect(b"Hello world")
    assert isinstance(result, dict)
    assert "encoding" in result
    assert "confidence" in result
    assert "language" in result


def test_detect_ascii():
    result = chardet.detect(b"Hello world")
    assert result["encoding"] == "ascii"
    assert result["confidence"] == 1.0


def test_detect_utf8_bom():
    result = chardet.detect(b"\xef\xbb\xbfHello")
    assert result["encoding"] == "utf-8-sig"


def test_detect_utf8_multibyte():
    data = "Héllo wörld café".encode("utf-8")
    result = chardet.detect(data)
    assert result["encoding"] == "utf-8"


def test_detect_empty():
    result = chardet.detect(b"")
    assert result["encoding"] is None
    assert result["confidence"] == 0.0


def test_detect_with_encoding_era():
    data = "Hello world".encode("ascii")
    result = chardet.detect(data, encoding_era=EncodingEra.MODERN_WEB)
    assert result["encoding"] is not None


def test_detect_with_max_bytes():
    data = "Hello world".encode("utf-8") * 100_000
    result = chardet.detect(data, max_bytes=100)
    assert result is not None


def test_detect_all_returns_list():
    result = chardet.detect_all(b"Hello world")
    assert isinstance(result, list)
    assert len(result) >= 1


def test_detect_all_sorted_by_confidence():
    data = "Héllo wörld".encode("utf-8")
    results = chardet.detect_all(data)
    confidences = [r["confidence"] for r in results]
    assert confidences == sorted(confidences, reverse=True)


def test_detect_all_each_is_dict():
    results = chardet.detect_all(b"Hello world")
    for r in results:
        assert "encoding" in r
        assert "confidence" in r
        assert "language" in r


def test_version_exists():
    assert hasattr(chardet, "__version__")
    assert isinstance(chardet.__version__, str)
```

**Step 2: Run tests to verify they fail**

```bash
uv run pytest tests/test_api.py -v
```

**Step 3: Write the implementation**

Update `src/chardet/__init__.py`:

```python
"""Universal character encoding detector — MIT-licensed rewrite."""

from __future__ import annotations

from chardet.enums import EncodingEra
from chardet.pipeline.orchestrator import run_pipeline

__version__ = "6.1.0"


def detect(
    data: bytes,
    max_bytes: int = 200_000,
    chunk_size: int = 65_536,
    encoding_era: EncodingEra = EncodingEra.MODERN_WEB,
) -> dict[str, str | float | None]:
    """Detect the encoding of the given byte string.

    Returns dict with 'encoding', 'confidence', and 'language' keys.
    """
    results = run_pipeline(data, encoding_era, max_bytes=max_bytes)
    return results[0].to_dict()


def detect_all(
    data: bytes,
    max_bytes: int = 200_000,
    chunk_size: int = 65_536,
    encoding_era: EncodingEra = EncodingEra.MODERN_WEB,
) -> list[dict[str, str | float | None]]:
    """Detect all possible encodings of the given byte string.

    Returns list of dicts sorted by confidence descending.
    """
    results = run_pipeline(data, encoding_era, max_bytes=max_bytes)
    return [r.to_dict() for r in results]
```

**Step 4: Run tests to verify they pass**

```bash
uv run pytest tests/test_api.py -v
```

**Step 5: Commit**

```bash
uv run ruff check . && uv run ruff format .
git add src/chardet/__init__.py tests/test_api.py
git commit -m "feat: add detect() and detect_all() public API"
```

---

### Task 16: UniversalDetector

**Files:**
- Create: `src/chardet/detector.py`
- Create: `tests/test_detector.py`

**Step 1: Write the failing tests**

```python
# tests/test_detector.py
import pytest

from chardet.detector import UniversalDetector
from chardet.enums import EncodingEra


def test_basic_lifecycle():
    detector = UniversalDetector()
    detector.feed(b"Hello world")
    detector.close()
    result = detector.result
    assert result["encoding"] is not None


def test_result_before_close():
    detector = UniversalDetector()
    detector.feed(b"Hello world")
    result = detector.result
    # Should return best guess so far (may be None)
    assert "encoding" in result
    assert "confidence" in result
    assert "language" in result


def test_reset():
    detector = UniversalDetector()
    detector.feed(b"Hello world")
    detector.close()
    detector.reset()
    result = detector.result
    assert result["encoding"] is None
    assert result["confidence"] == 0.0


def test_done_property():
    detector = UniversalDetector()
    assert detector.done is False


def test_done_after_bom():
    detector = UniversalDetector()
    detector.feed(b"\xef\xbb\xbfHello")
    assert detector.done is True
    assert detector.result["encoding"] == "utf-8-sig"


def test_feed_after_close_raises():
    detector = UniversalDetector()
    detector.feed(b"Hello")
    detector.close()
    with pytest.raises(ValueError):
        detector.feed(b"more data")


def test_feed_after_done_is_ignored():
    detector = UniversalDetector()
    detector.feed(b"\xef\xbb\xbfHello")
    assert detector.done is True
    # Should not raise, just silently ignore
    detector.feed(b"more data")


def test_multiple_feeds():
    detector = UniversalDetector()
    data = "Héllo wörld café".encode("utf-8")
    # Feed in chunks
    chunk_size = 5
    for i in range(0, len(data), chunk_size):
        detector.feed(data[i : i + chunk_size])
    detector.close()
    assert detector.result["encoding"] is not None


def test_encoding_era_parameter():
    detector = UniversalDetector(encoding_era=EncodingEra.MODERN_WEB)
    detector.feed(b"Hello world")
    detector.close()
    assert detector.result is not None


def test_max_bytes_parameter():
    detector = UniversalDetector(max_bytes=100)
    detector.feed(b"x" * 200)
    detector.close()
    assert detector.result is not None
```

**Step 2: Run tests to verify they fail**

```bash
uv run pytest tests/test_detector.py -v
```

**Step 3: Write the implementation**

```python
# src/chardet/detector.py
"""UniversalDetector — streaming encoding detection."""

from __future__ import annotations

from chardet.enums import EncodingEra
from chardet.pipeline.bom import detect_bom
from chardet.pipeline.orchestrator import run_pipeline

_NONE_RESULT: dict[str, str | float | None] = {
    "encoding": None,
    "confidence": 0.0,
    "language": None,
}


class UniversalDetector:
    """Streaming character encoding detector.

    Feed data incrementally with feed(), then call close() to finalize.
    """

    def __init__(
        self,
        encoding_era: EncodingEra = EncodingEra.MODERN_WEB,
        max_bytes: int = 200_000,
    ) -> None:
        self._encoding_era = encoding_era
        self._max_bytes = max_bytes
        self._buffer = bytearray()
        self._done = False
        self._closed = False
        self._result: dict[str, str | float | None] | None = None

    def feed(self, data: bytes) -> None:
        """Process a chunk of data."""
        if self._closed:
            raise ValueError("feed() called after close() without reset()")
        if self._done:
            return

        remaining = self._max_bytes - len(self._buffer)
        if remaining > 0:
            self._buffer.extend(data[:remaining])

        # Check for early exit via BOM
        if len(self._buffer) >= 4 and self._result is None:
            bom_result = detect_bom(bytes(self._buffer))
            if bom_result is not None:
                self._result = bom_result.to_dict()
                self._done = True

    def close(self) -> None:
        """Finalize detection after all data has been fed."""
        if self._closed:
            return
        self._closed = True

        if self._result is not None:
            return

        data = bytes(self._buffer)
        results = run_pipeline(data, self._encoding_era, max_bytes=self._max_bytes)
        self._result = results[0].to_dict()
        self._done = True

    def reset(self) -> None:
        """Reset detector state for reuse."""
        self._buffer = bytearray()
        self._done = False
        self._closed = False
        self._result = None

    @property
    def done(self) -> bool:
        """True when detection is confident enough to stop feeding."""
        return self._done

    @property
    def result(self) -> dict[str, str | float | None]:
        """Detection result dict with 'encoding', 'confidence', 'language'."""
        if self._result is not None:
            return self._result
        return dict(_NONE_RESULT)
```

**Step 4: Run tests to verify they pass**

```bash
uv run pytest tests/test_detector.py -v
```

**Step 5: Export UniversalDetector from chardet.__init__**

Add to `src/chardet/__init__.py`:

```python
from chardet.detector import UniversalDetector
```

**Step 6: Commit**

```bash
uv run ruff check . && uv run ruff format .
git add src/chardet/detector.py tests/test_detector.py src/chardet/__init__.py
git commit -m "feat: add UniversalDetector streaming API"
```

---

### Task 17: CLI — chardetect

**Files:**
- Create: `src/chardet/cli.py`
- Create: `tests/test_cli.py`

**Step 1: Write the failing tests**

```python
# tests/test_cli.py
import subprocess
import sys
import tempfile
from pathlib import Path


def test_cli_detects_file(tmp_path: Path):
    f = tmp_path / "test.txt"
    f.write_bytes("Hello world".encode("ascii"))
    result = subprocess.run(
        [sys.executable, "-m", "chardet.cli", str(f)],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "ascii" in result.stdout.lower()


def test_cli_detects_utf8_file(tmp_path: Path):
    f = tmp_path / "test.txt"
    f.write_bytes("Héllo wörld".encode("utf-8"))
    result = subprocess.run(
        [sys.executable, "-m", "chardet.cli", str(f)],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "utf-8" in result.stdout.lower()


def test_cli_stdin():
    result = subprocess.run(
        [sys.executable, "-m", "chardet.cli"],
        input=b"Hello world",
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "ascii" in result.stdout.lower()


def test_cli_version():
    result = subprocess.run(
        [sys.executable, "-m", "chardet.cli", "--version"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "6.1.0" in result.stdout


def test_cli_minimal_flag(tmp_path: Path):
    f = tmp_path / "test.txt"
    f.write_bytes(b"Hello world")
    result = subprocess.run(
        [sys.executable, "-m", "chardet.cli", "--minimal", str(f)],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    # Minimal should output just the encoding name
    assert result.stdout.strip() in ("ascii", "ASCII")


def test_cli_multiple_files(tmp_path: Path):
    f1 = tmp_path / "a.txt"
    f2 = tmp_path / "b.txt"
    f1.write_bytes(b"Hello")
    f2.write_bytes("Héllo".encode("utf-8"))
    result = subprocess.run(
        [sys.executable, "-m", "chardet.cli", str(f1), str(f2)],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    lines = result.stdout.strip().split("\n")
    assert len(lines) == 2
```

**Step 2: Run tests to verify they fail**

```bash
uv run pytest tests/test_cli.py -v
```

**Step 3: Write the implementation**

```python
# src/chardet/cli.py
"""Command-line interface for chardet."""

from __future__ import annotations

import argparse
import sys

import chardet
from chardet.enums import EncodingEra


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        description="Detect character encoding of files."
    )
    parser.add_argument("files", nargs="*", help="Files to detect encoding of")
    parser.add_argument(
        "--minimal", action="store_true", help="Output only the encoding name"
    )
    parser.add_argument(
        "--legacy", action="store_true", help="Include legacy encodings"
    )
    parser.add_argument(
        "-e",
        "--encoding-era",
        default=None,
        help="Encoding era filter (e.g., MODERN_WEB, LEGACY_ISO, ALL)",
    )
    parser.add_argument(
        "--version", action="version", version=f"chardet {chardet.__version__}"
    )

    args = parser.parse_args(argv)

    # Determine encoding era
    if args.encoding_era:
        era = EncodingEra[args.encoding_era.upper()]
    elif args.legacy:
        era = EncodingEra.ALL
    else:
        era = EncodingEra.MODERN_WEB

    # Collect inputs
    if args.files:
        for filepath in args.files:
            with open(filepath, "rb") as f:
                data = f.read()
            result = chardet.detect(data, encoding_era=era)
            if args.minimal:
                print(result["encoding"])
            else:
                print(
                    f"{filepath}: {result['encoding']} "
                    f"with confidence {result['confidence']}"
                )
    else:
        data = sys.stdin.buffer.read()
        result = chardet.detect(data, encoding_era=era)
        if args.minimal:
            print(result["encoding"])
        else:
            print(
                f"stdin: {result['encoding']} "
                f"with confidence {result['confidence']}"
            )


if __name__ == "__main__":
    main()
```

**Step 4: Run tests to verify they pass**

```bash
uv run pytest tests/test_cli.py -v
```

**Step 5: Commit**

```bash
uv run ruff check . && uv run ruff format .
git add src/chardet/cli.py tests/test_cli.py
git commit -m "feat: add chardetect CLI"
```

---

### Task 18: Accuracy Test Suite

**Files:**
- Create: `tests/test_accuracy.py`
- Create: `tests/conftest.py`

**Step 1: Write the test data fixture**

```python
# tests/conftest.py
"""Shared test fixtures."""

from __future__ import annotations

import os
import subprocess
import tempfile
from pathlib import Path

import pytest

_TEST_DATA_REPO = "https://github.com/chardet/chardet.git"
_TEST_DATA_SUBDIR = "tests"


@pytest.fixture(scope="session")
def chardet_test_data_dir() -> Path:
    """Resolve chardet test data directory.

    1. If tests/data/ exists in repo, use it (post-merge scenario).
    2. Otherwise, clone from GitHub and cache locally.
    """
    # Check for in-repo test data
    repo_root = Path(__file__).parent.parent
    local_data = repo_root / "tests" / "data"
    if local_data.is_dir() and any(local_data.iterdir()):
        return local_data

    # Clone and cache
    cache_dir = repo_root / "tests" / "data"
    if cache_dir.is_dir() and any(cache_dir.iterdir()):
        return cache_dir

    # Sparse checkout just the tests directory
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(
            ["git", "clone", "--depth=1", "--filter=blob:none",
             "--sparse", _TEST_DATA_REPO, tmp],
            check=True,
            capture_output=True,
        )
        subprocess.run(
            ["git", "sparse-checkout", "set", _TEST_DATA_SUBDIR],
            cwd=tmp,
            check=True,
            capture_output=True,
        )
        src = Path(tmp) / _TEST_DATA_SUBDIR
        cache_dir.mkdir(parents=True, exist_ok=True)
        # Copy test data files
        import shutil
        for item in src.iterdir():
            if item.name in ("__pycache__", ".git"):
                continue
            dest = cache_dir / item.name
            if item.is_dir():
                shutil.copytree(item, dest, dirs_exist_ok=True)
            else:
                shutil.copy2(item, dest)

    return cache_dir
```

**Step 2: Write the accuracy tests**

```python
# tests/test_accuracy.py
"""Accuracy evaluation against the chardet test suite."""

from __future__ import annotations

from pathlib import Path

import pytest

import chardet
from chardet.enums import EncodingEra

_MIN_OVERALL_ACCURACY = 0.75  # Start conservative, raise over time


def _collect_test_files(data_dir: Path) -> list[tuple[str, str, Path]]:
    """Collect (encoding, language, filepath) tuples from test data."""
    test_files = []
    for encoding_dir in sorted(data_dir.iterdir()):
        if not encoding_dir.is_dir():
            continue
        # Directory name format: "encoding-language" e.g. "utf-8-english"
        parts = encoding_dir.name.rsplit("-", 1)
        if len(parts) != 2:
            continue
        encoding_name, language = parts
        for filepath in sorted(encoding_dir.iterdir()):
            if filepath.is_file():
                test_files.append((encoding_name, language, filepath))
    return test_files


def test_overall_accuracy(chardet_test_data_dir: Path):
    """Test overall detection accuracy across all test files."""
    test_files = _collect_test_files(chardet_test_data_dir)
    if not test_files:
        pytest.skip("No test data found")

    correct = 0
    total = 0
    failures: list[str] = []

    for expected_encoding, language, filepath in test_files:
        data = filepath.read_bytes()
        result = chardet.detect(data, encoding_era=EncodingEra.ALL)
        detected = result["encoding"]

        total += 1
        if detected and detected.lower().replace("-", "") == expected_encoding.lower().replace("-", ""):
            correct += 1
        else:
            failures.append(
                f"  {filepath.parent.name}/{filepath.name}: "
                f"expected={expected_encoding}, got={detected} "
                f"(confidence={result['confidence']:.2f})"
            )

    accuracy = correct / total if total > 0 else 0.0
    print(f"\nAccuracy: {correct}/{total} = {accuracy:.1%}")
    if failures:
        print(f"Failures ({len(failures)}):")
        for f in failures[:20]:  # Show first 20
            print(f)
        if len(failures) > 20:
            print(f"  ... and {len(failures) - 20} more")

    assert accuracy >= _MIN_OVERALL_ACCURACY, (
        f"Overall accuracy {accuracy:.1%} below threshold {_MIN_OVERALL_ACCURACY:.0%}"
    )
```

**Step 3: Run accuracy tests**

```bash
uv run pytest tests/test_accuracy.py -v -s
```

This will clone chardet test data on first run. Review the accuracy report
and adjust the `_MIN_OVERALL_ACCURACY` threshold as models improve.

**Step 4: Commit**

```bash
uv run ruff check . && uv run ruff format .
git add tests/test_accuracy.py tests/conftest.py
git commit -m "feat: add accuracy test suite against chardet test data"
```

---

### Task 19: Benchmark Suite

**Files:**
- Create: `scripts/benchmark.py`
- Create: `tests/test_benchmark.py`

**Step 1: Write the benchmark script**

```python
# scripts/benchmark.py
"""Benchmark chardet detection speed and memory usage."""

from __future__ import annotations

import argparse
import statistics
import time
import tracemalloc
from pathlib import Path

import chardet
from chardet.enums import EncodingEra


def benchmark_file(data: bytes, iterations: int = 100) -> dict:
    """Benchmark detect() on a single data blob."""
    times = []
    for _ in range(iterations):
        start = time.perf_counter()
        chardet.detect(data, encoding_era=EncodingEra.ALL)
        elapsed = time.perf_counter() - start
        times.append(elapsed * 1000)  # Convert to ms

    return {
        "p50": statistics.median(times),
        "p95": sorted(times)[int(len(times) * 0.95)],
        "p99": sorted(times)[int(len(times) * 0.99)],
        "mean": statistics.mean(times),
    }


def benchmark_memory(data: bytes) -> int:
    """Measure peak memory usage for a detect() call."""
    tracemalloc.start()
    chardet.detect(data, encoding_era=EncodingEra.ALL)
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak


def main():
    parser = argparse.ArgumentParser(description="Benchmark chardet")
    parser.add_argument(
        "--data-dir",
        type=Path,
        default=Path("tests/data"),
        help="Path to test data directory",
    )
    parser.add_argument(
        "--iterations", type=int, default=100, help="Iterations per file"
    )
    args = parser.parse_args()

    if not args.data_dir.exists():
        print(f"Data dir {args.data_dir} not found. Run accuracy tests first.")
        return

    # Collect sample files (one per encoding)
    samples: list[tuple[str, bytes]] = []
    for enc_dir in sorted(args.data_dir.iterdir()):
        if not enc_dir.is_dir():
            continue
        for f in enc_dir.iterdir():
            if f.is_file():
                samples.append((enc_dir.name, f.read_bytes()))
                break  # One file per encoding

    print(f"Benchmarking {len(samples)} encoding samples, {args.iterations} iterations each\n")
    print(f"{'Encoding':<30} {'p50 (ms)':>10} {'p95 (ms)':>10} {'p99 (ms)':>10} {'Mem (KB)':>10}")
    print("-" * 75)

    all_p50s = []
    for name, data in samples:
        stats = benchmark_file(data, args.iterations)
        mem = benchmark_memory(data)
        all_p50s.append(stats["p50"])
        print(
            f"{name:<30} {stats['p50']:>10.2f} {stats['p95']:>10.2f} "
            f"{stats['p99']:>10.2f} {mem // 1024:>10}"
        )

    print("-" * 75)
    print(f"{'Overall median p50':<30} {statistics.median(all_p50s):>10.2f} ms")


if __name__ == "__main__":
    main()
```

**Step 2: Write the benchmark regression test**

```python
# tests/test_benchmark.py
"""Performance regression tests. Run with: pytest -m benchmark"""

import time

import pytest

import chardet
from chardet.enums import EncodingEra

pytestmark = pytest.mark.benchmark


def test_ascii_detection_speed():
    """ASCII detection should be very fast (deterministic Stage 1)."""
    data = b"Hello world, this is a plain ASCII text." * 100
    start = time.perf_counter()
    for _ in range(1000):
        chardet.detect(data)
    elapsed = time.perf_counter() - start
    per_call_ms = (elapsed / 1000) * 1000
    assert per_call_ms < 1.0, f"ASCII detection too slow: {per_call_ms:.2f}ms"


def test_utf8_detection_speed():
    """UTF-8 detection should be fast (deterministic Stage 1)."""
    data = "Héllo wörld café résumé naïve".encode("utf-8") * 100
    start = time.perf_counter()
    for _ in range(1000):
        chardet.detect(data)
    elapsed = time.perf_counter() - start
    per_call_ms = (elapsed / 1000) * 1000
    assert per_call_ms < 5.0, f"UTF-8 detection too slow: {per_call_ms:.2f}ms"


def test_bom_detection_speed():
    """BOM detection should be nearly instant."""
    data = b"\xef\xbb\xbfHello world" * 100
    start = time.perf_counter()
    for _ in range(1000):
        chardet.detect(data)
    elapsed = time.perf_counter() - start
    per_call_ms = (elapsed / 1000) * 1000
    assert per_call_ms < 1.0, f"BOM detection too slow: {per_call_ms:.2f}ms"
```

**Step 3: Run benchmarks**

```bash
uv run pytest tests/test_benchmark.py -m benchmark -v
uv run python scripts/benchmark.py --iterations 50
```

**Step 4: Commit**

```bash
uv run ruff check . && uv run ruff format .
git add scripts/benchmark.py tests/test_benchmark.py
git commit -m "feat: add benchmark suite and performance regression tests"
```

---

### Task 20: Integration Testing and Tuning

**Step 1: Run the full test suite**

```bash
uv run pytest -v --ignore=tests/test_benchmark.py
```

**Step 2: Review accuracy results**

Look at the accuracy test output. Identify encodings with low accuracy. Common
issues and fixes:

- If accuracy is low for specific encodings, retrain with more data:
  ```bash
  uv run python scripts/train.py --max-samples 5000
  ```
- If CJK encodings are confused, check structural probing scores
- If similar encodings (e.g., ISO-8859-1 vs Windows-1252) are misidentified,
  check that the training data captures their differences in the 0x80-0x9F range

**Step 3: Run benchmarks and compare to chardet**

```bash
pip install chardet  # Install original for comparison
uv run python scripts/benchmark.py
```

**Step 4: Tune thresholds**

Based on accuracy and benchmark results, adjust:
- `_BINARY_THRESHOLD` in `binary.py`
- `_STRUCTURAL_CONFIDENCE_THRESHOLD` in `orchestrator.py`
- `_PARALLEL_THRESHOLD` in `statistical.py`
- `_MIN_OVERALL_ACCURACY` in `test_accuracy.py`

**Step 5: Final commit**

```bash
uv run ruff check . && uv run ruff format .
git add -u
git commit -m "chore: tune detection thresholds based on accuracy/benchmark results"
```

---

### Task 21: Final Verification

**Step 1: Run all tests**

```bash
uv run pytest -v
```

**Step 2: Run benchmarks**

```bash
uv run pytest -m benchmark -v
```

**Step 3: Test package build**

```bash
uv build
ls -la dist/
```

Verify the wheel is a reasonable size.

**Step 4: Test installation in clean environment**

```bash
uv run --isolated python -c "import chardet; print(chardet.detect(b'Hello world'))"
```

**Step 5: Verify CLI works**

```bash
echo "Hello world" | uv run chardetect
```

**Step 6: Final commit if any changes**

```bash
uv run ruff check . && uv run ruff format .
git add -u
git commit -m "chore: final verification and cleanup"
```
