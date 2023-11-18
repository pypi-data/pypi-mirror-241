from typing import List, Dict, Set, Optional, Union
import pandas as pd
import logging
import os
import glob
import tabulate
import argparse


class Gen2Tab:

    """
    This class is used to store the gene information in a dictionary.
    The dictionary has the following structure:
    sample_dict = {
    "BUR-BAB-IMI-102146": {
                            "sequence_info": [
                              {"sequence":"BUR-BAB-IMI-102146_length_108_513"},
                              "start": 53228,
                              "end": 54445,
                              "strand": "+",
                              "gene": "ceoA",
                              "coverage": "1-1218/1218",
                              "convergence_map": "========/======"}
                              "gaps": "2/2",
                              "percentage_coverage"; 99.92,
                              "percentage_identity": 99.67,
                              "database": "card,
                              "accession": "U97042:0-1218",
                              "product": "ceoA is a periplasmic linker subunit of the CeoAB-OpcM efflux pump",
                              "resistance": [aminoglycoside,fluoroquinolone],
                              }
                            ]
                            "genes": {"ceoA"},
                            }
    }
    """

    def __init__(self):
        self.sample_dict: Dict[
            str,
            Dict[
                str, Union[List[Dict[str, Union[str, int, float, List[str]]]], Set[str]]
            ],
        ] = {}
        self.gen2id: Dict[str, int] = {}

    def add_sequence(
        self,
        file: str,
        sequence: str,
        gene: str,
        start: Optional[int] = None,
        end: Optional[int] = None,
        strand: Optional[str] = None,
        coverage: Optional[str] = None,
        convergence_map: Optional[str] = None,
        gaps: Optional[str] = None,
        percent_coverage: Optional[float] = 0.0,
        percent_identity: Optional[float] = 0.0,
        database: Optional[str] = None,
        accession: Optional[str] = None,
        product: Optional[str] = None,
        resistance: Optional[list] = None,
    ):
        """
        This method adds a sequence to the dictionary.
        """
        if file not in self.sample_dict:
            self.sample_dict[file] = {}
            self.sample_dict[file]["sequence_info"] = []
            self.sample_dict[file]["genes"] = set()
        self.sample_dict[file]["sequence_info"].append(
            {
                "sequence": sequence,
                "start": start,
                "end": end,
                "strand": strand,
                "gene": gene,
                "coverage": coverage,
                "convergence_map": convergence_map,
                "gaps": gaps,
                "percentage_coverage": percent_coverage,
                "percentage_identity": percent_identity,
                "database": database,
                "accession": accession,
                "product": product,
                "resistance": resistance,
            }
        )
        if gene not in self.sample_dict[file]["genes"]:
            self.sample_dict[file]["genes"].add(gene)

        if gene not in self.gen2id:
            self.gen2id[gene] = len(self.gen2id)

    def add_tab_file(self, file_path: str, sep="\t"):
        """
        This method adds a tab file to the dictionary.
        Example:
            #FILE	SEQUENCE	START	END	STRAND	GENE	COVERAGE	COVERAGE_MAP	GAPS	%COVERAGE	%IDENTITY	DATABASE	ACCESSION	PRODUCT
            BUR-BAB-IMI-102146	BUR-BAB-IMI-102146_length_108_513	53228	54445	+	ceoA	1-1218/1218	========/======	2/2	99.92	99.67	card	U97042:0-1218	ceoA is a periplasmic linker subunit of the CeoAB-OpcM efflux pump
        """

        df = pd.read_csv(file_path, sep=sep, header=0)
        logging.info(f"Number of samples in {file_path}: {len(df)}")
        for index, row in df.iterrows():
            self.add_sequence(
                file=row["#FILE"],
                sequence=row["SEQUENCE"],
                gene=row["GENE"],
                start=row["START"] if "START" in row else None,
                end=row["END"] if "END" in row else None,
                strand=row["STRAND"] if "STRAND" in row else None,
                coverage=row["COVERAGE"] if "COVERAGE" in row else None,
                convergence_map=row["COVERAGE_MAP"] if "COVERAGE_MAP" in row else None,
                gaps=row["GAPS"] if "GAPS" in row else None,
                percent_coverage=row["%COVERAGE"] if "%COVERAGE" in row else 0.0,
                percent_identity=row["%IDENTITY" if "%IDENTITY" in row else 0.0],
                database=row["DATABASE"] if "DATABASE" in row else None,
                accession=row["ACCESSION"] if "ACCESSION" in row else None,
                product=row["PRODUCT"] if "PRODUCT" in row else None,
            )

    def add_data(self, data_path: str, sep="\t"):
        # Test if path is a file or a directory
        if os.path.isfile(data_path):
            self.add_tab_file(data_path, sep=sep)
        elif os.path.isdir(data_path):
            for file in glob.glob(data_path + "/*.tab"):
                self.add_tab_file(file, sep=sep)
        else:
            raise Exception(f"Path {data_path} is not a file or a directory")

    # Create class from file
    @classmethod
    def from_file(cls, file_path: str, sep="\t"):
        gen2tab = cls()
        gen2tab.add_tab_file(file_path, sep)
        return gen2tab

    def get_table(
        self,
        min_coverage: float = -1.0,
        max_identity: float = -1.0,
        output_format: str = "tsv",
        output_path: Optional[str] = None,
    ):
        header = ["Sample"] + list(self.gen2id.keys())
        results = []
        for sample_no, sample in enumerate(self.sample_dict):
            matrix = [0] * len(self.gen2id)
            for sequence in self.sample_dict[sample]["sequence_info"]:
                if (
                    sequence["percentage_coverage"] >= min_coverage
                    and sequence["percentage_identity"] >= max_identity
                ):
                    matrix[self.gen2id[sequence["gene"]]] = 1

            results.append([sample] + matrix)

        if output_path is not None:
            with open(output_path, "w", encoding="utf8") as output_path:
                print(
                    tabulate.tabulate(results, header, tablefmt=output_format),
                    file=output_path,
                )

        else:
            print(
                tabulate.tabulate(results, header, tablefmt=output_format),
                file=output_path,
            )


