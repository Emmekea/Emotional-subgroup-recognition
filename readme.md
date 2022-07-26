# Emotional Subgroup Recognition

For the automatic recognition of emotional subgroups in images. Given an image with multiple people present, it starts with predicting individual emotions and proceeds to cluster them into emotional subgroups. We additionally provide annotations of individual emotions, of social groups, and of emotional subgroups for 171 images collected from several datasets. 

Run the following command to download this repository along with its dependencies:
```
git clone --recursive git@github.com:Emmekea/emotional-subgroup-recognition.git
``` 

For details about the methodology and results, we refer to our [IJCAI'22 paper](https://www.ijcai.org/proceedings/2022/0190.pdf). If you find our code useful for your research, please cite:

```
@inproceedings{ijcai2022-190,
  title     = {Automatic Recognition of Emotional Subgroups in Images},
  author    = {Veltmeijer, Emmeke A. and Gerritsen, Charlotte and Hindriks, Koen V.},
  booktitle = {Proceedings of the Thirty-First International Joint Conference on
               Artificial Intelligence, {IJCAI-22}},
  publisher = {International Joint Conferences on Artificial Intelligence Organization},
  editor    = {Luc De Raedt},
  pages     = {1363--1370},
  year      = {2022},
  month     = {7},
  note      = {Main Track}
  doi       = {10.24963/ijcai.2022/190},
  url       = {https://doi.org/10.24963/ijcai.2022/190},
}
```

## Requirements

- `requirements.txt` contains all required packages and their versions on which this code was tested.
- For gaze estimation, we make use of the [light version](https://github.com/OverEuro/deep-head-pose-lite) of [Hopenet](https://github.com/natanielruiz/deep-head-pose/tree/f7bbb9981c2953c2eca67748d6492a64c8243946) (Ruiz *et al*., 2018). If you haven't cloned our repository using `--recursive`, please run the following command to ensure this dependency is downloaded: `git submodule update --init --recursive`.

## Data

If you wish to work with the same data as in the paper, the original datasets they were retrieved from should be downloaded. To request access to these datasets, please go [here](https://iitrpr.ac.in/lasii/resources.html) for HAPPEI (Dhall *et al*., 2012) and GAF 3.0 (Dhall *et al*., 2018), and [here](http://sunai.uoc.edu/emotic/download.html) for EMOTIC (Kosti *et al.*, 2019). Once these datasets are acquired, place them in `datasets/` and run `collect.py`. This finds all images from `data.json`, renames them according to the index assigned to them in our study, and places them in `img/`. The ground truth annotations can be found in `data.json`.

## Usage

`emotional-subgroup-recognition.ipynb` contains all code necessary to extract features (`Part II: Feature extraction`), cluster emotional subgroups (`Part III: Emotional subgroup clustering`), and compare the output against the provided ground truth (`Part IV: Evaluating emotional subgroup classification`). If you wish to use the code on data that has no emotional subgroup ground truth available, only parts I (`Setting up`) through III are applicable. The resulting emotional subgroup clustering resulting from part III will be stored in `output_files/image_information.json`.

## References

Dhall, A., Joshi, J., Radwan, I., & Goecke, R. (2012, November). Finding happiest moments in a social context. In *Asian Conference on Computer Vision* (pp. 613-626). Springer, Berlin, Heidelberg.

Dhall, A., Kaur, A., Goecke, R., & Gedeon, T. (2018, October). Emotiw 2018: Audio-video, student engagement and group-level affect prediction. In *Proceedings of the 20th ACM International Conference on Multimodal Interaction* (pp. 653-656).

Kosti, R., Alvarez, J. M., Recasens, A., & Lapedriza, A. (2019). Context based emotion recognition using emotic dataset. *IEEE transactions on pattern analysis and machine intelligence*, 42(11), 2755-2766.

Ruiz, N., Chong, E., & Rehg, J. M. (2018). Fine-grained head pose estimation without keypoints. In *Proceedings of the IEEE conference on computer vision and pattern recognition workshops* (pp. 2074-2083).