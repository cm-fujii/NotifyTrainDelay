#!/bin/bash

BUCKET_NAME="cm-fujii.genki-deploy"

sam package \
    --output-template-file packaged.yaml \
    --s3-bucket $BUCKET_NAME
