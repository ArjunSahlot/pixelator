#!/bin/bash

download_link=https://github.com/ArjunSahlot/pixelator/archive/main.zip
temporary_dir=$(mktemp -d)
echo "Checking if curl is installed"
if [ $(dpkg-query -W -f='${Status}' curl3 2>/dev/null | grep -c "ok installed") -eq 0 ];
then
  echo -e "[0;31mcurl is not installed[0m"
  echo "Installing curl..."
  sudo apt install -y curl;
  echo -e "[0;32mcurl was successfully installed[0m"
else
  echo -e "[0;32mcurl is already installed[0m"
fi
&& curl -LO $download_link \
&& unzip -d $temporary_dir main.zip \
&& rm -rf main.zip \
&& mv $temporary_dir/pixelator-main $1/pixelator \
&& rm -rf $temporary_dir
echo -e "[0;32mSuccessfully downloaded to $1/pixelator[0m"
echo "Checking if pip is installed"
if [ $(dpkg-query -W -f='${Status}' pip3 2>/dev/null | grep -c "ok installed") -eq 0 ];
then
  echo -e "[0;31mpip is not installed[0m"
  echo "Installing pip..."
  sudo apt install -y python3-pip;
  echo -e "[0;32mpip was successfully installed[0m"
else
  echo -e "[0;32mpip is already installed[0m"
fi
echo "Installing requirements"
cd $1/pixelator
pip3 install -r requirements.txt
echo "[0;32mDone![0m"