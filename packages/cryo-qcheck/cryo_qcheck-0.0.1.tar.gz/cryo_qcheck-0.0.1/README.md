# cryo_qcheck
This package is work in progess which contains programs that help in accessing quality of cryoEM 3D map reconstruction. 

The details of the program are publised in biorxiv, a preprint server for biology.

Please follow the link to the paper. "https://www.biorxiv.org/content/10.1101/2022.12.31.521834v1"

Changes will be made to the up comming versions and accompied with paper published in peer review journal. 

The "qcheck" package presently constitutes one program which evalutes phase values from the 3D cryoEM reconstructed map and calcuates two statistical parameter to judge the quality of the reconstruction. 

The "pc_sk" program helps in quantitatively assess the presence of non-particles in the reconstructed map. 

The program takes two input parameters to perform calculations, one is the cryo-EM map which can have both mrc or map extension and second parameter is the map's contour value. 

The contour value is used to create a mask and then perform the calcualation. 

After the calucaltion are done, the output numerical values are printed on the console and a graph is saved into the folder with the name of the map provided for calculation. 



Usage:
python pc_sk.py example.mrc contour_value
