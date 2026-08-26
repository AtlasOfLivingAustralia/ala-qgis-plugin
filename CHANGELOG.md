## 1.0.3 (2026-08-27)

### Fix

- **quail_dialog.py**: increased the amount of records you can download (typo)

## 1.0.2 (2026-08-21)

### Fix

- **quail_dialog.py**: fixed an error where if a numeric identifier would identify a shape file, it was not being chosen

## 1.0.1 (2026-08-12)

### Fix

- **quail_dialog.py**: fixed speices list rendering, updated galah-python version, added exception for version that don't have pyarrow.compute
- **fixed-name-of-Australian-atlas**: fixed name of australian atlas
- **quail_dialog.py-and-help**: changed theme for help; added check in quail_dialog to make sure that users who don't have pyarrow installed with matching regex option still get options
- **logo,-species-list,-reqs**: made sure logo is showing, species list is able to download, and requirements are up to date

### Refactor

- **moving-files-around-for-release**: moving files around for release

## 1.0.0 (2026-06-26)

### Feat

- **continuing-improvements**: cleaned up code and comments; added dynamic sizing to the spatial window
- **continued-development**: major developments in handling taxonomy from text boxes vs files; added a lot of spatial functionality
- **whole-plugin**: continuing to ensure frontend links up with backend

### Fix

- **fixed-spatial-layers**: updated docs with icon and fixed an issue with spatial layers
- **fixed-atlases-and-docs**: fixed how each atlas is handled so they can all download occurrences within qgis; updated the docs with updated images of quail
- **finalising-plugin**: finalising plugin for initiali release
- **renamed-plugin-to-Quail**: renamed everything from a generic name to quail
- **plugin-itself**: species lists
- **dialog.py**: doi
- **UI-and-plugin**: information boxes, doi, taxonomy and stats
- **first-commit**: first commit
