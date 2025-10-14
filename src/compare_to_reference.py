"""Compare sample DNA sequences against a reference catalog of AMR genes."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List

import pandas as pd
from Bio import SeqIO


@dataclass
class ComparisonResult:
    """Stores the top AMR gene match for a sample sequence."""

    sample_id: str
    closest_gene: str
    similarity: float


def load_reference(reference_csv: str | Path) -> pd.DataFrame:
    """Load the AMR reference gene sequences from CSV."""

    reference_path = Path(reference_csv)
    if not reference_path.exists():
        raise FileNotFoundError(f"Reference CSV not found: {reference_path}")
    frame = pd.read_csv(reference_path)
    expected_columns = {"gene_name", "sequence"}
    if not expected_columns.issubset(frame.columns):
        raise ValueError(
            f"Reference CSV must contain columns {expected_columns}, found {frame.columns.tolist()}"
        )
    return frame


def load_samples(fasta_path: str | Path) -> List[tuple[str, str]]:
    """Parse the sample sequences from a FASTA file."""

    fasta_file = Path(fasta_path)
    if not fasta_file.exists():
        raise FileNotFoundError(f"Sample FASTA not found: {fasta_file}")
    records = []
    for record in SeqIO.parse(str(fasta_file), "fasta"):
        records.append((record.id, str(record.seq).upper()))
    if not records:
        raise ValueError(f"No sequences found in FASTA file: {fasta_file}")
    return records


def compute_similarity(sample_seq: str, reference_seq: str) -> float:
    """Compute a simple base-by-base similarity percentage."""

    sample = sample_seq.upper()
    reference = reference_seq.upper()
    if not sample or not reference:
        return 0.0

    matches = sum(1 for s, r in zip(sample, reference) if s == r)
    total_positions = max(len(sample), len(reference))
    if total_positions == 0:
        return 0.0
    return (matches / total_positions) * 100


def find_closest_match(
    sample_seq: str, reference_df: pd.DataFrame
) -> tuple[str, float]:
    """Determine the closest AMR gene match for a sample sequence."""

    best_gene = ""
    best_similarity = -1.0
    for _, row in reference_df.iterrows():
        similarity = compute_similarity(sample_seq, row["sequence"])
        if similarity > best_similarity:
            best_gene = row["gene_name"]
            best_similarity = similarity
    return best_gene, best_similarity


def compare_samples_to_reference(
    samples: Iterable[tuple[str, str]], reference_df: pd.DataFrame
) -> list[ComparisonResult]:
    """Compare each sample sequence to the reference catalog."""

    results: list[ComparisonResult] = []
    for sample_id, sequence in samples:
        closest_gene, similarity = find_closest_match(sequence, reference_df)
        results.append(
            ComparisonResult(
                sample_id=sample_id,
                closest_gene=closest_gene,
                similarity=round(similarity, 2),
            )
        )
    return results


def results_to_dataframe(results: Iterable[ComparisonResult]) -> pd.DataFrame:
    """Convert comparison results to a Pandas DataFrame."""

    data = [
        {
            "Sample_ID": result.sample_id,
            "Closest_AMR_Gene": result.closest_gene,
            "Similarity(%)": result.similarity,
        }
        for result in results
    ]
    return pd.DataFrame(data)


def main() -> None:
    """CLI entry point: compare samples to the AMR reference and print results."""

    import argparse

    parser = argparse.ArgumentParser(
        description="Compare sample sequences with AMR reference genes to identify the closest match."
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
    args = parser.parse_args()

    reference_df = load_reference(args.reference)
    samples = load_samples(args.fasta)
    results = compare_samples_to_reference(samples, reference_df)
    df = results_to_dataframe(results)
    if df.empty:
        raise SystemExit("No comparison results generated.")

    print(df.to_string(index=False))


if __name__ == "__main__":
    main()
