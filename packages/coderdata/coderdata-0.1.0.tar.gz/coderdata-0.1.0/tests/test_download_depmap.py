# tests/test_download_depmap.py

from coderdata.download.downloader import download_data_by_prefix
import os
import glob
import tempfile

def test_download_data_depmap():
    with tempfile.TemporaryDirectory() as temp_dir:
        os.chdir(temp_dir)

        #DepMap
        download_data_by_prefix('depmap')
        
        depmap_samples = glob.glob('depmap_samples*')
        assert len(depmap_samples) > 0, "File depmap_samples does not exist."
        
        depmap_experiments = glob.glob('depmap_experiments*')
        assert len(depmap_experiments) > 0, "File depmap_experiments does not exist."
        
        depmap_mutations = glob.glob('depmap_mutations*')
        assert len(depmap_mutations) > 0, "File depmap_mutations does not exist."
        
        depmap_proteomics = glob.glob('depmap_proteomics*')
        assert len(depmap_proteomics) > 0, "File depmap_proteomics does not exist."
        
        depmap_transcriptomics = glob.glob('depmap_transcriptomics*')
        assert len(depmap_transcriptomics) > 0, "File depmap_transcriptomics does not exist."
        
        depmap_drugs = glob.glob('depmap_drugs*')
        assert len(depmap_drugs) > 0, "File depmap_drugs does not exist."
        
        depmap_copy_number = glob.glob('depmap_copy_number*')
        assert len(depmap_copy_number) > 0, "File depmap_copy_number does not exist."
        