def main():
    args = parse_arguments()
    gen2tab = Gen2Tab()
    gen2tab.add_data(args.input)
    gen2tab.get_table(
        min_coverage=args.min_coverage,
        max_identity=args.max_identity,
        output_format=args.format,
        output_path=args.output,
    )


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Create a table with the presence/absence of genes in samples"
    )
    parser.add_argument(
        "-i",
        "--input",
        help="Input file or directory with tab files",
        required=True,
        type=str,
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Output file",
        required=False,
        type=str,
    )
    parser.add_argument(
        "-f",
        "--format",
        help="Output format",
        required=False,
        type=str,
        default="tsv",
        choices=[
            "plain",
            "simple",
            "github",
            "grid",
            "simple_grid",
            "rounded_grid",
            "heavy_grid",
            "mixed_grid",
            "double_grid",
            "fancy_grid",
            "outline",
            "simple_outline",
            "rounded_outline",
            "heavy_outline",
            "mixed_outline",
            "double_outline",
            "fancy_outline",
            "pipe",
            "orgtbl",
            "asciidoc",
            "jira",
            "presto",
            "pretty",
            "psql",
            "rst",
            "mediawiki",
            "moinmoin",
            "youtrack",
            "html",
            "unsafehtml",
            "latex",
            "latex_raw",
            "latex_booktabs",
            "latex_longtable",
            "textile",
            "tsv",
        ],
    )
    parser.add_argument(
        "-c",
        "--min_coverage",
        help="Minimum coverage",
        required=False,
        type=float,
        default=-1.0,
    )
    parser.add_argument(
        "-p",
        "--max_identity",
        help="Maximum identity",
        required=False,
        type=float,
        default=-1.0,
    )
    args = parser.parse_args()

    return args


if __name__ == "__main__":
    main()
