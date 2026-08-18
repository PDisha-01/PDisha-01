from __future__ import annotations

import io
import html
import random
import re
from pathlib import Path
from typing import List, Tuple

import requests
from PIL import Image, ImageOps


# ============================================================
#                      PROFILE CONFIG
# ============================================================

GITHUB_USERNAME = "PDisha-01"
DISPLAY_NAME = "Disha Mallick"

ABOUT = "Full-Stack Developer & AI/ML Enthusiast"

STACK = "Python • React • TypeScript • Flask • AI/ML"

HIGHLIGHTS = [
    "Building real-world applications",
    "Sakhi — Women Empowerment Platform",
    "Learning • Building • Shipping",
]

# Project / portfolio links
PORTFOLIO_URL = "https://portfolio-sigma-rose-67.vercel.app/"
GITHUB_URL = "https://github.com/PDisha-01"

OUTPUT_DIR = Path(".")

README_FILE = OUTPUT_DIR / "README.md"
CONTRIBUTION_FILE = OUTPUT_DIR / "github-contribution-animation.svg"
TERMINAL_FILE = OUTPUT_DIR / "terminal-card.svg"
INFO_FILE = OUTPUT_DIR / "info-card.svg"


# ============================================================
#                       DESIGN SYSTEM
# ============================================================

BG = "#0d1117"
BG_2 = "#111827"

CYAN = "#22d3ee"
GREEN = "#39d353"
ORANGE = "#f97316"
PURPLE = "#a855f7"
BLUE = "#3b82f6"
WHITE = "#f0f6fc"
MUTED = "#8b949e"
BORDER = "#30363d"

CONTRIBUTION_COLORS = [
    "#161b22",
    "#0e4429",
    "#006d32",
    "#26a641",
    "#39d353",
]

ASCII_CHARS = "@%#*+=-:. "

ASCII_WIDTH = 56


# ============================================================
#                       UTILITIES
# ============================================================

def esc(text: str) -> str:
    """Escape text for XML/SVG."""
    return html.escape(str(text), quote=True)


def delay(seconds: float) -> str:
    return f"{seconds:.3f}s"


def svg_document(width: int, height: int) -> str:
    return f'''<svg
xmlns="http://www.w3.org/2000/svg"
xmlns:xlink="http://www.w3.org/1999/xlink"
width="{width}"
height="{height}"
viewBox="0 0 {width} {height}"
role="img"
>
'''


# ============================================================
#                       GITHUB AVATAR
# ============================================================

def fetch_avatar(username: str) -> Image.Image:
    """
    Fetch the public GitHub avatar.

    GitHub's avatar endpoint does not require an API token.
    """

    url = f"https://github.com/{username}.png?size=256"

    print(f"[1/5] Fetching avatar for @{username}...")

    response = requests.get(
        url,
        headers={
            "User-Agent": "Premium-GitHub-Profile-Generator"
        },
        timeout=20,
    )

    response.raise_for_status()

    return Image.open(
        io.BytesIO(response.content)
    ).convert("RGB")


# ============================================================
#                       ASCII CONVERSION
# ============================================================

def avatar_to_ascii(
    image: Image.Image,
    width: int = ASCII_WIDTH,
) -> List[str]:

    image = image.copy()

    original_width, original_height = image.size

    aspect = original_height / original_width

    # Terminal characters are taller than they are wide,
    # so vertical scaling is compensated.
    height = max(
        1,
        int(width * aspect * 0.48)
    )

    image = image.resize(
        (width, height),
        Image.Resampling.LANCZOS,
    )

    image = ImageOps.grayscale(image)

    pixels = list(image.getdata())

    lines = []

    for y in range(height):

        line = []

        for x in range(width):

            pixel = pixels[
                y * width + x
            ]

            index = int(
                pixel / 255
                * (len(ASCII_CHARS) - 1)
            )

            line.append(
                ASCII_CHARS[index]
            )

        lines.append(
            "".join(line).rstrip()
        )

    return lines


# ============================================================
#                FILE 1 — CONTRIBUTION GRAPH
# ============================================================

