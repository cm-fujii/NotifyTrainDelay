BUCKET_NAME := cm-fujii.genki-deploy


build:
	sam build

deploy:
	sam package \
	    --output-template-file packaged.yaml \
		--s3-bucket $(BUCKET_NAME)

	sam deploy \
		--template-file packaged.yaml \
		--stack-name NotifyTrainDelayToSlack \
		--capabilities CAPABILITY_IAM
