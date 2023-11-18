
# tests/test_download_cptac.py

from coderdata.download.downloader import download_data_by_prefix
import os
import glob
import tempfile

def test_download_data_cptac():
    with tempfile.TemporaryDirectory() as temp_dir:
        os.chdir(temp_dir)

        #CPTAC
        download_data_by_prefix('cptac')
        
        cptac_copy_number = glob.glob('cptac_copy_number*')
        assert len(cptac_copy_number) > 0, "File cptac_copy_number does not exist."
        
        cptac_proteomics = glob.glob('cptac_proteomics*')
        assert len(cptac_proteomics) > 0, "File cptac_proteomics does not exist."
        
        cptac_samples = glob.glob('cptac_samples*')
        assert len(cptac_samples) > 0, "File cptac_samples does not exist."
        
        cptac_mutations = glob.glob('cptac_mutations*')
        assert len(cptac_mutations) > 0, "File cptac_mutations does not exist."
        
        cptac_transcriptomics = glob.glob('cptac_transcriptomics*')
        assert len(cptac_transcriptomics) > 0, "File cptac_transcriptomics does not exist."
        