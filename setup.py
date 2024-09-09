from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "Books-Recommendation-System-Using-ML"
AUTHOR_USER_NAME = "krishachikka"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ['streamlit', 'numpy','scikit-learn']


setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="A small package for Book Recommendation System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/krishachikka/Book-Recommendation-System-using-ML",
    author_email="chikkakrisha@gmail.com",
    packages=[SRC_REPO],
    license="MIT",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)