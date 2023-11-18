from setuptools import setup

setup(
    name="tabella-integration-test-client",
    version="1.0.0",
    author="John Doe",
    author_email="email@website.test",
    description="Tabella Integration Test Python HTTP client.",
    packages=["tabella_integration_test_client"],
    install_requires=["jsonrpc2-pyclient==4.3.0", "pydantic==2.3.0"],
)
