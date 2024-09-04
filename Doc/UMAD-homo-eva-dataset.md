# UMAD Homography Evaluation Dataset(under maintenance)

UMAD-homo-eva dataset Download Link: [Google Drive, about 290MB](https://drive.google.com/drive/folders/1CHx94Cp3-qkzFHd_r97-bI4FCqpWZeAH?usp=sharing), includes the <u>UMAD-homo-eva dataset overview and adaptive warping video</u>, with <u>414 pairs of reference and query images</u>, <u>their pose data</u>, and <u>corresponding ground truth feature point annotations in a .txt files</u>.

## Introduction

The UMAD-homo-eva dataset project provides the following components: 

- [UMAD-homo-eva dataset](#UMAD-homo-eva-dataset),

- [Adaptive Warping](#Adaptive-Warping),
- [Leaderboard](#Leaderboard), 
- [Feature Correspondence Point Annotation Tool](#Feature-Correspondence-Point-Annotation-Tool).

## UMAD-homo-eva dataset

![dataset-overview](../IMG/dataset-overview.png)

We chose 400+ image pairs from [UMAD](https://github.com/IMRL/UMAD) original dataset; For each evaluated image pair, we manually annotated 10 uniformly distributed matching points for quantitative comparisons by pre-labeling them using traditional feature point extraction and matching methods, use it to evaluate the image alignment algorithms.

**UMAD-homo-eva dataset**:

- UMAD-homo-eva dataset overview and adaptive warping video,
- 414 pairs of reference and query images,
- 414 pose data: The pose data is collected by our robot system using 3D LiDAR SLAM/localization. We use the rotation data from the pose data for <u>Rotation-induced Homography Warping</u> (coarse) in our Adaptive Warping,
- ground truth  .txt  files: 414 .txt  files, corresponding to the image pairs.

## Adaptive Warping

![adaptive-warping](../IMG/adaptive-warping.png)

Adaptive Warping is a **coarse-to-fine** image alignment (or image warping) method based on homography.

![PME-result](../IMG/PME-result.png)

You can view more visualizations from the [UMAD IROS 2024 video](https://www.youtube.com/watch?v=xORb4H-AyNw), or obtain more comparative data from the [Leaderboard](#Leaderboard).

## Leaderboard

![Leaderboard-from-UMAD](../IMG/leaderboard-from-UMAD.png)

We plan to add comparisons with more learning-based methods in the future.

## Feature Correspondence Point Annotation Tool

We are optimizing this annotation tool. Currently, this annotation tool uses traditional feature point detection and matching methods (SIFT) for pre-matching, followed by manual screening, and finally allows for manual annotation.

Reference: https://github.com/daisatojp/labelMatch

## Citation

This project is part of [UMAD](https://github.com/IMRL/UMAD). If you find this work useful, please consider citing the paper:

```
@article{li2024umad
  author    = {Li, Dong and Chen, Lineng and Xu, Cheng-Zhong and Kong, Hui},
  title     = {UMAD: University of Macau Anomaly Detection Benchmark Dataset},
  journal   = {arXiv preprint arXiv:2408.12527},
  year      = {2024},
}
```