# Generated by Django 2.0.1 on 2018-03-01 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('genomic_profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OncotatorOutput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hugo_symbol', models.TextField(blank=True, null=True)),
                ('entrez_gene_id', models.TextField(blank=True, null=True)),
                ('center', models.TextField(blank=True, null=True)),
                ('ncbi_build', models.TextField(blank=True, null=True)),
                ('chromosome', models.TextField(blank=True, null=True)),
                ('start_position', models.TextField(blank=True, null=True)),
                ('end_position', models.TextField(blank=True, null=True)),
                ('strand', models.TextField(blank=True, null=True)),
                ('variant_classification', models.TextField(blank=True, null=True)),
                ('variant_type', models.TextField(blank=True, null=True)),
                ('reference_allele', models.TextField(blank=True, null=True)),
                ('tumor_seq_allele1', models.TextField(blank=True, null=True)),
                ('tumor_seq_allele2', models.TextField(blank=True, null=True)),
                ('dbsnp_rs', models.TextField(blank=True, null=True)),
                ('dbsnp_val_status', models.TextField(blank=True, null=True)),
                ('tumor_sample_barcode', models.TextField(blank=True, null=True)),
                ('matched_norm_sample_barcode', models.TextField(blank=True, null=True)),
                ('match_norm_seq_allele1', models.TextField(blank=True, null=True)),
                ('match_norm_seq_allele2', models.TextField(blank=True, null=True)),
                ('tumor_validation_allele1', models.TextField(blank=True, null=True)),
                ('tumor_validation_allele2', models.TextField(blank=True, null=True)),
                ('match_norm_validation_allele1', models.TextField(blank=True, null=True)),
                ('match_norm_validation_allele2', models.TextField(blank=True, null=True)),
                ('verification_status', models.TextField(blank=True, null=True)),
                ('validation_status', models.TextField(blank=True, null=True)),
                ('mutation_status', models.TextField(blank=True, null=True)),
                ('sequencing_phase', models.TextField(blank=True, null=True)),
                ('sequence_source', models.TextField(blank=True, null=True)),
                ('validation_method', models.TextField(blank=True, null=True)),
                ('score', models.TextField(blank=True, null=True)),
                ('bam_file', models.TextField(blank=True, null=True)),
                ('sequencer', models.TextField(blank=True, null=True)),
                ('tumor_sample_uuid', models.TextField(blank=True, null=True)),
                ('matched_norm_sample_uuid', models.TextField(blank=True, null=True)),
                ('genome_change', models.TextField(blank=True, null=True)),
                ('annotation_transcript', models.TextField(blank=True, null=True)),
                ('transcript_strand', models.TextField(blank=True, null=True)),
                ('transcript_exon', models.TextField(blank=True, null=True)),
                ('transcript_position', models.TextField(blank=True, null=True)),
                ('cdna_change', models.TextField(blank=True, null=True)),
                ('codon_change', models.TextField(blank=True, null=True)),
                ('protein_change', models.TextField(blank=True, null=True)),
                ('other_transcripts', models.TextField(blank=True, null=True)),
                ('refseq_mrna_id', models.TextField(blank=True, null=True)),
                ('refseq_prot_id', models.TextField(blank=True, null=True)),
                ('swissprot_acc_id', models.TextField(blank=True, null=True)),
                ('swissprot_entry_id', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('uniprot_aapos', models.TextField(blank=True, null=True)),
                ('uniprot_region', models.TextField(blank=True, null=True)),
                ('uniprot_site', models.TextField(blank=True, null=True)),
                ('uniprot_natural_variations', models.TextField(blank=True, null=True)),
                ('uniprot_experimental_info', models.TextField(blank=True, null=True)),
                ('go_biological_process', models.TextField(blank=True, null=True)),
                ('go_cellular_component', models.TextField(blank=True, null=True)),
                ('go_molecular_function', models.TextField(blank=True, null=True)),
                ('cosmic_overlapping_mutations', models.TextField(blank=True, null=True)),
                ('cosmic_fusion_genes', models.TextField(blank=True, null=True)),
                ('cosmic_tissue_types_affected', models.TextField(blank=True, null=True)),
                ('cosmic_total_alterations_in_gene', models.TextField(blank=True, null=True)),
                ('tumorscape_amplification_peaks', models.TextField(blank=True, null=True)),
                ('tumorscape_deletion_peaks', models.TextField(blank=True, null=True)),
                ('tcgascape_amplification_peaks', models.TextField(blank=True, null=True)),
                ('tcgascape_deletion_peaks', models.TextField(blank=True, null=True)),
                ('drugbank', models.TextField(blank=True, null=True)),
                ('ref_context', models.TextField(blank=True, null=True)),
                ('gc_content', models.TextField(blank=True, null=True)),
                ('ccle_oncomap_overlapping_mutations', models.TextField(blank=True, null=True)),
                ('ccle_oncomap_total_mutations_in_gene', models.TextField(blank=True, null=True)),
                ('cgc_mutation_type', models.TextField(blank=True, null=True)),
                ('cgc_translocation_partner', models.TextField(blank=True, null=True)),
                ('cgc_tumor_types_somatic', models.TextField(blank=True, null=True)),
                ('cgc_tumor_types_germline', models.TextField(blank=True, null=True)),
                ('cgc_other_diseases', models.TextField(blank=True, null=True)),
                ('dnarepairgenes_role', models.TextField(blank=True, null=True)),
                ('familialcancerdatabase_syndromes', models.TextField(blank=True, null=True)),
                ('mutsig_published_results', models.TextField(blank=True, null=True)),
                ('oreganno_id', models.TextField(blank=True, null=True)),
                ('oreganno_values', models.TextField(blank=True, null=True)),
                ('number_1000gp3_aa', models.TextField(blank=True, db_column='1000gp3_aa', null=True)),
                ('number_1000gp3_ac', models.TextField(blank=True, db_column='1000gp3_ac', null=True)),
                ('number_1000gp3_af', models.TextField(blank=True, db_column='1000gp3_af', null=True)),
                ('number_1000gp3_afr_af', models.TextField(blank=True, db_column='1000gp3_afr_af', null=True)),
                ('number_1000gp3_amr_af', models.TextField(blank=True, db_column='1000gp3_amr_af', null=True)),
                ('number_1000gp3_an', models.TextField(blank=True, db_column='1000gp3_an', null=True)),
                ('number_1000gp3_ciend', models.TextField(blank=True, db_column='1000gp3_ciend', null=True)),
                ('number_1000gp3_cipos', models.TextField(blank=True, db_column='1000gp3_cipos', null=True)),
                ('number_1000gp3_cs', models.TextField(blank=True, db_column='1000gp3_cs', null=True)),
                ('number_1000gp3_dp', models.TextField(blank=True, db_column='1000gp3_dp', null=True)),
                ('number_1000gp3_eas_af', models.TextField(blank=True, db_column='1000gp3_eas_af', null=True)),
                ('number_1000gp3_end', models.TextField(blank=True, db_column='1000gp3_end', null=True)),
                ('number_1000gp3_eur_af', models.TextField(blank=True, db_column='1000gp3_eur_af', null=True)),
                ('number_1000gp3_imprecise', models.TextField(blank=True, db_column='1000gp3_imprecise', null=True)),
                ('number_1000gp3_mc', models.TextField(blank=True, db_column='1000gp3_mc', null=True)),
                ('number_1000gp3_meinfo', models.TextField(blank=True, db_column='1000gp3_meinfo', null=True)),
                ('number_1000gp3_mend', models.TextField(blank=True, db_column='1000gp3_mend', null=True)),
                ('number_1000gp3_mlen', models.TextField(blank=True, db_column='1000gp3_mlen', null=True)),
                ('number_1000gp3_mstart', models.TextField(blank=True, db_column='1000gp3_mstart', null=True)),
                ('number_1000gp3_ns', models.TextField(blank=True, db_column='1000gp3_ns', null=True)),
                ('number_1000gp3_sas_af', models.TextField(blank=True, db_column='1000gp3_sas_af', null=True)),
                ('number_1000gp3_svlen', models.TextField(blank=True, db_column='1000gp3_svlen', null=True)),
                ('number_1000gp3_svtype', models.TextField(blank=True, db_column='1000gp3_svtype', null=True)),
                ('number_1000gp3_tsd', models.TextField(blank=True, db_column='1000gp3_tsd', null=True)),
                ('achilles_lineage_results_top_genes', models.TextField(blank=True, null=True)),
                ('cgc_cancer_germline_mut', models.TextField(blank=True, db_column='cgc_cancer germline mut', null=True)),
                ('cgc_cancer_molecular_genetics', models.TextField(blank=True, db_column='cgc_cancer molecular genetics', null=True)),
                ('cgc_cancer_somatic_mut', models.TextField(blank=True, db_column='cgc_cancer somatic mut', null=True)),
                ('cgc_cancer_syndrome', models.TextField(blank=True, db_column='cgc_cancer syndrome', null=True)),
                ('cgc_chr', models.TextField(blank=True, null=True)),
                ('cgc_chr_band', models.TextField(blank=True, db_column='cgc_chr band', null=True)),
                ('cgc_geneid', models.TextField(blank=True, null=True)),
                ('cgc_name', models.TextField(blank=True, null=True)),
                ('cgc_other_germline_mut', models.TextField(blank=True, db_column='cgc_other germline mut', null=True)),
                ('cgc_tissue_type', models.TextField(blank=True, db_column='cgc_tissue type', null=True)),
                ('cosmic_fusiongenes_fusion_id', models.TextField(blank=True, null=True)),
                ('cosmic_n_overlapping_mutations', models.TextField(blank=True, null=True)),
                ('cosmic_overlapping_mutation_descriptions', models.TextField(blank=True, null=True)),
                ('cosmic_overlapping_primary_sites', models.TextField(blank=True, null=True)),
                ('clinvar_assembly', models.TextField(blank=True, null=True)),
                ('clinvar_hgmd_id', models.TextField(blank=True, null=True)),
                ('clinvar_sym', models.TextField(blank=True, null=True)),
                ('clinvar_type', models.TextField(blank=True, null=True)),
                ('clinvar_rs', models.TextField(blank=True, null=True)),
                ('ensembl_so_accession', models.TextField(blank=True, null=True)),
                ('ensembl_so_term', models.TextField(blank=True, null=True)),
                ('exac_ac', models.TextField(blank=True, null=True)),
                ('exac_ac_afr', models.TextField(blank=True, null=True)),
                ('exac_ac_amr', models.TextField(blank=True, null=True)),
                ('exac_ac_adj', models.TextField(blank=True, null=True)),
                ('exac_ac_consanguineous', models.TextField(blank=True, null=True)),
                ('exac_ac_eas', models.TextField(blank=True, null=True)),
                ('exac_ac_female', models.TextField(blank=True, null=True)),
                ('exac_ac_fin', models.TextField(blank=True, null=True)),
                ('exac_ac_hemi', models.TextField(blank=True, null=True)),
                ('exac_ac_het', models.TextField(blank=True, null=True)),
                ('exac_ac_hom', models.TextField(blank=True, null=True)),
                ('exac_ac_male', models.TextField(blank=True, null=True)),
                ('exac_ac_nfe', models.TextField(blank=True, null=True)),
                ('exac_ac_oth', models.TextField(blank=True, null=True)),
                ('exac_ac_popmax', models.TextField(blank=True, null=True)),
                ('exac_ac_sas', models.TextField(blank=True, null=True)),
                ('exac_af', models.TextField(blank=True, null=True)),
                ('exac_an', models.TextField(blank=True, null=True)),
                ('exac_an_afr', models.TextField(blank=True, null=True)),
                ('exac_an_amr', models.TextField(blank=True, null=True)),
                ('exac_an_adj', models.TextField(blank=True, null=True)),
                ('exac_an_consanguineous', models.TextField(blank=True, null=True)),
                ('exac_an_eas', models.TextField(blank=True, null=True)),
                ('exac_an_female', models.TextField(blank=True, null=True)),
                ('exac_an_fin', models.TextField(blank=True, null=True)),
                ('exac_an_male', models.TextField(blank=True, null=True)),
                ('exac_an_nfe', models.TextField(blank=True, null=True)),
                ('exac_an_oth', models.TextField(blank=True, null=True)),
                ('exac_an_popmax', models.TextField(blank=True, null=True)),
                ('exac_an_sas', models.TextField(blank=True, null=True)),
                ('exac_baseqranksum', models.TextField(blank=True, null=True)),
                ('exac_ccc', models.TextField(blank=True, null=True)),
                ('exac_csq', models.TextField(blank=True, null=True)),
                ('exac_clippingranksum', models.TextField(blank=True, null=True)),
                ('exac_db', models.TextField(blank=True, null=True)),
                ('exac_doubleton_dist', models.TextField(blank=True, null=True)),
                ('exac_dp', models.TextField(blank=True, null=True)),
                ('exac_dp_hist', models.TextField(blank=True, null=True)),
                ('exac_ds', models.TextField(blank=True, null=True)),
                ('exac_end', models.TextField(blank=True, null=True)),
                ('exac_esp_ac', models.TextField(blank=True, null=True)),
                ('exac_esp_af_global', models.TextField(blank=True, null=True)),
                ('exac_esp_af_popmax', models.TextField(blank=True, null=True)),
                ('exac_fs', models.TextField(blank=True, null=True)),
                ('exac_gq_hist', models.TextField(blank=True, null=True)),
                ('exac_gq_mean', models.TextField(blank=True, null=True)),
                ('exac_gq_stddev', models.TextField(blank=True, null=True)),
                ('exac_hwp', models.TextField(blank=True, null=True)),
                ('exac_haplotypescore', models.TextField(blank=True, null=True)),
                ('exac_hemi_afr', models.TextField(blank=True, null=True)),
                ('exac_hemi_amr', models.TextField(blank=True, null=True)),
                ('exac_hemi_eas', models.TextField(blank=True, null=True)),
                ('exac_hemi_fin', models.TextField(blank=True, null=True)),
                ('exac_hemi_nfe', models.TextField(blank=True, null=True)),
                ('exac_hemi_oth', models.TextField(blank=True, null=True)),
                ('exac_hemi_sas', models.TextField(blank=True, null=True)),
                ('exac_het_afr', models.TextField(blank=True, null=True)),
                ('exac_het_amr', models.TextField(blank=True, null=True)),
                ('exac_het_eas', models.TextField(blank=True, null=True)),
                ('exac_het_fin', models.TextField(blank=True, null=True)),
                ('exac_het_nfe', models.TextField(blank=True, null=True)),
                ('exac_het_oth', models.TextField(blank=True, null=True)),
                ('exac_het_sas', models.TextField(blank=True, null=True)),
                ('exac_hom_afr', models.TextField(blank=True, null=True)),
                ('exac_hom_amr', models.TextField(blank=True, null=True)),
                ('exac_hom_consanguineous', models.TextField(blank=True, null=True)),
                ('exac_hom_eas', models.TextField(blank=True, null=True)),
                ('exac_hom_fin', models.TextField(blank=True, null=True)),
                ('exac_hom_nfe', models.TextField(blank=True, null=True)),
                ('exac_hom_oth', models.TextField(blank=True, null=True)),
                ('exac_hom_sas', models.TextField(blank=True, null=True)),
                ('exac_inbreedingcoeff', models.TextField(blank=True, null=True)),
                ('exac_k1_run', models.TextField(blank=True, null=True)),
                ('exac_k2_run', models.TextField(blank=True, null=True)),
                ('exac_k3_run', models.TextField(blank=True, null=True)),
                ('exac_kg_ac', models.TextField(blank=True, null=True)),
                ('exac_kg_af_global', models.TextField(blank=True, null=True)),
                ('exac_kg_af_popmax', models.TextField(blank=True, null=True)),
                ('exac_mleac', models.TextField(blank=True, null=True)),
                ('exac_mleaf', models.TextField(blank=True, null=True)),
                ('exac_mq', models.TextField(blank=True, null=True)),
                ('exac_mq0', models.TextField(blank=True, null=True)),
                ('exac_mqranksum', models.TextField(blank=True, null=True)),
                ('exac_ncc', models.TextField(blank=True, null=True)),
                ('exac_negative_train_site', models.TextField(blank=True, null=True)),
                ('exac_popmax', models.TextField(blank=True, null=True)),
                ('exac_positive_train_site', models.TextField(blank=True, null=True)),
                ('exac_qd', models.TextField(blank=True, null=True)),
                ('exac_readposranksum', models.TextField(blank=True, null=True)),
                ('exac_vqslod', models.TextField(blank=True, null=True)),
                ('exac_clinvar_conflicted', models.TextField(blank=True, null=True)),
                ('exac_clinvar_measureset_id', models.TextField(blank=True, null=True)),
                ('exac_clinvar_mut', models.TextField(blank=True, null=True)),
                ('exac_clinvar_pathogenic', models.TextField(blank=True, null=True)),
                ('exac_culprit', models.TextField(blank=True, null=True)),
                ('familial_cancer_genes_reference', models.TextField(blank=True, null=True)),
                ('familial_cancer_genes_synonym', models.TextField(blank=True, null=True)),
                ('hgnc_accession_numbers', models.TextField(blank=True, db_column='hgnc_accession numbers', null=True)),
                ('hgnc_ccds_ids', models.TextField(blank=True, db_column='hgnc_ccds ids', null=True)),
                ('hgnc_chromosome', models.TextField(blank=True, null=True)),
                ('hgnc_date_modified', models.TextField(blank=True, db_column='hgnc_date modified', null=True)),
                ('hgnc_date_name_changed', models.TextField(blank=True, db_column='hgnc_date name changed', null=True)),
                ('hgnc_date_symbol_changed', models.TextField(blank=True, db_column='hgnc_date symbol changed', null=True)),
                ('hgnc_ensembl_gene_id', models.TextField(blank=True, db_column='hgnc_ensembl gene id', null=True)),
                ('hgnc_ensembl_id_supplied_by_ensembl_field', models.TextField(blank=True, db_column='hgnc_ensembl id(supplied by ensembl)', null=True)),
                ('hgnc_enzyme_ids', models.TextField(blank=True, db_column='hgnc_enzyme ids', null=True)),
                ('hgnc_gene_family_description', models.TextField(blank=True, db_column='hgnc_gene family description', null=True)),
                ('hgnc_hgnc_id', models.TextField(blank=True, db_column='hgnc_hgnc id', null=True)),
                ('hgnc_locus_group', models.TextField(blank=True, db_column='hgnc_locus group', null=True)),
                ('hgnc_locus_type', models.TextField(blank=True, db_column='hgnc_locus type', null=True)),
                ('hgnc_name_synonyms', models.TextField(blank=True, db_column='hgnc_name synonyms', null=True)),
                ('hgnc_omim_id_supplied_by_ncbi_field', models.TextField(blank=True, db_column='hgnc_omim id(supplied by ncbi)', null=True)),
                ('hgnc_previous_names', models.TextField(blank=True, db_column='hgnc_previous names', null=True)),
                ('hgnc_previous_symbols', models.TextField(blank=True, db_column='hgnc_previous symbols', null=True)),
                ('hgnc_primary_ids', models.TextField(blank=True, db_column='hgnc_primary ids', null=True)),
                ('hgnc_pubmed_ids', models.TextField(blank=True, db_column='hgnc_pubmed ids', null=True)),
                ('hgnc_record_type', models.TextField(blank=True, db_column='hgnc_record type', null=True)),
                ('hgnc_refseq_supplied_by_ncbi_field', models.TextField(blank=True, db_column='hgnc_refseq(supplied by ncbi)', null=True)),
                ('hgnc_secondary_ids', models.TextField(blank=True, db_column='hgnc_secondary ids', null=True)),
                ('hgnc_status', models.TextField(blank=True, null=True)),
                ('hgnc_synonyms', models.TextField(blank=True, null=True)),
                ('hgnc_ucsc_id_supplied_by_ucsc_field', models.TextField(blank=True, db_column='hgnc_ucsc id(supplied by ucsc)', null=True)),
                ('hgnc_uniprot_id_supplied_by_uniprot_field', models.TextField(blank=True, db_column='hgnc_uniprot id(supplied by uniprot)', null=True)),
                ('hgnc_vega_ids', models.TextField(blank=True, db_column='hgnc_vega ids', null=True)),
                ('hgvs_coding_dna_change', models.TextField(blank=True, null=True)),
                ('hgvs_genomic_change', models.TextField(blank=True, null=True)),
                ('hgvs_protein_change', models.TextField(blank=True, null=True)),
                ('oreganno_bin', models.TextField(blank=True, null=True)),
                ('uniprot_alt_uniprot_accessions', models.TextField(blank=True, null=True)),
                ('annotation_transcript2', models.TextField(blank=True, null=True)),
                ('build', models.TextField(blank=True, null=True)),
                ('ccds_id', models.TextField(blank=True, null=True)),
                ('dbnsfp_1000gp1_ac', models.TextField(blank=True, null=True)),
                ('dbnsfp_1000gp1_af', models.TextField(blank=True, null=True)),
                ('dbnsfp_1000gp1_afr_ac', models.TextField(blank=True, null=True)),
                ('dbnsfp_1000gp1_afr_af', models.TextField(blank=True, null=True)),
                ('dbnsfp_1000gp1_amr_ac', models.TextField(blank=True, null=True)),
                ('dbnsfp_1000gp1_amr_af', models.TextField(blank=True, null=True)),
                ('dbnsfp_1000gp1_asn_ac', models.TextField(blank=True, null=True)),
                ('dbnsfp_1000gp1_asn_af', models.TextField(blank=True, null=True)),
                ('dbnsfp_1000gp1_eur_ac', models.TextField(blank=True, null=True)),
                ('dbnsfp_1000gp1_eur_af', models.TextField(blank=True, null=True)),
                ('dbnsfp_ancestral_allele', models.TextField(blank=True, null=True)),
                ('dbnsfp_cadd_phred', models.TextField(blank=True, null=True)),
                ('dbnsfp_cadd_raw', models.TextField(blank=True, null=True)),
                ('dbnsfp_cadd_raw_rankscore', models.TextField(blank=True, null=True)),
                ('dbnsfp_esp6500_aa_af', models.TextField(blank=True, null=True)),
                ('dbnsfp_esp6500_ea_af', models.TextField(blank=True, null=True)),
                ('dbnsfp_ensembl_geneid', models.TextField(blank=True, null=True)),
                ('dbnsfp_ensembl_transcriptid', models.TextField(blank=True, null=True)),
                ('dbnsfp_fathmm_pred', models.TextField(blank=True, null=True)),
                ('dbnsfp_fathmm_rankscore', models.TextField(blank=True, null=True)),
                ('dbnsfp_fathmm_score', models.TextField(blank=True, null=True)),
                ('dbnsfp_gerp_nr', models.TextField(blank=True, db_column='dbnsfp_gerp++_nr', null=True)),
                ('dbnsfp_gerp_rs', models.TextField(blank=True, db_column='dbnsfp_gerp++_rs', null=True)),
                ('dbnsfp_gerp_rs_rankscore', models.TextField(blank=True, db_column='dbnsfp_gerp++_rs_rankscore', null=True)),
                ('dbnsfp_interpro_domain', models.TextField(blank=True, null=True)),
                ('dbnsfp_lrt_omega', models.TextField(blank=True, null=True)),
                ('dbnsfp_lrt_converted_rankscore', models.TextField(blank=True, null=True)),
                ('dbnsfp_lrt_pred', models.TextField(blank=True, null=True)),
                ('dbnsfp_lrt_score', models.TextField(blank=True, null=True)),
                ('dbnsfp_lr_pred', models.TextField(blank=True, null=True)),
                ('dbnsfp_lr_rankscore', models.TextField(blank=True, null=True)),
                ('dbnsfp_lr_score', models.TextField(blank=True, null=True)),
                ('dbnsfp_mutationassessor_pred', models.TextField(blank=True, null=True)),
                ('dbnsfp_mutationassessor_rankscore', models.TextField(blank=True, null=True)),
                ('dbnsfp_mutationassessor_score', models.TextField(blank=True, null=True)),
                ('dbnsfp_mutationtaster_converted_rankscore', models.TextField(blank=True, null=True)),
                ('dbnsfp_mutationtaster_pred', models.TextField(blank=True, null=True)),
                ('dbnsfp_mutationtaster_score', models.TextField(blank=True, null=True)),
                ('dbnsfp_polyphen2_hdiv_pred', models.TextField(blank=True, null=True)),
                ('dbnsfp_polyphen2_hdiv_rankscore', models.TextField(blank=True, null=True)),
                ('dbnsfp_polyphen2_hdiv_score', models.TextField(blank=True, null=True)),
                ('dbnsfp_polyphen2_hvar_pred', models.TextField(blank=True, null=True)),
                ('dbnsfp_polyphen2_hvar_rankscore', models.TextField(blank=True, null=True)),
                ('dbnsfp_polyphen2_hvar_score', models.TextField(blank=True, null=True)),
                ('dbnsfp_radialsvm_pred', models.TextField(blank=True, null=True)),
                ('dbnsfp_radialsvm_rankscore', models.TextField(blank=True, null=True)),
                ('dbnsfp_radialsvm_score', models.TextField(blank=True, null=True)),
                ('dbnsfp_reliability_index', models.TextField(blank=True, null=True)),
                ('dbnsfp_sift_converted_rankscore', models.TextField(blank=True, null=True)),
                ('dbnsfp_sift_pred', models.TextField(blank=True, null=True)),
                ('dbnsfp_sift_score', models.TextField(blank=True, null=True)),
                ('dbnsfp_slr_test_statistic', models.TextField(blank=True, null=True)),
                ('dbnsfp_siphy_29way_logodds', models.TextField(blank=True, null=True)),
                ('dbnsfp_siphy_29way_logodds_rankscore', models.TextField(blank=True, null=True)),
                ('dbnsfp_siphy_29way_pi', models.TextField(blank=True, null=True)),
                ('dbnsfp_unisnp_ids', models.TextField(blank=True, null=True)),
                ('dbnsfp_uniprot_aapos', models.TextField(blank=True, null=True)),
                ('dbnsfp_uniprot_acc', models.TextField(blank=True, null=True)),
                ('dbnsfp_uniprot_id', models.TextField(blank=True, null=True)),
                ('dbnsfp_aaalt', models.TextField(blank=True, null=True)),
                ('dbnsfp_aapos', models.TextField(blank=True, null=True)),
                ('dbnsfp_aapos_fathmm', models.TextField(blank=True, null=True)),
                ('dbnsfp_aapos_sift', models.TextField(blank=True, null=True)),
                ('dbnsfp_aaref', models.TextField(blank=True, null=True)),
                ('dbnsfp_cds_strand', models.TextField(blank=True, null=True)),
                ('dbnsfp_codonpos', models.TextField(blank=True, null=True)),
                ('dbnsfp_fold_degenerate', models.TextField(blank=True, null=True)),
                ('dbnsfp_genename', models.TextField(blank=True, null=True)),
                ('dbnsfp_hg18_pos_1_coor_field', models.TextField(blank=True, db_column='dbnsfp_hg18_pos(1_coor)', null=True)),
                ('dbnsfp_phastcons100way_vertebrate', models.TextField(blank=True, null=True)),
                ('dbnsfp_phastcons100way_vertebrate_rankscore', models.TextField(blank=True, null=True)),
                ('dbnsfp_phastcons46way_placental', models.TextField(blank=True, null=True)),
                ('dbnsfp_phastcons46way_placental_rankscore', models.TextField(blank=True, null=True)),
                ('dbnsfp_phastcons46way_primate', models.TextField(blank=True, null=True)),
                ('dbnsfp_phastcons46way_primate_rankscore', models.TextField(blank=True, null=True)),
                ('dbnsfp_phylop100way_vertebrate', models.TextField(blank=True, null=True)),
                ('dbnsfp_phylop100way_vertebrate_rankscore', models.TextField(blank=True, null=True)),
                ('dbnsfp_phylop46way_placental', models.TextField(blank=True, null=True)),
                ('dbnsfp_phylop46way_placental_rankscore', models.TextField(blank=True, null=True)),
                ('dbnsfp_phylop46way_primate', models.TextField(blank=True, null=True)),
                ('dbnsfp_phylop46way_primate_rankscore', models.TextField(blank=True, null=True)),
                ('dbnsfp_refcodon', models.TextField(blank=True, null=True)),
                ('entrez_gene_id2', models.TextField(blank=True, null=True)),
                ('gencode_transcript_name', models.TextField(blank=True, null=True)),
                ('gencode_transcript_status', models.TextField(blank=True, null=True)),
                ('gencode_transcript_tags', models.TextField(blank=True, null=True)),
                ('gencode_transcript_type', models.TextField(blank=True, null=True)),
                ('gene_type', models.TextField(blank=True, null=True)),
                ('havana_transcript', models.TextField(blank=True, null=True)),
                ('init_t_lod', models.TextField(blank=True, null=True)),
                ('judgement', models.TextField(blank=True, null=True)),
                ('refseq_mrna_id2', models.TextField(blank=True, null=True)),
                ('secondary_variant_classification', models.TextField(blank=True, null=True)),
                ('t_alt_count', models.TextField(blank=True, null=True)),
                ('t_lod_fstar', models.TextField(blank=True, null=True)),
                ('t_ref_count', models.TextField(blank=True, null=True)),
                ('tumor_f', models.TextField(blank=True, null=True)),
                ('genomicprofile', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='genomic_profiles.GenomicProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Pathogenicity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PVS1', models.TextField(blank=True, null=True)),
                ('PM1', models.TextField(blank=True, null=True)),
                ('PM2', models.TextField(blank=True, null=True)),
                ('PM3', models.TextField(blank=True, null=True)),
                ('PM4', models.TextField(blank=True, null=True)),
                ('PM5', models.TextField(blank=True, null=True)),
                ('PM6', models.TextField(blank=True, null=True)),
                ('PS1', models.TextField(blank=True, null=True)),
                ('PS2', models.TextField(blank=True, null=True)),
                ('PS3', models.TextField(blank=True, null=True)),
                ('PS4', models.TextField(blank=True, null=True)),
                ('PP1', models.TextField(blank=True, null=True)),
                ('PP2', models.TextField(blank=True, null=True)),
                ('PP3', models.TextField(blank=True, null=True)),
                ('PP4', models.TextField(blank=True, null=True)),
                ('PP5', models.TextField(blank=True, null=True)),
                ('BP1', models.TextField(blank=True, null=True)),
                ('BP2', models.TextField(blank=True, null=True)),
                ('BP3', models.TextField(blank=True, null=True)),
                ('BP4', models.TextField(blank=True, null=True)),
                ('BP5', models.TextField(blank=True, null=True)),
                ('BP6', models.TextField(blank=True, null=True)),
                ('BP7', models.TextField(blank=True, null=True)),
                ('BS1', models.TextField(blank=True, null=True)),
                ('BS2', models.TextField(blank=True, null=True)),
                ('BS3', models.TextField(blank=True, null=True)),
                ('BS4', models.TextField(blank=True, null=True)),
                ('BA1', models.TextField(blank=True, null=True)),
                ('Pathogenicity', models.TextField(blank=True, null=True)),
                ('Pathogenicity_Rule', models.TextField(blank=True, null=True)),
                ('Google_Scholar', models.TextField(blank=True, null=True)),
                ('oncotatoroutput', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='pathogenicity.OncotatorOutput')),
            ],
        ),
    ]
