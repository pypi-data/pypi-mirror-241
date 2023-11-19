# coding=utf-8
# Copyright 2023 Iker García-Ferrero
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from typing import List, Dict, Set, Optional, Union
import pandas as pd
import logging
import os
import glob
import argparse


class Gene2Tab:

    """
    This class is used to store the gene information in a dictionary.
    The dictionary has the following structure:
    sample_dict = {
    "Isolate1": {
                            "sequence_info": [
                              {"sequence":"Isolate1_length_108_513"},
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

    We will also store a dictionary with the gene names and the id of the gene.
    gen2id = {
        "ceoA": 0,
        "ceoB": 1,
        "ceoC": 2,
        }
    """

    def __init__(self):
        """
        This method initializes the dictionary.
        """
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
        This method adds a sample to the dictionary.

        Args:
            file (str): Sample name
            sequence (str): Sequence name
            gene (str): Gene name
            start (int, optional): Start position of the gene. Defaults to None.
            end (int, optional): End position of the gene. Defaults to None.
            strand (str, optional): Strand of the gene. Defaults to None.
            coverage (str, optional): Coverage of the gene. Defaults to None.
            convergence_map (str, optional): Convergence map of the gene. Defaults to None.
            gaps (str, optional): Gaps of the gene. Defaults to None.
            percent_coverage (float, optional): Percentage of coverage of the gene. Defaults to 0.0.
            percent_identity (float, optional): Percentage of identity of the gene. Defaults to 0.0.
            database (str, optional): Database of the gene. Defaults to None.
            accession (str, optional): Accession of the gene. Defaults to None.
            product (str, optional): Product of the gene. Defaults to None.
            resistance (list, optional): List of resistances of the gene. Defaults to None.
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
            #FILE	SEQUENCE	START	END	STRAND	GENE	COVERAGE	COVERAGE_MAP	GAPS	%COVERAGE	%IDENTITY	DATABASE	ACCESSION	PRODUCT	RESISTANCE
            Isolate1	S1-length_108_513	53228	54445	+	ceoA	1-1218/1218	========/======	2/2	99.92	99.67	card	U97042:0-1218	ceoA is a periplasmic linker subunit of the CeoAB-OpcM efflux pump	aminoglycoside;fluoroquinolone


        Args:
            file_path (str): Path to the tab file
            sep (str, optional): Delimiter of the tab file. Defaults to "\t".

        """

        df = pd.read_csv(file_path, sep=sep, header=0)
        logging.info(f"Number of genes in {file_path}: {len(df)}")
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
        """
        This method adds a tab file or a directory with tab files to the dictionary.
        We will automatically detect if the path is a file or a directory.

        Args:
            data_path (str): Path to the tab file or directory
            sep (str, optional): Delimiter of the tab file. Defaults to "\t".
        """
        # Test if path is a file or a directory
        data_path = os.path.abspath(data_path)
        if os.path.isfile(data_path):
            logging.info(f"Adding file {data_path}")
            self.add_tab_file(data_path, sep=sep)
        elif os.path.isdir(data_path):
            logging.info(f"Adding directory {data_path}")
            for file in glob.glob(data_path + "/*.tab"):
                logging.info(f"Adding file {file}")
                self.add_tab_file(file, sep=sep)
        else:
            raise Exception(f"Path {data_path} is not a file or a directory")

    # Create class from file
    @classmethod
    def from_file(cls, file_path: str, delimiter="\t"):
        """
        This method creates a class from a tab file or directory with tab files.

        Args:
            file_path (str): Path to the tab file or directory
            delimiter (str, optional): Delimiter of the tab file. Defaults to "\t".

        Returns:
            Gene2Tab: Class with the information of the tab file or directory
        """
        Gene2Tab = cls()
        Gene2Tab.add_data(file_path, delimiter)
        return Gene2Tab

    def get_table(
        self,
        min_coverage: float = -1.0,
        min_identity: float = -1.0,
        output_format: str = "csv",
        output_path: Optional[str] = None,
        delimiter: str = ",",
        transpose: bool = False,
    ):
        """
        This method creates a table with the presence/absence of genes in samples.
        If the gene is present in the sample, the value will be 1, otherwise 0.

        Args:
            min_coverage (float, optional): Minimum coverage to consider a gene present in a sample. Defaults to -1.0.
            min_identity (float, optional): Minimum identity to consider a gene present in a sample. Defaults to -1.0.
            output_format (str, optional): Output format. Defaults to "csv".
            output_path (Optional[str], optional): Output path. If set we will save the table in the output path.
                                                   If not set we will print the table in the console. Defaults to None.
            delimiter (str, optional): Output file delimiter, used if output format is csv. Defaults to ",".
            transpose (bool, optional): Transpose the table. Genes as rows and samples as columns. Defaults to False.

        """
        results = [["Sample"] + list(self.gen2id.keys())]
        for sample_no, sample in enumerate(self.sample_dict):
            matrix = [0] * len(self.gen2id)
            for sequence in self.sample_dict[sample]["sequence_info"]:
                if (
                    sequence["percentage_coverage"] >= min_coverage
                    and sequence["percentage_identity"] >= min_identity
                ):
                    matrix[self.gen2id[sequence["gene"]]] = 1

            results.append([sample] + matrix)

        if transpose:
            results = list(map(list, zip(*results)))

        if output_format != "csv":
            import tabulate

            header = results[0]
            results = results[1:]
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
        else:
            import csv

            if output_path is not None:
                with open(output_path, "w", encoding="utf8") as output_path:
                    writer = csv.writer(output_path, delimiter=delimiter)
                    writer.writerows(results)
            else:
                for row in results:
                    print(delimiter.join([str(x) for x in row]))


def main():
    """
    Main function of the script.
    """
    # Set logging
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )
    args = parse_arguments()
    mytab = Gene2Tab.from_file(args.input, delimiter=args.input_file_delimiter)
    mytab.get_table(
        min_coverage=args.min_coverage,
        min_identity=args.min_identity,
        output_format=args.format,
        output_path=args.output,
        delimiter=args.output_file_delimiter,
        transpose=args.transpose,
    )


def parse_arguments():
    """
    This function parses the arguments of the script.

    Returns:
        argparse.Namespace: Arguments of the script
    """
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
        default="csv",
        choices=[
            "csv",
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
        help="Minimum coverage to consider a gene present in a sample",
        required=False,
        type=float,
        default=0.9,
    )
    parser.add_argument(
        "-p",
        "--min_identity",
        help="Minimum identity to consider a gene present in a sample",
        required=False,
        type=float,
        default=0.9,
    )

    parser.add_argument(
        "--input_file_delimiter",
        help="Input file delimiter, default: tab",
        required=False,
        type=str,
        default="\t",
    )

    parser.add_argument(
        "--output_file_delimiter",
        help="Output file delimiter, used if output format is csv, default: comma",
        required=False,
        type=str,
        default=",",
    )

    parser.add_argument(
        "-t",
        "--transpose",
        help="Transpose the table. Genes as rows and samples as columns",
        required=False,
        action="store_true",
    )

    args = parser.parse_args()

    return args


if __name__ == "__main__":
    main()
