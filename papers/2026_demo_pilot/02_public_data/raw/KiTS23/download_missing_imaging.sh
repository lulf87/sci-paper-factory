#!/usr/bin/env bash
set -euo pipefail

ROOT="$HOME/sci-paper-factory/papers/2026_demo_pilot/02_public_data/raw/KiTS23/dataset"
LIST="$HOME/sci-paper-factory/papers/2026_demo_pilot/02_public_data/provenance/KiTS23_missing_imaging_cases.txt"

while read -r case_id; do
  [[ -z "$case_id" ]] && continue
  [[ "$case_id" =~ ^# ]] && continue

  num="${case_id#case_}"
  out_dir="$ROOT/$case_id"
  out_file="$out_dir/imaging.nii.gz"
  part_file="$out_file.part"
  url="https://kits19.sfo2.digitaloceanspaces.com/master_${num}.nii.gz"

  mkdir -p "$out_dir"

  # 已有正式文件时，先校验；通过才 skip，不通过就删掉重下
  if [[ -f "$out_file" ]]; then
    if gzip -t "$out_file" >/dev/null 2>&1; then
      echo "[skip] $case_id"
      continue
    else
      echo "[bad ] $case_id existing file is corrupted, redownloading"
      rm -f "$out_file"
    fi
  fi

  # 如果上次留下 part 文件，先检查是否其实已经完整
  if [[ -f "$part_file" ]]; then
    if gzip -t "$part_file" >/dev/null 2>&1; then
      mv "$part_file" "$out_file"
      echo "[ok  ] $case_id (recovered from .part)"
      continue
    fi
  fi

  echo "[download] $case_id"

  # 单个 case 内部无限重试；断线后继续续传
  while true; do
    if curl -L \
      -C - \
      --fail \
      --connect-timeout 20 \
      --retry 20 \
      --retry-delay 5 \
      --retry-connrefused \
      -o "$part_file" \
      "$url"; then

      if gzip -t "$part_file" >/dev/null 2>&1; then
        mv "$part_file" "$out_file"
        echo "[ok] $case_id"
        break
      else
        echo "[warn] $case_id downloaded file failed gzip test, retrying..."
        rm -f "$part_file"
      fi
    else
      echo "[warn] $case_id download interrupted, retrying in 15s..."
      sleep 15
    fi
  done

done < "$LIST"