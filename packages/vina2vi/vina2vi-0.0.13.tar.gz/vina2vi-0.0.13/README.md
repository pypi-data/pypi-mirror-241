# vina2vi
`vina2vi` stands for _**Vi**etnamese **n**o **a**ccent **to** **Vi**etnamese_,  
which is a Python package aiming at helping foreigners **decrypt** Vietnamese messages.  

Among other things, we plan to make `vina2vi` capable of
- Restoring Vietnamese diacritics
- Correcting spelling
- Translating acronyms, **đổi vần**, etc.


## Installation
During development, I have used Python3.10.
But I think all Python versions >= 3.8 will be fine.

Run the following command to install `vina2vi`:

```bash
pip install vina2vi
```

Alternatively, one can also install the latest commit from GitLab as follows.

```bash
pip install git+https://gitlab.com/phunc20/vina2vi
```


## Usage
I only work on this project on my spare time,
and work slowly. This README is meant to
get changed fast and a lot. Therefore, please pay
attention to the versions and the corresponding README.
For the moment, there is not much in
the package that is super useful. As time goes by, I will add more.

I roughly classify the code into the following categories
- `models`
- `metrics`
- `util`


### `vina2vi/models/`
For example, one can try to play with a Transformer model
```python
In [1]: from vina2vi.models.tf.tuto_transformer import Translator

In [2]: translator = Translator.from_pretrained()

In [3]: translator.translate("Sang nay toi dan con toi di cong vien choi.")
Out[3]: 'sang này tôi đàn con tôi đi công viên chơi .'

In [4]: translator.translate("Truong dai hoc xa hoi va nhan van")
Out[4]: 'trường đại học xã hội và nhân văn'
```

Or with a bigram model
```python
In [1]: from vina2vi.models.char_based.bigram import Bigram

In [2]: bigram = Bigram.from_pretrained()

In [3]: bigram.translate("Sang nay toi dan con toi di cong vien choi.")
Out[3]: 'Sang này tôi đãn cón tôi đi cóng viện chôi.'

In [4]: bigram.translate("Truong dai hoc xa hoi va nhan van")
Out[4]: 'Trường đãi hôc xã hôi và nhàn vàn'
```

In particular, the CRF model in `vina2vi/models/crf.py` is a direct borrow from
[`trungtv`](https://github.com/trungtv/pyvi). The only reason I put a GitHub installation
link, like in `requirements.txt`, is that the original repo has a small bug and that it seems
that that pacakge is no longer maintained. As a result, I forked the work and made
a few commits to fix the small bug.

However, it seems that PyPi does not accept `pyproject.toml` containing any GitHub link
as dependency. Therefore, in order to use the CRF model, please install the `pyvi` package
according to `requirements.txt`.


### `vina2vi/util.py`
For example, there is an utility function to help tell whether a string contains
non-Vietnamese characters, `is_foreign`. As the name suggests,
- If the string contains characters other than the modern Vietnamese alphabets,
  then `is_foreign` returns `True`
- If the string consists exclusively of characters of modern Vietnamese alphabets,
  then `is_foreign` returns `False`
    - Languages whose alphabets are a subset of Vietnamese's are thus considered as Vietnamese
    - Currently, we do not consider chữ Nôm as Vietnamese; maybe we will in the future

```python
In [1]: from vina2vi.util import Vietnamese

In [2]: Vietnamese.is_foreign("Российская Федерация\tRossiyskaya Federatsiya")
Out[2]: True

In [3]: Vietnamese.is_foreign("\n\tRossiyskaya Federatsiya")
Out[3]: False

In [4]: Vietnamese.is_foreign("Tôi nói tiếng Việt Nam\t碎呐㗂越南")
Out[4]: True

In [5]: Vietnamese.is_foreign("Tôi nói tiếng Việt Nam\t")
Out[5]: False
```

There are also four useful normalizers (from Hugging Face's `tokenizers` library)

1. `uncased_vi_normalizer`
1. `cased_vi_normalizer`
1. `uncased_vina_normalizer`
1. `cased_vina_normalizer`

which help

1. Make sure that similar-looking characters are not only similar but also exactly the same
1. (In the case of `(un)cased_vina_normalizer`) Remove diacritics


## Evaluation and Data
`vina2vi/metrics/evaluate_models.py` helps give a quick overview of the models' performances.
```bash
$ python evaluate_models.py
                                 mean  median
baseline                       0.7862  0.7813
bigram                         0.8405  0.8399
crf_trungtv                    0.8591  0.8561
tf_tuto_transformer (cased)    0.8691  0.8758
tf_tuto_transformer (uncased)  0.8918  0.9101
```
where the `mean` and `median` stand for the mean and median similarities calculated on some test
dataset (to be described below).

`vina2vi/data/`: Different types of text are collected with balance --
Modern literature, lyrics, classics, etc.
```bash
$ wc -c vina2vi/data/*.txt
 3576 vina2vi/data/canh_dong_bat_tan.txt
 2261 vina2vi/data/cho_toi_xin_mot_ve_di_tuoi_tho.txt
 1775 vina2vi/data/chuyen_tinh_nguoi_trinh_nu_ten_thi.txt
 3174 vina2vi/data/tron_tim.txt
 1613 vina2vi/data/truyen_kieu.txt
12399 total
```
