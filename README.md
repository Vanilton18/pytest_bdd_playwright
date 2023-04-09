# Acceptance Test + Pytest-bdd + Playwright

<details>

<summary> Setup </summary>

#### Clone the repo

`git clone ....`

`cd pytest_bdd_playwright`

Active a virtualenv to the project with Python 3+

#### Libs

Install the libs below:

`pip install pytest-bdd pytest-playwright`

or

`pip install -r requirements.txt`

Install Browsers of Playwright

From source code run:

`python playwright_install.py` (This case select browsers by CLI)

or 

`plawright install`

</details>

<details>

<summary> Run Tests </summary>

**Run All Tests**

`pytest`

**Run Verbose Mode**

`pytest -v` 

from project root.

#### To run an individual test by feature tag

`pytest -k "tag1"`

Other example

`pytest -k "tag1 and tag2"`

</details>

<details>

<summary> Generate Steps of Features </summary>

`pytest-bdd generate <feature file name> .. <feature file nameN>`

Generate steps from file

`pytest-bdd generate features/some.feature > tests/steps/test_some.py`

Generate Only Missing Steps

`pytest --generate-missing --feature tests/features`

Other example

`pytest --generate-missing --feature tests/features/pokedex.feature`

</details>

<details>

<summary> References </summary>

https://pytest-bdd.readthedocs.io/en/latest/#example

https://docs.pytest.org/en/6.2.x/

https://playwright.dev/python/docs/test-runners#usage

</details>