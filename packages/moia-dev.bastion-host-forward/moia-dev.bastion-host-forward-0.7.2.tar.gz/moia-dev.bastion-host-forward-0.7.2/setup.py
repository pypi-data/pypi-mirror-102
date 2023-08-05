import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "moia-dev.bastion-host-forward",
    "version": "0.7.2",
    "description": "@moia-dev/bastion-host-forward",
    "license": "Apache-2.0",
    "url": "https://github.com/moia-oss/bastion-host-forward",
    "long_description_content_type": "text/markdown",
    "author": "MOIA GmbH",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/moia-oss/bastion-host-forward"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "moia_dev.bastion_host_forward",
        "moia_dev.bastion_host_forward._jsii"
    ],
    "package_data": {
        "moia_dev.bastion_host_forward._jsii": [
            "bastion-host-forward@0.7.2.jsii.tgz"
        ],
        "moia_dev.bastion_host_forward": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "aws-cdk.aws-ec2>=1.97.0, <2.0.0",
        "aws-cdk.aws-elasticache>=1.97.0, <2.0.0",
        "aws-cdk.aws-iam>=1.97.0, <2.0.0",
        "aws-cdk.aws-rds>=1.97.0, <2.0.0",
        "aws-cdk.aws-redshift>=1.97.0, <2.0.0",
        "aws-cdk.core>=1.97.0, <2.0.0",
        "constructs>=3.0.3, <4.0.0",
        "jsii>=1.27.0, <2.0.0",
        "publication>=0.0.3"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Typing :: Typed",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
