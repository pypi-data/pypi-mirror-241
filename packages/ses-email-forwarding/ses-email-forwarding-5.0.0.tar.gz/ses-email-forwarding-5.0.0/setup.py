import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "ses-email-forwarding",
    "version": "5.0.0",
    "description": "@seeebiii/ses-email-forwarding",
    "license": "MIT",
    "url": "https://github.com/seeebiii/ses-email-forwarding",
    "long_description_content_type": "text/markdown",
    "author": "Sebastian Hesse<info@sebastianhesse.de>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/seeebiii/ses-email-forwarding"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "ses_email_forwarding",
        "ses_email_forwarding._jsii"
    ],
    "package_data": {
        "ses_email_forwarding._jsii": [
            "ses-email-forwarding@5.0.0.jsii.tgz"
        ],
        "ses_email_forwarding": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.7",
    "install_requires": [
        "aws-cdk-lib>=2.105.0, <3.0.0",
        "constructs>=10.0.5, <11.0.0",
        "jsii>=1.91.0, <2.0.0",
        "publication>=0.0.3",
        "typeguard~=2.13.3"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Typing :: Typed",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
