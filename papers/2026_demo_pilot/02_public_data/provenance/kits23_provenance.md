
# KiTS23 provenance record

## Dataset identity

- dataset_name: KiTS23
- dataset_local_root: /Users/lulingfeng/sci-paper-factory/papers/2026_demo_pilot/02_public_data/raw/KiTS23/dataset
- acquisition_method: staged acquisition; KiTS23 snapshot obtained via official release route, with missing imaging files subsequently recovered by a local bash script using curl resume/retry logic and the case list in `KiTS23_missing_imaging_cases.txt`
- download_date_local: 2026-03-17
- recorded_by: Lu Lingfeng

## Official source

- challenge homepage: https://kits-challenge.org/kits23/
- official repository: https://github.com/neheller/kits23
- declared dataset version: 0.1.4
- declared data license: CC BY-NC-SA 4.0
- declared code license: MIT

## Local integrity snapshot

- number_of_case_directories_found: 489
- segmentation_files_found: 489
- missing_segmentation_cases: none
- checksum_manifest_path: papers/2026_demo_pilot/02_public_data/provenance/kits23_sha256_manifest.txt

## Notes

- Imaging recovery script used the following URL pattern:
  `https://kits19.sfo2.digitaloceanspaces.com/master_${num}.nii.gz`
- Recovery target file path per case:
  `/Users/lulingfeng/sci-paper-factory/papers/2026_demo_pilot/02_public_data/raw/KiTS23/dataset/case_xxxxx/imaging.nii.gz`
- Missing imaging case list source:
  `papers/2026_demo_pilot/02_public_data/provenance/KiTS23_missing_imaging_cases.txt`
- Script behavior:
  resume partial downloads (`-C -`), validate gzip integrity (`gzip -t`), delete corrupted files, and retry until success.
- Official KiTS23 distribution notes:
  segmentations are managed through the GitHub release route, while imaging is fetched from separate servers.
