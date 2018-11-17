#### Caveat
all paths valid for `vast.ai` `paperspace` docker image. If you use something else - paths must be changed according to your setup

#### My favorite tools install [optional]

```bash
apt install software-properties-common
add-apt-repository ppa:ultradvorka/ppa
apt get update
apt install htop hstr
hstr --show-configuration >> ~/.bashrc
pip install gpustat
```
#### Initialization

```bash
mkdir ~/data
ln -s /notebooks ~/fastai
cd ~/fastai
git pull
conda env update
jupyter notebook --generate-config
jupyter notebook --no-browser --ip=127.0.0.1 --port=8080 --allow-root
```

#### Console with ability to reconnect
[autossh](https://www.everythingcli.org/ssh-tunnelling-for-fun-and-profit-autossh/) must be installed
```bash
autossh -p <port> -M 0 -o "ServerAliveInterval 30" -o "ServerAliveCountMax 3" -L 8080:localhost:8080 root@<ip>
```

#### Download external data
`cd` to downloads dir first
```bash
cd  data
```
* dl1 lesson1.ipynb
```bash
wget http://files.fast.ai/data/dogscats.zip
unzip dogscats.zip
```
* dl1 lesson1-rxt50.ipynb
```bash
cd  data
wget http://files.fast.ai/models/weights.tgz
tar -xf weights.tgz
ln -s /notebooks/courses/dl1/data/weights /notebooks/courses/dl1/fastai/weights
```
* dl2 pascal.ipynb
```bash
mkdir pascal && cd $_
curl -OL http://pjreddie.com/media/files/VOCtrainval_06-Nov-2007.tar
curl -OL https://storage.googleapis.com/coco-dataset/external/PASCAL_VOC.zip
tar -xf VOCtrainval_06-Nov-2007.tar
unzip PASCAL_VOC.zip
mv PASCAL_VOC/*.json .
rmdir PASCAL_VOC
ln -s /data data && cd $_
```

#### copy models from/to local machine

* from remote to local
```bash
scp -P <port> -i <path to key> root@52.204.230.7:/remote/folder/file  file
# for example
# scp -P 25484 -i ~/.ssh/vastai_rsa root@52.204.230.7:/data/dogscats/models/lession1-resnet34-2.pth lession1-resnet34-2.pth
```
* from local to remote
```bash
scp -P <port> -i <path to key>
```

#### make commands
* `make new` create new conda env from `environment.yml`
* `make tests` run tests (env must be activated)
* `make freeze` save list of installed in conda env (env must be activated) packages


#### create conda kernel manually
list existed kernels: `jupyter kernelspec list`
**note** not working as expected(always active current shell environment) for me. Workaround: `jupyter notebook` mustbe started in **activated** `flask-ai` environment

From root conda environment
```bash
conda install nb_conda
source activate flask-ai
python -m ipykernel install --name flask-ai
conda install ipykernel
python -m ipykernel install --name flask-ai
```
then restart jupyter  
