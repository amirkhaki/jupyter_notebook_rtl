
# Jupyter Notebook RTL

**Jupyter Notebook RTL** is a Python tool that adds right-to-left (RTL) text support for Jupyter notebooks. It's designed for users working in RTL languages such as Persian, Arabic, and Hebrew.

## Features
- Updates only Markdown cells with `direction=rtl` in their metadata.
- Outputs a modified notebook with RTL-supported cells.

## Requirements
- Python 3.x

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/amirkhaki/jupyter_notebook_rtl
   cd jupyter_notebook_rtl
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Convert a Jupyter notebook to RTL format:
```bash
python3 ./main.py /path/to/notebook.ipynb /path/to/out.ipynb
```
Only Markdown cells with `direction=rtl` in their metadata will be updated. 

To set the RTL direction for a cell, use the "Toggle current cell LTR/RTL direction" command in Jupyter Notebook v6 (this feature is removed in v7).

Once the notebook is generated:
1. Open it in Jupyter Notebook.
2. Run the last cell to apply RTL formatting.
3. Save the notebook after running the cell to ensure the RTL changes are preserved.
