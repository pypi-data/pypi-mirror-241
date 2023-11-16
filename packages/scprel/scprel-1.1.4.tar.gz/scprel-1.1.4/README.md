## Scprel - Single-Cell Data Preprocessing in Python

### Import scprel as:

    import scprel

This package allows to perform basic preprocessing steps for single-cell analysis of multiple samples. It includes scrublets detection, quality control, normalization, leiden clustering and infercnv calculations. This package is the result of integrating some of the scanpy, decoupler, infercnvpy and anndata functions. It is designed to facilitate workflow when analyzing multiple samples.

### Example of usage:

    from scprel import scrun
    
	scrun(names = ['sample1', 'sample2'], path = '/content/drive/MyDrive/MyDirectory/')

* *names - list of sample names in your directory (.h5 format);* 
* *path - path to the directory with samples*

The result of this function is the adata file with concatenated samples, filtered by 'mt' and 'ribo' genes, with annotated gene locations and annotated tumor cells based on cnv score. The resulting file will be saved in your default home directory and is ready for batch correction and further analysis.