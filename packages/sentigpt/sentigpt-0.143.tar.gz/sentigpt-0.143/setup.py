from setuptools import setup, find_packages

setup(
    name='sentigpt',
    version='0.143',
    author='xikest',
    description='Sentiment analyze with gpt',
    packages=find_packages(),
    python_requires='>=3.7',
    install_requires=[
        'matplotlib',
        'numpy',
        'openpyxl',
        'pandas',
        'tqdm',
        'seaborn',
        'openai'
    ],


    url='https://github.com/xikest/app_plotvisual',  # GitHub 프로젝트 페이지 링크
    project_urls={
        'Source': 'https://github.com/xikest/app_plotvisual',  # GitHub 프로젝트 페이지 링크
        'Bug Tracker': 'https://github.com/xikest/app_plotvisual/issues',  # 버그 트래커 링크
    },
)