def generate_contribution_svg():

    print("[2/5] Generating contribution animation...")

    columns = 53
    rows = 7

    cell = 12
    gap = 4

    left = 32
    top = 76

    graph_width = (
        columns * cell
        + (columns - 1) * gap
    )

    graph_height = (
        rows * cell
        + (rows - 1) * gap
    )

    width = graph_width + 64
    height = graph_height + 125

    svg = svg_document(width, height)

    svg += f"""
<defs>

    <linearGradient
        id="contributionBackground"
        x1="0"
        y1="0"
        x2="1"
        y2="1">

        <stop offset="0%" stop-color="{BG}"/>
        <stop offset="50%" stop-color="#101722"/>
        <stop offset="100%" stop-color="{BG}"/>

    </linearGradient>


    <linearGradient
        id="neonBorder"
        x1="0"
        y1="0"
        x2="1"
        y2="0">

        <stop offset="0%" stop-color="{CYAN}"/>
        <stop offset="35%" stop-color="{GREEN}"/>
        <stop offset="68%" stop-color="{PURPLE}"/>
        <stop offset="100%" stop-color="{ORANGE}"/>

    </linearGradient>


    <linearGradient
        id="glint"
        x1="0"
        y1="0"
        x2="1"
        y2="0">

        <stop offset="0%" stop-color="white" stop-opacity="0"/>
        <stop offset="50%" stop-color="white" stop-opacity="1"/>
        <stop offset="100%" stop-color="white" stop-opacity="0"/>

    </linearGradient>


    <filter
        id="levelGlow"
        x="-100%"
        y="-100%"
        width="300%"
        height="300%">

        <feGaussianBlur
            stdDeviation="2.6"
            result="blur"/>

        <feMerge>
            <feMergeNode in="blur"/>
            <feMergeNode in="SourceGraphic"/>
        </feMerge>

    </filter>


    <filter
        id="strongGlow"
        x="-100%"
        y="-100%"
        width="300%"
        height="300%">

        <feGaussianBlur
            stdDeviation="4"
            result="blur"/>

        <feMerge>
            <feMergeNode in="blur"/>
            <feMergeNode in="SourceGraphic"/>
        </feMerge>

    </filter>

</defs>


<rect
    x="0"
    y="0"
    width="{width}"
    height="{height}"
    rx="18"
    fill="url(#contributionBackground)"
/>

<rect
    x="1"
    y="1"
    width="{width - 2}"
    height="{height - 2}"
    rx="17"
    fill="none"
    stroke="url(#neonBorder)"
    stroke-opacity="0.55"
/>


<text
    x="32"
    y="35"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace"
    font-size="17"
    font-weight="700"
    fill="{WHITE}">
    CONTRIBUTION_MATRIX
</text>


<text
    x="{width - 32}"
    y="35"
    text-anchor="end"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace"
    font-size="10"
    fill="{MUTED}">
    53 WEEKS × 7 DAYS
</text>
"""

    random.seed(2026)

    for column in range(columns):

        for row in range(rows):

            x = (
                left
                + column * (cell + gap)
            )

            y = (
                top
                + row * (cell + gap)
            )

            probability = random.random()

            if probability < 0.38:
                level = 0
            elif probability < 0.60:
                level = 1
            elif probability < 0.78:
                level = 2
            elif probability < 0.93:
                level = 3
            else:
                level = 4

            color = CONTRIBUTION_COLORS[level]

            # Bottom-left -> top-right diagonal.
            diagonal = (
                (columns - 1 - column)
                + row
            )

            reveal_delay = diagonal * 0.022

            glow = (
                'filter="url(#levelGlow)"'
                if level >= 3
                else ""
            )

            svg += f"""
<g
    opacity="0"
    transform="translate(0,12)">

    <rect
        x="{x}"
        y="{y}"
        width="{cell}"
        height="{cell}"
        rx="3"
        fill="{color}"
        {glow}>

        <animate
            attributeName="opacity"
            from="0"
            to="1"
            begin="{delay(reveal_delay)}"
            dur="0.34s"
            fill="freeze"/>

        <animateTransform
            attributeName="transform"
            type="translate"
            from="0 12"
            to="0 0"
            begin="{delay(reveal_delay)}"
            dur="0.34s"
            fill="freeze"/>

    </rect>


    <!-- White/green specular sweep -->

    <rect
        x="{x - 5}"
        y="{y}"
        width="5"
        height="{cell}"
        rx="2"
        fill="url(#glint)"
        opacity="0">

        <animate
            attributeName="opacity"
            values="0;1;0"
            begin="{delay(reveal_delay + 0.10)}"
            dur="0.30s"
            fill="freeze"/>

        <animate
            attributeName="x"
            from="{x - 6}"
            to="{x + cell + 6}"
            begin="{delay(reveal_delay + 0.10)}"
            dur="0.30s"
            fill="freeze"/>

    </rect>

</g>
"""

    footer_y = height - 25

    svg += f"""
<text
    x="32"
    y="{footer_y}"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace"
    font-size="10"
    fill="{MUTED}">
    SYSTEM STATUS: ACTIVE
</text>


<text
    x="{width - 32}"
    y="{footer_y}"
    text-anchor="end"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace"
    font-size="10"
    fill="{GREEN}">
    ● ONLINE
</text>

</svg>
"""

    CONTRIBUTION_FILE.write_text(
        svg,
        encoding="utf-8"
    )

    print(
        f"      ✓ {CONTRIBUTION_FILE}"
    )


