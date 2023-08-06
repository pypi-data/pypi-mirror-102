# Changelog
This changelog is inspired by [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [0.2a1] - 21-04-19
### Fixed
- Failed tests in python version 3.6 due to different inheritance behavior of 
  enum.IntFlag.
- A single AUnit now is being processed by *justunits.to_string*.

## Removed
- The concept of *AnyUnit* and *AUnit* carrying their own style definition and the
  *StyledDetection* is removed before releasing the first alpha release on *pipy.org*.

## [0.2a0] - unreleased
### Added
- A huge chunk of code for unit detection, definition and formatting into different
  styles.
  
## [0.1a0] - unreleased
### Changed
- renamed *encode_text* with *join_unit*
- *join_unit* does not enforce unit separator if `None` or empty unit is supplied. This
  behavior reflects for entities, which doesn't need a unit.

## [0.0a1] - unreleased
Start of justunits.