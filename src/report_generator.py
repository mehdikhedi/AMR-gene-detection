"""Helpers for generating AMR comparison reports."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.compare_to_reference import (
    ComparisonResult,
    compare_samples_to_reference,
    load_reference,
    load_samples,
    results_to_dataframe,
)


def generate_report(fasta_path: str | Path, reference_csv: str | Path) -> pd.DataFrame:
    """Compare samples to the reference catalog and return a dataframe report."""

    reference_df = load_reference(reference_csv)
    samples = load_samples(fasta_path)
    results: list[ComparisonResult] = compare_samples_to_reference(samples, reference_df)
    return results_to_dataframe(results)


def save_report(df: pd.DataFrame, output_csv: str | Path) -> Path:
    """Persist the report dataframe to CSV and return the output path."""

    output_path = Path(output_csv)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    return output_path


def main() -> None:
    """CLI helper to build a comparison report and save it as CSV."""

    import argparse

    parser = argparse.ArgumentParser(
        description="Generate a CSV report of AMR gene matches for sample sequences."
    )
    parser.add_argument(
        "--fasta",
        type=Path,
        default=Path("data/sample_sequences.fasta"),
        help="Path to the sample FASTA file.",
    )
    parser.add_argument(
        "--reference",
        type=Path,
        default=Path("data/resistance_genes_reference.csv"),
        help="Path to the AMR reference CSV file.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/amr_matches_report.csv"),
        help="Destination CSV for the comparison results.",
    )
    args = parser.parse_args()

    df = generate_report(args.fasta, args.reference)
    if df.empty:
        raise SystemExit("No comparison results generated.")

    save_path = save_report(df, args.output)
    print(f"Report saved to {save_path.resolve()}")
    print(df.to_string(index=False))


if __name__ == "__main__":
    main()
