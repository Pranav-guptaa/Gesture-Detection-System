from fastai import *
from fastai.vision import *
import fastai

tfms = get_transforms()
bs = 64
path = 'D:\\DATA\\(SEMESTER-4)\\Minor Project\\asl_alphabet_train\\asl_alphabet_train'
training = 'D:\\DATA\\(SEMESTER-4)\\Minor Project\\asl_alphabet_train\\asl_alphabet_train\\'
testing = 'D:\\DATA\\(SEMESTER-4)\\Minor Project\\asl_alphabet_test\\asl_alphabet_test\\'

data = ImageDataBunch.from_folder(path=path, train = training, test = testing, ds_tfms=get_transforms(),size=224,valid_pct=0.3)

learn = create_cnn(data, models.resnet34, metrics=error_rate)

learn.fit_one_cycle(6)

learn.lr_find()

learn.recorder.plot()

learn.unfreeze()

learn.fit_one_cycle(8, max_lr=slice(1e-5,1e-4))

learn.export()