import ipywidgets as widgets
from IPython.display import display
import sys

def in_jupyter():
    """Check if the code is running in a Jupyter Notebook."""
    if 'ipykernel' not in sys.modules:
        return True
    else:
        return False


def upload_files(allowed_extensions=['.xlsx', '.xls', '.csv', '.tsv']):
    uploader = widgets.FileUpload(
        accept=', '.join(allowed_extensions),
        multiple=False
    )

    uploaded_files = {}

    def on_upload_change(change):
        if change['name'] == 'data':
            uploaded_files.clear()  # Clear previous uploads
            for filename, file_info in uploader.value.items():
                if any(filename.endswith(ext) for ext in allowed_extensions):
                    uploaded_files[filename] = file_info['content']
                    print(f"Uploaded '{filename}' ({len(file_info['content'])} bytes).")
                else:
                    print(f"File '{filename}' is not a supported format.")

    uploader.observe(on_upload_change, names='_counter')
    display(uploader)

    return uploader, uploaded_files