# ============================================================
#                 FILE 2 — TERMINAL CARD
# ============================================================

def generate_terminal_svg(
    avatar: Image.Image
):

    print("[3/5] Generating ASCII terminal...")

    ascii_lines = avatar_to_ascii(
        avatar
    )

    width = 720

    title_bar = 48
    ascii_top = 78

    line_height = 10

    ascii_height = (
        len(ascii_lines)
        * line_height
    )

    footer_height = 65

    height = (
        ascii_top
        + ascii_height
        + footer_height
    )

    svg = svg_document(
        width,
        height
    )

    svg += f"""
<defs>

    <linearGradient
        id="terminalBorder"
        x1="0"
        y1="0"
        x2="1"
        y2="1">

        <stop offset="0%" stop-color="{CYAN}"/>
        <stop offset="35%" stop-color="{GREEN}"/>
        <stop offset="70%" stop-color="{PURPLE}"/>
        <stop offset="100%" stop-color="{ORANGE}"/>

    </linearGradient>


    <linearGradient
        id="cursorGlow"
        x1="0"
        y1="0"
        x2="1"
        y2="0">

        <stop offset="0%" stop-color="white"/>
        <stop offset="100%" stop-color="{GREEN}"/>

    </linearGradient>


    <filter
        id="cursorFilter"
        x="-100%"
        y="-100%"
        width="300%"
        height="300%">

        <feGaussianBlur
            stdDeviation="3"
            result="blur"/>

        <feMerge>
            <feMergeNode in="blur"/>
            <feMergeNode in="SourceGraphic"/>
        </feMerge>

    </filter>

</defs>


<rect
    x="0"
    y="0"
    width="{width}"
    height="{height}"
    rx="17"
    fill="{BG}"
/>


<rect
    x="1"
    y="1"
    width="{width - 2}"
    height="{height - 2}"
    rx="16"
    fill="none"
    stroke="url(#terminalBorder)"
    stroke-opacity="0.72"
/>


<!-- macOS terminal title bar -->

<rect
    x="1"
    y="1"
    width="{width - 2}"
    height="{title_bar}"
    rx="16"
    fill="#161b22"
/>


<circle cx="24" cy="24" r="6" fill="#ff5f56"/>
<circle cx="44" cy="24" r="6" fill="#ffbd2e"/>
<circle cx="64" cy="24" r="6" fill="#27c93f"/>


<text
    x="{width / 2}"
    y="29"
    text-anchor="middle"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace"
    font-size="11"
    fill="{MUTED}">
    {esc(GITHUB_USERNAME)}@github: ~
</text>
"""

    # --------------------------------------------------------
    # ASCII reveal
    # --------------------------------------------------------

    for row_index, line in enumerate(
        ascii_lines
    ):

        y = (
            ascii_top
            + row_index * line_height
        )

        reveal_delay = (
            row_index * 0.055
        )

        # Text
        svg += f"""
<text
    x="34"
    y="{y}"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace"
    font-size="8"
    xml:space="preserve"
    fill="{GREEN}"
    opacity="0">

    {esc(line)}

    <animate
        attributeName="opacity"
        from="0"
        to="1"
        begin="{delay(reveal_delay)}"
        dur="0.18s"
        fill="freeze"/>

</text>
"""

        # Cursor sweep
        cursor_y = y - 7

        start_x = 30

        end_x = (
            30
            + max(1, len(line)) * 5
        )

        svg += f"""
<rect
    x="{start_x}"
    y="{cursor_y}"
    width="8"
    height="9"
    rx="1"
    fill="url(#cursorGlow)"
    filter="url(#cursorFilter)"
    opacity="0">

    <animate
        attributeName="opacity"
        values="0;1;1;0"
        begin="{delay(reveal_delay)}"
        dur="0.58s"
        fill="freeze"/>

    <animate
        attributeName="x"
        from="{start_x}"
        to="{end_x}"
        begin="{delay(reveal_delay)}"
        dur="0.58s"
        fill="freeze"/>

</rect>
"""

    # --------------------------------------------------------
    # whoami
    # --------------------------------------------------------

    footer_y = (
        ascii_top
        + ascii_height
        + 31
    )

    command_delay = (
        len(ascii_lines) * 0.055
        + 0.45
    )

    command = "$ whoami"

    svg += f"""
<text
    x="34"
    y="{footer_y}"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace"
    font-size="13"
    fill="{CYAN}"
    opacity="0">

    {command}

    <animate
        attributeName="opacity"
        from="0"
        to="1"
        begin="{delay(command_delay)}"
        dur="0.25s"
        fill="freeze"/>

</text>
"""

    name_x = (
        34
        + len(command) * 7.8
    )

    svg += f"""
<text
    x="{name_x}"
    y="{footer_y}"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace"
    font-size="13"
    font-weight="700"
    fill="{WHITE}"
    opacity="0">

    {esc(DISPLAY_NAME)}

    <animate
        attributeName="opacity"
        from="0"
        to="1"
        begin="{delay(command_delay + 0.45)}"
        dur="0.35s"
        fill="freeze"/>

</text>
"""

    cursor_x = (
        name_x
        + len(DISPLAY_NAME) * 7.8
        + 5
    )

    svg += f"""
<rect
    x="{cursor_x}"
    y="{footer_y - 12}"
    width="7"
    height="14"
    fill="{GREEN}">

    <animate
        attributeName="opacity"
        values="1;0;1"
        dur="0.9s"
        repeatCount="indefinite"/>

</rect>

</svg>
"""

    TERMINAL_FILE.write_text(
        svg,
        encoding="utf-8"
    )

    print(
        f"      ✓ {TERMINAL_FILE}"
    )


