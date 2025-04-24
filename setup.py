import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

__version__ = "0.0.1"

REPO_NAME = "automatic-ticket-classification-system"
AUTH_USER_NAME = "ravichandran1610"
SRC_REPO = "ticketClassifier"
AUTH_EMAIL = "rravii.r@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTH_USER_NAME,
    author_email=AUTH_EMAIL,
    description="App for classify the ticket to right Assignment group",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f'https://github.com/{AUTH_USER_NAME}/{REPO_NAME}',
    project_urls = {
        "Bug Tracker": f'https://github.com/{AUTH_USER_NAME}/{REPO_NAME}/issues'
    },
    package_dir={'':'src'},
    packages=setuptools.find_packages(where="src")
)