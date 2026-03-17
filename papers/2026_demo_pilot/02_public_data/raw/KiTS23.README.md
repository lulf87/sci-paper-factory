# KiTS23 expected local layout

Recommended checkout target:

```bash
git clone https://github.com/neheller/kits23 02_public_data/raw/KiTS23
cd 02_public_data/raw/KiTS23
pip install -e .
kits23_download_data
```

## Expected layout after clone + official download script

```text
02_public_data/raw/KiTS23/
├── dataset/
│   ├── kits23.json
│   ├── case_00000/
│   │   ├── imaging.nii.gz
│   │   ├── segmentation.nii.gz
│   │   └── instances/
│   ├── case_00001/
│   │   ├── imaging.nii.gz
│   │   ├── segmentation.nii.gz
│   │   └── instances/
│   └── ...
├── kits23/
├── README.md
├── changelog.md
└── setup.py
```

## Notes
- `segmentation.nii.gz` and `instances/` are tracked in the official repository tree.
- `imaging.nii.gz` is fetched by the official `kits23_download_data` entrypoint.
- The official download script writes imaging files into `dataset/case_XXXXX/imaging.nii.gz`.
