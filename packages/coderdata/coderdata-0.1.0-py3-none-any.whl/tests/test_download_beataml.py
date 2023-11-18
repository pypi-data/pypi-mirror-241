# tests/test_download_beataml.py

from coderdata.download.downloader import download_data_by_prefix
import os
import glob
import tempfile

def test_download_data_beataml():
    with tempfile.TemporaryDirectory() as temp_dir:
        os.chdir(temp_dir)

        #BeatAML
        download_data_by_prefix('beataml')
        
        beataml_drugs = glob.glob('beataml_drugs*')
        assert len(beataml_drugs) > 0, "File beataml_drugs  does not exist."
        
        beataml_experiments = glob.glob('beataml_experiments*')
        assert len(beataml_experiments) > 0, "File beataml_experiments does not exist."
        
        beataml_mutations = glob.glob('beataml_mutations*')
        assert len(beataml_mutations) > 0, "File beataml_mutations does not exist."
        
        beataml_proteomics = glob.glob('beataml_proteomics*')
        assert len(beataml_proteomics) > 0, "File beataml_proteomics  does not exist."
        
        beataml_samples = glob.glob('beataml_samples*')
        assert len(beataml_samples) > 0, "File beataml_samples does not exist."
        
        beataml_transcriptomics = glob.glob('beataml_transcriptomics*')
        assert len(beataml_transcriptomics) > 0, "File beataml_transcriptomics does not exist."