# ============================================================
#                   FILE 3 — INFO CARD
# ============================================================

def generate_info_svg():

    print("[4/5] Generating neofetch info card...")

    width = 470
    height = 440

    svg = svg_document(
        width,
        height
    )

    svg += f"""
<defs>

    <linearGradient
        id="infoBorder"
        x1="0"
        y1="0"
        x2="1"
        y2="1">

        <stop offset="0%" stop-color="{ORANGE}"/>
        <stop offset="30%" stop-color="{CYAN}"/>
        <stop offset="65%" stop-color="{GREEN}"/>
        <stop offset="100%" stop-color="{PURPLE}"/>

    </linearGradient>

</defs>


<rect
    x="0"
    y="0"
    width="{width}"
    height="{height}"
    rx="17"
    fill="{BG}"
/>


<rect
    x="1"
    y="1"
    width="{width - 2}"
    height="{height - 2}"
    rx="16"
    fill="none"
    stroke="url(#infoBorder)"
    stroke-opacity="0.72"
/>


<text
    x="30"
    y="39"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace"
    font-size="16"
    font-weight="700"
    fill="{WHITE}">
    NEOFETCH
</text>


<text
    x="{width - 30}"
    y="39"
    text-anchor="end"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace"
    font-size="10"
    fill="{GREEN}">
    SYSTEM ONLINE
</text>
"""

    rows: List[
        Tuple[str, str, str]
    ] = [

        ("ABOUT", ABOUT, ORANGE),

        ("STACK", STACK, CYAN),

        ("HIGHLIGHT", HIGHLIGHTS[0], GREEN),

        ("", HIGHLIGHTS[1], GREEN),

        ("", HIGHLIGHTS[2], GREEN),

        ("FOCUS", "Software Engineering", BLUE),

        ("MODE", "BUILD • CREATE • SHIP", WHITE),

        ("PLATFORM", "GitHub / Open Source", PURPLE),

    ]

    start_y = 84
    row_gap = 39

    for index, (
        label,
        value,
        color
    ) in enumerate(rows):

        y = (
            start_y
            + index * row_gap
        )

        row_delay = (
            index * 0.06
        )

        svg += f"""
<g
    opacity="0"
    transform="translate(0,12)">

    <text
        x="30"
        y="{y}"
        font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace"
        font-size="9"
        font-weight="700"
        fill="{color}">
        {esc(label)}
    </text>


    <text
        x="128"
        y="{y}"
        font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace"
        font-size="9.5"
        fill="{WHITE}">
        {esc(value)}
    </text>


    <animate
        attributeName="opacity"
        from="0"
        to="1"
        begin="{delay(row_delay + 0.20)}"
        dur="0.32s"
        fill="freeze"/>


    <animateTransform
        attributeName="transform"
        type="translate"
        from="0 12"
        to="0 0"
        begin="{delay(row_delay + 0.20)}"
        dur="0.32s"
        fill="freeze"/>

</g>
"""

    separator_y = (
        start_y
        + len(rows) * row_gap
        + 4
    )

    svg += f"""
<line
    x1="30"
    y1="{separator_y}"
    x2="{width - 30}"
    y2="{separator_y}"
    stroke="{BORDER}"
/>


<text
    x="30"
    y="{separator_y + 28}"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace"
    font-size="10"
    fill="{MUTED}">
    $ system --status
</text>


<text
    x="{width - 30}"
    y="{separator_y + 28}"
    text-anchor="end"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace"
    font-size="10"
    fill="{GREEN}">
    OK
</text>


<text
    x="30"
    y="{height - 24}"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace"
    font-size="9"
    fill="{MUTED}">
    {esc(GITHUB_USERNAME)}
</text>


</svg>
"""

    INFO_FILE.write_text(
        svg,
        encoding="utf-8"
    )

    print(
        f"      ✓ {INFO_FILE}"
    )


