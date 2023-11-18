# tests/test_downloader.py

from coderdata.download.downloader import download_data_by_prefix
import os

def test_download_data_by_prefix():
    # Test the function with expected inputs
    download_data_by_prefix('hcmi')
    # Assert that the expected output file exists
    assert os.path.exists('hcmi_mutations.csv*')
    assert os.path.exists('hcmi_samples.csv*')
    assert os.path.exists('hcmi_transcriptomics.csv*')
    assert os.path.exists('hcmi_copy_number.csv*')
                