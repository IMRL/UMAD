# UMAD-Dataset-Usage-Guide-Doc

You can download the <u>UMAD-1.0 dataset</u> from [Google Drive, 10.73GB](https://drive.google.com/drive/folders/1UmZ3vA1cOunB-2wgz8T1fJDebhb-gmax). 

We may update the UMAD dataset in the future, but currently, UMAD-1.0 is the latest version.

## Dataset Directory Structure

```
UMAD                                     # UMAD Dataset folder
|
--- UMAD-1.0                         # Version
|       |
|       ---- data                         # image data
|       |      |
|       |      ---- 1.N6                                              # Scene
|       |       |       ---- 00                                         # Sequece
|       |       |         |     ---- G1                                 # reference image
|       |       |         |          |    ---- rgb                      # 00000000.jpg - xxxxxxxx.jpg
|       |       |         |     ---- Q1                                 # query image
|       |       |         |          |    ---- rgb                      # 00000000.jpg - xxxxxxxx.jpg
|       |       |       ---- 01
|                              .
|                              .
|       |       |       ---- N
|       |      ---- 2.Bridge
|                     .
|                     .
|       |      ---- 3.Central-Avenue 
|                     .
|                     .
|       |      ---- 4.Border-Road-1
|                     .
|                     .
|       |      ---- 5.Border-Road-2
|                     .
|                     .
|       |      ---- 6.N2
|                     .
|                     .
|       |
|       ---- gt                               # Ground truth binary mask .png files 
|       |      ---- 1.N6
|       |       |       ---- 00                                     # Sequece
|       |       |         |          ---- rgb                      # 00000000.png - xxxxxxxx.png
|       |       |       ---- 01
|                              .
|                              .
|       |       |       ---- N
|       |      ---- 2.Bridge
|                     .
|                     .
|       |      ---- 3.Central-Avenue
|                     .
|                     .
|       |      ---- 4.Border-Road-1
|                     .
|                     .
|       |      ---- 5.Border-Road-2
|                     .
|                     .
|       |      ---- 6.N2
|                     .
|                     .
|
--- README.md
```

## Dataset Ground truth Mask Label

![3-07-00001668-and-6-21-00003570](IMG/3-07-00001668-and-6-21-00003570.png)

We have annotated 8 different semantic labels on the UMAD dataset. You can refer to the [UMAD-IROS-2024 paper](https://arxiv.org/pdf/2408.12527) for more details.

Label description:

| Label_index | Label description                       | Label_binary_intensity_value |
| ----------- | --------------------------------------- | ---------------------------- |
| 1           | Anomalous Objects (Only in Query Image) | 128                          |
| 2           | Horizon                                 | 64                           |
| 3           | People in Query Image                   | 32                           |
| 4           | Dynamic Vehicles in Query Image         | 16                           |
| 5           | Moved Objects in Query Image            | 8                            |
| 6           | People in Query Image                   | 4                            |
| 7           | Dynamic Vehicles in Reference Image     | 2                            |
| 8           | Moved Objects in Reference Image        | 1                            |

Since reference .jpg and query .jpg may each contain objects, and these objects might <u>overlap if placed in a single mask image</u>, we use a <u>binary ground truth mask .png</u> file to describe them. (Note: A set of data, reference .jpg and query .jpg, share the same size ground truth mask .png file.)

For a set of data, assume <u>reference-00000001.jpg</u> and <u>query-00000001.jpg</u>, as well as their ground truth mask file <u>mask-00000001.png</u>.  

For example, when the pixel value at a point in the mask-00000001.png is <span style="color: red;">196</span>, which is represented in binary as <span style="color: red;">11000100</span>, so this point belongs to the <span style="color: red;">Anomalous Objects(128, 1000000)</span> in the query data, the <span style="color: red;">Horizon(64, 01000000)</span>, and the <span style="color: red;">People in Query Image(4, 00000100)</span>.

> 11000100 = 
>
> 10000000 +       # 128,   Anomalous Objects (Only in Query Image)
>
> 01000000 +       #  64,    Horizon
>
> 00000100          #   4,      People in Query Image

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

## Note

You can contact Dong Li via email(lidong8421bcd@gmail.com) or [open an issue on UMAD repo](https://github.com/IMRL/UMAD/issues) directly If you have any questions.

