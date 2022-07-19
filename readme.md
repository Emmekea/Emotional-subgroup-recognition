# Emotional Subgroup Recognition

For the automatic recognition of emotional subgroups in images. Given an image with multiple people present, it starts with predicting individual emotions and proceeds to cluster them into emotional subgroups. We additionally provide annotations of individual emotions, of social groups, and of emotional subgroups for 171 images collected from several datasets.

For details about the methodology and results, we refer to our IJCAI'22 paper (link will follow after proceedings are published). If you find our code useful for your research, please cite:

```
@InProceedings{Ruiz_2018_CVPR_Workshops,
author = {Veltmeijer, Emmeke A. and Gerritsen, Charlotte and Hindriks, Koen V.},
title = {Automatic Recognition of Emotional Subgroups in Images},
booktitle = {ijcai},
month = {July},
year = {2022}
}
```

## Requirements

- `requirements.txt` contains all required packages and their versions on which this code was tested.
- For gaze estimation, we make use of the [light version](https://github.com/OverEuro/deep-head-pose-lite) of [Hopenet](https://github.com/natanielruiz/deep-head-pose/tree/f7bbb9981c2953c2eca67748d6492a64c8243946) (Ruiz et al., 2018).  `stable_hopenetlite.py` should be placed in the root directory, `shuff_epoch_120.pkl` in `model/`.
- If you wish to work with the same data as in the paper, `data.json` contains all original image names together with the dataset they were retrieved from. To request access to these datasets, please go [here](https://iitrpr.ac.in/lasii/resources.html) for HAPPEI (Dhall et al., 2012) and GAF 3.0 (Dhall et al., 2018), and [here](http://sunai.uoc.edu/emotic/download.html) for EMOTIC (Kosti et al., 2019). Once the images from `data.json` are collected, place them in `img/`, then run `image_renaming.py` to rename the images according to the index assigned to them in `data.json`.

## Usage

`emotional-subgroup-recognition.ipynb` contains all code necessary to extract features (`Part II: Feature extraction`), cluster emotional subgroups (`Part III: Emotional subgroup clustering`), and compare the output against the provided ground truth (`Part IV: Evaluating emotional subgroup classification`). If you wish to use the code on data that has no emotional subgroup ground truth available, only parts I (`Setting up`) through III are applicable. The resulting emotional subgroup clustering resulting from part III will be stored in `output_files/image_information.json`.

## References

@inproceedings{dhall2012finding,
  title={Finding happiest moments in a social context},
  author={Dhall, Abhinav and Joshi, Jyoti and Radwan, Ibrahim and Goecke, Roland},
  booktitle={Asian Conference on Computer Vision},
  pages={613--626},
  year={2012},
  organization={Springer}
}
@inproceedings{dhall2018emotiw,
  title={Emotiw 2018: Audio-video, student engagement and group-level affect prediction},
  author={Dhall, Abhinav and Kaur, Amanjot and Goecke, Roland and Gedeon, Tom},
  booktitle={Proceedings of the 20th ACM International Conference on Multimodal Interaction},
  pages={653--656},
  year={2018}
}
@article{kosti2019context,
  title={Context based emotion recognition using emotic dataset},
  author={Kosti, Ronak and Alvarez, Jose M and Recasens, Adria and Lapedriza, Agata},
  journal={IEEE transactions on pattern analysis and machine intelligence},
  volume={42},
  number={11},
  pages={2755--2766},
  year={2019},
  publisher={IEEE}
}
@InProceedings{Ruiz_2018_CVPR_Workshops,
author = {Ruiz, Nataniel and Chong, Eunji and Rehg, James M.},
title = {Fine-Grained Head Pose Estimation Without Keypoints},
booktitle = {The IEEE Conference on Computer Vision and Pattern Recognition (CVPR) Workshops},
month = {June},
year = {2018}
}