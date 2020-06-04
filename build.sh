#!/bin/bash -x

rm -rf layer && mkdir -p layer/python

# Install ffmpeg
cd layer/python
curl -LO https://johnvansickle.com/ffmpeg/builds/ffmpeg-git-amd64-static.tar.xz
tar xf ffmpeg-git-amd64-static.tar.xz
mv ffmpeg-git-*-amd64-static/{ffmpeg,ffprobe} .
rm -rf ffmpeg-git-*

# Return back to the dir where build.sh is located to keep docker run command consistent
cd ../..

# Install Pillow
docker run --rm -v "$PWD":/var/task lambci/lambda:build-python3.7 bash -c "
cd layer/python &&
python3.7 -m pip install pillow==7.0.0 -t ./
"
