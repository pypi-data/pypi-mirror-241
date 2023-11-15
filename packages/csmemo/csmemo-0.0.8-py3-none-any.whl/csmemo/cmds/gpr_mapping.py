#!/usr/bin/env python3
import argparse
import os
import pandas as pd
from cobra.io import read_sbml_model
from corda.util import reaction_confidence
from csmemo.csmbuilder import safe_eval_gpr


MEM_METHODS = ['min', 'sum']


def create_parser():
    parser = argparse.ArgumentParser(description="Map gene omic' data into reactions through the GPR")

    parser.add_argument('sbml_fname', action="store", help='SBML file to use a the model reference')

    parser.add_argument('gene_omic_csv', action="store", help='CSV file storing the gene omic data')

    parser.add_argument('--omic-col', action="store", required=True, dest="omic_col",
                        help='Column ID where the omic data is stored')

    parser.add_argument('--gene-col', action="store", dest="gene_id_col", default="gene_id",
                        help='Gene identifier name used as column name')

    parser.add_argument('--sep', action='store', dest='sep', default='\t', help='Field delimiter for CSV')

    parser.add_argument('--fill-missing', action='store', dest='fill_missing', default=0, type=float,
                        help='Default value to fill missing genes in omic dataset')

    parser.add_argument('--index_col', action='store', dest='index_col', default='reaction_id')

    parser.add_argument('--rxn-info', action='store_true', dest='rxn_info', default=False)

    parser.add_argument('--out', action="store", required=True, dest="output_fname",
                        help='Output file name to store the reaction with omic associated values')

    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()

    assert os.path.isfile(args.sbml_fname)
    assert os.path.isfile(args.gene_omic_csv)

    # Reading Reference Genome-Scale Model
    print(f" - Reading SBML Model from {args.sbml_fname}:", end=" ")
    model = read_sbml_model(args.sbml_fname)
    print(" - OK!")

    # Reading DataFrame including gene confidence
    print(f" - Reading gene omic data {args.gene_omic_csv}:" , end=" ")
    df_gene_omic = pd.read_csv(args.gene_omic_csv, sep='\t', index_col=args.gene_id_col)
    print(" - OK!")

    for g in model.genes:
        if g.id in df_gene_omic.index:
            continue
        print(" - Gene not found:", g.id)
        df_gene_omic.at[g.id, args.omic_col] = args.fill_missing

    print(f" - Mapping {args.omic_col} into reaction using GPRs:", end=" ")

    data = []
    for r in model.reactions:
        if len(r.genes) == 0:
            continue

        conf_genes = {g.id: df_gene_omic.loc[g.id, args.omic_col] for g in r.genes}
        mapped_value = safe_eval_gpr(r.gpr, conf_genes)
        if args.rxn_info:
            data.append((r.id, mapped_value, r.gene_reaction_rule, r.reaction, r.subsystem))
        else:
            data.append((r.id, mapped_value))

    print(" - OK!")

    if args.rxn_info:
        df_reaction_omic = pd.DataFrame(data, columns=[args.index_col, args.omic_col, 'gpr', 'reaction', 'subsystem'])
        df_reaction_omic = df_reaction_omic.set_index(args.index_col)
        df_reaction_omic.sort_values([args.omic_col], inplace=True)
    else:
        df_reaction_omic = pd.DataFrame(data, columns=[args.index_col, args.omic_col])
        df_reaction_omic = df_reaction_omic.set_index(args.index_col)

    
    print(f" - Writing results to {args.output_fname}")
    df_reaction_omic.to_csv(args.output_fname, sep=args.sep)
    



main()

