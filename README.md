# ffmpeg Python Lambda Layer
Inspired by [sqlite-lambda-layer](https://github.com/dschep/sqlite-lambda-layer), this project builds a lambda layer with ffmeg and [Pillow](https://pypi.org/project/Pillow/0) installed.

## How to use
First you must clone the repo, build the file, and publish it to AWS:
```shell
git clone git@github.com:d-me-tree/ffmpeg-lambda-layer.git
cd ffmpeg-lambda-layer
./build.sh
sls deploy
```
Then see [the docs](https://serverless.com/framework/docs/providers/aws/guide/functions/#layers)
and configure your lambda to use the layer you just published.

## Other helpful resources
- [How to compile resources for AWS Lambda?!](https://medium.com/@mohd.lutfalla/how-to-compile-resources-for-aws-lambda-f46fadc03290)
- [How to publish and use AWS Lambda Layers with the Serverless Framework](https://www.serverless.com/blog/publish-aws-lambda-layers-serverless-framework/)
- [How to process media in AWS Lambda? (ffmpeg)](https://medium.com/@mohd.lutfalla/how-to-process-media-in-aws-lambda-ffmpeg-f53491cf8768)
