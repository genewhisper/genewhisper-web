from django.db import models
from projects.models import Project


class OncotatorOutput(models.Model):
    # id = models.CharField(unique=True, max_length=43, blank=True, null=True)
    project = models.OneToOneField(Project, primary_key=True, on_delete=models.CASCADE)

    hugo_symbol = models.CharField(db_column='Hugo_Symbol', max_length=14, blank=True,
                                   null=True)  # Field name made lowercase.
    entrez_gene_id = models.IntegerField(db_column='Entrez_Gene_Id', blank=True,
                                         null=True)  # Field name made lowercase.
    center = models.CharField(db_column='Center', max_length=11, blank=True, null=True)  # Field name made lowercase.
    ncbi_build = models.CharField(db_column='NCBI_Build', max_length=11, blank=True,
                                  null=True)  # Field name made lowercase.
    chromosome = models.CharField(db_column='Chromosome', max_length=10, blank=True,
                                  null=True)  # Field name made lowercase.
    start_position = models.IntegerField(db_column='Start_position', blank=True,
                                         null=True)  # Field name made lowercase.
    end_position = models.IntegerField(db_column='End_position', blank=True, null=True)  # Field name made lowercase.
    strand = models.CharField(db_column='Strand', max_length=11, blank=True, null=True)  # Field name made lowercase.
    variant_classification = models.CharField(db_column='Variant_Classification', max_length=17, blank=True,
                                              null=True)  # Field name made lowercase.
    variant_type = models.CharField(db_column='Variant_Type', max_length=3, blank=True,
                                    null=True)  # Field name made lowercase.
    reference_allele = models.CharField(db_column='Reference_Allele', max_length=1, blank=True,
                                        null=True)  # Field name made lowercase.
    tumor_seq_allele1 = models.CharField(db_column='Tumor_Seq_Allele1', max_length=1, blank=True,
                                         null=True)  # Field name made lowercase.
    tumor_seq_allele2 = models.CharField(db_column='Tumor_Seq_Allele2', max_length=1, blank=True,
                                         null=True)  # Field name made lowercase.
    dbsnp_rs = models.IntegerField(db_column='dbSNP_RS', blank=True, null=True)  # Field name made lowercase.
    dbsnp_val_status = models.IntegerField(db_column='dbSNP_Val_Status', blank=True,
                                           null=True)  # Field name made lowercase.
    tumor_sample_barcode = models.CharField(db_column='Tumor_Sample_Barcode', max_length=14, blank=True,
                                            null=True)  # Field name made lowercase.
    matched_norm_sample_barcode = models.CharField(db_column='Matched_Norm_Sample_Barcode', max_length=15, blank=True,
                                                   null=True)  # Field name made lowercase.
    match_norm_seq_allele1 = models.CharField(db_column='Match_Norm_Seq_Allele1', max_length=11, blank=True,
                                              null=True)  # Field name made lowercase.
    match_norm_seq_allele2 = models.CharField(db_column='Match_Norm_Seq_Allele2', max_length=11, blank=True,
                                              null=True)  # Field name made lowercase.
    tumor_validation_allele1 = models.CharField(db_column='Tumor_Validation_Allele1', max_length=11, blank=True,
                                                null=True)  # Field name made lowercase.
    tumor_validation_allele2 = models.CharField(db_column='Tumor_Validation_Allele2', max_length=11, blank=True,
                                                null=True)  # Field name made lowercase.
    match_norm_validation_allele1 = models.CharField(db_column='Match_Norm_Validation_Allele1', max_length=11,
                                                     blank=True, null=True)  # Field name made lowercase.
    match_norm_validation_allele2 = models.CharField(db_column='Match_Norm_Validation_Allele2', max_length=11,
                                                     blank=True, null=True)  # Field name made lowercase.
    verification_status = models.CharField(db_column='Verification_Status', max_length=11, blank=True,
                                           null=True)  # Field name made lowercase.
    validation_status = models.CharField(db_column='Validation_Status', max_length=11, blank=True,
                                         null=True)  # Field name made lowercase.
    mutation_status = models.CharField(db_column='Mutation_Status', max_length=11, blank=True,
                                       null=True)  # Field name made lowercase.
    sequencing_phase = models.CharField(db_column='Sequencing_Phase', max_length=11, blank=True,
                                        null=True)  # Field name made lowercase.
    sequence_source = models.CharField(db_column='Sequence_Source', max_length=11, blank=True,
                                       null=True)  # Field name made lowercase.
    validation_method = models.CharField(db_column='Validation_Method', max_length=11, blank=True,
                                         null=True)  # Field name made lowercase.
    score = models.CharField(db_column='Score', max_length=11, blank=True, null=True)  # Field name made lowercase.
    bam_file = models.CharField(db_column='BAM_file', max_length=11, blank=True,
                                null=True)  # Field name made lowercase.
    sequencer = models.CharField(db_column='Sequencer', max_length=11, blank=True,
                                 null=True)  # Field name made lowercase.
    tumor_sample_uuid = models.CharField(db_column='Tumor_Sample_UUID', max_length=14, blank=True,
                                         null=True)  # Field name made lowercase.
    matched_norm_sample_uuid = models.CharField(db_column='Matched_Norm_Sample_UUID', max_length=15, blank=True,
                                                null=True)  # Field name made lowercase.
    genome_change = models.CharField(db_column='Genome_Change', max_length=25, blank=True,
                                     null=True)  # Field name made lowercase.
    annotation_transcript = models.CharField(db_column='Annotation_Transcript', max_length=17, blank=True,
                                             null=True)  # Field name made lowercase.
    transcript_strand = models.CharField(db_column='Transcript_Strand', max_length=1, blank=True,
                                         null=True)  # Field name made lowercase.
    transcript_exon = models.IntegerField(db_column='Transcript_Exon', blank=True,
                                          null=True)  # Field name made lowercase.
    transcript_position = models.IntegerField(db_column='Transcript_Position', blank=True,
                                              null=True)  # Field name made lowercase.
    cdna_change = models.CharField(db_column='cDNA_Change', max_length=10, blank=True,
                                   null=True)  # Field name made lowercase.
    codon_change = models.CharField(db_column='Codon_Change', max_length=22, blank=True,
                                    null=True)  # Field name made lowercase.
    protein_change = models.CharField(db_column='Protein_Change', max_length=9, blank=True,
                                      null=True)  # Field name made lowercase.
    other_transcripts = models.CharField(db_column='Other_Transcripts', max_length=729, blank=True,
                                         null=True)  # Field name made lowercase.
    refseq_mrna_id = models.CharField(db_column='Refseq_mRNA_Id', max_length=89, blank=True,
                                      null=True)  # Field name made lowercase.
    refseq_prot_id = models.CharField(db_column='Refseq_prot_Id', max_length=89, blank=True,
                                      null=True)  # Field name made lowercase.
    swissprot_acc_id = models.CharField(db_column='SwissProt_acc_Id', max_length=6, blank=True,
                                        null=True)  # Field name made lowercase.
    swissprot_entry_id = models.CharField(db_column='SwissProt_entry_Id', max_length=11, blank=True,
                                          null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=112, blank=True,
                                   null=True)  # Field name made lowercase.
    uniprot_aapos = models.IntegerField(db_column='UniProt_AApos', blank=True, null=True)  # Field name made lowercase.
    uniprot_region = models.CharField(db_column='UniProt_Region', max_length=131, blank=True,
                                      null=True)  # Field name made lowercase.
    uniprot_site = models.IntegerField(db_column='UniProt_Site', blank=True, null=True)  # Field name made lowercase.
    uniprot_natural_variations = models.CharField(db_column='UniProt_Natural_Variations', max_length=369, blank=True,
                                                  null=True)  # Field name made lowercase.
    uniprot_experimental_info = models.CharField(db_column='UniProt_Experimental_Info', max_length=60, blank=True,
                                                 null=True)  # Field name made lowercase.
    go_biological_process = models.CharField(db_column='GO_Biological_Process', max_length=5179, blank=True,
                                             null=True)  # Field name made lowercase.
    go_cellular_component = models.CharField(db_column='GO_Cellular_Component', max_length=806, blank=True,
                                             null=True)  # Field name made lowercase.
    go_molecular_function = models.CharField(db_column='GO_Molecular_Function', max_length=1121, blank=True,
                                             null=True)  # Field name made lowercase.
    cosmic_overlapping_mutations = models.CharField(db_column='COSMIC_overlapping_mutations', max_length=22, blank=True,
                                                    null=True)  # Field name made lowercase.
    cosmic_fusion_genes = models.TextField(db_column='COSMIC_fusion_genes', blank=True,
                                           null=True)  # Field name made lowercase.
    cosmic_tissue_types_affected = models.CharField(db_column='COSMIC_tissue_types_affected', max_length=562,
                                                    blank=True, null=True)  # Field name made lowercase.
    cosmic_total_alterations_in_gene = models.IntegerField(db_column='COSMIC_total_alterations_in_gene', blank=True,
                                                           null=True)  # Field name made lowercase.
    tumorscape_amplification_peaks = models.CharField(db_column='Tumorscape_Amplification_Peaks', max_length=249,
                                                      blank=True, null=True)  # Field name made lowercase.
    tumorscape_deletion_peaks = models.CharField(db_column='Tumorscape_Deletion_Peaks', max_length=370, blank=True,
                                                 null=True)  # Field name made lowercase.
    tcgascape_amplification_peaks = models.CharField(db_column='TCGAscape_Amplification_Peaks', max_length=219,
                                                     blank=True, null=True)  # Field name made lowercase.
    tcgascape_deletion_peaks = models.CharField(db_column='TCGAscape_Deletion_Peaks', max_length=427, blank=True,
                                                null=True)  # Field name made lowercase.
    drugbank = models.CharField(db_column='DrugBank', max_length=1728, blank=True,
                                null=True)  # Field name made lowercase.
    ref_context = models.CharField(max_length=21, blank=True, null=True)
    gc_content = models.TextField(blank=True, null=True)  # This field type is a guess.
    ccle_oncomap_overlapping_mutations = models.IntegerField(db_column='CCLE_ONCOMAP_overlapping_mutations', blank=True,
                                                             null=True)  # Field name made lowercase.
    ccle_oncomap_total_mutations_in_gene = models.IntegerField(db_column='CCLE_ONCOMAP_total_mutations_in_gene',
                                                               blank=True, null=True)  # Field name made lowercase.
    cgc_mutation_type = models.CharField(db_column='CGC_Mutation_Type', max_length=20, blank=True,
                                         null=True)  # Field name made lowercase.
    cgc_translocation_partner = models.CharField(db_column='CGC_Translocation_Partner', max_length=124, blank=True,
                                                 null=True)  # Field name made lowercase.
    cgc_tumor_types_somatic = models.CharField(db_column='CGC_Tumor_Types_Somatic', max_length=86, blank=True,
                                               null=True)  # Field name made lowercase.
    cgc_tumor_types_germline = models.CharField(db_column='CGC_Tumor_Types_Germline', max_length=74, blank=True,
                                                null=True)  # Field name made lowercase.
    cgc_other_diseases = models.CharField(db_column='CGC_Other_Diseases', max_length=70, blank=True,
                                          null=True)  # Field name made lowercase.
    dnarepairgenes_role = models.CharField(db_column='DNARepairGenes_Role', max_length=58, blank=True,
                                           null=True)  # Field name made lowercase.
    familialcancerdatabase_syndromes = models.CharField(db_column='FamilialCancerDatabase_Syndromes', max_length=112,
                                                        blank=True, null=True)  # Field name made lowercase.
    mutsig_published_results = models.CharField(db_column='MUTSIG_Published_Results', max_length=38, blank=True,
                                                null=True)  # Field name made lowercase.
    oreganno_id = models.CharField(db_column='OREGANNO_ID', max_length=11, blank=True,
                                   null=True)  # Field name made lowercase.
    oreganno_values = models.CharField(db_column='OREGANNO_Values', max_length=120, blank=True,
                                       null=True)  # Field name made lowercase.
    column_1000gp3_aa = models.CharField(db_column='Column_1000gp3_AA', max_length=4, blank=True,
                                         null=True)  # Field name made lowercase.
    column_1000gp3_ac = models.IntegerField(db_column='Column_1000gp3_AC', blank=True,
                                            null=True)  # Field name made lowercase.
    column_1000gp3_af = models.TextField(db_column='Column_1000gp3_AF', blank=True,
                                         null=True)  # Field name made lowercase. This field type is a guess.
    column_1000gp3_afr_af = models.TextField(db_column='Column_1000gp3_AFR_AF', blank=True,
                                             null=True)  # Field name made lowercase. This field type is a guess.
    column_1000gp3_amr_af = models.TextField(db_column='Column_1000gp3_AMR_AF', blank=True,
                                             null=True)  # Field name made lowercase. This field type is a guess.
    column_1000gp3_an = models.IntegerField(db_column='Column_1000gp3_AN', blank=True,
                                            null=True)  # Field name made lowercase.
    column_1000gp3_ciend = models.CharField(db_column='Column_1000gp3_CIEND', max_length=1, blank=True,
                                            null=True)  # Field name made lowercase.
    column_1000gp3_cipos = models.CharField(db_column='Column_1000gp3_CIPOS', max_length=1, blank=True,
                                            null=True)  # Field name made lowercase.
    column_1000gp3_cs = models.IntegerField(db_column='Column_1000gp3_CS', blank=True,
                                            null=True)  # Field name made lowercase.
    column_1000gp3_dp = models.IntegerField(db_column='Column_1000gp3_DP', blank=True,
                                            null=True)  # Field name made lowercase.
    column_1000gp3_eas_af = models.TextField(db_column='Column_1000gp3_EAS_AF', blank=True,
                                             null=True)  # Field name made lowercase. This field type is a guess.
    column_1000gp3_end = models.IntegerField(db_column='Column_1000gp3_END', blank=True,
                                             null=True)  # Field name made lowercase.
    column_1000gp3_eur_af = models.IntegerField(db_column='Column_1000gp3_EUR_AF', blank=True,
                                                null=True)  # Field name made lowercase.
    column_1000gp3_imprecise = models.CharField(db_column='Column_1000gp3_IMPRECISE', max_length=5, blank=True,
                                                null=True)  # Field name made lowercase.
    column_1000gp3_mc = models.IntegerField(db_column='Column_1000gp3_MC', blank=True,
                                            null=True)  # Field name made lowercase.
    column_1000gp3_meinfo = models.CharField(db_column='Column_1000gp3_MEINFO', max_length=3, blank=True,
                                             null=True)  # Field name made lowercase.
    column_1000gp3_mend = models.IntegerField(db_column='Column_1000gp3_MEND', blank=True,
                                              null=True)  # Field name made lowercase.
    column_1000gp3_mlen = models.IntegerField(db_column='Column_1000gp3_MLEN', blank=True,
                                              null=True)  # Field name made lowercase.
    column_1000gp3_mstart = models.IntegerField(db_column='Column_1000gp3_MSTART', blank=True,
                                                null=True)  # Field name made lowercase.
    column_1000gp3_ns = models.IntegerField(db_column='Column_1000gp3_NS', blank=True,
                                            null=True)  # Field name made lowercase.
    column_1000gp3_sas_af = models.TextField(db_column='Column_1000gp3_SAS_AF', blank=True,
                                             null=True)  # Field name made lowercase. This field type is a guess.
    column_1000gp3_svlen = models.IntegerField(db_column='Column_1000gp3_SVLEN', blank=True,
                                               null=True)  # Field name made lowercase.
    column_1000gp3_svtype = models.IntegerField(db_column='Column_1000gp3_SVTYPE', blank=True,
                                                null=True)  # Field name made lowercase.
    column_1000gp3_tsd = models.IntegerField(db_column='Column_1000gp3_TSD', blank=True,
                                             null=True)  # Field name made lowercase.
    achilles_lineage_results_top_genes = models.CharField(db_column='ACHILLES_Lineage_Results_Top_Genes',
                                                          max_length=122, blank=True,
                                                          null=True)  # Field name made lowercase.
    cgc_cancer_germline_mut = models.CharField(db_column='CGC_Cancer_Germline_Mut', max_length=3, blank=True,
                                               null=True)  # Field name made lowercase.
    cgc_cancer_molecular_genetics = models.CharField(db_column='CGC_Cancer_Molecular_Genetics', max_length=3,
                                                     blank=True, null=True)  # Field name made lowercase.
    cgc_cancer_somatic_mut = models.CharField(db_column='CGC_Cancer_Somatic_Mut', max_length=3, blank=True,
                                              null=True)  # Field name made lowercase.
    cgc_cancer_syndrome = models.CharField(db_column='CGC_Cancer_Syndrome', max_length=50, blank=True,
                                           null=True)  # Field name made lowercase.
    cgc_chr = models.IntegerField(db_column='CGC_Chr', blank=True, null=True)  # Field name made lowercase.
    cgc_chr_band = models.CharField(db_column='CGC_Chr_Band', max_length=14, blank=True,
                                    null=True)  # Field name made lowercase.
    cgc_geneid = models.IntegerField(db_column='CGC_GeneID', blank=True, null=True)  # Field name made lowercase.
    cgc_name = models.CharField(db_column='CGC_Name', max_length=65, blank=True,
                                null=True)  # Field name made lowercase.
    cgc_other_germline_mut = models.CharField(db_column='CGC_Other_Germline_Mut', max_length=3, blank=True,
                                              null=True)  # Field name made lowercase.
    cgc_tissue_type = models.CharField(db_column='CGC_Tissue_Type', max_length=9, blank=True,
                                       null=True)  # Field name made lowercase.
    cosmic_fusiongenes_fusion_id = models.IntegerField(db_column='COSMIC_FusionGenes_fusion_id', blank=True,
                                                       null=True)  # Field name made lowercase.
    cosmic_n_overlapping_mutations = models.IntegerField(db_column='COSMIC_n_overlapping_mutations', blank=True,
                                                         null=True)  # Field name made lowercase.
    cosmic_overlapping_mutation_descriptions = models.CharField(db_column='COSMIC_overlapping_mutation_descriptions',
                                                                max_length=26, blank=True,
                                                                null=True)  # Field name made lowercase.
    cosmic_overlapping_primary_sites = models.CharField(db_column='COSMIC_overlapping_primary_sites', max_length=66,
                                                        blank=True, null=True)  # Field name made lowercase.
    clinvar_assembly = models.CharField(db_column='ClinVar_ASSEMBLY', max_length=6, blank=True,
                                        null=True)  # Field name made lowercase.
    clinvar_hgmd_id = models.CharField(db_column='ClinVar_HGMD_ID', max_length=8, blank=True,
                                       null=True)  # Field name made lowercase.
    clinvar_sym = models.CharField(db_column='ClinVar_SYM', max_length=7, blank=True,
                                   null=True)  # Field name made lowercase.
    clinvar_type = models.CharField(db_column='ClinVar_TYPE', max_length=1, blank=True,
                                    null=True)  # Field name made lowercase.
    clinvar_rs = models.CharField(db_column='ClinVar_rs', max_length=11, blank=True,
                                  null=True)  # Field name made lowercase.
    ensembl_so_accession = models.CharField(db_column='Ensembl_so_accession', max_length=10, blank=True,
                                            null=True)  # Field name made lowercase.
    ensembl_so_term = models.CharField(db_column='Ensembl_so_term', max_length=23, blank=True,
                                       null=True)  # Field name made lowercase.
    exac_ac = models.IntegerField(db_column='ExAC_AC', blank=True, null=True)  # Field name made lowercase.
    exac_ac_afr = models.IntegerField(db_column='ExAC_AC_AFR', blank=True, null=True)  # Field name made lowercase.
    exac_ac_amr = models.IntegerField(db_column='ExAC_AC_AMR', blank=True, null=True)  # Field name made lowercase.
    exac_ac_adj = models.IntegerField(db_column='ExAC_AC_Adj', blank=True, null=True)  # Field name made lowercase.
    exac_ac_consanguineous = models.IntegerField(db_column='ExAC_AC_CONSANGUINEOUS', blank=True,
                                                 null=True)  # Field name made lowercase.
    exac_ac_eas = models.IntegerField(db_column='ExAC_AC_EAS', blank=True, null=True)  # Field name made lowercase.
    exac_ac_female = models.IntegerField(db_column='ExAC_AC_FEMALE', blank=True,
                                         null=True)  # Field name made lowercase.
    exac_ac_fin = models.IntegerField(db_column='ExAC_AC_FIN', blank=True, null=True)  # Field name made lowercase.
    exac_ac_hemi = models.IntegerField(db_column='ExAC_AC_Hemi', blank=True, null=True)  # Field name made lowercase.
    exac_ac_het = models.IntegerField(db_column='ExAC_AC_Het', blank=True, null=True)  # Field name made lowercase.
    exac_ac_hom = models.IntegerField(db_column='ExAC_AC_Hom', blank=True, null=True)  # Field name made lowercase.
    exac_ac_male = models.IntegerField(db_column='ExAC_AC_MALE', blank=True, null=True)  # Field name made lowercase.
    exac_ac_nfe = models.IntegerField(db_column='ExAC_AC_NFE', blank=True, null=True)  # Field name made lowercase.
    exac_ac_oth = models.IntegerField(db_column='ExAC_AC_OTH', blank=True, null=True)  # Field name made lowercase.
    exac_ac_popmax = models.IntegerField(db_column='ExAC_AC_POPMAX', blank=True,
                                         null=True)  # Field name made lowercase.
    exac_ac_sas = models.IntegerField(db_column='ExAC_AC_SAS', blank=True, null=True)  # Field name made lowercase.
    exac_af = models.TextField(db_column='ExAC_AF', blank=True,
                               null=True)  # Field name made lowercase. This field type is a guess.
    exac_an = models.IntegerField(db_column='ExAC_AN', blank=True, null=True)  # Field name made lowercase.
    exac_an_afr = models.IntegerField(db_column='ExAC_AN_AFR', blank=True, null=True)  # Field name made lowercase.
    exac_an_amr = models.IntegerField(db_column='ExAC_AN_AMR', blank=True, null=True)  # Field name made lowercase.
    exac_an_adj = models.IntegerField(db_column='ExAC_AN_Adj', blank=True, null=True)  # Field name made lowercase.
    exac_an_consanguineous = models.IntegerField(db_column='ExAC_AN_CONSANGUINEOUS', blank=True,
                                                 null=True)  # Field name made lowercase.
    exac_an_eas = models.IntegerField(db_column='ExAC_AN_EAS', blank=True, null=True)  # Field name made lowercase.
    exac_an_female = models.IntegerField(db_column='ExAC_AN_FEMALE', blank=True,
                                         null=True)  # Field name made lowercase.
    exac_an_fin = models.IntegerField(db_column='ExAC_AN_FIN', blank=True, null=True)  # Field name made lowercase.
    exac_an_male = models.IntegerField(db_column='ExAC_AN_MALE', blank=True, null=True)  # Field name made lowercase.
    exac_an_nfe = models.IntegerField(db_column='ExAC_AN_NFE', blank=True, null=True)  # Field name made lowercase.
    exac_an_oth = models.IntegerField(db_column='ExAC_AN_OTH', blank=True, null=True)  # Field name made lowercase.
    exac_an_popmax = models.IntegerField(db_column='ExAC_AN_POPMAX', blank=True,
                                         null=True)  # Field name made lowercase.
    exac_an_sas = models.IntegerField(db_column='ExAC_AN_SAS', blank=True, null=True)  # Field name made lowercase.
    exac_baseqranksum = models.TextField(db_column='ExAC_BaseQRankSum', blank=True,
                                         null=True)  # Field name made lowercase. This field type is a guess.
    exac_ccc = models.IntegerField(db_column='ExAC_CCC', blank=True, null=True)  # Field name made lowercase.
    exac_csq = models.TextField(db_column='ExAC_CSQ', blank=True, null=True)  # Field name made lowercase.
    exac_clippingranksum = models.TextField(db_column='ExAC_ClippingRankSum', blank=True,
                                            null=True)  # Field name made lowercase. This field type is a guess.
    exac_db = models.CharField(db_column='ExAC_DB', max_length=5, blank=True, null=True)  # Field name made lowercase.
    exac_doubleton_dist = models.TextField(db_column='ExAC_DOUBLETON_DIST', blank=True,
                                           null=True)  # Field name made lowercase. This field type is a guess.
    exac_dp = models.IntegerField(db_column='ExAC_DP', blank=True, null=True)  # Field name made lowercase.
    exac_dp_hist = models.CharField(db_column='ExAC_DP_HIST', max_length=206, blank=True,
                                    null=True)  # Field name made lowercase.
    exac_ds = models.CharField(db_column='ExAC_DS', max_length=5, blank=True, null=True)  # Field name made lowercase.
    exac_end = models.IntegerField(db_column='ExAC_END', blank=True, null=True)  # Field name made lowercase.
    exac_esp_ac = models.IntegerField(db_column='ExAC_ESP_AC', blank=True, null=True)  # Field name made lowercase.
    exac_esp_af_global = models.TextField(db_column='ExAC_ESP_AF_GLOBAL', blank=True,
                                          null=True)  # Field name made lowercase. This field type is a guess.
    exac_esp_af_popmax = models.TextField(db_column='ExAC_ESP_AF_POPMAX', blank=True,
                                          null=True)  # Field name made lowercase. This field type is a guess.
    exac_fs = models.TextField(db_column='ExAC_FS', blank=True,
                               null=True)  # Field name made lowercase. This field type is a guess.
    exac_gq_hist = models.CharField(db_column='ExAC_GQ_HIST', max_length=197, blank=True,
                                    null=True)  # Field name made lowercase.
    exac_gq_mean = models.TextField(db_column='ExAC_GQ_MEAN', blank=True,
                                    null=True)  # Field name made lowercase. This field type is a guess.
    exac_gq_stddev = models.TextField(db_column='ExAC_GQ_STDDEV', blank=True,
                                      null=True)  # Field name made lowercase. This field type is a guess.
    exac_hwp = models.IntegerField(db_column='ExAC_HWP', blank=True, null=True)  # Field name made lowercase.
    exac_haplotypescore = models.IntegerField(db_column='ExAC_HaplotypeScore', blank=True,
                                              null=True)  # Field name made lowercase.
    exac_hemi_afr = models.IntegerField(db_column='ExAC_Hemi_AFR', blank=True, null=True)  # Field name made lowercase.
    exac_hemi_amr = models.IntegerField(db_column='ExAC_Hemi_AMR', blank=True, null=True)  # Field name made lowercase.
    exac_hemi_eas = models.IntegerField(db_column='ExAC_Hemi_EAS', blank=True, null=True)  # Field name made lowercase.
    exac_hemi_fin = models.IntegerField(db_column='ExAC_Hemi_FIN', blank=True, null=True)  # Field name made lowercase.
    exac_hemi_nfe = models.IntegerField(db_column='ExAC_Hemi_NFE', blank=True, null=True)  # Field name made lowercase.
    exac_hemi_oth = models.IntegerField(db_column='ExAC_Hemi_OTH', blank=True, null=True)  # Field name made lowercase.
    exac_hemi_sas = models.IntegerField(db_column='ExAC_Hemi_SAS', blank=True, null=True)  # Field name made lowercase.
    exac_het_afr = models.IntegerField(db_column='ExAC_Het_AFR', blank=True, null=True)  # Field name made lowercase.
    exac_het_amr = models.IntegerField(db_column='ExAC_Het_AMR', blank=True, null=True)  # Field name made lowercase.
    exac_het_eas = models.IntegerField(db_column='ExAC_Het_EAS', blank=True, null=True)  # Field name made lowercase.
    exac_het_fin = models.IntegerField(db_column='ExAC_Het_FIN', blank=True, null=True)  # Field name made lowercase.
    exac_het_nfe = models.IntegerField(db_column='ExAC_Het_NFE', blank=True, null=True)  # Field name made lowercase.
    exac_het_oth = models.IntegerField(db_column='ExAC_Het_OTH', blank=True, null=True)  # Field name made lowercase.
    exac_het_sas = models.IntegerField(db_column='ExAC_Het_SAS', blank=True, null=True)  # Field name made lowercase.
    exac_hom_afr = models.IntegerField(db_column='ExAC_Hom_AFR', blank=True, null=True)  # Field name made lowercase.
    exac_hom_amr = models.IntegerField(db_column='ExAC_Hom_AMR', blank=True, null=True)  # Field name made lowercase.
    exac_hom_consanguineous = models.IntegerField(db_column='ExAC_Hom_CONSANGUINEOUS', blank=True,
                                                  null=True)  # Field name made lowercase.
    exac_hom_eas = models.IntegerField(db_column='ExAC_Hom_EAS', blank=True, null=True)  # Field name made lowercase.
    exac_hom_fin = models.IntegerField(db_column='ExAC_Hom_FIN', blank=True, null=True)  # Field name made lowercase.
    exac_hom_nfe = models.IntegerField(db_column='ExAC_Hom_NFE', blank=True, null=True)  # Field name made lowercase.
    exac_hom_oth = models.IntegerField(db_column='ExAC_Hom_OTH', blank=True, null=True)  # Field name made lowercase.
    exac_hom_sas = models.IntegerField(db_column='ExAC_Hom_SAS', blank=True, null=True)  # Field name made lowercase.
    exac_inbreedingcoeff = models.TextField(db_column='ExAC_InbreedingCoeff', blank=True,
                                            null=True)  # Field name made lowercase. This field type is a guess.
    exac_k1_run = models.CharField(db_column='ExAC_K1_RUN', max_length=3, blank=True,
                                   null=True)  # Field name made lowercase.
    exac_k2_run = models.CharField(db_column='ExAC_K2_RUN', max_length=4, blank=True,
                                   null=True)  # Field name made lowercase.
    exac_k3_run = models.CharField(db_column='ExAC_K3_RUN', max_length=5, blank=True,
                                   null=True)  # Field name made lowercase.
    exac_kg_ac = models.IntegerField(db_column='ExAC_KG_AC', blank=True, null=True)  # Field name made lowercase.
    exac_kg_af_global = models.TextField(db_column='ExAC_KG_AF_GLOBAL', blank=True,
                                         null=True)  # Field name made lowercase. This field type is a guess.
    exac_kg_af_popmax = models.TextField(db_column='ExAC_KG_AF_POPMAX', blank=True,
                                         null=True)  # Field name made lowercase. This field type is a guess.
    exac_mleac = models.IntegerField(db_column='ExAC_MLEAC', blank=True, null=True)  # Field name made lowercase.
    exac_mleaf = models.IntegerField(db_column='ExAC_MLEAF', blank=True, null=True)  # Field name made lowercase.
    exac_mq = models.TextField(db_column='ExAC_MQ', blank=True,
                               null=True)  # Field name made lowercase. This field type is a guess.
    exac_mq0 = models.IntegerField(db_column='ExAC_MQ0', blank=True, null=True)  # Field name made lowercase.
    exac_mqranksum = models.TextField(db_column='ExAC_MQRankSum', blank=True,
                                      null=True)  # Field name made lowercase. This field type is a guess.
    exac_ncc = models.IntegerField(db_column='ExAC_NCC', blank=True, null=True)  # Field name made lowercase.
    exac_negative_train_site = models.CharField(db_column='ExAC_NEGATIVE_TRAIN_SITE', max_length=5, blank=True,
                                                null=True)  # Field name made lowercase.
    exac_popmax = models.CharField(db_column='ExAC_POPMAX', max_length=3, blank=True,
                                   null=True)  # Field name made lowercase.
    exac_positive_train_site = models.CharField(db_column='ExAC_POSITIVE_TRAIN_SITE', max_length=5, blank=True,
                                                null=True)  # Field name made lowercase.
    exac_qd = models.TextField(db_column='ExAC_QD', blank=True,
                               null=True)  # Field name made lowercase. This field type is a guess.
    exac_readposranksum = models.TextField(db_column='ExAC_ReadPosRankSum', blank=True,
                                           null=True)  # Field name made lowercase. This field type is a guess.
    exac_vqslod = models.TextField(db_column='ExAC_VQSLOD', blank=True,
                                   null=True)  # Field name made lowercase. This field type is a guess.
    exac_clinvar_conflicted = models.IntegerField(db_column='ExAC_clinvar_conflicted', blank=True,
                                                  null=True)  # Field name made lowercase.
    exac_clinvar_measureset_id = models.IntegerField(db_column='ExAC_clinvar_measureset_id', blank=True,
                                                     null=True)  # Field name made lowercase.
    exac_clinvar_mut = models.IntegerField(db_column='ExAC_clinvar_mut', blank=True,
                                           null=True)  # Field name made lowercase.
    exac_clinvar_pathogenic = models.IntegerField(db_column='ExAC_clinvar_pathogenic', blank=True,
                                                  null=True)  # Field name made lowercase.
    exac_culprit = models.CharField(db_column='ExAC_culprit', max_length=15, blank=True,
                                    null=True)  # Field name made lowercase.
    familial_cancer_genes_reference = models.CharField(db_column='Familial_Cancer_Genes_Reference', max_length=24,
                                                       blank=True, null=True)  # Field name made lowercase.
    familial_cancer_genes_synonym = models.CharField(db_column='Familial_Cancer_Genes_Synonym', max_length=167,
                                                     blank=True, null=True)  # Field name made lowercase.
    hgnc_accession_numbers = models.CharField(db_column='HGNC_Accession_Numbers', max_length=38, blank=True,
                                              null=True)  # Field name made lowercase.
    hgnc_ccds_ids = models.CharField(db_column='HGNC_CCDS_IDs', max_length=166, blank=True,
                                     null=True)  # Field name made lowercase.
    hgnc_chromosome = models.CharField(db_column='HGNC_Chromosome', max_length=18, blank=True,
                                       null=True)  # Field name made lowercase.
    hgnc_date_modified = models.DateTimeField(db_column='HGNC_Date_Modified', blank=True,
                                              null=True)  # Field name made lowercase.
    hgnc_date_name_changed = models.DateTimeField(db_column='HGNC_Date_Name_Changed', blank=True,
                                                  null=True)  # Field name made lowercase.
    hgnc_date_symbol_changed = models.DateTimeField(db_column='HGNC_Date_Symbol_Changed', blank=True,
                                                    null=True)  # Field name made lowercase.
    hgnc_ensembl_gene_id = models.CharField(db_column='HGNC_Ensembl_Gene_ID', max_length=15, blank=True,
                                            null=True)  # Field name made lowercase.
    hgnc_ensembl_id_supplied_by_ensembl = models.CharField(db_column='HGNC_Ensembl_ID_supplied_by_Ensembl',
                                                           max_length=15, blank=True,
                                                           null=True)  # Field name made lowercase.
    hgnc_enzyme_ids = models.CharField(db_column='HGNC_Enzyme_IDs', max_length=18, blank=True,
                                       null=True)  # Field name made lowercase.
    hgnc_gene_family_description = models.CharField(db_column='HGNC_Gene_family_description', max_length=198,
                                                    blank=True, null=True)  # Field name made lowercase.
    hgnc_hgnc_id = models.IntegerField(db_column='HGNC_HGNC_ID', blank=True, null=True)  # Field name made lowercase.
    hgnc_locus_group = models.CharField(db_column='HGNC_Locus_Group', max_length=19, blank=True,
                                        null=True)  # Field name made lowercase.
    hgnc_locus_type = models.CharField(db_column='HGNC_Locus_Type', max_length=25, blank=True,
                                       null=True)  # Field name made lowercase.
    hgnc_name_synonyms = models.CharField(db_column='HGNC_Name_Synonyms', max_length=235, blank=True,
                                          null=True)  # Field name made lowercase.
    hgnc_omim_id_supplied_by_ncbi = models.CharField(db_column='HGNC_OMIM_ID_supplied_by_NCBI', max_length=14,
                                                     blank=True, null=True)  # Field name made lowercase.
    hgnc_previous_names = models.CharField(db_column='HGNC_Previous_Names', max_length=196, blank=True,
                                           null=True)  # Field name made lowercase.
    hgnc_previous_symbols = models.CharField(db_column='HGNC_Previous_Symbols', max_length=34, blank=True,
                                             null=True)  # Field name made lowercase.
    hgnc_primary_ids = models.IntegerField(db_column='HGNC_Primary_IDs', blank=True,
                                           null=True)  # Field name made lowercase.
    hgnc_pubmed_ids = models.CharField(db_column='HGNC_Pubmed_IDs', max_length=38, blank=True,
                                       null=True)  # Field name made lowercase.
    hgnc_record_type = models.CharField(db_column='HGNC_Record_Type', max_length=8, blank=True,
                                        null=True)  # Field name made lowercase.
    hgnc_refseq_supplied_by_ncbi = models.CharField(db_column='HGNC_RefSeq_supplied_by_NCBI', max_length=12, blank=True,
                                                    null=True)  # Field name made lowercase.
    hgnc_secondary_ids = models.IntegerField(db_column='HGNC_Secondary_IDs', blank=True,
                                             null=True)  # Field name made lowercase.
    hgnc_status = models.CharField(db_column='HGNC_Status', max_length=8, blank=True,
                                   null=True)  # Field name made lowercase.
    hgnc_synonyms = models.CharField(db_column='HGNC_Synonyms', max_length=97, blank=True,
                                     null=True)  # Field name made lowercase.
    hgnc_ucsc_id_supplied_by_ucsc = models.CharField(db_column='HGNC_UCSC_ID_supplied_by_UCSC', max_length=10,
                                                     blank=True, null=True)  # Field name made lowercase.
    hgnc_uniprot_id_supplied_by_uniprot = models.CharField(db_column='HGNC_UniProt_ID_supplied_by_UniProt',
                                                           max_length=6, blank=True,
                                                           null=True)  # Field name made lowercase.
    hgnc_vega_ids = models.CharField(db_column='HGNC_VEGA_IDs', max_length=18, blank=True,
                                     null=True)  # Field name made lowercase.
    hgvs_coding_dna_change = models.CharField(db_column='HGVS_coding_DNA_change', max_length=32, blank=True,
                                              null=True)  # Field name made lowercase.
    hgvs_genomic_change = models.CharField(db_column='HGVS_genomic_change', max_length=25, blank=True,
                                           null=True)  # Field name made lowercase.
    hgvs_protein_change = models.CharField(db_column='HGVS_protein_change', max_length=29, blank=True,
                                           null=True)  # Field name made lowercase.
    oreganno_bin = models.IntegerField(db_column='ORegAnno_bin', blank=True, null=True)  # Field name made lowercase.
    uniprot_alt_uniprot_accessions = models.CharField(db_column='UniProt_alt_uniprot_accessions', max_length=209,
                                                      blank=True, null=True)  # Field name made lowercase.
    annotation_transcript1 = models.CharField(max_length=17, blank=True, null=True)
    build = models.IntegerField(blank=True, null=True)
    ccds_id = models.CharField(max_length=11, blank=True, null=True)
    dbnsfp_1000gp1_ac = models.CharField(db_column='dbNSFP_1000Gp1_AC', max_length=3, blank=True,
                                         null=True)  # Field name made lowercase.
    dbnsfp_1000gp1_af = models.CharField(db_column='dbNSFP_1000Gp1_AF', max_length=11, blank=True,
                                         null=True)  # Field name made lowercase.
    dbnsfp_1000gp1_afr_ac = models.CharField(db_column='dbNSFP_1000Gp1_AFR_AC', max_length=3, blank=True,
                                             null=True)  # Field name made lowercase.
    dbnsfp_1000gp1_afr_af = models.CharField(db_column='dbNSFP_1000Gp1_AFR_AF', max_length=3, blank=True,
                                             null=True)  # Field name made lowercase.
    dbnsfp_1000gp1_amr_ac = models.CharField(db_column='dbNSFP_1000Gp1_AMR_AC', max_length=3, blank=True,
                                             null=True)  # Field name made lowercase.
    dbnsfp_1000gp1_amr_af = models.CharField(db_column='dbNSFP_1000Gp1_AMR_AF', max_length=3, blank=True,
                                             null=True)  # Field name made lowercase.
    dbnsfp_1000gp1_asn_ac = models.CharField(db_column='dbNSFP_1000Gp1_ASN_AC', max_length=3, blank=True,
                                             null=True)  # Field name made lowercase.
    dbnsfp_1000gp1_asn_af = models.CharField(db_column='dbNSFP_1000Gp1_ASN_AF', max_length=11, blank=True,
                                             null=True)  # Field name made lowercase.
    dbnsfp_1000gp1_eur_ac = models.CharField(db_column='dbNSFP_1000Gp1_EUR_AC', max_length=3, blank=True,
                                             null=True)  # Field name made lowercase.
    dbnsfp_1000gp1_eur_af = models.CharField(db_column='dbNSFP_1000Gp1_EUR_AF', max_length=3, blank=True,
                                             null=True)  # Field name made lowercase.
    dbnsfp_ancestral_allele = models.CharField(db_column='dbNSFP_Ancestral_allele', max_length=3, blank=True,
                                               null=True)  # Field name made lowercase.
    dbnsfp_cadd_phred = models.CharField(db_column='dbNSFP_CADD_phred', max_length=11, blank=True,
                                         null=True)  # Field name made lowercase.
    dbnsfp_cadd_raw = models.CharField(db_column='dbNSFP_CADD_raw', max_length=19, blank=True,
                                       null=True)  # Field name made lowercase.
    dbnsfp_cadd_raw_rankscore = models.CharField(db_column='dbNSFP_CADD_raw_rankscore', max_length=15, blank=True,
                                                 null=True)  # Field name made lowercase.
    dbnsfp_esp6500_aa_af = models.CharField(db_column='dbNSFP_ESP6500_AA_AF', max_length=8, blank=True,
                                            null=True)  # Field name made lowercase.
    dbnsfp_esp6500_ea_af = models.CharField(db_column='dbNSFP_ESP6500_EA_AF', max_length=8, blank=True,
                                            null=True)  # Field name made lowercase.
    dbnsfp_ensembl_geneid = models.CharField(db_column='dbNSFP_Ensembl_geneid', max_length=127, blank=True,
                                             null=True)  # Field name made lowercase.
    dbnsfp_ensembl_transcriptid = models.CharField(db_column='dbNSFP_Ensembl_transcriptid', max_length=271, blank=True,
                                                   null=True)  # Field name made lowercase.
    dbnsfp_fathmm_pred = models.CharField(db_column='dbNSFP_FATHMM_pred', max_length=31, blank=True,
                                          null=True)  # Field name made lowercase.
    dbnsfp_fathmm_rankscore = models.CharField(db_column='dbNSFP_FATHMM_rankscore', max_length=15, blank=True,
                                               null=True)  # Field name made lowercase.
    dbnsfp_fathmm_score = models.CharField(db_column='dbNSFP_FATHMM_score', max_length=78, blank=True,
                                           null=True)  # Field name made lowercase.
    dbnsfp_gerp_nr = models.CharField(db_column='dbNSFP_GERP_NR', max_length=11, blank=True,
                                      null=True)  # Field name made lowercase.
    dbnsfp_gerp_rs = models.CharField(db_column='dbNSFP_GERP_RS', max_length=13, blank=True,
                                      null=True)  # Field name made lowercase.
    dbnsfp_gerp_rs_rankscore = models.CharField(db_column='dbNSFP_GERP_RS_rankscore', max_length=15, blank=True,
                                                null=True)  # Field name made lowercase.
    dbnsfp_interpro_domain = models.CharField(db_column='dbNSFP_Interpro_domain', max_length=183, blank=True,
                                              null=True)  # Field name made lowercase.
    dbnsfp_lrt_omega = models.CharField(db_column='dbNSFP_LRT_Omega', max_length=17, blank=True,
                                        null=True)  # Field name made lowercase.
    dbnsfp_lrt_converted_rankscore = models.CharField(db_column='dbNSFP_LRT_converted_rankscore', max_length=15,
                                                      blank=True, null=True)  # Field name made lowercase.
    dbnsfp_lrt_pred = models.CharField(db_column='dbNSFP_LRT_pred', max_length=3, blank=True,
                                       null=True)  # Field name made lowercase.
    dbnsfp_lrt_score = models.CharField(db_column='dbNSFP_LRT_score', max_length=17, blank=True,
                                        null=True)  # Field name made lowercase.
    dbnsfp_lr_pred = models.CharField(db_column='dbNSFP_LR_pred', max_length=3, blank=True,
                                      null=True)  # Field name made lowercase.
    dbnsfp_lr_rankscore = models.CharField(db_column='dbNSFP_LR_rankscore', max_length=15, blank=True,
                                           null=True)  # Field name made lowercase.
    dbnsfp_lr_score = models.CharField(db_column='dbNSFP_LR_score', max_length=13, blank=True,
                                       null=True)  # Field name made lowercase.
    dbnsfp_mutationassessor_pred = models.CharField(db_column='dbNSFP_MutationAssessor_pred', max_length=3, blank=True,
                                                    null=True)  # Field name made lowercase.
    dbnsfp_mutationassessor_rankscore = models.CharField(db_column='dbNSFP_MutationAssessor_rankscore', max_length=15,
                                                         blank=True, null=True)  # Field name made lowercase.
    dbnsfp_mutationassessor_score = models.CharField(db_column='dbNSFP_MutationAssessor_score', max_length=13,
                                                     blank=True, null=True)  # Field name made lowercase.
    dbnsfp_mutationtaster_converted_rankscore = models.CharField(db_column='dbNSFP_MutationTaster_converted_rankscore',
                                                                 max_length=15, blank=True,
                                                                 null=True)  # Field name made lowercase.
    dbnsfp_mutationtaster_pred = models.CharField(db_column='dbNSFP_MutationTaster_pred', max_length=3, blank=True,
                                                  null=True)  # Field name made lowercase.
    dbnsfp_mutationtaster_score = models.CharField(db_column='dbNSFP_MutationTaster_score', max_length=17, blank=True,
                                                   null=True)  # Field name made lowercase.
    dbnsfp_polyphen2_hdiv_pred = models.CharField(db_column='dbNSFP_Polyphen2_HDIV_pred', max_length=27, blank=True,
                                                  null=True)  # Field name made lowercase.
    dbnsfp_polyphen2_hdiv_rankscore = models.CharField(db_column='dbNSFP_Polyphen2_HDIV_rankscore', max_length=9,
                                                       blank=True, null=True)  # Field name made lowercase.
    dbnsfp_polyphen2_hdiv_score = models.CharField(db_column='dbNSFP_Polyphen2_HDIV_score', max_length=83, blank=True,
                                                   null=True)  # Field name made lowercase.
    dbnsfp_polyphen2_hvar_pred = models.CharField(db_column='dbNSFP_Polyphen2_HVAR_pred', max_length=27, blank=True,
                                                  null=True)  # Field name made lowercase.
    dbnsfp_polyphen2_hvar_rankscore = models.CharField(db_column='dbNSFP_Polyphen2_HVAR_rankscore', max_length=9,
                                                       blank=True, null=True)  # Field name made lowercase.
    dbnsfp_polyphen2_hvar_score = models.CharField(db_column='dbNSFP_Polyphen2_HVAR_score', max_length=83, blank=True,
                                                   null=True)  # Field name made lowercase.
    dbnsfp_radialsvm_pred = models.CharField(db_column='dbNSFP_RadialSVM_pred', max_length=3, blank=True,
                                             null=True)  # Field name made lowercase.
    dbnsfp_radialsvm_rankscore = models.CharField(db_column='dbNSFP_RadialSVM_rankscore', max_length=15, blank=True,
                                                  null=True)  # Field name made lowercase.
    dbnsfp_radialsvm_score = models.CharField(db_column='dbNSFP_RadialSVM_score', max_length=15, blank=True,
                                              null=True)  # Field name made lowercase.
    dbnsfp_reliability_index = models.CharField(db_column='dbNSFP_Reliability_index', max_length=4, blank=True,
                                                null=True)  # Field name made lowercase.
    dbnsfp_sift_converted_rankscore = models.CharField(db_column='dbNSFP_SIFT_converted_rankscore', max_length=15,
                                                       blank=True, null=True)  # Field name made lowercase.
    dbnsfp_sift_pred = models.CharField(db_column='dbNSFP_SIFT_pred', max_length=3, blank=True,
                                        null=True)  # Field name made lowercase.
    dbnsfp_sift_score = models.CharField(db_column='dbNSFP_SIFT_score', max_length=9, blank=True,
                                         null=True)  # Field name made lowercase.
    dbnsfp_slr_test_statistic = models.CharField(db_column='dbNSFP_SLR_test_statistic', max_length=17, blank=True,
                                                 null=True)  # Field name made lowercase.
    dbnsfp_siphy_29way_logodds = models.CharField(db_column='dbNSFP_SiPhy_29way_logOdds', max_length=15, blank=True,
                                                  null=True)  # Field name made lowercase.
    dbnsfp_siphy_29way_logodds_rankscore = models.CharField(db_column='dbNSFP_SiPhy_29way_logOdds_rankscore',
                                                            max_length=15, blank=True,
                                                            null=True)  # Field name made lowercase.
    dbnsfp_siphy_29way_pi = models.CharField(db_column='dbNSFP_SiPhy_29way_pi', max_length=49, blank=True,
                                             null=True)  # Field name made lowercase.
    dbnsfp_unisnp_ids = models.CharField(db_column='dbNSFP_UniSNP_ids', max_length=3, blank=True,
                                         null=True)  # Field name made lowercase.
    dbnsfp_uniprot_aapos = models.CharField(db_column='dbNSFP_Uniprot_aapos', max_length=55, blank=True,
                                            null=True)  # Field name made lowercase.
    dbnsfp_uniprot_acc = models.CharField(db_column='dbNSFP_Uniprot_acc', max_length=116, blank=True,
                                          null=True)  # Field name made lowercase.
    dbnsfp_uniprot_id = models.CharField(db_column='dbNSFP_Uniprot_id', max_length=29, blank=True,
                                         null=True)  # Field name made lowercase.
    dbnsfp_aaalt = models.CharField(db_column='dbNSFP_aaalt', max_length=3, blank=True,
                                    null=True)  # Field name made lowercase.
    dbnsfp_aapos = models.CharField(db_column='dbNSFP_aapos', max_length=67, blank=True,
                                    null=True)  # Field name made lowercase.
    dbnsfp_aapos_fathmm = models.CharField(db_column='dbNSFP_aapos_FATHMM', max_length=351, blank=True,
                                           null=True)  # Field name made lowercase.
    dbnsfp_aapos_sift = models.CharField(db_column='dbNSFP_aapos_SIFT', max_length=44, blank=True,
                                         null=True)  # Field name made lowercase.
    dbnsfp_aaref = models.CharField(db_column='dbNSFP_aaref', max_length=3, blank=True,
                                    null=True)  # Field name made lowercase.
    dbnsfp_cds_strand = models.CharField(db_column='dbNSFP_cds_strand', max_length=3, blank=True,
                                         null=True)  # Field name made lowercase.
    dbnsfp_codonpos = models.CharField(db_column='dbNSFP_codonpos', max_length=3, blank=True,
                                       null=True)  # Field name made lowercase.
    dbnsfp_fold_degenerate = models.CharField(db_column='dbNSFP_fold_degenerate', max_length=3, blank=True,
                                              null=True)  # Field name made lowercase.
    dbnsfp_genename = models.CharField(db_column='dbNSFP_genename', max_length=22, blank=True,
                                       null=True)  # Field name made lowercase.
    dbnsfp_hg18_pos_1_coor = models.CharField(db_column='dbNSFP_hg18_pos_1_coor', max_length=19, blank=True,
                                              null=True)  # Field name made lowercase.
    dbnsfp_phastcons100way_vertebrate = models.CharField(db_column='dbNSFP_phastCons100way_vertebrate', max_length=17,
                                                         blank=True, null=True)  # Field name made lowercase.
    dbnsfp_phastcons100way_vertebrate_rankscore = models.CharField(
        db_column='dbNSFP_phastCons100way_vertebrate_rankscore', max_length=15, blank=True,
        null=True)  # Field name made lowercase.
    dbnsfp_phastcons46way_placental = models.CharField(db_column='dbNSFP_phastCons46way_placental', max_length=17,
                                                       blank=True, null=True)  # Field name made lowercase.
    dbnsfp_phastcons46way_placental_rankscore = models.CharField(db_column='dbNSFP_phastCons46way_placental_rankscore',
                                                                 max_length=15, blank=True,
                                                                 null=True)  # Field name made lowercase.
    dbnsfp_phastcons46way_primate = models.CharField(db_column='dbNSFP_phastCons46way_primate', max_length=17,
                                                     blank=True, null=True)  # Field name made lowercase.
    dbnsfp_phastcons46way_primate_rankscore = models.CharField(db_column='dbNSFP_phastCons46way_primate_rankscore',
                                                               max_length=15, blank=True,
                                                               null=True)  # Field name made lowercase.
    dbnsfp_phylop100way_vertebrate = models.CharField(db_column='dbNSFP_phyloP100way_vertebrate', max_length=19,
                                                      blank=True, null=True)  # Field name made lowercase.
    dbnsfp_phylop100way_vertebrate_rankscore = models.CharField(db_column='dbNSFP_phyloP100way_vertebrate_rankscore',
                                                                max_length=15, blank=True,
                                                                null=True)  # Field name made lowercase.
    dbnsfp_phylop46way_placental = models.CharField(db_column='dbNSFP_phyloP46way_placental', max_length=19, blank=True,
                                                    null=True)  # Field name made lowercase.
    dbnsfp_phylop46way_placental_rankscore = models.CharField(db_column='dbNSFP_phyloP46way_placental_rankscore',
                                                              max_length=15, blank=True,
                                                              null=True)  # Field name made lowercase.
    dbnsfp_phylop46way_primate = models.CharField(db_column='dbNSFP_phyloP46way_primate', max_length=19, blank=True,
                                                  null=True)  # Field name made lowercase.
    dbnsfp_phylop46way_primate_rankscore = models.CharField(db_column='dbNSFP_phyloP46way_primate_rankscore',
                                                            max_length=15, blank=True,
                                                            null=True)  # Field name made lowercase.
    dbnsfp_refcodon = models.CharField(db_column='dbNSFP_refcodon', max_length=7, blank=True,
                                       null=True)  # Field name made lowercase.
    entrez_gene_id_1 = models.IntegerField(blank=True, null=True)
    gencode_transcript_name = models.CharField(max_length=18, blank=True, null=True)
    gencode_transcript_status = models.CharField(max_length=8, blank=True, null=True)
    gencode_transcript_tags = models.CharField(max_length=85, blank=True, null=True)
    gencode_transcript_type = models.CharField(max_length=23, blank=True, null=True)
    gene_type = models.CharField(max_length=20, blank=True, null=True)
    havana_transcript = models.CharField(max_length=20, blank=True, null=True)
    init_t_lod = models.TextField(blank=True, null=True)  # This field type is a guess.
    judgement = models.CharField(max_length=4, blank=True, null=True)
    refseq_mrna_id_1 = models.CharField(max_length=20, blank=True, null=True)
    secondary_variant_classification = models.CharField(max_length=17, blank=True, null=True)
    t_alt_count = models.IntegerField(blank=True, null=True)
    t_lod_fstar = models.TextField(blank=True, null=True)  # This field type is a guess.
    t_ref_count = models.IntegerField(blank=True, null=True)
    tumor_f = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'oncotator_output'
