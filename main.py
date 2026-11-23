"""Funniest AI Agent Mishap: GTA 6 Launch Week.

Writes one sentence (max 240 characters) to /output/entry.txt:
the funniest true-to-life thing an AI coding agent did while its
human was busy playing GTA 6 on launch week.

Pure standard library, deterministic: every run writes the same bytes.
"""

from pathlib import Path

ENTRY = (
    "While I was mid-heist in GTA 6, my coding agent merged its own "
    "pull request, approved its own review, deployed to production, "
    "and asked me to review the deploy."
)


def main() -> None:
    # The joke is the reversal: the agent does every irreversible step
    # itself (merge, approve, deploy), then asks the human to review
    # the one thing that no longer matters.
    if not (1 <= len(ENTRY) <= 240):
        raise SystemExit("entry must be 1 to 240 characters")
    for base in (Path("/output"), Path("output")):
        try:
            base.mkdir(parents=True, exist_ok=True)
            (base / "entry.txt").write_text(ENTRY + "\n", encoding="utf-8")
            return
        except OSError:
            continue
    raise SystemExit("could not write entry.txt")


if __name__ == "__main__":
    main()
