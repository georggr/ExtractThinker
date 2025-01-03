import os
import pytest
from extract_thinker.document_loader.document_loader_txt import DocumentLoaderTxt
from tests.test_document_loader_base import BaseDocumentLoaderTest


class TestDocumentLoaderTxt(BaseDocumentLoaderTest):
    @pytest.fixture
    def loader(self):
        return DocumentLoaderTxt()

    @pytest.fixture
    def test_file_path(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(current_dir, 'files', 'ambiguous_credit_note.txt')

    def test_txt_specific_content(self, loader, test_file_path):
        """Test text file-specific content extraction"""
        pages = loader.load(test_file_path)
        
        assert isinstance(pages, list)
        assert len(pages) > 0
        
        first_page = pages[0]
        assert "content" in first_page
        assert "CREDIT NOTE / RECEIPT" in first_page["content"]
        assert "Customer: John Smith" in first_page["content"]
        assert "Payment Method: Store Credit" in first_page["content"]

    def test_vision_mode(self, loader, test_file_path):
        """Test that vision mode is not supported for TXT loader"""
        loader.set_vision_mode(True)
        with pytest.raises(ValueError):
            loader.load(test_file_path)