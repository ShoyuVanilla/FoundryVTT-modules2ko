import os
import sys
import shutil
import json
import yaml

root_dir = os.path.dirname(__file__)
translations_dir = os.path.join(root_dir, 'translations')
localizations_dir = os.path.join(root_dir, 'module/localizations')
metadata_path = os.path.join(root_dir, 'module/metadata.json')

os.makedirs(localizations_dir, exist_ok=True)

metadata = {}

for root, dirs, files in os.walk(translations_dir):
	for dirname in dirs:
		sub_dir = os.path.join(translations_dir, dirname)
		meta_filename = os.path.join(sub_dir, 'meta.yml')
		translation_filename = os.path.join(sub_dir, 'ko.json')
		with open(meta_filename) as f:
			metadatum = yaml.safe_load(f)
		name = metadatum.pop('name')
		metadata[name] = metadatum
		shutil.copyfile(translation_filename, os.path.join(localizations_dir, name + '.json'))

with open(metadata_path, "w") as f:
	json.dump(metadata, f, ensure_ascii=False, indent=2)