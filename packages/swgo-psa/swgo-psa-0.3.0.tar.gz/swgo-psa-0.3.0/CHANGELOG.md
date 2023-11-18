# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

## [0.3.0] - 2023-11-17

### Added

- documentation skeleton and gh-pages action
- `swgo.psa.adaptive_sum`

### Fixed

- add `scipy` to list of dependencies
- versioning scheme on TestPyPi
- expose all functions for wildcard import

## [0.2.0] - 2023-11-17

### Added

- type annotations
- `swgo.psa.upsample`
- `swgo.psa.differentiate`
- `swgo.psa.deconvolve_pole_zero`

### Changed

- make `swgo.psa.adaptive_centroid` work for lists as well

### Fixed

- return value of `swgo.psa.adaptive_centroid` was of type `int` (via `peak_index`) on malformed inputs
- upload of dev versions to TestPyPi

## [0.1.0] - 2023-11-16

### Added

- `swgo.psa.adaptive_centroid` function to calculate a robust pulse centroid