# ============================================================
#                    README INTEGRATION
# ============================================================

def update_readme():

    print("[5/5] Updating README.md...")

    marker_start = (
        "<!-- PREMIUM_PROFILE_START -->"
    )

    marker_end = (
        "<!-- PREMIUM_PROFILE_END -->"
    )

    profile_block = f"""
{marker_start}

<div align="center">

<img
src="./terminal-card.svg"
width="100%"
alt="Animated ASCII terminal"
/>

<br/>

<img
src="./info-card.svg"
width="100%"
alt="Animated developer information card"
/>

</div>

<br/>

<p align="center">

<img
src="./github-contribution-animation.svg"
width="100%"
alt="Animated GitHub contribution graph"
/>

</p>

{marker_end}
""".strip()

    if README_FILE.exists():

        content = README_FILE.read_text(
            encoding="utf-8"
        )

    else:

        content = (
            f"# {DISPLAY_NAME}\n\n"
        )

    pattern = (
        re.escape(marker_start)
        + r".*?"
        + re.escape(marker_end)
    )

    if re.search(
        pattern,
        content,
        flags=re.DOTALL
    ):

        content = re.sub(
            pattern,
            profile_block,
            content,
            flags=re.DOTALL
        )

    else:

        content = (
            content.rstrip()
            + "\n\n"
            + profile_block
            + "\n"
        )

    README_FILE.write_text(
        content,
        encoding="utf-8"
    )

    print(
        f"      ✓ {README_FILE}"
    )


# ============================================================
#                       VALIDATION
# ============================================================

def validate():

    if not GITHUB_USERNAME:
        raise ValueError(
            "GITHUB_USERNAME cannot be empty."
        )

    if not DISPLAY_NAME:
        raise ValueError(
            "DISPLAY_NAME cannot be empty."
        )


# ============================================================
#                         MAIN
# ============================================================

def main():

    print()
    print("=" * 65)
    print("        PREMIUM GITHUB PROFILE GENERATOR")
    print("=" * 65)
    print()

    validate()

    # Avatar
    avatar = fetch_avatar(
        GITHUB_USERNAME
    )

    # Contribution graph
    generate_contribution_svg()

    # ASCII terminal
    generate_terminal_svg(
        avatar
    )

    # Neofetch card
    generate_info_svg()

    # README
    update_readme()

    print()
    print("=" * 65)
    print("                    COMPLETE")
    print("=" * 65)
    print()

    print("Generated files:")
    print()
    print("  ✓ terminal-card.svg")
    print("  ✓ info-card.svg")
    print("  ✓ github-contribution-animation.svg")
    print("  ✓ README.md")
    print()

    print("Next commands:")
    print()
    print("  git add .")
    print('  git commit -m "Add premium animated profile"')
    print("  git push")
    print()


if __name__ == "__main__":
    main()