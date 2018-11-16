<a href="https://github.com/IaroslavR/structlog-boilerplate/blob/master/LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-green.svg"></a> 
<a href="https://github.com/ambv/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<a href="https://docs.python.org/3.6/"><img alt="Python: 3.6" src="https://upload.wikimedia.org/wikipedia/commons/3/34/Blue_Python_3.6_Shield_Badge.svg"></a>


### REST server template for fast.ai

Based on [Five Minutes from Machine Learning to RESTful API](https://jobs.zalando.com/tech/blog/connexion-zalando-open-source/?gh_src=4n3gxh1), answers from [forums.fast.ai](https://forums.fast.ai) and [cource v3 preview](https://github.com/fastai/course-v3/blob/master/nbs/dl1/lesson1-pets.ipynb)

### How to use
- see [INSTALL](INSTALL.md) for conda kernel installation details
- install venv and run server
```bash
git clone https://github.com/IaroslavR/fastai-rest-server-template.git
cd fastai-rest-server-template
make new
source activate flask-ai
python app.py

```
- open `http://127.0.0.1:5000/ui/` in browser

### Additional reading
- [SSH tunnelling how-to](https://www.everythingcli.org/ssh-tunnelling-for-fun-and-profit-local-vs-remote/)
- [tmux how-to](https://github.com/reshamas/fastai_deeplearn_part1/blob/master/tools/tmux.md#section-c)
- [fastai docs](https://docs.fast.ai/vision.html)
- [The 1cycle policy](https://sgugger.github.io/the-1cycle-policy.html)

