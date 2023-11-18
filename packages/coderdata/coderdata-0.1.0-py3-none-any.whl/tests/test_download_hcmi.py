# tests/test_download_hcmi.py

from coderdata.download.downloader import download_data_by_prefix
import os
import glob
import tempfile


def test_download_data_hcmi():
    with tempfile.TemporaryDirectory() as temp_dir:
        os.chdir(temp_dir)

        #HCMI
        download_data_by_prefix('hcmi')
        
        hcmi_mutations = glob.glob('hcmi_mutations*')
        assert len(hcmi_mutations) > 0, "File hcmi_mutations does not exist."
        
        hcmi_samples = glob.glob('hcmi_samples*')
        assert len(hcmi_samples) > 0, "File hcmi_samples does not exist."
        
        hcmi_transcriptomics = glob.glob('hcmi_transcriptomics*')
        assert len(hcmi_transcriptomics) > 0, "File hcmi_transcriptomics does not exist."
        
        hcmi_copynum = glob.glob('hcmi_copy_number*')
        assert len(hcmi_copynum) > 0, "File hcmi_copy_number  does not exist."
        
        