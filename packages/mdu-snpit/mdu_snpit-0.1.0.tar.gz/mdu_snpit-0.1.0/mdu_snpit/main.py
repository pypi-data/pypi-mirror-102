import json
import pysam
import os
from collections import Counter
import importlib_resources as pk_resources
import argparse

def load_json(mfile):
    with pk_resources.path("mdu_snpit.db", mfile) as nf:
        with open(nf) as json_file:
            data = json.load(json_file)
    return data

pos_db = load_json("snpit.db.json")
id_dict = load_json("snpit.id.json")
count_db = load_json("snpit.count.json")

def use_vcf(vcf_file):
    id_counter = Counter()
    result_dict = {}
    myvcf = pysam.VariantFile(vcf_file)
    sample_name = ""
    for rec in myvcf.fetch():
        chrom = rec.chrom
        if sample_name == "":
            sample_name = chrom
        elif sample_name != chrom:
            win_id, score = find_high_score(id_counter)
            result_dict[sample_name] = [win_id, score]
            id_counter.clear()
        pos = str(rec.pos)
        alt = rec.alts[0]
        #print(alt)
        qual = float(rec.qual)
        #print(qual)
        if qual < 100 or len(alt) > 1:
            continue
        pos_line = pos_db.get(pos, {})
        #print(pos_line)
        m_id_list = pos_line.get(alt, [])
        #print(m_id_list)
        for m_id in m_id_list:
            id_counter[m_id] += 1
    #print(id_counter)
    win_id, score = find_high_score(id_counter)
    result_dict[sample_name] = [win_id, score]
    print_out_result(result_dict)
    return

def use_tab(tab_file):
    id_counter = Counter()
    with open(tab_file, 'r') as mytab:
        count = 0
        sample_name = ""
        result_dict = {}
        for line in mytab:
            if count == 0:
                count += 1
                continue
            info = line.strip().split("\t")
            my_s_name = info[0]
            if sample_name == "":
                sample_name = my_s_name
            elif sample_name != my_s_name:
                win_id, score = find_high_score(id_counter)
                result_dict[sample_name] = [win_id, score]
                id_counter.clear()
            pos = info[1]
            g_type = info[2]
            alt = info[4]
            if g_type != "snp":
                continue
            pos_line = pos_db.get(pos, {})
            m_id_list = pos_line.get(alt, [])
            for m_id in m_id_list:
                id_counter[m_id] += 1
    #print(id_counter)
    win_id, score = find_high_score(id_counter)
    result_dict[sample_name] = [win_id, score]
    print_out_result(result_dict)

def find_high_score(mycounter):
    id_score = {}
    high_score = 0
    high_id = ""
    for mid, count in mycounter.items():
        total = count_db.get(mid)
        score = round(float(count)/total*100, 2)
        id_score[mid] = score
        if score > high_score:
            high_id = mid
            high_score = score
    #print(id_score)
    return (high_id, high_score)
def use_fasta(fasta_file):
    myfasta = pysam.FastaFile(fasta_file)
    result_dict = {}
    for sample_name in myfasta.references:
        id_counter = Counter()
        for pos in pos_db:
            num = int(pos)
            pos_line = pos_db.get(pos)
            #print(pos_line)
            fa_call = myfasta.fetch(reference=sample_name, start=num-1, end=num)
            #print("fa:", fa_call)
            m_id_list = pos_line.get(fa_call, [])
            for m_id in m_id_list:
                id_counter[m_id] += 1
        win_id, score = find_high_score(id_counter)
        result_dict[sample_name] = [win_id, score]
    myfasta.close()
    #win_id, score = find_high_score(id_counter)
    print_out_result(result_dict)

def print_out_result(result_dict):
    print("Sample\tSpecies\tLineage\tSublineage\tName\tPercentage")
    for sample_name in result_dict:
        win_id, score = result_dict.get(sample_name)
        if win_id == "":
            #print(f"{sample_name}\tN/A\tN/A\tN/A\tN/A\tN/A")
            print("\t".join([sample_name, "N/A", "N/A", "N/A", "N/A", "N/A"]))
        else:
            info = id_dict[win_id]
            info = list(map(lambda x: "N/A" if len(x) == 0 else x, info))
            #print(f"{sample_name}\t{info[1]}\t{info[2]}\t{info[3]}\t{info[0]\t{score}}")
            print("\t".join([sample_name, info[1], info[2], info[3], info[0], str(score)]))

def main():
    #use_fasta("snps.aligned.fa")
    #use_tab("snps.tab")
    #use_vcf("snps.vcf")
    #use_fasta("ref.fa")
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="fasta file, or snps.tab or vcf file")
    args = parser.parse_args()
    if not os.path.exists(args.input):
        print(f"{args.input} does not exist, please check your input")
    else:
        file_type = args.input.split(".")[-1]
        if file_type == "fasta" or file_type == "fa":
            use_fasta(args.input)
        elif file_type == "tab":
            use_tab(args.input)
        elif file_type == "vcf":
            use_vcf(args.input)
        else:
            print(f"Input file type error, please check your input")

if __name__ == "__main__":
    main()
