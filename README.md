


<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div>
  <p>
    <a href="https://github.com/kpwhri/social-isolation-runrex">
      <img src="images/logo.png" alt="Logo">
    </a>
  </p>

  <h3 align="center">Social Isolation Runrex</h3>

  <p>
    Feature extraction for developing an algorithm to identify social isolation cases.
    Additional steps will require use of these variables to build a predictive algorithm.
  </p>
</div>


<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

This algorithm is based on the description in Zhu et al (2019): "Automatically identifying social isolation from clinical narratives for patients with prostate Cancer".
That algorithm was implemented in Linguamatics, and actual implementation details are somewhat obscure (e.g., what exactly was the lexicon/list of terms used?)

This implementation follows the spirit of Zhu et al, but includes additional hypothetical cases, more terms, and includes (optionally) the skipped category of 'lives alone'.

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* Python 3.8+
* runrex package: https://github.com/kpwhri/runrex

### Installation
 
1. Clone the repo
```sh
git clone https://github.com/kpwhri/social-isolation-runrex.git
```
2. Install requirements
```sh
pip install -r requirements.txt -r requirements-dev.txt
```
3. Run tests.
```sh
set/export PYTHONPATH=src
pytest tests
```


<!-- USAGE EXAMPLES -->
## Usage

The first entry (1. Running Runrex Application) is the primary use. This will identity 'concepts' in the text.
 Secondary use converts these 'concepts' into various other formats. For these, additional packages (`pandas` and `sqlalchemy`) are required.
 Install with `pip install -r requirements-extra.txt`.

### 1. Running Runrex Application

* Build a configuration file as defined in [runrex](https://github.com/kpwhri/runrex)
    - Full details defined in that project's [schema.py](https://github.com/kpwhri/runrex/blob/master/src/runrex/schema.py)
* Run the application
    - `python src/run.py runrex.conf.(py|json|yaml)`
* Organize outputs
    - `python src/extract_and_load_json.py  --file [OUTPUT file from RUNREX; ends in jsonl] --version runrex`

### 2. Build Variables
Build secondary variables for subsequent analysis. You can use the pre-built variables (default) or supply your own.
 These secondary variables build on the output of running regex.

To force all output columns to fit within the 32 characters required by a SAS dataset, add the option `--max-col-length 32`.

These will often require additional metadata to complete. The recommended table structure for the included secondary variables is:

#### Meta Table
Please create a CSV file with the following columns:

* `doc_id` = this should correspond to the id that was supplied to the runrex algorithm. It may be specified in the `config.py` file.
* `patient_id` = patient id or studyid; this is only used to aggregate the data to the patient level
* `total_text_length` = the length of the note (e.g., in SQL Server `len(text)` is fine)
* `date` = preferably not a datetime; preferable format is 'YYYY-mm-dd' (e.g., '2011-02-17' for Feb 17, 2011)
* `text` = the complete text; this will be used in step #3 to create files for manual review of concepts

#### Build Secondary Variables
* `python src/build_variables.py --file [PATH to output from 'extract_and_load_json' above] --metafile [PATH to table created above ("Meta Table")]`

### 3. Build Review Lists
Build CSV files of each algorithm/category for manual review of algorithms/categories output by `run.py`.

#### Step A
* First, you'll need to take a look at the runrex configuration file (something like 'config.py' which is supplied as input?). Open that up and see if you have a line that looks like this:
    - `'loginfo': {'directory': r'C:\path\to\somewhere'}`

* If so, locate that file and use it as the `--log-file` in Step B (you can skip to Step B).
* Otherwise, re-run runrex with the `loginfo` option specified.

#### Step B

* `python build_review_lists.py --output-file [PATH  to runrex output file; original jsonl or the transformed to csv] --log-file [PATH to log file from step B] --metafile [PATH to CSV table created in step #1]`
*  This will generate a series of CSV files (randomly ordered) for manual review. There are currently offset problems in runrex, so this does not currently work as well as desired.

## Variables Identified

Variables (called 'algorithms') are broken down into various 'categories'. Either can be used in building features.

### Output Variable Names

TODO

### Variable List

Complete data dictionaries are included in the [res/ directory](res):
* Complete variable names: [data-dictionary.csv](res/data-dictionary.csv)
* Reduced variable names for SAS: [data-dictionary-sas.csv](res/data-dictionary-sas.csv)

| Algorithm                                           | Category  | Description      |
|-----------------------------------------------------|-----------|------------------|
| [isolation](src/social_isolation/algo/isolation.py) | ISOLATION | Social isolation |
| [alone](src/social_isolation/algo/alone.py)         | ALONE     | Lives alone      |


## Output Format

Recommended format is `jsonl`. For more details, see [runrex](https://github.com/kpwhri/runrex).


## Versions

<!-- Uses [SEMVER](https://semver.org/). -->

Updates/changes are not expected. Versioning likely based on release timing in `YYYYmm`. See https://github.com/kpwhri/social-isolation-runrex/releases.

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/kpwhri/social-isolation-runrex/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` or https://kpwhri.mit-license.org for more information.



<!-- CONTACT -->
## Contact

Please use the [issue tracker](https://github.com/kpwhri/social-isolation-runrex/issues). 


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/kpwhri/social-isolation-runrex.svg?style=flat-square
[contributors-url]: https://github.com/kpwhri/social-isolation-runrex/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/kpwhri/social-isolation-runrex.svg?style=flat-square
[forks-url]: https://github.com/kpwhri/social-isolation-runrex/network/members
[stars-shield]: https://img.shields.io/github/stars/kpwhri/social-isolation-runrex.svg?style=flat-square
[stars-url]: https://github.com/kpwhri/social-isolation-runrex/stargazers
[issues-shield]: https://img.shields.io/github/issues/kpwhri/social-isolation-runrex.svg?style=flat-square
[issues-url]: https://github.com/kpwhri/social-isolation-runrex/issues
[license-shield]: https://img.shields.io/github/license/kpwhri/social-isolation-runrex.svg?style=flat-square
[license-url]: https://kpwhri.mit-license.org/
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/company/kaiserpermanentewashingtonresearch
<!-- [product-screenshot]: images/screenshot.png -->