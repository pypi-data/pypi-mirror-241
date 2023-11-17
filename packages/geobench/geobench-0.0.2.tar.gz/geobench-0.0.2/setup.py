# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['geobench', 'geobench.tests', 'geobench.torch_toolbox']

package_data = \
{'': ['*']}

install_requires = \
['h5py>=3.8.0,<4.0.0',
 'huggingface_hub>=0.19.3,<0.20.0',
 'pandas>=1.5.3,<2.0.0',
 'rasterio>=1.3.8,<2.0.0',
 'requests>=2.26.0,<3.0.0',
 'scipy>=1.11.2,<2.0.0',
 'seaborn>=0.12.2,<0.13.0',
 'tqdm>=4.65.0,<5.0.0']

entry_points = \
{'console_scripts': ['geobench-download = '
                     'geobench.geobench_download:download_benchmark',
                     'geobench-test = geobench.tests.launch_pytest:start']}

setup_kwargs = {
    'name': 'geobench',
    'version': '0.0.2',
    'description': 'A benchmark designed to advance foundation models for Earth monitoring, tailored for remote sensing. It encompasses six classification and six segmentation tasks, curated for precision and model evaluation. The package also features a comprehensive evaluation methodology and showcases results from 20 established baseline models.',
    'long_description': '# GEO-Bench: Toward Foundation Models for Earth Monitoring\n\nGeoBench is a [ServiceNow Research](https://www.servicenow.com/research) project. \n\n[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)\n[![Language: Python](https://img.shields.io/badge/language-Python%203.9%2B-green?logo=python&logoColor=green)](https://www.python.org)\n\nGEO-Bench is a General Earth Observation benchmark for evaluating the performances of large pre-trained models on geospatial data. Read the [full paper](https://arxiv.org/abs/2306.03831) for usage details and evaluation of existing pre-trained vision models.\n\n<img src="https://github.com/ServiceNow/geo-bench/raw/main/banner.png" width="500" />\n\n## Installation\n\nYou can install GEO-Bench with [pip](https://pip.pypa.io/):\n\n```console\npip install geo-benchmark\n```\n\nNote: Python 3.9+ is required.\n\n## Downloading the data\n\nSet `$GEO_BENCH_DIR` to your preferred location. If not set, it will be stored in `$HOME/dataset/geobench`.\n\nNext, use the [download script](https://github.com/ServiceNow/geo-bench/blob/main/geobench/geobench_download.py). This will automatically download from [Hugging Face](https://huggingface.co/datasets/recursix/geo-bench-1.0)\n\nRun the command:\n\n```console\ngeobench-download\n```\n\nYou need ~65 GB of free disk space for download and unzip (once all .zip are deleted it takes 57GB).\nIf some files are already downloaded, it will verify the md5 checksum. Feel free to restart the downloader if it is interrupted.\n\n## Test installation\nYou can run tests. \nNote: Make sure the benchmark is downloaded before launching tests.\n\n```console\npip install pytest\n```\n\n```console\ngeobench-test\n```\n\n## Loading Datasets\n\nSee [`example_load_dataset.py`](https://github.com/ServiceNow/geo-bench/blob/main/geobench/example_load_datasets.py) for how to iterate over datasets.\n\n```python\nimport geobench\n\nfor task in geobench.task_iterator(benchmark_name="classification_v1.0"):\n    dataset = task.get_dataset(split="train")\n    sample = dataset[0]\n    for band in sample.bands:\n        print(f"{band.band_info.name}: {band.data.shape}")\n```\n## Visualizing Results\n\nSee the notebook [`baseline_results.ipynb`](https://github.com/ServiceNow/geo-bench/blob/main/geobench/baseline_results.ipynb) for an example of how to visualize the results.\n\n\n',
    'author': 'Alexandre Lacoste',
    'author_email': 'alexandre.lacoste@servicenow.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9.0,<3.13',
}


setup(**setup_kwargs)
