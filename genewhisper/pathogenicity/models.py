from django.db import models
from projects.models import Project


class OncotatorOutput(models.Model):
    # id = models.IntegerField()
    project = models.OneToOneField(Project, on_delete=models.CASCADE, primary_key=True, )
    hugo_symbol = models.TextField(blank=True, null=True)  # This field type is a guess.
    entrez_gene_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    center = models.TextField(blank=True, null=True)  # This field type is a guess.
    ncbi_build = models.TextField(blank=True, null=True)  # This field type is a guess.
    chromosome = models.TextField(blank=True, null=True)  # This field type is a guess.
    start_position = models.TextField(blank=True, null=True)  # This field type is a guess.
    end_position = models.TextField(blank=True, null=True)  # This field type is a guess.
    strand = models.TextField(blank=True, null=True)  # This field type is a guess.
    variant_classification = models.TextField(blank=True, null=True)  # This field type is a guess.
    variant_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    reference_allele = models.TextField(blank=True, null=True)  # This field type is a guess.
    tumor_seq_allele1 = models.TextField(blank=True, null=True)  # This field type is a guess.
    tumor_seq_allele2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbsnp_rs = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbsnp_val_status = models.TextField(blank=True, null=True)  # This field type is a guess.
    tumor_sample_barcode = models.TextField(blank=True, null=True)  # This field type is a guess.
    matched_norm_sample_barcode = models.TextField(blank=True, null=True)  # This field type is a guess.
    match_norm_seq_allele1 = models.TextField(blank=True, null=True)  # This field type is a guess.
    match_norm_seq_allele2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    tumor_validation_allele1 = models.TextField(blank=True, null=True)  # This field type is a guess.
    tumor_validation_allele2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    match_norm_validation_allele1 = models.TextField(blank=True, null=True)  # This field type is a guess.
    match_norm_validation_allele2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    verification_status = models.TextField(blank=True, null=True)  # This field type is a guess.
    validation_status = models.TextField(blank=True, null=True)  # This field type is a guess.
    mutation_status = models.TextField(blank=True, null=True)  # This field type is a guess.
    sequencing_phase = models.TextField(blank=True, null=True)  # This field type is a guess.
    sequence_source = models.TextField(blank=True, null=True)  # This field type is a guess.
    validation_method = models.TextField(blank=True, null=True)  # This field type is a guess.
    score = models.TextField(blank=True, null=True)  # This field type is a guess.
    bam_file = models.TextField(blank=True, null=True)  # This field type is a guess.
    sequencer = models.TextField(blank=True, null=True)  # This field type is a guess.
    tumor_sample_uuid = models.TextField(blank=True, null=True)  # This field type is a guess.
    matched_norm_sample_uuid = models.TextField(blank=True, null=True)  # This field type is a guess.
    genome_change = models.TextField(blank=True, null=True)  # This field type is a guess.
    annotation_transcript = models.TextField(blank=True, null=True)  # This field type is a guess.
    transcript_strand = models.TextField(blank=True, null=True)  # This field type is a guess.
    transcript_exon = models.TextField(blank=True, null=True)  # This field type is a guess.
    transcript_position = models.TextField(blank=True, null=True)  # This field type is a guess.
    cdna_change = models.TextField(blank=True, null=True)  # This field type is a guess.
    codon_change = models.TextField(blank=True, null=True)  # This field type is a guess.
    protein_change = models.TextField(blank=True, null=True)  # This field type is a guess.
    other_transcripts = models.TextField(blank=True, null=True)  # This field type is a guess.
    refseq_mrna_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    refseq_prot_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    swissprot_acc_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    swissprot_entry_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    description = models.TextField(blank=True, null=True)  # This field type is a guess.
    uniprot_aapos = models.TextField(blank=True, null=True)  # This field type is a guess.
    uniprot_region = models.TextField(blank=True, null=True)  # This field type is a guess.
    uniprot_site = models.TextField(blank=True, null=True)  # This field type is a guess.
    uniprot_natural_variations = models.TextField(blank=True, null=True)  # This field type is a guess.
    uniprot_experimental_info = models.TextField(blank=True, null=True)  # This field type is a guess.
    go_biological_process = models.TextField(blank=True, null=True)  # This field type is a guess.
    go_cellular_component = models.TextField(blank=True, null=True)  # This field type is a guess.
    go_molecular_function = models.TextField(blank=True, null=True)  # This field type is a guess.
    cosmic_overlapping_mutations = models.TextField(blank=True, null=True)  # This field type is a guess.
    cosmic_fusion_genes = models.TextField(blank=True, null=True)  # This field type is a guess.
    cosmic_tissue_types_affected = models.TextField(blank=True, null=True)  # This field type is a guess.
    cosmic_total_alterations_in_gene = models.TextField(blank=True, null=True)  # This field type is a guess.
    tumorscape_amplification_peaks = models.TextField(blank=True, null=True)  # This field type is a guess.
    tumorscape_deletion_peaks = models.TextField(blank=True, null=True)  # This field type is a guess.
    tcgascape_amplification_peaks = models.TextField(blank=True, null=True)  # This field type is a guess.
    tcgascape_deletion_peaks = models.TextField(blank=True, null=True)  # This field type is a guess.
    drugbank = models.TextField(blank=True, null=True)  # This field type is a guess.
    ref_context = models.TextField(blank=True, null=True)  # This field type is a guess.
    gc_content = models.TextField(blank=True, null=True)  # This field type is a guess.
    ccle_oncomap_overlapping_mutations = models.TextField(blank=True, null=True)  # This field type is a guess.
    ccle_oncomap_total_mutations_in_gene = models.TextField(blank=True, null=True)  # This field type is a guess.
    cgc_mutation_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    cgc_translocation_partner = models.TextField(blank=True, null=True)  # This field type is a guess.
    cgc_tumor_types_somatic = models.TextField(blank=True, null=True)  # This field type is a guess.
    cgc_tumor_types_germline = models.TextField(blank=True, null=True)  # This field type is a guess.
    cgc_other_diseases = models.TextField(blank=True, null=True)  # This field type is a guess.
    dnarepairgenes_role = models.TextField(blank=True, null=True)  # This field type is a guess.
    familialcancerdatabase_syndromes = models.TextField(blank=True, null=True)  # This field type is a guess.
    mutsig_published_results = models.TextField(blank=True, null=True)  # This field type is a guess.
    oreganno_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    oreganno_values = models.TextField(blank=True, null=True)  # This field type is a guess.
    number_1000gp3_aa = models.TextField(db_column='1000gp3_aa', blank=True,
                                         null=True)  # Field renamed because it wasn't a valid Python identifier. This field type is a guess.
    number_1000gp3_ac = models.TextField(db_column='1000gp3_ac', blank=True,
                                         null=True)  # Field renamed because it wasn't a valid Python identifier. This field type is a guess.
    number_1000gp3_af = models.TextField(db_column='1000gp3_af', blank=True,
                                         null=True)  # Field renamed because it wasn't a valid Python identifier. This field type is a guess.
    number_1000gp3_afr_af = models.TextField(db_column='1000gp3_afr_af', blank=True,
                                             null=True)  # Field renamed because it wasn't a valid Python identifier. This field type is a guess.
    number_1000gp3_amr_af = models.TextField(db_column='1000gp3_amr_af', blank=True,
                                             null=True)  # Field renamed because it wasn't a valid Python identifier. This field type is a guess.
    number_1000gp3_an = models.TextField(db_column='1000gp3_an', blank=True,
                                         null=True)  # Field renamed because it wasn't a valid Python identifier. This field type is a guess.
    number_1000gp3_ciend = models.TextField(db_column='1000gp3_ciend', blank=True,
                                            null=True)  # Field renamed because it wasn't a valid Python identifier. This field type is a guess.
    number_1000gp3_cipos = models.TextField(db_column='1000gp3_cipos', blank=True,
                                            null=True)  # Field renamed because it wasn't a valid Python identifier. This field type is a guess.
    number_1000gp3_cs = models.TextField(db_column='1000gp3_cs', blank=True,
                                         null=True)  # Field renamed because it wasn't a valid Python identifier. This field type is a guess.
    number_1000gp3_dp = models.TextField(db_column='1000gp3_dp', blank=True,
                                         null=True)  # Field renamed because it wasn't a valid Python identifier. This field type is a guess.
    number_1000gp3_eas_af = models.TextField(db_column='1000gp3_eas_af', blank=True,
                                             null=True)  # Field renamed because it wasn't a valid Python identifier. This field type is a guess.
    number_1000gp3_end = models.TextField(db_column='1000gp3_end', blank=True,
                                          null=True)  # Field renamed because it wasn't a valid Python identifier. This field type is a guess.
    number_1000gp3_eur_af = models.TextField(db_column='1000gp3_eur_af', blank=True,
                                             null=True)  # Field renamed because it wasn't a valid Python identifier. This field type is a guess.
    number_1000gp3_imprecise = models.TextField(db_column='1000gp3_imprecise', blank=True,
                                                null=True)  # Field renamed because it wasn't a valid Python identifier. This field type is a guess.
    number_1000gp3_mc = models.TextField(db_column='1000gp3_mc', blank=True,
                                         null=True)  # Field renamed because it wasn't a valid Python identifier. This field type is a guess.
    number_1000gp3_meinfo = models.TextField(db_column='1000gp3_meinfo', blank=True,
                                             null=True)  # Field renamed because it wasn't a valid Python identifier. This field type is a guess.
    number_1000gp3_mend = models.TextField(db_column='1000gp3_mend', blank=True,
                                           null=True)  # Field renamed because it wasn't a valid Python identifier. This field type is a guess.
    number_1000gp3_mlen = models.TextField(db_column='1000gp3_mlen', blank=True,
                                           null=True)  # Field renamed because it wasn't a valid Python identifier. This field type is a guess.
    number_1000gp3_mstart = models.TextField(db_column='1000gp3_mstart', blank=True,
                                             null=True)  # Field renamed because it wasn't a valid Python identifier. This field type is a guess.
    number_1000gp3_ns = models.TextField(db_column='1000gp3_ns', blank=True,
                                         null=True)  # Field renamed because it wasn't a valid Python identifier. This field type is a guess.
    number_1000gp3_sas_af = models.TextField(db_column='1000gp3_sas_af', blank=True,
                                             null=True)  # Field renamed because it wasn't a valid Python identifier. This field type is a guess.
    number_1000gp3_svlen = models.TextField(db_column='1000gp3_svlen', blank=True,
                                            null=True)  # Field renamed because it wasn't a valid Python identifier. This field type is a guess.
    number_1000gp3_svtype = models.TextField(db_column='1000gp3_svtype', blank=True,
                                             null=True)  # Field renamed because it wasn't a valid Python identifier. This field type is a guess.
    number_1000gp3_tsd = models.TextField(db_column='1000gp3_tsd', blank=True,
                                          null=True)  # Field renamed because it wasn't a valid Python identifier. This field type is a guess.
    achilles_lineage_results_top_genes = models.TextField(blank=True, null=True)  # This field type is a guess.
    cgc_cancer_germline_mut = models.TextField(db_column='cgc_cancer germline mut', blank=True,
                                               null=True)  # Field renamed to remove unsuitable characters. This field type is a guess.
    cgc_cancer_molecular_genetics = models.TextField(db_column='cgc_cancer molecular genetics', blank=True,
                                                     null=True)  # Field renamed to remove unsuitable characters. This field type is a guess.
    cgc_cancer_somatic_mut = models.TextField(db_column='cgc_cancer somatic mut', blank=True,
                                              null=True)  # Field renamed to remove unsuitable characters. This field type is a guess.
    cgc_cancer_syndrome = models.TextField(db_column='cgc_cancer syndrome', blank=True,
                                           null=True)  # Field renamed to remove unsuitable characters. This field type is a guess.
    cgc_chr = models.TextField(blank=True, null=True)  # This field type is a guess.
    cgc_chr_band = models.TextField(db_column='cgc_chr band', blank=True,
                                    null=True)  # Field renamed to remove unsuitable characters. This field type is a guess.
    cgc_geneid = models.TextField(blank=True, null=True)  # This field type is a guess.
    cgc_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    cgc_other_germline_mut = models.TextField(db_column='cgc_other germline mut', blank=True,
                                              null=True)  # Field renamed to remove unsuitable characters. This field type is a guess.
    cgc_tissue_type = models.TextField(db_column='cgc_tissue type', blank=True,
                                       null=True)  # Field renamed to remove unsuitable characters. This field type is a guess.
    cosmic_fusiongenes_fusion_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    cosmic_n_overlapping_mutations = models.TextField(blank=True, null=True)  # This field type is a guess.
    cosmic_overlapping_mutation_descriptions = models.TextField(blank=True, null=True)  # This field type is a guess.
    cosmic_overlapping_primary_sites = models.TextField(blank=True, null=True)  # This field type is a guess.
    clinvar_assembly = models.TextField(blank=True, null=True)  # This field type is a guess.
    clinvar_hgmd_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    clinvar_sym = models.TextField(blank=True, null=True)  # This field type is a guess.
    clinvar_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    clinvar_rs = models.TextField(blank=True, null=True)  # This field type is a guess.
    ensembl_so_accession = models.TextField(blank=True, null=True)  # This field type is a guess.
    ensembl_so_term = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_ac = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_ac_afr = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_ac_amr = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_ac_adj = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_ac_consanguineous = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_ac_eas = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_ac_female = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_ac_fin = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_ac_hemi = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_ac_het = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_ac_hom = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_ac_male = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_ac_nfe = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_ac_oth = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_ac_popmax = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_ac_sas = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_af = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_an = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_an_afr = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_an_amr = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_an_adj = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_an_consanguineous = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_an_eas = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_an_female = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_an_fin = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_an_male = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_an_nfe = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_an_oth = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_an_popmax = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_an_sas = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_baseqranksum = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_ccc = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_csq = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_clippingranksum = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_db = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_doubleton_dist = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_dp = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_dp_hist = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_ds = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_end = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_esp_ac = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_esp_af_global = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_esp_af_popmax = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_fs = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_gq_hist = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_gq_mean = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_gq_stddev = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_hwp = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_haplotypescore = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_hemi_afr = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_hemi_amr = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_hemi_eas = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_hemi_fin = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_hemi_nfe = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_hemi_oth = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_hemi_sas = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_het_afr = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_het_amr = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_het_eas = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_het_fin = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_het_nfe = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_het_oth = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_het_sas = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_hom_afr = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_hom_amr = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_hom_consanguineous = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_hom_eas = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_hom_fin = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_hom_nfe = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_hom_oth = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_hom_sas = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_inbreedingcoeff = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_k1_run = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_k2_run = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_k3_run = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_kg_ac = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_kg_af_global = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_kg_af_popmax = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_mleac = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_mleaf = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_mq = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_mq0 = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_mqranksum = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_ncc = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_negative_train_site = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_popmax = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_positive_train_site = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_qd = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_readposranksum = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_vqslod = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_clinvar_conflicted = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_clinvar_measureset_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_clinvar_mut = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_clinvar_pathogenic = models.TextField(blank=True, null=True)  # This field type is a guess.
    exac_culprit = models.TextField(blank=True, null=True)  # This field type is a guess.
    familial_cancer_genes_reference = models.TextField(blank=True, null=True)  # This field type is a guess.
    familial_cancer_genes_synonym = models.TextField(blank=True, null=True)  # This field type is a guess.
    hgnc_accession_numbers = models.TextField(db_column='hgnc_accession numbers', blank=True,
                                              null=True)  # Field renamed to remove unsuitable characters. This field type is a guess.
    hgnc_ccds_ids = models.TextField(db_column='hgnc_ccds ids', blank=True,
                                     null=True)  # Field renamed to remove unsuitable characters. This field type is a guess.
    hgnc_chromosome = models.TextField(blank=True, null=True)  # This field type is a guess.
    hgnc_date_modified = models.TextField(db_column='hgnc_date modified', blank=True,
                                          null=True)  # Field renamed to remove unsuitable characters. This field type is a guess.
    hgnc_date_name_changed = models.TextField(db_column='hgnc_date name changed', blank=True,
                                              null=True)  # Field renamed to remove unsuitable characters. This field type is a guess.
    hgnc_date_symbol_changed = models.TextField(db_column='hgnc_date symbol changed', blank=True,
                                                null=True)  # Field renamed to remove unsuitable characters. This field type is a guess.
    hgnc_ensembl_gene_id = models.TextField(db_column='hgnc_ensembl gene id', blank=True,
                                            null=True)  # Field renamed to remove unsuitable characters. This field type is a guess.
    hgnc_ensembl_id_supplied_by_ensembl_field = models.TextField(db_column='hgnc_ensembl id(supplied by ensembl)',
                                                                 blank=True,
                                                                 null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    hgnc_enzyme_ids = models.TextField(db_column='hgnc_enzyme ids', blank=True,
                                       null=True)  # Field renamed to remove unsuitable characters. This field type is a guess.
    hgnc_gene_family_description = models.TextField(db_column='hgnc_gene family description', blank=True,
                                                    null=True)  # Field renamed to remove unsuitable characters. This field type is a guess.
    hgnc_hgnc_id = models.TextField(db_column='hgnc_hgnc id', blank=True,
                                    null=True)  # Field renamed to remove unsuitable characters. This field type is a guess.
    hgnc_locus_group = models.TextField(db_column='hgnc_locus group', blank=True,
                                        null=True)  # Field renamed to remove unsuitable characters. This field type is a guess.
    hgnc_locus_type = models.TextField(db_column='hgnc_locus type', blank=True,
                                       null=True)  # Field renamed to remove unsuitable characters. This field type is a guess.
    hgnc_name_synonyms = models.TextField(db_column='hgnc_name synonyms', blank=True,
                                          null=True)  # Field renamed to remove unsuitable characters. This field type is a guess.
    hgnc_omim_id_supplied_by_ncbi_field = models.TextField(db_column='hgnc_omim id(supplied by ncbi)', blank=True,
                                                           null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    hgnc_previous_names = models.TextField(db_column='hgnc_previous names', blank=True,
                                           null=True)  # Field renamed to remove unsuitable characters. This field type is a guess.
    hgnc_previous_symbols = models.TextField(db_column='hgnc_previous symbols', blank=True,
                                             null=True)  # Field renamed to remove unsuitable characters. This field type is a guess.
    hgnc_primary_ids = models.TextField(db_column='hgnc_primary ids', blank=True,
                                        null=True)  # Field renamed to remove unsuitable characters. This field type is a guess.
    hgnc_pubmed_ids = models.TextField(db_column='hgnc_pubmed ids', blank=True,
                                       null=True)  # Field renamed to remove unsuitable characters. This field type is a guess.
    hgnc_record_type = models.TextField(db_column='hgnc_record type', blank=True,
                                        null=True)  # Field renamed to remove unsuitable characters. This field type is a guess.
    hgnc_refseq_supplied_by_ncbi_field = models.TextField(db_column='hgnc_refseq(supplied by ncbi)', blank=True,
                                                          null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    hgnc_secondary_ids = models.TextField(db_column='hgnc_secondary ids', blank=True,
                                          null=True)  # Field renamed to remove unsuitable characters. This field type is a guess.
    hgnc_status = models.TextField(blank=True, null=True)  # This field type is a guess.
    hgnc_synonyms = models.TextField(blank=True, null=True)  # This field type is a guess.
    hgnc_ucsc_id_supplied_by_ucsc_field = models.TextField(db_column='hgnc_ucsc id(supplied by ucsc)', blank=True,
                                                           null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    hgnc_uniprot_id_supplied_by_uniprot_field = models.TextField(db_column='hgnc_uniprot id(supplied by uniprot)',
                                                                 blank=True,
                                                                 null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    hgnc_vega_ids = models.TextField(db_column='hgnc_vega ids', blank=True,
                                     null=True)  # Field renamed to remove unsuitable characters. This field type is a guess.
    hgvs_coding_dna_change = models.TextField(blank=True, null=True)  # This field type is a guess.
    hgvs_genomic_change = models.TextField(blank=True, null=True)  # This field type is a guess.
    hgvs_protein_change = models.TextField(blank=True, null=True)  # This field type is a guess.
    oreganno_bin = models.TextField(blank=True, null=True)  # This field type is a guess.
    uniprot_alt_uniprot_accessions = models.TextField(blank=True, null=True)  # This field type is a guess.
    annotation_transcript2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    build = models.TextField(blank=True, null=True)  # This field type is a guess.
    ccds_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_1000gp1_ac = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_1000gp1_af = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_1000gp1_afr_ac = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_1000gp1_afr_af = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_1000gp1_amr_ac = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_1000gp1_amr_af = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_1000gp1_asn_ac = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_1000gp1_asn_af = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_1000gp1_eur_ac = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_1000gp1_eur_af = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_ancestral_allele = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_cadd_phred = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_cadd_raw = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_cadd_raw_rankscore = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_esp6500_aa_af = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_esp6500_ea_af = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_ensembl_geneid = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_ensembl_transcriptid = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_fathmm_pred = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_fathmm_rankscore = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_fathmm_score = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_gerp_nr = models.TextField(db_column='dbnsfp_gerp++_nr', blank=True,
                                      null=True)  # Field renamed to remove unsuitable characters. This field type is a guess.
    dbnsfp_gerp_rs = models.TextField(db_column='dbnsfp_gerp++_rs', blank=True,
                                      null=True)  # Field renamed to remove unsuitable characters. This field type is a guess.
    dbnsfp_gerp_rs_rankscore = models.TextField(db_column='dbnsfp_gerp++_rs_rankscore', blank=True,
                                                null=True)  # Field renamed to remove unsuitable characters. This field type is a guess.
    dbnsfp_interpro_domain = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_lrt_omega = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_lrt_converted_rankscore = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_lrt_pred = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_lrt_score = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_lr_pred = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_lr_rankscore = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_lr_score = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_mutationassessor_pred = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_mutationassessor_rankscore = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_mutationassessor_score = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_mutationtaster_converted_rankscore = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_mutationtaster_pred = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_mutationtaster_score = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_polyphen2_hdiv_pred = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_polyphen2_hdiv_rankscore = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_polyphen2_hdiv_score = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_polyphen2_hvar_pred = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_polyphen2_hvar_rankscore = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_polyphen2_hvar_score = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_radialsvm_pred = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_radialsvm_rankscore = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_radialsvm_score = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_reliability_index = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_sift_converted_rankscore = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_sift_pred = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_sift_score = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_slr_test_statistic = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_siphy_29way_logodds = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_siphy_29way_logodds_rankscore = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_siphy_29way_pi = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_unisnp_ids = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_uniprot_aapos = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_uniprot_acc = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_uniprot_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_aaalt = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_aapos = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_aapos_fathmm = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_aapos_sift = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_aaref = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_cds_strand = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_codonpos = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_fold_degenerate = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_genename = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_hg18_pos_1_coor_field = models.TextField(db_column='dbnsfp_hg18_pos(1_coor)', blank=True,
                                                    null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    dbnsfp_phastcons100way_vertebrate = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_phastcons100way_vertebrate_rankscore = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_phastcons46way_placental = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_phastcons46way_placental_rankscore = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_phastcons46way_primate = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_phastcons46way_primate_rankscore = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_phylop100way_vertebrate = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_phylop100way_vertebrate_rankscore = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_phylop46way_placental = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_phylop46way_placental_rankscore = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_phylop46way_primate = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_phylop46way_primate_rankscore = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbnsfp_refcodon = models.TextField(blank=True, null=True)  # This field type is a guess.
    entrez_gene_id2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    gencode_transcript_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    gencode_transcript_status = models.TextField(blank=True, null=True)  # This field type is a guess.
    gencode_transcript_tags = models.TextField(blank=True, null=True)  # This field type is a guess.
    gencode_transcript_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    gene_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    havana_transcript = models.TextField(blank=True, null=True)  # This field type is a guess.
    init_t_lod = models.TextField(blank=True, null=True)  # This field type is a guess.
    judgement = models.TextField(blank=True, null=True)  # This field type is a guess.
    refseq_mrna_id2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    secondary_variant_classification = models.TextField(blank=True, null=True)  # This field type is a guess.
    t_alt_count = models.TextField(blank=True, null=True)  # This field type is a guess.
    t_lod_fstar = models.TextField(blank=True, null=True)  # This field type is a guess.
    t_ref_count = models.TextField(blank=True, null=True)  # This field type is a guess.
    tumor_f = models.TextField(blank=True, null=True)  # This field type is a guess.
    PVS1 = models.TextField(blank=True, null=True)
